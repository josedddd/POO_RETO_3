
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
