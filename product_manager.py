from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        print("\nAvailable Products:")
        for product in self.products:
            product.display_info()

    def total_inventory_value(self):
        return sum(product.price * product.quantity for product in self.products)

    def remove_product(self, product_name):
        self.products = [p for p in self.products if p.name != product_name]
