# POO_RETO_3
Este es el reto 3 :)

Aqui explicare como hice las cosas generalmente:

Para el ejercicio en clase, cree lo que dice el ejercicio, es decir cree una clase linea, que tiene dos atributos de instancia que son el punto 1 y el punto 2 (estos pertenecen a la clase punto y por eso esto es composicion). Cabe aclarar que importo math porque me piden la pendiente en grados. 

```python
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
