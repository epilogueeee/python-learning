import csv
from itertools import islice

def read_records(path):
    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for n, row in enumerate(reader, start=2):
            try:
                record = {
                    "time": row["time"],
                    "lane": int(row["lane"]),
                    "vehicle_type": row["vehicle_type"],
                    "speed": float(row["speed"])
                }
            except (ValueError, KeyError):
                print(f"跳过第{n}行")
                continue
            yield record

def only_overspeed(records, limit):
    for record in records:
        if record["speed"] > limit:
            yield record

for r in islice(only_overspeed(read_records("traffic_big.csv"), 95), 3):
    print(r)

total = sum(1 for _ in only_overspeed(read_records("traffic_big.csv"), 95))
print(total) 

def fake_video(n_frames, fps=25):
    for i in range(n_frames):
        yield {"index": i, "timestamp": round(i / fps, 2)}

def batched(iterable, n):
    batch = []
    for x in iterable:
        batch.append(x)
        if len(batch) == n:
            yield batch
            batch = []
    if batch:
        yield batch

for batch in batched(fake_video(10), 4):
    print([f["index"] for f in batch], batch[0]["timestamp"])