import csv

class TrafficRecord:

    VALID_TYPES = {"car", "truck", "bus", "motorcycle"}

    def __init__(self, time_str: str, lane: int, vehicle_type: str, speed: float):

        if speed < 0:
            raise ValueError(f"speed is negative {speed}")
        if lane < 1:
            raise ValueError(f"lane number smaller than 1 {lane}")
        if vehicle_type not in self.VALID_TYPES:
            raise ValueError(f"incorrect vehicle type {vehicle_type}")
        if len(time_str.split(":")) != 3:
            raise ValueError(f"time stamp not correct {time_str}")

        self.time = time_str
        self.lane = lane
        self.vehicle_type = vehicle_type.lower()
        self.speed = speed

    def is_overspeed(self, limit: float) -> bool:
        return self.speed > limit

    def over_by(self, limit) -> float:
        return max(0.0, self.speed - limit)

    def minute(self) -> str:
        return self.time[:5]

    def seconds_of_day(self) -> int:
        return int(self.time[:2]) * 3600 + int(self.time[3:5]) * 60 + int(self.time[6:8])

    def speed_ms(self) -> float:
        return self.speed / 3.6

    def describe(self, limit: float) -> str:
        status = f"超速 {self.over_by(limit):.1f}" if self.is_overspeed(limit) else "正常"
        return f"{self.time} 车道{self.lane} {self.vehicle_type} {self.speed} km/h({status})"

def read_records(path: str) -> tuple:
    """return right list and wrong list with wrong information"""
    records = []
    errors = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for line_no, row in enumerate(reader, start=2):
                try:
                    record = TrafficRecord(
                        row["time"],
                        int(row["lane"]),
                        row["vehicle_type"],
                        float(row["speed"]),
                    )
                    records.append(record)
                except (ValueError, TypeError, AttributeError) as e:
                    errors.append((line_no, str(e)))
    except FileNotFoundError:
        print(f"cannot find file: {path}")
    except UnicodeDecodeError:
        print(f"file is not UTF-8 encoded: {path}")

    return records, errors

class TrafficDataset:

    def __init__(self, records: list, errors: list = None):
        self.records = records
        self.errors = [] if errors is None else errors

    @staticmethod
    def from_csv(path: str) -> "TrafficDataset":
        records, errors = read_records(path)
        return TrafficDataset(records, errors)

    def __repr__(self):
        return f"TrafficDataset {len(self.records)} records"

    def __len__(self):
        return len(self.records)

    def __getitem__(self, key):
        return self.records[key]

    def __contains__(self, item):
        return item in self.records

    def filter_by_lane(self, lane: int):
        return TrafficDataset(r for r in self.records if r.lane == lane)

    def filter_by_type(self, type: str):
        return TrafficDataset(r for r in self.records if r.vehicle_type == type)

    def filter_overspeed(self, limit: float):
        return TrafficDataset(r for r in self.records if r.speed > limit)

    def filter_by_minute(self, minute: str):
        return TrafficDataset(r for r in self.records if r.time[:5] == minute)
    
    def lane_statistics(self) -> dict:
        speeds_by_lane = {}
        for r in self.records:
            speeds_by_lane.setdefault(r.lane, []).append(r.speed)

        return {
            lane: {
                "count": len(speeds),
                "average": sum(speeds) / len(speeds),
                "max": max(speeds),
                "min": min(speeds),
            }
            for lane, speeds in speeds_by_lane.items()
        }

    def count_by_type(self) -> dict:
        counts = {}
        for r in self.records:
            counts[r.vehicle_type] = counts.get(r.vehicle_type, 0) + 1
        return counts

    def average_speed_by_type(self) -> dict:
        speeds_by_type = {}
        for r in self.records:
            speeds_by_type.setdefault(r.vehicle_type, []).append(r.speed)
        return {t: sum(s) / len(s) for t, s in speeds_by_type.items()}

    def flow_by_minute(self) -> dict:
        flow = {}
        for r in self.records:
            minute = r.minute()
            flow[minute] = flow.get(minute, 0) + 1
        return flow

    def peak_minute(self) -> tuple:
        flow = self.flow_by_minute()
        if not flow:
            return None, 0
        return max(flow.items(), key=lambda item: item[1])


if __name__ == "__main__":
    ds = TrafficDataset.from_csv("traffic_raw.csv")

    print(ds, len(ds))
    print(ds[0])
    print(ds[:3], type(ds[:3]))
    print(ds[0] in ds)
    print(bool(TrafficDataset([])))

    print(len(ds.filter_by_lane(2).filter_overspeed(60)))
    print(len(ds))                

    print(ds.lane_statistics())
    print(ds.count_by_type())
    print(ds.peak_minute())