import csv

def read_records(path: str) -> tuple:
    """return right list and wrong list with wrong information"""
    records = []
    errors = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for line_no, row in enumerate(reader, start=2):
                try:
                    time_str = row["time"]
                    lane = int(row["lane"])
                    vehicle_type = row["vehicle_type"].lower()
                    speed = float(row["speed"])
                    if speed < 0:
                        raise ValueError(f"speed is negative: {speed}")
                    records.append({
                        "time": time_str,
                        "lane": lane,
                        "vehicle_type": vehicle_type,
                        "speed": speed,
                    })
                except (ValueError, TypeError, AttributeError) as e:
                    errors.append((line_no, str(e)))
    except FileNotFoundError:
        print(f"cannot find file: {path}")
    return records, errors

path = "traffic_raw_wrong.csv"
records, errors = read_records(path)
print(f"correct records {len(records)}, wrong records {len(errors)}")
for line_no, msg in errors:
    print(f"number {line_no}: {msg}")

def lane_statistics(records: list) -> dict:
    speeds_by_lane = {}
    if not records:
        return {}
    for row in records:
        speeds_by_lane.setdefault(row["lane"], []).append(row["speed"])
    result = {}
    for lane, speeds in speeds_by_lane.items():
        result[lane] = {
            "count": len(speeds),
            "average": sum(speeds) / len(speeds),
            "max": max(speeds),
            "min": min(speeds),
        }
    return result

print(lane_statistics([]))
print(lane_statistics(records[:1]))

