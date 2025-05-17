
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
            discount_options.append(real_bill * 0.82)

        discount_bill = min(discount_options)
        return f"Valor sin descuento {round(real_bill, 2)}, Valor con descuento {round(discount_bill, 2)}"


#Menu
# Bebidas
drink1 = Beverage(name="Coca_cola", price=5.00, bottle_type="glass", size="medium")
drink2 = Beverage(name="Lemonade", price=4.00, bottle_type="plastic", size="big")
drink3 = Beverage(name="Iced_Tea", price=4.50, bottle_type="glass", size="small")
drink4 = Beverage(name="Orange_Juice", price=6.00, bottle_type="glass", size="big")

# Postres
dessert1 = Dessert(name="Ice_cream", price=7.00, flavour="vanilla")
dessert2 = Dessert(name="Chocolate_cake", price=8.00, flavour="chocolate")
dessert3 = Dessert(name="Cheesecake", price=9.00, flavour="strawberry")

# Aperitivos
apetizer1 = Apetizer(name="Potato_chips", price=3.00, sauce="Tomato")
apetizer2 = Apetizer(name="Nachos", price=4.50, sauce="Cheese")
apetizer3 = Apetizer(name="Onion_rings", price=4.00, sauce="BBQ")
apetizer4 = Apetizer(name="Garlic_bread", price=3.50, sauce="Garlic")

# Platos fuertes
main_plate1 = MainPlate(name="Hamburger", price=10.00, accompaniment_1="fries", accompaniment_2="salad")
main_plate2 = MainPlate(name="Grilled_Chicken", price=12.00, accompaniment_1="rice", accompaniment_2="vegetables")
main_plate3 = MainPlate(name="Pasta_Bolognese", price=11.00, accompaniment_1="bread", accompaniment_2="parmesan")
main_plate4 = MainPlate(name="Steak", price=15.00, accompaniment_1="mashed potatoes", accompaniment_2="grilled vegetables")

# Creo una orden
order1 = Order(1)
order1.add_items(drink1, 2)
order1.add_items(dessert1, 4)
order1.add_items(apetizer1, 6)
order1.add_items(main_plate1, 7)
print(order1.show_order())
print(order1.calculate_bill())

