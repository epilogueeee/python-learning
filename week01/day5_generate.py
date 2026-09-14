import random
import csv

with open("traffic_raw.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["time", "lane", "vehicle_type", "speed"])
    i = 0
    start = 8 * 3600 + 30 * 60
    for i in range(50):
        now = start + i * 3
        h = now // 3600
        m = (now % 3600) // 60
        s = now % 60
        time_str = f"{h:02d}:{m:02d}:{s:02d}"
        lane_str = str(random.randint(1, 4))
        vehicle_type_str = random.choice(["car", "truck", "bus"])
        speed_str = str(round(random.uniform(20, 100), 1))
        writer.writerow([time_str, lane_str, vehicle_type_str, speed_str])
        i += 1

