# models.py

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.cart = Cart()

class Seller:
    def __init__(self, username, email, password, store_name):
        self.username = username
        self.email = email
        self.password = password
        self.store_name = store_name
        self.products = []

class Product:
    def __init__(self, name, description, price, seller):
        self.name = name
        self.description = description
        self.price = price
        self.seller = seller

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity=1):
        self.items.append({'product': product, 'quantity': quantity})

    def remove_item(self, product_name):
        self.items = [item for item in self.items if item['product'].name != product_name]

    def get_total(self):
        return sum(item['product'].price * item['quantity'] for item in self.items)
