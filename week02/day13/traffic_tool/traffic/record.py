from datetime import datetime

class TrafficRecord:
    """一条车辆检测记录"""

    VALID_TYPES = {"car", "truck", "bus", "motorcycle"}

    def __init__(self, time_str: str, lane: int, vehicle_type: str, speed: float):
        try:
            datetime.strptime(time_str, "%H:%M:%S")
        except ValueError:
            raise ValueError(f"时间格式应为 HH:MM:SS: {time_str}")
        if vehicle_type not in self.VALID_TYPES:
            raise ValueError(f"车型不在合法类型:{vehicle_type}")
        if lane < 1:
            raise ValueError(f"lane number is not correct: {lane}")
        if not isinstance(speed, float):
            raise TypeError(f"speed is not float: {speed}")
        if speed < 0:
            raise ValueError(f"speed is negative: {speed}")
        self.time = time_str
        self.lane = lane
        self.vehicle_type = vehicle_type
        self.speed = speed

    @classmethod
    def from_dict(cls, data: dict) -> "TrafficRecord":
        return cls(data["time"], data["lane"], data["vehicle_type"], data["speed"])

    @property
    def minute(self) -> str:    # "08:30"
        return self.time[:5]
                  
    @property
    def seconds_of_day(self) -> int:    # 30615
        return int(self.time[:2]) * 3600 + int(self.time[3:5]) * 60 + int((self.time[6:8]))      
    
    @property
    def speed_ms(self) -> float:    # m/s
        return self.speed / 3.6

    def is_overspeed(self, limit: float) -> bool:
        return self.speed > limit
    
    def over_by(self, limit: float) -> float:
        return max(0.0, self.speed - limit)
    
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