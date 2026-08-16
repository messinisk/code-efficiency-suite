"""
Αυτή η ενότητα κώδικα περιέχει τη class SuiteMetryx \n\
και suite_test που ειναι decorator για τη μέτρηση της απόδοσης των συναρτήσεων.

user code:

@suite_test()
def fsum(n: int) -> float:
  return sum(i for i in range(n))

run :
print("fsum(100)", fsum(100))
print("fsum(1_000)", fsum(1_000))
print("fsum(10_000)", fsum(10_000))
print("fsum(100_000)", fsum(100_000))
print("fsum(1_000_000)", fsum(1_000_000))

output:

  fsum(100) {'speed': Decimal('0.00004940000053466065'), 'memory': Decimal('0.00037384033203125'), 'size': Decimal('28')}
  fsum(1_000) {'speed': Decimal('0.0006408089993783506'), 'memory': Decimal('0.00043487548828125'), 'size': Decimal('28')}
  fsum(10_000) {'speed': Decimal('0.00752489099977538'), 'memory': Decimal('0.0008249282836914062'), 'size': Decimal('28')}
  fsum(100_000) {'speed': Decimal('0.08154692100015382'), 'memory': Decimal('0.0025577545166015625'), 'size': Decimal('32')}
  fsum(1_000_000) {'speed': Decimal('0.7673067390005599'), 'memory': Decimal('0.0036478042602539062'), 'size': Decimal('32')}
"""




from collections.abc import Callable
from typing import Any
from decorator import decorator
from dataclasses import dataclass
from decimal import Decimal
import time
import tracemalloc
# Import sys for sys.getsizeof()
import sys 

@dataclass
class SuiteMetryx:
  """Added default None for easier instance creation"""
  speed: Decimal | None = None 
  memory: Decimal | None = None
  size: Decimal | None = None

# A global instance of SuiteMetryx to hold the current metrics.
# You can set its attributes (e.g., _global_suite_metrics.speed = Decimal('...'))
# before calling a decorated function.
_global_suite_metrics = SuiteMetryx()

def suite_test() -> Callable[[Callable[..., Any]],
                             Callable[..., dict[str, Any]]]:
  """A decorator factory to add metadata to a function's output."""

  @decorator # Apply @decorator to the actual wrapper function
  def _decorator(func: Callable[..., Any], *args: Any, **kwargs: Any) -> dict[str, Any]:
    # This _decorator function now directly acts as the wrapper, thanks to @decorator.
    # It receives the decorated function (func) and its arguments.

    # Measure speed
    start_time = time.perf_counter()

    # Measure memory
    tracemalloc.start()

    result = func(*args, **kwargs) # Execute the original function

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.perf_counter()

    # Calculate size of the returned object in bytes
    object_size = sys.getsizeof(result)

    _global_suite_metrics.speed = Decimal(str(end_time - start_time)) # Convert to Decimal
    _global_suite_metrics.memory = Decimal(str(peak / (1024 * 1024))) # Peak memory in MB, converted to Decimal
    _global_suite_metrics.size = Decimal(str(object_size)) # Size in bytes, converted to Decimal

    # IMPORTANT: The user's previous request was NOT to return 'result'.
    # If 'result' is desired in the output dictionary, please let me know.
    return {
        "speed": _global_suite_metrics.speed,
        "memory": _global_suite_metrics.memory,
        "size": _global_suite_metrics.size,
    }
  return _decorator
