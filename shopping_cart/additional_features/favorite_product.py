'''
In this example, we have two classes: Product and User. The Product class represents a product with attributes
like name and price. The User class represents a user with a name and a list of favorite products.
The User class has methods to add a favorite product, remove a favorite product, and display the list
of favorite products.

In the example usage, we create an instance of the User class called user and some instances of the Product class.
We add the products to the user's favorites using the add_favorite() method and display the favorite products using
the display_favorites() method. Then, we remove one of the favorite products using the remove_favorite() method and 
display the updated list of favorite products.

You can extend this code by adding more functionality, such as saving favorites to a file or database, implementing
user authentication, or providing additional features for managing and interacting with the favorite products.
'''

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price}"


class User:
    def __init__(self, name):
        self.name = name
        self.favorites = []

    def add_favorite(self, product):
        self.favorites.append(product)

    def remove_favorite(self, product):
        if product in self.favorites:
            self.favorites.remove(product)

    def display_favorites(self):
        if not self.favorites:
            print("No favorite products found.")
            return
        print("Favorite products:")
        for product in self.favorites:
            print(product)


# Example usage:
user = User("John")

product1 = Product("Phone", 500)
product2 = Product("Laptop", 1000)
product3 = Product("Headphones", 100)

user.add_favorite(product1)
user.add_favorite(product2)
user.add_favorite(product3)

user.display_favorites()

user.remove_favorite(product2)

user.display_favorites()
