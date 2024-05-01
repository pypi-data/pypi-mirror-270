# pytest-initry

Plugin for sending automation test data from Pytest to the [initry](https://github.com/initry/initry).

### Install and setup:

1. Install:
   ```
   pip install pytest-initry
   ```
2. Configure pytest.ini:
    ```ini
    [pytest]
    initry_host = localhost
    initry_port = 8000
    initry_grpc_port = 50051
    initry_batching = False
    initry_junit_xml_only = False
    ```
3. CLI can also be used, but it's not the preferred method. The arguments will be the same as those mentioned for the pytest.ini config file.
    ```bash
    pytest --initry-host=localhost --initry-batching=True
    ```
   
### Arguments:
#### initry_host
Initry API Backend hostname. Use the same value as `INITRY_API_HOST` for backend .env and `NEXT_PUBLIC_INITRY_API_HOST` for frontend .env.

Example: `localhost`, `192.168.1.2`, etc.
<br><br>

#### initry_port
Initry API Backend port. Use the same value as `INITRY_API_EXTERNAL_PORT` for backend .env and `NEXT_PUBLIC_INITRY_API_EXTERNAL_PORT` for frontend .env.

Example: 8000, etc.
<br><br>

#### initry_grpc_port
Initry gRPC Backend port. Use the same value as `INITRY_GRPC_EXTERNAL_PORT` for backend .env.

Example: 50051, etc.
<br><br>

#### initry_batching
Batching mode: Use only if you have thousands of very fast unit tests. Data from the plugin to the Initry backend will be sent in batches.

Will not work with `initry_junit_xml_only`

Example: True, False.
<br><br>

#### initry_junit_xml_only
Real-time mode will be disabled, only the Pytest XML JUnit report will be sent at the end of the test run.

Will not work with `initry_batching`

Use together with pytest argument `--junitxml=your_xml_file.name.xml`

Example: True, False.
<br><br>

### Examples:

`pytest`: Pytest will be executed in real-time mode.

`pytest` *(with initry_batching=True)*: Pytest will be executed in real-time mode, but data will be sent to the server in batches to reduce network overhead. Real-time data will only display task finalized statuses without the 'running' state.

`pytest --junitxml=test.xml`: Pytest will be executed in real-time mode, and additional information will be collected from the generated JUnit XML file after the test run finalization.

`pytest --junitxml=test.xml` *(with initry_junit_xml_only=True)*:  Pytest will be executed without providing real-time data, and information will be gathered after the test run ends using the generated JUnit XML file.



### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
