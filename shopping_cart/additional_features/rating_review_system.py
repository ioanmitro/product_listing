'''
This code defines a Product class with attributes for the product name, a list of ratings, and a list of reviews.
The class has methods to add ratings and reviews to the respective lists, calculate the average rating, and display
the reviews.
In the example usage, we create an instance of the Product class called product. We add some ratings and reviews
to it using the add_rating() and add_review() methods. Then, we display the average rating using the average_rating() 
method and print the reviews using the display_reviews() method.
Note that this is a basic implementation, and you can enhance it further based on your specific requirements.
For example, you can add user authentication, validation checks, or even store the ratings and reviews in a database.
'''


class Product:
    def __init__(self, name):
        self.name = name
        self.ratings = []
        self.reviews = []
    
    def add_rating(self, rating):
        self.ratings.append(rating)
    
    def add_review(self, review):
        self.reviews.append(review)
    
    def average_rating(self):
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)
    
    def display_reviews(self):
        if not self.reviews:
            print("No reviews available for this product.")
            return
        for review in self.reviews:
            print(review)

# Example usage:
product = Product("Phone")

product.add_rating(4.5)
product.add_rating(3.8)
product.add_rating(5)

product.add_review("Great phone! Fast and reliable.")
product.add_review("The battery life could be better.")

print("Average rating:", product.average_rating())
print("Reviews:")
product.display_reviews()
