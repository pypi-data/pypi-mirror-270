import uuid
import time
import hashlib
import pytest
from _pytest.mark import deselect_by_keyword, deselect_by_mark
import grpc
import httpx
from .protobufs import test_run_pb2_grpc
from .protobufs import test_pb2_grpc
from .protobufs import tests_pb2_grpc
from .protobufs import test_run_pb2
from .protobufs import test_pb2
from .protobufs import tests_pb2
from google.protobuf.timestamp_pb2 import Timestamp


class GrpcClient:
    def __init__(self, server_address, service_stub):
        self.server_address = server_address
        self.service_stub = service_stub

    def _create_channel(self):
        return grpc.insecure_channel(self.server_address)

    def _handle_rpc_error(self, e):
        pass

    def call_rpc_method(self, method_name, request):
        with self._create_channel() as channel:
            stub = self.service_stub(channel)

            try:
                rpc_method = getattr(stub, method_name)
                response = rpc_method(request)
                return response
            except grpc.RpcError as e:
                self._handle_rpc_error(e)
                return None


def is_main_node(config):
    return not hasattr(config, "workerinput")


class PytestInitry:
    def __init__(self, config=None):
        self.config = config
        self.tests = list()
        self.xmlpath = config.option.xmlpath
        self.test_uuid = None
        self.pairs = []
        self.start_records = []
        self.initry_batching_ini = config.getoption("initry_batching") or config.getini("initry_batching")
        self.initry_batching = self.initry_batching_ini
        self.initry_host = config.getoption("initry_host") or config.getini("initry_host")
        self.initry_port = config.getoption("initry_port") or config.getini("initry_port")
        self.initry_grpc_port = config.getoption("initry_grpc_port") or config.getini("initry_grpc_port")
        self.initry_junit_xml_only = config.getoption("initry_junit_xml_only") or config.getini("initry_junit_xml_only")
        self.test_run_grpc_client = GrpcClient(
            f"{self.initry_host}:{self.initry_grpc_port}",
            test_run_pb2_grpc.TestRunServiceStub,
        )
        self.test_grpc_client = GrpcClient(f"{self.initry_host}:{self.initry_grpc_port}", test_pb2_grpc.TestServiceStub)
        self.cs_test_grpc_client = GrpcClient(
            f"{self.initry_host}:{self.initry_grpc_port}",
            test_pb2_grpc.ClientStreamTestServiceStub,
        )
        self.tests_grpc_client = GrpcClient(
            f"{self.initry_host}:{self.initry_grpc_port}",
            tests_pb2_grpc.TestsServiceStub,
        )

    def nodeid_converter(self, nodeid):
        """
        Convert a nodeid string into a standardized format.

        Parameters:
            nodeid (str): The original nodeid string to be converted.

        Returns:
            str: The converted nodeid string with '/' replaced by '.' and '::' replaced by '.'.
                 Additionally, '.py' extension is removed.

        Example:
            >>> self.nodeid_converter("tests/classes/test_1.py::TestClass::test_one")
            'tests.classes.test_1.TestClass.test_one'
        """
        return nodeid.replace("/", ".").replace("::", ".").replace(".py", "")

    def generate_test_id(self, shared_uuid, data):
        string = (shared_uuid + data).encode("utf-8")
        number_str = str(int(hashlib.md5(string).hexdigest(), 16))[0:31]
        number = int(number_str)
        hex_number = hex(number)[2:]
        hex_number_padded = hex_number.zfill(32)
        return str(uuid.UUID(hex=hex_number_padded))

    def append_test(self, item, shared_uuid):
        test = dict()
        test["location"] = item.location[2]
        test["nodeid"] = self.nodeid_converter(item.nodeid)
        if shared_uuid:
            test["uuid"] = self.generate_test_id(shared_uuid, item.nodeid)
        else:
            test["uuid"] = str(uuid.uuid4())
        test["test_run_uuid"] = shared_uuid
        test["description"] = item._obj.__doc__
        self.tests.append(test)

    def pytest_collection_modifyitems(self, session, items, config):
        if not is_main_node(config):
            shared_uuid = session.config.workerinput["shared_uuid"]
        else:
            shared_uuid = session.config.shared_uuid

        started_at = Timestamp(seconds=int(time.time()))

        deselect_by_keyword(items, config)
        deselect_by_mark(items, config)

        for item in session.items:
            self.append_test(item, shared_uuid)

        if self.initry_junit_xml_only is False:
            plugin_type = "pytest.initry"
            if self.xmlpath:
                plugin_type = "pytest.initry.xml"

            request_data = test_run_pb2.CreateTestRunRequest(
                tests_count=len(session.items),
                started_at=started_at,
                uuid=shared_uuid,
                plugin_type=plugin_type,
            )
        else:
            request_data = test_run_pb2.CreateTestRunRequest(
                uuid=shared_uuid,
                started_at=started_at,
                plugin_type="pytest.xml",
            )
        self.test_run_grpc_client.call_rpc_method("CreateTestRun", request_data)

        if self.initry_junit_xml_only:
            request_data = tests_pb2.CreateTestsRequest(tests=self.tests, only_tests_info=True)
        else:
            request_data = tests_pb2.CreateTestsRequest(tests=self.tests)
        self.tests_grpc_client.call_rpc_method("CreateTests", request_data)

    def pytest_runtest_logstart(self, nodeid):
        if self.initry_junit_xml_only is False:
            for item in self.tests:
                if item["nodeid"] == self.nodeid_converter(nodeid):
                    self.test_uuid = item["uuid"]

            if self.test_uuid is not None:
                request_data = test_pb2.StartTestRequest(
                    uuid=self.test_uuid,
                    started_at=Timestamp(seconds=int(time.time())),
                    status=test_pb2.TestStatus.RUNNING,
                )
                if self.initry_batching:
                    self.start_records.append(request_data)
                else:
                    self.test_grpc_client.call_rpc_method("StartTest", request_data)

    def started_finished_pairs(self, report):
        if self.initry_junit_xml_only is False:

            def find_something(uuid: str):
                _started_at = [req.started_at for req in self.pairs if req.uuid == uuid and hasattr(req, "started_at")][
                    0
                ]
                _stopped_at = [req.stopped_at for req in self.pairs if req.uuid == uuid and hasattr(req, "stopped_at")][
                    0
                ]
                _status = [req.status for req in self.pairs if req.uuid == uuid and hasattr(req, "stopped_at")][0]
                return _started_at, _stopped_at, _status

            request = None
            for item in self.pairs:
                started_at, stopped_at, status = find_something(item.uuid)
                request = test_pb2.ModifyTestRequest(
                    uuid=item.uuid,
                    started_at=started_at,
                    stopped_at=stopped_at,
                    status=status,
                    log=report.longreprtext,
                    stdout=report.capstdout,
                    stderr=report.capstderr,
                )
            yield request

    def create_pairs_for_batching(self, request, report):
        if self.initry_junit_xml_only is False:
            start_record = [record for record in self.start_records if record.uuid == self.test_uuid][0]
            if start_record:
                # send start and stop to self.pairs
                self.pairs.append(start_record)
                self.pairs.append(request)

                # clean start_records for previous start_record
                self.start_records = [record for record in self.start_records if record.uuid != self.test_uuid]

                self.cs_test_grpc_client.call_rpc_method("ModifyTest", self.started_finished_pairs(report))
                self.pairs = []

    def pytest_runtest_logreport(self, report):
        if self.initry_junit_xml_only is False:
            if self.test_uuid is not None:
                if report.when == "call" and report.outcome == "failed":
                    if report.failed and not hasattr(report, "wasxfail"):
                        request = test_pb2.StopTestRequest(
                            uuid=self.test_uuid,
                            stopped_at=Timestamp(seconds=int(time.time())),
                            status=test_pb2.TestStatus.FAILED,
                            log=report.longreprtext,
                            stdout=report.capstdout,
                            stderr=report.capstderr,
                        )
                        if not self.initry_batching:
                            self.test_grpc_client.call_rpc_method("StopTest", request)
                        else:
                            self.create_pairs_for_batching(request, report)
                elif report.when == "setup" and report.outcome == "failed":
                    if report.failed and not hasattr(report, "wasxfail"):
                        request = test_pb2.StopTestRequest(
                            uuid=self.test_uuid,
                            stopped_at=Timestamp(seconds=int(time.time())),
                            status=test_pb2.TestStatus.FAILED,
                            log=report.longreprtext,
                            stdout=report.capstdout,
                            stderr=report.capstderr,
                        )
                        if not self.initry_batching:
                            self.test_grpc_client.call_rpc_method("StopTest", request)
                        else:
                            self.create_pairs_for_batching(request, report)
                elif report.when == "call" and report.outcome == "passed":
                    request = test_pb2.StopTestRequest(
                        uuid=self.test_uuid,
                        stopped_at=Timestamp(seconds=int(time.time())),
                        status=test_pb2.TestStatus.PASSED,
                    )
                    if not self.initry_batching:
                        self.test_grpc_client.call_rpc_method("StopTest", request)
                    else:
                        self.create_pairs_for_batching(request, report)

                elif (report.when == "call" and report.outcome == "skipped") or (
                    report.when == "setup" and report.outcome == "skipped"
                ):
                    request = test_pb2.StopTestRequest(
                        uuid=self.test_uuid,
                        stopped_at=Timestamp(seconds=int(time.time())),
                        status=test_pb2.TestStatus.SKIPPED,
                        log=report.longreprtext,
                        stdout=report.capstdout,
                        stderr=report.capstderr,
                    )
                    if not self.initry_batching:
                        self.test_grpc_client.call_rpc_method("StopTest", request)
                    else:
                        self.create_pairs_for_batching(request, report)
                elif report.when == "call" and report.outcome == "xfailed":
                    request = test_pb2.StopTestRequest(
                        uuid=self.test_uuid,
                        stopped_at=Timestamp(seconds=int(time.time())),
                        status=test_pb2.TestStatus.EXPECTED_FAILED,
                        log=report.longreprtext,
                        stdout=report.capstdout,
                        stderr=report.capstderr,
                    )
                    if not self.initry_batching:
                        self.test_grpc_client.call_rpc_method("StopTest", request)
                    else:
                        self.create_pairs_for_batching(request, report)
                elif report.when == "call" and report.outcome == "xpassed":
                    request = test_pb2.StopTestRequest(
                        uuid=self.test_uuid,
                        stopped_at=Timestamp(seconds=int(time.time())),
                        status=test_pb2.TestStatus.EXPECTED_PASSED,
                    )
                    if not self.initry_batching:
                        self.test_grpc_client.call_rpc_method("StopTest", request)
                    else:
                        self.create_pairs_for_batching(request, report)

    def pytest_sessionfinish(self, session):
        if not is_main_node(session.config):
            shared_uuid = session.config.workerinput["shared_uuid"]
        else:
            shared_uuid = session.config.shared_uuid

        if self.xmlpath:
            files = {"file": open(self.config.option.xmlpath, "rb")}
            with httpx.Client(timeout=360) as client:
                if self.initry_junit_xml_only:
                    data = {"uuid": shared_uuid, "mode": "xml_only"}
                else:
                    data = {"uuid": shared_uuid, "mode": "store"}
                url = f"http://{self.initry_host}:{self.initry_port}/api/test-runs/xml"
                client.post(url, files=files, data=data)
        request_data = test_run_pb2.StopTestRunRequest(uuid=shared_uuid, stopped_at=Timestamp(seconds=int(time.time())))
        self.test_run_grpc_client.call_rpc_method("StopTestRun", request_data)


def pytest_addoption(parser):
    group = parser.getgroup("pytest-initry")
    group.addoption(
        "--initry-host",
        default=None,
        dest="initry_host",
        action="store",
        help="initry host",
    )
    group.addoption(
        "--initry-port",
        default=None,
        dest="initry_port",
        action="store",
        help="initry port",
    )
    group.addoption(
        "--initry-grpc-port",
        default=None,
        dest="initry_grpc_port",
        action="store",
        help="initry gRPC port",
    )
    group.addoption(
        "--initry-batching",
        default=None,
        dest="initry_batching",
        action="store",
        help="batch mode",
    )
    group.addoption(
        "--initry-junitxml-only",
        default=None,
        dest="initry_junit_xml_only",
        action="store",
        help="No realtime, only use JUnit XML report as source data",
    )
    parser.addini("initry_host", help="initry host", default=None)
    parser.addini("initry_port", help="initry port", default=None)
    parser.addini("initry_grpc_port", help="initry gRPC port", default=None)
    parser.addini("initry_batching", type="bool", help="batch mode", default=None)
    parser.addini(
        "initry_junit_xml_only",
        type="bool",
        help="No realtime, only use JUnit XML report as source data",
        default=False,
    )


def pytest_configure(config):
    if is_main_node(config):
        config.shared_uuid = str(uuid.uuid4())
    initry = config.getoption("initry_host") or config.getini("initry_host")
    if initry:
        plugin = PytestInitry(config)
        config._initry = plugin
        config.pluginmanager.register(plugin)
    junitxml = config.option.xmlpath
    junit_xml_only = config.getoption("initry_junit_xml_only") or config.getini("initry_junit_xml_only")
    batching = config.getoption("initry_batching") or config.getini("initry_batching")

    if junit_xml_only is True and junitxml is None:
        pytest_unconfigure(config)
        raise pytest.UsageError("'initry_junit_xml_only' config option must be used only with 'junitxml' argument")

    if junit_xml_only is True and batching is True:
        raise pytest.UsageError(
            "'initry_batching' config option must not be used together with 'initry_junit_xml_only'. "
            "There is no point in doing so because the 'initry_junit_xml_only' mode does not utilize real-time reporting."
        )


def pytest_configure_node(node):
    node.workerinput["shared_uuid"] = node.config.shared_uuid


def pytest_unconfigure(config):
    plugin = getattr(config, "_initry", None)
    if plugin is not None:
        del config._initry
        config.pluginmanager.unregister(plugin)
