import pytest
from darca_log_facility import DarcaLogger

@pytest.fixture(scope="session")
def test_logger():
    """
    Provides a test logger instance for capturing logs during testing.
    """
    return DarcaLogger("test-logger").get_logger()


@pytest.fixture
def capture_logs(caplog):
    """
    Pytest fixture to capture logs at the ERROR level.
    """
    with caplog.at_level("ERROR"):
        yield caplog
