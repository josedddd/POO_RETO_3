# Diagrama de Clases del Menú

```mermaid
classDiagram
    class MenuItem {
        name: str
        price: float
        calculate_price(quantity: int) float
    }

    class Beverage {
        bottle_type: str
        size: str
        with_ice(answer) str
    }

    class Apetizer {
        sauce: str
    }

    class Dessert {
        flavour: str
    }

    class MainPlate {
        accompaniment1: str
        accompaniment2: str
    }

    class Order {
        number: int
        order: list
        add_items(menu_item: MenuItem, quantity: int)
        show_order() list
        calculate_bill() str
    }

    MenuItem <|-- Beverage
    MenuItem <|-- Apetizer
    MenuItem <|-- Dessert
    MenuItem <|-- MainPlate
    Order *-- MenuItem : contains

