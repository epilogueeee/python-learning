from traffic_io import read_records

def group_by_lane(records: list) -> dict:
    """group by lane return {lane number: [all records of this lane]}"""
    result = {}
    for row in records:
        lane = row["lane"]
        if lane not in result:
            result[lane] = []
        result[lane].append(row)
    return result

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

def count_by_type(records: list) -> dict:
    """count numbers of each vehicle type"""
    counts = {}
    for row in records:
        vehicle_type = row["vehicle_type"]
        counts[vehicle_type] = counts.get(vehicle_type, 0) + 1
    return counts

if __name__ == "__name__":

    data_path =r"C:\Users\HSC\PyLearning\python-learning\traffic_raw.csv"
    records = read_records(data_path)

    grouped = group_by_lane(records)
    for lane in sorted(grouped):
        print(f"lane {lane}: {len(grouped[lane])}")

    print(lane_statistics(records))

    print(count_by_type(records))