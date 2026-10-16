import random
import time
import functools

#1
speeds = [62.5, 45.0, 78.3, 55.1, 91.2, 38.7, 66.0, 59.9]
limits = {"city": 50, "arterial": 60, "highway": 80}

def make_over_speed_checker(limit):
    def is_overspeed(speed):
        return speed > limit
    return is_overspeed

checkers = {lane_type: make_over_speed_checker(limit) for lane_type, limit in limits.items()}
overspeed_count = {lane_type: sum(1 for speed in speeds if judgement(speed)) for lane_type, judgement in checkers.items()}
print(overspeed_count)

#2
random.seed(0)
SPEEDS = [random.uniform(20, 120) for _ in range(1_000_000)]

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed_ms = (time.perf_counter() - start) * 1000
        print(f"[timer] {func.__name__} 耗时 {elapsed_ms:.1f} ms")
        return result
    return wrapper

@timer
def count_overspeed_loop(speeds, limit=60):
    total = 0
    for s in speeds:
        if s > limit:
            total += 1
    return total

@timer
def count_overspeed_gen(speeds, limit=60):
    return sum(1 for s in speeds if s > limit)

#3
def check_range(low, high):
    """检查第一个参数（车速列表）是否非空且都在 [low, high] 内"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(speeds, *args, **kwargs):
            if not speeds:
                raise ValueError(f"{func.__name__}: 车速列表为空")
            bad = [s for s in speeds if not low <= s <= high]
            if bad:
                raise ValueError(f"{func.__name__}: 车速超出 [{low}, {high}]：{bad}")
            return func(speeds, *args, **kwargs)
        return wrapper
    return decorator


@check_range(0, 250)
def average_speed(speeds):
    return sum(speeds) / len(speeds)


@check_range(0, 250)
def percentile(speeds, p=85):
    """第 p 百分位车速（交通工程常用 85 位车速）"""
    ordered = sorted(speeds)
    index = int(len(ordered) * p / 100)
    return ordered[min(index, len(ordered) - 1)]


print(average_speed([60, 70, 80]))          # 70.0
print(percentile([60, 70, 80, 90], p=50))   # 80

for call in (lambda: average_speed([60, -5, 300]), lambda: percentile([])):
    try:
        call()
    except ValueError as e:
        print("错误：", e)