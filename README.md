# POO_RETO_3

Este es el reto 3 :)

Aquí explicaré cómo hice las cosas generalmente:

# Ejercicio en clase

Para el ejercicio en clase, creé lo que dice el ejercicio, es decir, una clase **Línea**, que tiene dos atributos de instancia: el punto 1 y el punto 2 (estos pertenecen a la clase **Punto** y por eso esto es composición). Cabe aclarar que importo `math` porque me piden la pendiente en grados.

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
Ahora bien, para las otras dos funciones de "vertical cross" y "horizontal cross", el método más sencillo para resolverlo es ver si el punto inicial y final pasan por 0, ya que ambos son atributos de instancia. (Sé que es un poco como trampa, pero cumple su función y es el método más rápido).

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
Y eso es todo. En el resto del código se inicializa el rectángulo añadiendo un cuarto método y además se añade la función `interference_line`, que me dice si el rectángulo toca o no una recta, usando el método de la línea que se definió previamente: `discretized_line` (muestra de composición). 

Cabe mencionar que las funciones de intersección con un punto o una línea solo sirven si se inicializa con el método 3 o 4, así que se recomienda utilizar estos (no quise cambiarlo, perdón ;().


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

Con respecto al restaurante, primero creé el diagrama UML para tener un mejor contexto de las relaciones entre clases y luego se hizo lo que las instrucciones decían. Algo interesante es que el método `calculate_price` tiene como parámetro la cantidad, algo que se utilizará más adelante para calcular la cuenta total. 

Además, se hacen las relaciones de herencia como indica la instrucción (todos los ítems heredan de `MenuItem`). Cabe aclarar que a cada clase la personalicé un poco y le puse más atributos de instancia, como salsa o acompañamiento.

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
Por último, en la clase `Order` uso composición para crear una lista con los pedidos. Además, utilizo un ciclo `for` para ir sumando el total de la cuenta. Por último, aplico tres descuentos: uno por la cantidad de elementos (para esto se usa el parámetro `quantity`) y los otros dos por "combo", es decir, por productos específicos.
```python

class Order:
    def __init__(self, number):
        self.number = number
        self.order = []

    def add_items(self, menu_item: MenuItem, quantity: int) -> list:
        self.order.append((menu_item, quantity))

    def show_order(self) -> list:
        return [f"{item.name}, {quantity}" for item, quantity in self.order]

    def calculate_bill(self) -> str:
        real_bill = 0
        total_quantity = 0
        names = []
        for menu_item, quantity in self.order:
            names.append(menu_item.name)
            real_bill += menu_item.calculate_price(quantity)
            total_quantity += quantity

        discount_options = [real_bill]
        if total_quantity >= 10:
            discount_options.append(real_bill * 0.9)
        if "Hamburger" in names and "Coca_cola" in names:
            discount_options.append(real_bill * 0.7)
        elif "Ice_cream" in names and "Chocolate_cake" in names:
            discount_options.append(real_bill * 0.8)

        discount_bill = min(discount_options)
        return f"Valor sin descuento {round(real_bill, 2)}, Valor con descuento {round(discount_bill, 2)}"
 ```
Creo el menu y un ejemplo de que el codigo si funciona.
```python

##Menu
## Bebidas
Coca_cola = Beverage(name="Coca Cola", price=5.00, bottle_type="glass", size="medium")
Lemonade = Beverage(name="Lemonade", price=4.00, bottle_type="plastic", size="big")
Iced_Tea = Beverage(name="Iced Tea", price=4.50, bottle_type="glass", size="small")
Orange_Juice = Beverage(name="Orange Juice", price=6.00, bottle_type="glass", size="big")

# Postres
Ice_cream_vanilla = Dessert(name="Ice Cream", price=7.00, flavour="vanilla")
Chocolate_cake = Dessert(name="Chocolate Cake", price=8.00, flavour="chocolate")
Cheesecake_strawberry = Dessert(name="Cheesecake", price=9.00, flavour="strawberry")

# Aperitivos
Potato_chips_Tomato = Apetizer(name="Potato Chips", price=3.00, sauce="Tomato")
Nachos_Cheese = Apetizer(name="Nachos", price=4.50, sauce="Cheese")
Onion_rings_BBQ = Apetizer(name="Onion Rings", price=4.00, sauce="BBQ")
Garlic_bread_Garlic = Apetizer(name="Garlic Bread", price=3.50, sauce="Garlic")

# Platos fuertes
Hamburger_fries_salad = MainPlate(name="Hamburger", price=10.00, accompaniment_1="fries", accompaniment_2="salad")
Grilled_Chicken_rice_vegetables = MainPlate(name="Grilled Chicken", price=12.00, accompaniment_1="rice", accompaniment_2="vegetables")
Pasta_Bolognese_bread_parmesan = MainPlate(name="Pasta Bolognese", price=11.00, accompaniment_1="bread", accompaniment_2="parmesan")
Steak_mashed_grilled = MainPlate(name="Steak", price=15.00, accompaniment_1="mashed potatoes", accompaniment_2="grilled vegetables")

# Creo una orden de ejemplo
order1 = Order(1)
order1.add_items(Coca_cola, 2)
order1.add_items(Ice_cream_vanilla, 4)
order1.add_items(Potato_chips_Tomato, 6)
order1.add_items(Hamburger_fries_salad, 7)

#Verifico que funcione correctamente
print(order1.show_order())
print(order1.calculate_bill())
```
