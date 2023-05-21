'''
An updated version of the code that enables users to add products to a shopping cart,
shows a summary of selected items, allows adhustment of quantities, removal of items,
and clearing of the entire cart.
'''


class Product:
    def __init__(self, name, image_url, description, price_code, additional_info):
        self.name = name
        self.image_url = image_url
        self.description = description
        self.price_code = price_code
        self.additional_info = additional_info

class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        for item in self.items:
            if item.product == product:
                item.quantity += quantity
                return
        cart_item = CartItem(product, quantity)
        self.items.append(cart_item)

    def remove_item(self, product):
        for item in self.items:
            if item.product == product:
                self.items.remove(item)
                return

    def clear_cart(self):
        self.items = []

    def get_total_quantity(self):
        total_quantity = 0
        for item in self.items:
            total_quantity += item.quantity
        return total_quantity

    def get_total_price_code(self):
        total_price_code = 0
        for item in self.items:
            total_price_code += item.quantity * int(item.product.price_code[2:])
        return total_price_code

# Creating instances of products
iphone_12 = Product(
    name="iPhone 12",
    image_url="https://example.com/iphone12.jpg",
    description="The iPhone 12 features a stunning Super Retina XDR display, A14 Bionic chip, advanced dual-camera system, and 5G capability.",
    price_code="PC01",
    additional_info="Additional information about the iPhone 12."
)

sony_headphones = Product(
    name="Sony WH-1000XM4 Wireless Noise-Canceling Headphones",
    image_url="https://example.com/sony-headphones.jpg",
    description="These wireless headphones offer industry-leading noise cancellation, exceptional sound quality, and smart listening features.",
    price_code="PC02",
    additional_info="Additional information about the Sony headphones."
)

samsung_tv = Product(
    name="Samsung QLED Q80T 4K Smart TV",
    image_url="https://example.com/samsung-tv.jpg",
    description="This QLED TV delivers stunning picture quality, enhanced gaming capabilities, and a smart TV experience with built-in voice control.",
    price_code="PC03",
    additional_info="Additional information about the Samsung QLED TV."
)

# Creating an instance of the shopping cart
cart = ShoppingCart()

# Adding items to the cart
cart.add_item(iphone_12, 2)
cart.add_item(sony_headphones, 1)

# Displaying the shopping cart summary
print("Shopping Cart Summary:")
print("----------------------")
for item in cart.items:
    print("Product:", item.product.name)
    print("Price Code:", item.product.price_code)
    print("Quantity:", item.quantity)
    print("----------------------")
print("Total Quantity:", cart.get_total_quantity())
print("Total Price Code:", cart.get_total_price_code())
print()

# Adjusting quantities
cart.items[0].quantity = 3

# Removing an item
cart.remove_item(sony_headphones)

# Clearing the cart
cart.clear_cart()

# Displaying the updated shopping cart summary
print("Updated Shopping Cart Summary:")
print("----------------------")
for item in cart.items:
    print("Product:", item.product.name)
    print("Price Code:", item.product.price_code)
    print("Quantity:", item.quantity)
    print("----------------------")