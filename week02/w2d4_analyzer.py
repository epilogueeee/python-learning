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

    def load(self):
        pass

class CsvSource(RecordSource):
    def __init__(self, path):
        self.path = path

    def load(self):
        result = []
        with open(self.path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for record in reader:
                result.append(TrafficRecord.from_dict(record))
        return result

class MemorySource(RecordSource):

    def __init__(self, records):
        self.records = records

    def load(self):
        return list(self.records)
class MultiSource(RecordSource):

    def __init__(self, sources):
        self.sources = sources

    def load(self):
        result = []
        for source in self.sources:
            result.append(source.load())
        return result
    
class TrafficAnalyzer:

    def __init__(self, source: RecordSource, limit: float = 60):
        self.source = source
        self.limit = limit
        self.records = source.load()

