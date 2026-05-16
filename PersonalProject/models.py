class Product:
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product_obj):
        self.items.append(product_obj)

    def calculate_subtotal(self):
        return sum(item.price for item in self.items)