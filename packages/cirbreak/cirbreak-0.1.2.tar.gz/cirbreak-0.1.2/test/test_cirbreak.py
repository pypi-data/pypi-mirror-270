import pytest
from cirbreak.cirbreak import circuit_breaker
from unittest.mock import Mock

def replace_function(x):
    return x

@pytest.mark.parametrize(
    "failure_threshold,recovery_timeout,replace_function,consecutive,test_id,values",
    [
        (3, 10, None, False, "happy_path_defaults", [2]),
        (1, 5, replace_function, True, "happy_path_custom_with_replacement", [1, 2]),
        (5, 20, None, True, "happy_path_high_threshold", [2]),
        (0, 10, None, False, "edge_case_zero_threshold", [2]),
        (3, 0, None, False, "edge_case_zero_recovery", [2]),
        (-1, 10, None, False, "error_case_negative_threshold", [2]),
        (3, -5, None, False, "error_case_negative_recovery", [2]),
    ],
)
def test_circuit_breaker(
    failure_threshold, recovery_timeout, replace_function, consecutive, test_id, values
):

    @circuit_breaker(
        failure_threshold=failure_threshold,
        recovery_timeout=recovery_timeout,
        replace_function=replace_function,
        consecutive=consecutive,
    )
    def test_function(x):
        if replace_function is not None and x[0] == 1:
            raise Exception("Test exception")
        return x[0] * 2

    if replace_function:
        with pytest.raises(Exception) as exc_info:
            test_function(values)
        assert str(exc_info.value) == "Test exception"
    else:
        result = test_function(values)
        expected_result = 4 if replace_function is None else 2
        assert result == expected_result, f"Test ID: {test_id} - Expected the function to return {expected_result}"