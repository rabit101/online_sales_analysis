from cart import Cart

from product import Product
from product_manager import ProductManager
from cart import Cart

manager = ProductManager()
manager.add_product(Product("Laptop", 1200, 3))
manager.add_product(Product("Telefon", 800, 5))
manager.add_product(Product("Slusalice", 150, 10))

manager.display_products()
print(f"\nUkupna vrednost svih proizvoda: {manager.total_inventory_value()} RSD")

manager.remove_product("Telefon")
print("\nNakon uklanjanja proizvoda:")
manager.display_products()

# === Cart funkcionalnost ===
cart = Cart()
cart.add_to_cart(manager.products[0])
cart.add_to_cart(manager.products[1])

cart.display_cart()
print(f"\nUkupna vrednost za naplatu: {cart.calculate_total()} RSD")
# === Cart funkcionalnost ===
cart = Cart()
cart.add_to_cart(manager.products[0])  # Laptop
cart.add_to_cart(manager.products[1])  # Slusalice

cart.display_cart()
print(f"\nUkupna vrednost za naplatu: {cart.calculate_total()} RSD")
