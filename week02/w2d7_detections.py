detections = [
    {"cls": "car",        "conf": 0.92, "bbox": (100, 200, 180, 260)},
    {"cls": "truck",      "conf": 0.45, "bbox": (300, 150, 460, 280)},
    {"cls": "car",        "conf": 0.78, "bbox": (500, 210, 570, 265)},
    {"cls": "bus",        "conf": 0.88, "bbox": (50, 100, 250, 240)},
    {"cls": "car",        "conf": 0.33, "bbox": (620, 220, 660, 250)},
    {"cls": "motorcycle", "conf": 0.67, "bbox": (400, 300, 430, 340)},
    {"cls": "truck",      "conf": 0.81, "bbox": (700, 140, 880, 290)},
    {"cls": "car",        "conf": 0.95, "bbox": (250, 230, 320, 280)},
]

#B1
kept = list(filter(lambda detection: detection["conf"] >= 0.5, detections))
print(f"B1: {len(kept)} detections")

#B2
areas = [abs(x2 - x1) * abs(y2 - y1) for x1, y1, x2, y2 in (d["bbox"] for d in kept)]
print(f"B2: {areas}")

#B3
types = sorted({d["cls"] for d in kept})
print(f"B3: {types}")

#B4
counts = {c: sum(1 for d in kept if d["cls"] == c) for c in types}
print(f"B4: {counts}")

#B5
max_conf = {c: max(d["conf"] for d in kept if d["cls"] == c) for c in types}
print(f"B5: {max_conf}")

#B6
max_conf_3 = [(d["cls"], d["conf"]) for d in sorted(kept, key=lambda d: d["conf"], reverse=True)][:3]
print(f"B6: {max_conf_3}")

#B7
sort_2 = [(c, d["conf"]) for c in types for d in sorted(kept, key=lambda d: d["conf"], reverse=True) if d["cls"] == c]
print(f"B7: {sort_2}")

#B8
exceed = any(area > 20000 for area in areas)
print(f"B8: {exceed}")

#B9
kept_05 = all(d["conf"] >= 0.5 for d in kept)
detections_05 = all(d["conf"] >= 0.5 for d in detections)
print(f"B9: {kept_05} {detections_05}")

#B10
centers = [((x1 + x2) / 2, (y1 + y2) / 2) for x1, y1, x2, y2 in (d["bbox"] for d in kept)]
print(f"B10: {centers}")