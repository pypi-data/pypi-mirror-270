import time
from functools import wraps
from typing import Any, Callable, Optional


def circuit_breaker(
    failure_threshold: int = 3,
    recovery_timeout: int = 10,
    replace_function: Optional[Callable] = None,
    consecutive: bool = False,
) -> Callable:
    """
    Creates a decorator for applying a circuit breaker pattern to a function.

    Args:
        failure_threshold: The number of failures
            allowed before the circuit opens.
        recovery_timeout: The time window in seconds
            within which the circuit attempts recovery.
        replace_function: A function to replace the
            original function during circuit recovery.
        consecutive: A flag indicating whether consecutive
            failures should trigger a suspension or redirection.

    Returns:
        A decorator function that applies the circuit
            breaker logic to the decorated function.
    """

    def decorator(function):
        cb = CirBreak(
            failure_threshold,
            recovery_timeout,
            consecutive
            )

        @wraps(function)
        def wrapper(*args, **kwargs):
            return cb.call(
                function,
                *args,
                replace_function=replace_function,
                **kwargs)

        return wrapper

    return decorator


class CirBreak:
    """
    Circuit breaker implementation to control the flow of
        function calls based on failure thresholds and recovery timeouts.

    Args:
        failure_threshold: The number of failures
            allowed before the circuit opens.
        recovery_timeout: The time window in seconds
            within which the circuit attempts recovery.
        consecutive: A flag indicating whether consecutive
            failures should trigger a suspension or redirection.
    Methods:
        call(function, *args, replace_function=None, **kwargs):
            Executes the provided function, handling failures
            based on circuit state.
        is_open():
        Checks if the circuit is currently open based on the failure count.
        reset(): Resets the failure count and last failure time.
        attempt_recovery(replace_function, *args, **kwargs):
            Tries torecover the circuit within the defined timeout.
        record_failure():
            Records a failure, incrementing the failure count
            and updating the last failure time.
    """

    def __init__(
        self,
        failure_threshold: int = 3,
        recovery_timeout: int = 10,
        consecutive: bool = False,
    ) -> None:
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failure_count = 0
        self.last_failure_time = 0
        self.in_recovery = False
        self.consecutive = False
        self.consecutive = consecutive

    def call(
        self,
        function: Callable,
        *args: Any,
        replace_function: Optional[Callable] = None,
        **kwargs: Any
    ) -> Any:
        if self.is_open() and not self.attempt_recovery(
            replace_function, *args, **kwargs
        ):
            raise Exception("Circuit breaker is open (failed).")
        try:
            result = function(*args, **kwargs)
            if self.consecutive:
                self.reset()
            return result
        except Exception as e:
            self.record_failure()
            raise e

    def is_open(self) -> bool:
        return self.failure_count >= self.failure_threshold

    def reset(self) -> None:
        self.failure_count = 0
        self.last_failure_time = 0

    def attempt_recovery(
        self, replace_function: Optional[Callable], *args: Any, **kwargs: Any
    ) -> bool:
        if time.time() - self.last_failure_time < self.recovery_timeout:
            if replace_function and not self.in_recovery:
                self.in_recovery = True
                replace_function(*args, **kwargs)
                self.in_recovery = False
            return False
        self.reset()
        return True

    def record_failure(self) -> None:
        self.failure_count += 1
        self.last_failure_time = time.time()

