import csv

class TrafficRecord:

    def __init__(self, time: str, lane: int, vehicle_type: str, speed: float):

        self.time = time
        self.lane = lane
        self.vehicle_type = vehicle_type
        self.speed = speed

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            data["time"],
            int(data["lane"]),
            data["vehicle_type"],
            float(data["speed"])
        )

class RecordSource:

    def load(self) -> list:
        """return TrafficRecord list"""
        raise NotImplementedError("子类必须实现 load")

    def describe(self) -> str:
        return f"{type(self).__name__}({len(self.load())} 条记录）"

class CsvSource(RecordSource):
    
    def __init__(self, path: str):
        self.path = path

    def load(self) -> list:
        with open(self.path, "r", encoding="utf-8") as f:
            records = []
            reader = csv.DictReader(f)
            for row in reader:
                record = TrafficRecord.from_dict(row)
                records.append(record)
        return records

class MemorySource(RecordSource):

    def __init__(self, records: list):
        self.records = records
    
    def load(self) -> list:
        return list(self.records)

class MultiSource(RecordSource):

    def __init__(self, sources: list):
        self.sources = sources

    def load(self) -> list:
        records = []
        for source in self.sources:
            records.extend(source.load())
        return records

