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