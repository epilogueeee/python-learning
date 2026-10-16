import csv
import random

random.seed(1)
with open("traffic_big.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["time", "lane", "vehicle_type", "speed"])
    for i in range(10000):
        h, m, s = 8 + i // 3600, (i // 60) % 60, i % 60
        if i % 997 == 0:      # 故意混入脏数据
            w.writerow([f"{h:02d}:{m:02d}:{s:02d}", "x", "car", "abc"])
            continue
        w.writerow([f"{h:02d}:{m:02d}:{s:02d}", random.randint(1, 3),
                    random.choice(["car", "truck", "bus"]),
                    round(random.uniform(30, 100), 1)])