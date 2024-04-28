# CircuitBreaker

This Python library provides a `circuit_breaker` decorator for implementing the circuit breaker pattern in your applications.

The circuit breaker pattern is a resiliency mechanism that helps protect external dependencies from cascading failures. It works by monitoring the success and failure rates of calls to a function and taking preventive measures to avoid overloading the dependency.

### How it Works

The `circuit_breaker` decorator takes several optional arguments:

* `failure_threshold`: The number of consecutive failures allowed before the circuit opens (defaults to 3).
* `recovery_timeout`: The time window in seconds after which the circuit attempts recovery (defaults to 10).
* `replace_function`:  A function to execute during the circuit open state. This function should accept the same arguments as the decorated function (optional).
* `consecutive`: A flag indicating whether consecutive failures trigger opening (defaults to False).

Here's a basic example of using the decorator:

```python
import time
from cirbreak import circuit_breaker

def replace(number):
    print("Another function", number)

@circuit_breaker(
    failure_threshold=5, recovery_timeout=10, replace_function=replace, consecutive=False
)
def test_circuit_breaker(number):
    if number % 3 == 0:
        raise Exception("Number is divisible by 3")
    else:
        print(number)

for i in range(1, 30):
    try:
        test_circuit_breaker(i)
    except Exception as e:
        print(e)
    time.sleep(1)
```

In this example, the replace function is provided as the replace_function argument to the circuit_breaker decorator. The replacement function should receive the same arguments as the decorated function. This setup allows for custom handling during the circuit open state, such as logging or alternative processing.
