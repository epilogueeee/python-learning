import csv

data_path =r"C:\Users\HSC\PyLearning\python-learning\traffic_raw.csv"

def read_records(path: str) -> list:
    """read csv file and return a list which contain dict"""
    with open(path, "r", encoding="utf-8") as f:
        out = []
        reader = csv.DictReader(f)
        for row in reader:
            out.append({
                "time": row["time"], 
                "lane": int(row["lane"]), 
                "vehicle_type": row["vehicle_type"].lower(), 
                "speed": float(row["speed"]),
            })
    return out

records = read_records(data_path)

def group_by_lane(records: list) -> dict:
    """group by lane return {lane number: [all records of this lane]}"""
    result = {}
    for row in records:
        lane = row["lane"]
        if lane not in result:
            result[lane] = []
        result[lane].append(row)
    return result

grouped = group_by_lane(records)
for lane in sorted(grouped):
    print(f"lane {lane}: {len(grouped[lane])}")

def lane_statistics(records: list) -> dict:
    """return {lane number: {"count": n, "average": x, "max": y, "min": z}}"""
    result = {}
    speed_result = {}
    for row in records:
        lane = row["lane"]
        speed = row["speed"]
        speed_result.setdefault(lane, []).append(speed)
    for number, stats in speed_result.items():
        result[number] = {
            "count": len(stats),
            "average": sum(stats) / len(stats),
            "max": max(stats),
            "min": min(stats)
        }
    return result

print(lane_statistics(records))

def count_by_type(records: list) -> dict:
    """count numbers of each vehicle type"""
    counts = {}
    for row in records:
        vehicle_type = row["vehicle_type"]
        counts[vehicle_type] = counts.get(vehicle_type, 0) + 1
    return counts

print(count_by_type(records))

def average_speed_by_type(records: list) -> dict:
    """return avrage speed of each type vehicle"""
    result_speeds = {}
    result = {}
    for row in records:
        vehicle_type = row["vehicle_type"]
        speed = row["speed"]
        result_speeds.setdefault(vehicle_type, []).append(speed)
    for vehicle_type, speeds in result_speeds.items():
        result[vehicle_type] = sum(speeds) / len(speeds)
    return result

print(average_speed_by_type(records))

def write_summary(stats: dict, path: str) -> None:
    rows = []
    for lane, s in stats.items():
        rows.append({"lane": lane, **s})
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["lane", "count", "average", "max", "min"])
        writer.writeheader()
        writer.writerows(rows)

stats = lane_statistics(records)
summary_path = r"C:\Users\HSC\PyLearning\python-learning\lane_summary.csv"
write_summary(stats, summary_path)

def write_overspeed(records: list, limit: float, path: str) -> None:
    """write all overspeed records into a new csv and add over_by"""
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["time", "lane", "vehicle_type", "speed", "over_by"])
        writer.writeheader()
        for row in records:
            if row["speed"] > limit:
                new_row = row.copy()
                new_row["over_by"] = round((row["speed"] - limit), 1)
                writer.writerow(new_row)

overspeed_path = r"C:\Users\HSC\PyLearning\python-learning\overspeed.csv"
write_overspeed(records, 60, overspeed_path)

print(f"{'lane':<6}{'count':>7}{'average':>10}{'max':>8}{'min':>8}")
print("-" * 39)

for lane in sorted(stats):
    s = stats[lane]
    print(f"{lane:<6}{s['count']:>7}{s['average']:>10.1f}"
          f"{s['max']:>8.1f}{s['min']:>8.1f}")