# CircuitBreaker

This Python library provides a `circuit_breaker` decorator for implementing the circuit breaker pattern in your applications.

The circuit breaker pattern is a resiliency mechanism that helps protect external dependencies from cascading failures. It works by monitoring the success and failure rates of calls to a function and taking preventive measures to avoid overloading the dependency.

### How it Works

The `circuit_breaker` decorator takes several optional arguments:

* `failure_threshold`: The number of consecutive failures allowed before the circuit opens (defaults to 3).
* `recovery_timeout`: The time window in seconds after which the circuit attempts recovery (defaults to 10).
* `replace_function`: A function to execute during circuit open state (optional).
* `consecutive`: A flag indicating whether consecutive failures trigger opening (defaults to False).

Here's a basic example of using the decorator:

```python
from cirbreak import circuit_breaker

@circuit_breaker(failure_threshold=5)
def external_call():
    # Simulate a call to an external service
    if random.random() > 0.5:
        raise Exception("External service error")
    return "Success!"

try:
    response = external_call()
    print(response)
except Exception as e:
    print(f"Error: {e}")
