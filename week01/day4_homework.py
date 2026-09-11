intersection = {
    "north": {"morning": 320, "noon": 180, "evening": 410},
    "south": {"morning": 280, "noon": 195, "evening": 380},
    "east":  {"morning": 150, "noon": 120, "evening": 220},
    "west":  {"morning": 190, "noon": 140, "evening": 260},
}

def get_flow(data: dict, direction: str, period: str) -> int:
    """get flow of one direction and one period"""
    value = data.get(direction, {})
    flow = value.get(period, 0)
    return flow

print(get_flow(intersection, "south", "morning"))

def total_by_direction(data: dict) -> dict:
    """return total flow of every direction as {"north"}: 910 ..."""
    result = {}
    for direction, period in data.items():
        total = 0
        for flow in period.values():
            total += flow
        result[direction] = total
    return result

print(total_by_direction(intersection))

def total_by_period(data: dict) -> dict:
    """return total flow by every period as {"morning": 940 ...}"""
    result = {}
    for periods in data.values():
        for time, flow in periods.items():
            result[time] = result.get(time, 0) + flow
    return result

print(total_by_period(intersection))

def rank_directions(data: dict) -> list:
    """rank total flow in directions as [(number 1, north, 910 vehicles)]"""
    result = {}
    for direction, periods in data.items():
        result[direction] = sum(periods.values())
    ranked = sorted(result.items(), key=lambda item: item[1], reverse=True)
    return ranked

ranked = rank_directions(intersection)
for rank, (direction, total) in enumerate(ranked, start=1):
    print(f"number {rank}: {direction}, {total} vehicles")

def find_peak(data: dict) -> tuple:
    """return maximum flow as (direction, time, flow)"""
    max_flow = 0
    max_flow_time = None
    max_flow_direction = None
    for direction, periods in data.items():
        for time, flow in periods.items():
            if flow > max_flow:
                max_flow = flow
                max_flow_time = time
                max_flow_direction = direction
    return max_flow_direction, max_flow_time, max_flow

print(find_peak(intersection))

hourly = [45, 62, 38, 71, 55, 83, 29, 67, 51, 44,
          76, 33, 58, 91, 42, 65, 37, 79, 48, 56, 63, 88, 41, 52]

print(f"morning_0_5 = {hourly[:5]}")
print(f"morning_peak = {hourly[7:9]}")
print(f"last_3 = {hourly[-3:]}")
print(f"sample_2 = {hourly[::3]}")
print(f"reverse_list = {hourly[::-1]}")
print(f"early_half = {sum(hourly[:12])}")
print(f"later_half = {sum(hourly[12:])}")
if sum(hourly[:12]) > sum(hourly[12:]):
    print("early half is lager")
else:
    print("later half is larger")

records = ["car", "truck", "car", "bus", "car", "truck",
           "motorcycle", "car", "bus", "truck"]

def count_types(records: list) -> dict:
    """count numbers of each type vehicle and return a dict"""
    counts = {}
    for vehicle in records:
        counts[vehicle] = counts.get(vehicle, 0) + 1
    return counts

print(count_types(records))

def rank_counts(records: list) -> list:
    """rank the number of each type vehicle"""
    counts = count_types(records)
    ranked = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return ranked

print(rank_counts(records))

def percentage_vehicle(records: list) -> dict:
    counts = count_types(records)
    result = {}
    for vtype, number in counts.items():
        result[vtype] = number / len(records)
    return result

print(percentage_vehicle(records))

morning_plates = ["A123", "B456", "C789", "D000", "E111"]
evening_plates = ["B456", "C789", "F222", "G333"]

morning_plates_set = set(morning_plates)
evening_plates_set = set(evening_plates)
print(f"both morning and evening {morning_plates_set & evening_plates_set}")
print(f"only morning {morning_plates_set - evening_plates_set}")
print(f"total different vehicles {len(morning_plates_set | evening_plates_set)}")
print(f"no repeat in morning plates: {len(list(morning_plates_set)) == len(morning_plates)}")