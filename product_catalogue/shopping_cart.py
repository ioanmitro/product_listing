class Product:
    def __init__(self, name, price_code):
        self.name = name
        self.price_code = price_code


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        for item in self.items:
            if item['product'] == product:
                item['quantity'] += quantity
                break
        else:
            self.items.append({'product': product, 'quantity': quantity})

    def remove_item(self, product):
        for item in self.items:
            if item['product'] == product:
                self.items.remove(item)
                break

    def adjust_quantity(self, product, quantity):
        for item in self.items:
            if item['product'] == product:
                item['quantity'] = quantity
                break

    def clear_cart(self):
        self.items = []

    def get_total_price(self):
        total_price = 0
        for item in self.items:
            product = item['product']
            quantity = item['quantity']
            total_price += self.calculate_price(product, quantity)
        return total_price

    def calculate_price(self, product, quantity):
        # Add your pricing logic here
        # You can use the product's price_code or any other method to calculate the price
        return quantity * 10  # Placeholder price calculation

    def display_cart(self):
        if not self.items:
            print("Shopping Cart is empty.")
            return

        print("Shopping Cart:")
        for index, item in enumerate(self.items):
            product = item['product']
            quantity = item['quantity']
            print(f"Item {index + 1}: {product.name} ({product.price_code}) - Quantity: {quantity}")

        total_price = self.get_total_price()
        print(f"Total Price: {total_price}")


# Example usage:
# Create some products
product1 = Product("Product 1", "A")
product2 = Product("Product 2", "B")
product3 = Product("Product 3", "C")

# Create a shopping cart
cart = ShoppingCart()

# Add items to the cart
cart.add_item(product1, 2)
cart.add_item(product2, 1)
cart.add_item(product3, 3)

# Display the cart
cart.display_cart()

# Adjust the quantity of an item
cart.adjust_quantity(product1, 5)

# Display the updated cart
cart.display_cart()

# Remove an item from the cart
cart.remove_item(product2)

# Display the updated cart
cart.display_cart()

# Clear the cart
cart.clear_cart()

# Display the cleared cart
cart.display_cart()


'''
The add_item method has been modified to check if the product already exists in the cart. If it does, the quantity is updated; otherwise, a new item is added to the cart.
The remove_item method now accepts a product as an argument and removes it from the cart if found.
The adjust_quantity method allows users to modify the quantity of a specific item in the cart.
The display_cart method now includes a check for an empty cart and displays an appropriate message.
Feel free to modify the calculate_price method to suit your pricing logic.
'''