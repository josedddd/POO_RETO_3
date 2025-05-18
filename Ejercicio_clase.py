import math


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line():
    def __init__(self, point_start: Point, point_end: Point):
        self.point_start = point_start
        self.point_end = point_end
        self.slope = math.atan2((point_end.y - point_start.y),(point_end.x - point_start.x))
        self.slope_degrees = math.degrees(self.slope)
        self.length = ((point_end.x - point_start.x) ** 2 + (point_end.y - point_start.y) ** 2) ** 0.5

    def compute_slope(self) -> float:
        return self.slope_degrees

    def compute_length(self) -> float:
        return self.length

    def compute_vertical_cross(self) -> bool:
        if self.point_start.x <= 0 <= self.point_end.x:
            return True
        else:
            return False

    def compute_horizontal_cross(self) -> bool:
        if self.point_start.y <= 0 <= self.point_end.y:
            return True
        else:
            return False

    def discretized_line(self, distance: int) -> list:
        x_start = self.point_start.x
        x_end = self.point_end.x
        delta_x = x_end - x_start
        step = delta_x / (distance - 1)
        x_values = [x_start + i * step for i in range(distance)]
        y_values = [ self.point_start.y + (x) * math.tan(self.slope) for x in x_values]
        return list[x_values, y_values]


class Rectangle():
    def __init__(self, width: float, height: float, point_center: Point, method: int):
        self.height = height
        self.width = width
        if method == 1:
            self.point_left_down = Point(point_center.x - width / 2,
                                         point_center.y - height / 2)
        elif method == 2:
            self.point_center = point_center
            self.point_left_down = Point(point_center.x - width / 2,
                                         point_center.y - height / 2)
        elif method == 3:
            self.point_left_down = Point(point_center.x - width / 2,
                                         point_center.y - height / 2)
            self.point_right_up = Point(point_center.x + width / 2,
                                        point_center.y + height / 2)
        elif method == 4:
            self.point_right_up = Point(point_center.x + width / 2,
                                        point_center.y + height / 2)
            self.point_right_down = Point(point_center.x + width / 2,
                                          point_center.y - height / 2)
            self.point_left_down = Point(point_center.x - width / 2,
                                        point_center.y - height / 2)
            self.point_left_up = Point(point_center.x - width / 2,
                                       point_center.y + height / 2)

            self.LineH_up = Line(self.point_left_up, self.point_right_up)
            self.LineH_down = Line(self.point_left_down, self.point_right_down)
            self.LineV_right = Line(self.point_right_down, self.point_right_up)
            self.LineV_left = Line(self.point_left_down, self.point_left_up)

    def compute_area(self) -> float:
        area = self.width * self.height
        return area

    def compute_perimeter(self) -> float:
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def compute_interference_point(self, point: Point) -> bool:
        if (self.point_left_down.x <= point.x <= self.point_right_down.x and
                self.point_left_down.y <= point.y <= self.point_left_up.y):
            return True
        else:
            return False
        
    def compute_interference_line(self, line:Line) -> bool :
        discretized_line=line.discretized_line(distance=100)
        for x,y in discretized_line:
            if y>= self.height+self.point_left_down.y:
                return True
        return False

