rows = [
    ("08:30:15", 2, "car",   62.5),
    ("08:30:22", 1, "truck", 45.0),
    ("08:30:31", 2, "car",   78.3),
    ("08:30:40", 3, "bus",   55.1),
]
header = ("time", "lane", "vehicle_type", "speed")

records = [dict(zip(header, r)) for r in rows]
times, lane, vehicle, speed = zip(*rows)
avg_s = sum(speed) / len(speed)
header_wrong = ("time", "lane", "vehicle_type")
records_wrong = [dict(zip(header_wrong, r, strict=True)) for r in rows]