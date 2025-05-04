# main.py
from product import Product
from product_manager import ProductManager

# Kreiramo ProductManager instancu
manager = ProductManager()

# Dodajemo proizvode
manager.add_product(Product("Laptop", 1200, 3))
manager.add_product(Product("Telefon", 800, 5))
manager.add_product(Product("Slusalice", 150, 10))

# Prikazujemo proizvode
manager.display_products()

# Prikaz ukupne vrednosti inventara
print(f"\nUkupna vrednost svih proizvoda: {manager.total_inventory_value()} RSD")
