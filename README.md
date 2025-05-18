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

```
Ahora bien, para las otras dos funciones de "vertical cross" y de "horizontal cross", el metodo mas sencillo para resolverlo es ver si el punto incial y final pasan por 0, ya que ambos son atributos de instancia. (Yo se que es un poco como trampa, pero cumple su funcion y es el metodo mas rapido)
```python
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
```
En consiguiente este codigo coresponde al metodo opcional el cual era discretizar la linea (con esto tambien se puede calcular el vertical cross y el horizontal cross) Lo que Hago aqui es primero defino la pendiente, y creo los intervalos (o steps) en los que quiero que la linea sea discretizada 
```python

 def discretized_line(self, distance: int) -> list:
        x_start = self.point_start.x
        x_end = self.point_end.x
        delta_x = x_end - x_start
        step = delta_x / (distance - 1)
        x_values = [x_start + i * step for i in range(distance)]
        y_values = [ self.point_start.y + (x) * math.tan(self.slope) for x in x_values]
        return list(zip(x_values, y_values))
