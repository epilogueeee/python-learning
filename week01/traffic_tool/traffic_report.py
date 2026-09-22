def print_errors(errors: list) -> None:
    if not errors:
        print("no data error found")
        return

    print(f"skipped {len(errors)} invalid records:")
    for line_no, msg in errors:
        print(f"  line {line_no}: {msg}")


def print_lane_table(stats: dict) -> None:
    if not stats:
        print("no lane data")
        return

    header = f"{'lane':<6}{'count':>7}{'average':>10}{'max':>8}{'min':>8}"
    print(header)
    print("-" * len(header))

    for lane in sorted(stats):
        s = stats[lane]
        print(f"{lane:<6}{s['count']:>7}{s['average']:>10.1f}"
              f"{s['max']:>8.1f}{s['min']:>8.1f}")


def print_type_table(counts: dict, averages: dict) -> None:
    if not counts:
        print("no vehicle type data")
        return

    total = sum(counts.values())

    header = f"{'type':<14}{'count':>7}{'ratio':>9}{'avg speed':>12}"
    print(header)
    print("-" * len(header))

    for vehicle_type in sorted(counts):
        count = counts[vehicle_type]
        ratio = count / total
        avg = averages.get(vehicle_type, 0.0)
        print(f"{vehicle_type:<14}{count:>7}{ratio:>9.1%}{avg:>12.2f}")


def print_overspeed_list(records: list, limit: float) -> None:
    overspeed = [r for r in records if r["speed"] > limit]

    if not overspeed:
        print(f"no vehicle over {limit} km/h")
        return

    print(f"{len(overspeed)} vehicles over {limit} km/h:")
    header = f"{'time':<12}{'lane':>6}{'type':>12}{'speed':>9}{'over by':>10}"
    print(header)
    print("-" * len(header))

    for r in sorted(overspeed, key=lambda x: x["speed"], reverse=True):
        over_by = r["speed"] - limit
        print(f"{r['time']:<12}{r['lane']:>6}{r['vehicle_type']:>12}"
              f"{r['speed']:>9.1f}{over_by:>10.1f}")

def print_flow_distribution(flow: dict, max_flow: tuple) -> None:
    block = "\u2588"
    for minute, number in flow.items():
        if minute == max_flow[0]:
            print(f"{minute} {block * number} {number} <- peak")
        else:
            print(f"{minute} {block * number} {number}")

if __name__ == "__main__":
    
    fake_stats = {
        1: {"count": 17, "average": 51.176, "max": 95.2, "min": 20.2},
        2: {"count": 10, "average": 54.27, "max": 88.5, "min": 27.8},
    }
    fake_counts = {"car": 15, "truck": 21, "bus": 14}
    fake_averages = {"car": 55.78, "truck": 52.8, "bus": 47.81}
    fake_errors = [(5, "could not convert string to float: ''"),
                   (10, "speed is negative: -95.2")]
    fake_records = [
        {"time": "08:30:15", "lane": 2, "vehicle_type": "car", "speed": 82.5},
        {"time": "08:31:02", "lane": 1, "vehicle_type": "truck", "speed": 65.3},
        {"time": "08:31:40", "lane": 3, "vehicle_type": "bus", "speed": 45.0},
    ]

    print_errors(fake_errors)
    print()
    print_lane_table(fake_stats)
    print()
    print_type_table(fake_counts, fake_averages)
    print()
    print_overspeed_list(fake_records, 60)