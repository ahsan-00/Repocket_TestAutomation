# conftest.py

import pytest
from utils.driver_factory import DriverFactory

def pytest_addoption(parser):
    parser.addoption(
        "--platform", action="store", default="android", help="Platform to test on: android or ios"
    )

@pytest.fixture(scope="function")
def driver(request):
    platform = request.config.getoption("--platform")
    factory = DriverFactory(platform)
    driver = factory.create_driver()
    yield driver
    driver.quit()
