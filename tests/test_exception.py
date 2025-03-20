import pytest
import traceback
from darca_exception import DarcaException


def test_darca_exception_basic():
    """
    Test basic initialization of DarcaException.
    """
    exc = DarcaException("Test error", error_code="TEST_001", metadata={"key": "value"})
    
    assert exc.message == "Test error"
    assert exc.error_code == "TEST_001"
    assert exc.metadata == {"key": "value"}
    assert exc.cause is None


def test_darca_exception_default_values():
    """
    Test DarcaException initializes correctly when optional parameters are omitted.
    """
    exc = DarcaException("Default error")
    
    assert exc.message == "Default error"
    assert exc.error_code == "UNKNOWN_ERROR"
    assert exc.metadata == {}
    assert exc.cause is None


def test_darca_exception_with_cause():
    """
    Test that DarcaException correctly stores an underlying cause.
    """
    original_exception = ValueError("Underlying issue")
    exc = DarcaException("Higher-level error", error_code="WRAP_001", cause=original_exception)
    
    assert exc.message == "Higher-level error"
    assert exc.error_code == "WRAP_001"
    assert exc.cause == original_exception
    assert "Underlying issue" in str(exc)  # Check __str__ output


def test_darca_exception_to_dict():
    """
    Test that DarcaException correctly converts to a dictionary.
    """
    exc = DarcaException("Dict test", error_code="DICT_001", metadata={"key": "value"})
    exc_dict = exc.to_dict()

    assert isinstance(exc_dict, dict)
    assert exc_dict["error_code"] == "DICT_001"
    assert exc_dict["message"] == "Dict test"
    assert exc_dict["metadata"] == {"key": "value"}
    assert exc_dict["cause"] is None
    assert "stack_trace" in exc_dict


def test_darca_exception_to_dict_with_cause():
    """
    Test that DarcaException's `to_dict` method correctly includes a cause.
    """
    try:
        raise ValueError("Underlying error")
    except ValueError as cause:
        exc = DarcaException("Wrapper error", error_code="WRAP_001", cause=cause)
        exc_dict = exc.to_dict()
    
    assert exc_dict["cause"] == "Underlying error"
    assert "stack_trace" in exc_dict


def test_darca_exception_string_representation():
    """
    Test that __str__ and __repr__ return correct values.
    """
    exc = DarcaException("String test", error_code="STR_001")
    assert str(exc) == "[STR_001] String test"
    assert repr(exc) == "DarcaException(error_code=STR_001, message=String test)"


def test_darca_exception_string_representation_with_cause():
    """
    Test that __str__ includes the cause when present.
    """
    try:
        raise ValueError("Root cause")
    except ValueError as cause:
        exc = DarcaException("Wrapper exception", error_code="WRAP_002", cause=cause)
    
    assert "[WRAP_002] Wrapper exception, caused by Root cause" in str(exc)


def test_darca_exception_logging(capture_logs):
    """
    Test that DarcaException logs errors correctly.
    """
    try:
        raise DarcaException("Log test", error_code="LOG_001")
    except DarcaException:
        pass  # Expected

    assert any("Log test" in record.message for record in capture_logs.records)


def test_darca_exception_logging_with_cause(capture_logs):
    """
    Test that DarcaException logs errors with a cause correctly.
    """
    try:
        raise ValueError("Initial problem")
    except ValueError as cause:
        try:
            raise DarcaException("Higher-level error", error_code="LOG_002", cause=cause)
        except DarcaException:
            pass  # Expected

    assert any("Higher-level error" in record.message for record in capture_logs.records)
    assert any("Initial problem" in record.message for record in capture_logs.records)
