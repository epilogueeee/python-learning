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

    def width(self) -> float:
        return self.x2 - self.x1

    def height(self) -> float:
        return self.y2 - self.y1

    def area(self) -> float:
        return self.width() * self.height()

    def center(self) -> tuple:
        return self.x1 + self.width() / 2, self.y1 + self.height() / 2

    def contains(self, x: float, y: float) -> bool:
        return x > self.x1 and x < self.x2 and y > self.y1 and y < self.y2

    def iou(self, other) -> float:
        left_up_x = max(self.x1, other.x1)
        left_up_y = max(self.y1, other.y1)
        right_down_x = min(self.x2, other.x2)
        right_down_y = min(self.y2, other.y2)
        if right_down_x - left_up_x < 0 or right_down_y - left_up_y < 0 :
            IoU = 0
        else:
            IoU = ((right_down_x - left_up_x) * (right_down_y - left_up_y)) / (self.area() + other.area() - (right_down_x - left_up_x) * (right_down_y - left_up_y))

        return IoU

if __name__ == "__main__":
    a = BoundingBox(0, 0, 10, 10)
    b = BoundingBox(5, 5, 15, 15)
    print(a.iou(b))
    print(a.iou(a))