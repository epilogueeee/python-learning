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

if __name__ == "__main__":

    r1 = TrafficRecord("08:10:55", 1, "car", 55.25)
    r2 = TrafficRecord("08:12:25", 2, "truck", 50.55)
    r3 = TrafficRecord("08:15:05", 3, "bus", 70.25)

    print(r3.is_overspeed(60))
    print(r3.over_by(60))
    print(r1.minute())
    print(r2.seconds_of_day())
    print(r1.speed_ms())
    print(r3.describe(60))