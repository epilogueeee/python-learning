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

    def __repr__(self):
        return f"TrafficRecord('{self.time}', {self.lane}, '{self.vehicle_type}', {self.speed})"

    def __str__(self):
        return f"{self.time} lane{self.lane} {self.vehicle_type} {self.speed}km/h"

    def __eq__(self, value):
        if not isinstance(value, TrafficRecord):
            return NotImplemented
        return(
            self.time == value.time
            and self.lane == value.lane
            and self.vehicle_type == value.vehicle_type
            and self.speed == value.speed
        )

    def ___hash__(self):
        return hash((self.time, self.lane, self.vehicle_type, self.speed))

    def __lt__(self, other):
        if not isinstance(other, TrafficRecord):
            return NotImplemented
        return self.speed < other.speed
    

if __name__ == "__main__":

    r1 = TrafficRecord("08:10:55", 1, "car", 55.25)
    r2 = TrafficRecord("08:12:25", 2, "truck", 50.55)
    r3 = TrafficRecord("08:15:05", 3, "bus", 70.25)
    print(r1)
    print(repr(r1))
    print([r1, r2])
    print(f"{r1}")