import csv
from datetime import datetime

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

def write_type_summary(counts: dict, averages: dict, path: str) -> None:

    total = sum(counts.values())

    rows = []
    for vehicle_type in sorted(counts):
        count = counts[vehicle_type]
        rows.append({
            "vehicle_type": vehicle_type,
            "count": count,
            "ratio_percent": round(count / total * 100, 1),
            "avg_speed": round(averages.get(vehicle_type, 0.0), 1),
        })

    fieldnames = ["vehicle_type", "count", "ratio_percent", "avg_speed"]
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def write_error_log(errors: list, input_path: str, path: str) -> None:
    
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(path, "w", encoding="utf-8") as f:
    
        f.write("# 数据异常日志\n")
        f.write(f"# 输入文件：{input_path}\n")
        f.write(f"# 生成时间：{now}\n")
        f.write(f"# 异常行数：{len(errors)}\n\n")

        if not errors:
            f.write("没有发现异常数据\n")
            return

        for line_no, msg in errors:
            f.write(f"第 {line_no:<4} 行  {msg}\n")

if __name__ == "__name__":

    from traffic_stats import lane_statistics
    data_path =r"C:\Users\HSC\PyLearning\python-learning\traffic_raw.csv"
    records = read_records(data_path)

    stats = lane_statistics(records)
    summary_path = r"C:\Users\HSC\PyLearning\python-learning\lane_summary.csv"
    write_summary(stats, summary_path)

    overspeed_path = r"C:\Users\HSC\PyLearning\python-learning\overspeed.csv"
    write_overspeed(records, 60, overspeed_path)
