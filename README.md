# POO_RETO_3
Este es el reto 3 :)

Aqui explicare como hice las cosas generalmente:

# Ejercicio en clase
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
```
Y eso es todo, en el resto de codgio se inicializa el rectangulo añadiendo un cuarto metodo y ademas se añade la funcion de interference_line, que me dice si el rectangulo toca o no una recta, usando al metodo de la linea que se definio previamente: discretized line (muestra de composicion)
```python

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
```
# Restaurante

Con respecto al restaurante, en esta primera parte se hizo lo que las instrucciones decian, algo interesante es que al metodo calculate price, tiene como parametro la cantidad. Cabe aclarar que a cada clase la personalize un poco y le puse mas atributos de instancia, como salsa, o acompañamiento 
```python

class MenuItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def calculate_price(self, quantity: int) -> float:
        return self.price * quantity


class Beverage(MenuItem):
    def __init__(self, name, price, bottle_type: str, size: str):
        super().__init__(name, price)
        self.size = size
        self.bottle_type = bottle_type

    def with_ice(self, answer) -> str:
        if answer == "yes":
            return f"your {self.name} is with ice"
        elif answer == "no":
            return f"your {self.name} is without ice"


class Apetizer(MenuItem):
    def __init__(self, name, price, sauce: str):
        super().__init__(name, price)
        self.sauce = sauce


class Dessert(MenuItem):
    def __init__(self, name, price, flavour: str):
        super().__init__(name, price)
        self.flavour = flavour


class MainPlate(MenuItem):
    def __init__(self, name, price, accompaniment_1: str, accompaniment_2: str):
        super().__init__(name, price)
        self.accompaniment1 = accompaniment_1
        self.accompaniment2 = accompaniment_2
```


