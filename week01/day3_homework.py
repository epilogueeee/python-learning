speeds = [45, 62, 38, 71, 55, 83, 29, 67, 51, 44,
          76, 33, 58, 91, 42, 65, 37, 79, 48, 56]
limit = 50
bounds = [20, 40, 60, 80]

def count_overspeed(speeds: list, limit: float) -> tuple:
    """return overspeed number and percentage"""
    number = 0
    for s in speeds:
        if s > limit:
            number += 1
    percentage = number / len(speeds) * 100
    return number, percentage

def find_min_max(speeds: list) -> tuple:
    """return min and max speed"""
    min = speeds[0]
    max = speeds[0]
    for s in speeds:
        if s < min:
            min = s
        if s > max:
            max = s
    return min, max

def calculate_average(speeds: list) -> float:
    """return average speed"""
    if not speeds:
        return 0.0
    total = 0
    for s in speeds:
        total += s
    average = total / len(speeds)
    return average

def count_by_interval(speeds: list, bounds: list) -> list:
    """return count list by interval"""
    count = [0] * (len(bounds) + 1)
    for s in speeds:
        for i, upper in enumerate(bounds):
            if s < upper:
                count[i] += 1
                break
        else:
            count[-1] += 1
    return count

def locate_overspeed(speeds: list, limit: float) -> list:
    """return [(number, speed, overspeed amount),...]"""
    over_speed_vehicle = []
    for i, s in enumerate(speeds):
        if s > limit:
            over_speed_vehicle.append([i+1, s, s-limit])
    return over_speed_vehicle

def analyze_speeds(speeds: list, limit: float) ->dict:
    """return a dict that contain count, over_count, over_rate, average, min, max"""
    conclusion = {
        "count": len(speeds),
        "over_count": count_overspeed(speeds, limit)[0],
        "over_rate": count_overspeed(speeds, limit)[1],
        "average": calculate_average(speeds),
        "min": find_min_max(speeds)[0],
        "max": find_min_max(speeds)[1]
    }
    return conclusion

def print_report(stats: dict, counts: list, bounds: list) ->None:
    """print report"""
    print(stats)
    lower = 0
    for upper, i in zip(bounds, counts):
        print(f"[{lower}, {upper}], {i}, {'*'*i}\n")
        lower += 20
    print(f"[80,  ], {counts[-1]}, {'*'*counts[-1]}\n")

print_report(analyze_speeds(speeds, limit), count_by_interval(speeds, bounds), bounds)

x = 0
test_list = [0]
def test_field(test: list):
    x = 1
    test.append(1)
    return x, test

print(test_field(test_list))