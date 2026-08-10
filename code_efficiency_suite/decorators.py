# decorators.py
from collections.abc import Callable
from typing import Any

from decorator import decorator

from .metrics.code_size import analyze_code_size
from .metrics.memory import measure_memory
from .metrics.size import measure_size
from .metrics.speed import measure_speed
from .metrics.system import system_info
from .regression.line import regression_point
from .utils.conditions import check_condition


def suite_test(
    speed: str | None = None,
    memory: str | None = None,
    size: str | None = None,
    code: str | None = None
) -> Callable[[Callable[..., Any]], Callable[..., dict[str, Any]]]:
    @decorator
    def wrapper(func, *args, **kwargs):

        # 1) SPEED
        t = measure_speed(func, *args, **kwargs)

        # 2) MEMORY
        mem = measure_memory(func, *args, **kwargs)

        # 3) SIZE (object)
        obj = func(*args, **kwargs)
        obj_size = measure_size(obj)

        # 4) CODE SIZE (disk + RAM)
        if code:
            code_stats = analyze_code_size(code)
        else:
            code_stats = None

        # 5) SYSTEM INFO (single/multi)
        sysinfo = system_info()

        # 6) REGRESSION POINT
        reg = regression_point(t)

        # 7) CONDITIONS
        results = {
            "speed": check_condition(t, speed),
            "memory": check_condition(mem, memory),
            "size": check_condition(obj_size, size)
        }

        return {
            "time": t,
            "memory": mem,
            "size": obj_size,
            "code": code_stats,
            "system": sysinfo,
            "regression": reg,
            "results": results
        }

    return wrapper
