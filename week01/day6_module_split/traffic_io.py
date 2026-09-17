import csv
from traffic_stats import lane_statistics

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

def write_summary(stats: dict, path: str) -> None:
    rows = []
    for lane, s in stats.items():
        rows.append({"lane": lane, **s})
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["lane", "count", "average", "max", "min"])
        writer.writeheader()
        writer.writerows(rows)

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

if __name__ == "__name__":

    data_path =r"C:\Users\HSC\PyLearning\python-learning\traffic_raw.csv"
    records = read_records(data_path)

    stats = lane_statistics(records)
    summary_path = r"C:\Users\HSC\PyLearning\python-learning\lane_summary.csv"
    write_summary(stats, summary_path)

    overspeed_path = r"C:\Users\HSC\PyLearning\python-learning\overspeed.csv"
    write_overspeed(records, 60, overspeed_path)
