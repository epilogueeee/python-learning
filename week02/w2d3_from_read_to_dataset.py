import csv

class TrafficRecord:

    def __init__(self, time: str, lane: int, vehicle_type: str, speed: float):

        self.time = time
        self.lane = lane
        self.vehicle_type = vehicle_type
        self.speed = speed

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError(f"speed must be a number")
        if value < 0:
            raise ValueError(f"speed must be positive")
        self._speed = float(value)

    @property
    def minute(self):
        return self.time[:5]

    @property
    def speed_ms(self):
        return self.speed / 3.6

    @property
    def seconds_of_day(self):
        return int(self.time[:2]) * 3600 + int(self.time[3:5]) * 60 + int(self.time[6:8])

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            data["time"],
            int(data["lane"]),
            data["vehicle_type"],
            float(data["speed"])
        )

def read_records(path: str) -> list:
    with open(path, "r", encoding="utf-8") as f:
        records = []
        reader = csv.DictReader(f)
        for row in reader:
            record = TrafficRecord.from_dict(row)
            records.append(record)
    return records

class TrafficDataset:

    def __init__(self, records: list):
        self.records = records

    @classmethod
    def from_csv(cls, path: str):
        records = read_records(path)
        return cls(records)

    @property
    def speeds(self):
        return [r.speed for r in self.records]

    @property
    def is_empty(self):
        return self.records == []

    @classmethod
    def from_csv_files(cls, paths: list):
        records = []
        for path in paths:
            records.extend(read_records(path))
        return cls(records)

class BoundingBox:

    def __init__(self, x1: float, y1: float, x2: float, y2: float, label: str = "", conf: float = 1.0):

        if x1 > x2 or y1 > y2:
            raise ValueError(f"box location incorrect")
        if conf < 0 or conf > 1:
            raise ValueError(f"conf incorrect")

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.label = label
        self.conf = conf

    @property
    def width(self):
        return self.x2 - self.x1

    @property
    def height(self):
        return self.y2 - self.y1

    @property
    def area(self):
        return self.width * self.height

    @property
    def center(self):
        return self.x1 + self.width / 2, self.y1 + self.height / 2

    @classmethod
    def from_xywh(cls, x: float, y: float, w: float, h: float, **kwargs):
        return cls(x - w / 2, y - h / 2, x + w / 2, y + h / 2, **kwargs)
    