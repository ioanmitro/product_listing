'''
This code defines a Product class to store the details of each product. It then creates lists 
of products for different categories(electronics, home appliances, and fashion). Finally, it loops 
through each category and prints the product details, including the name, image URL, description,
and price code.
The inforamtion details can be altered adding the information that we want for the catalogues
'''

class Product:
    def __init__(self, name, image_url, description, price_code):
        self.name = name
        self.image_url = image_url
        self.description = description
        self.price_code = price_code

# Electronics
electronics = [
    Product(
        name="iPhone 12",
        image_url="https://example.com/iphone12.jpg",
        description="The iPhone 12 features a stunning Super Retina XDR display, A14 Bionic chip, advanced dual-camera system, and 5G capability.",
        price_code="PC01"
    ),
    Product(
        name="Sony WH-1000XM4 Wireless Noise-Canceling Headphones",
        image_url="https://example.com/sony-headphones.jpg",
        description="These wireless headphones offer industry-leading noise cancellation, exceptional sound quality, and smart listening features.",
        price_code="PC02"
    ),
    Product(
        name="Samsung QLED Q80T 4K Smart TV",
        image_url="https://example.com/samsung-tv.jpg",
        description="This QLED TV delivers stunning picture quality, enhanced gaming capabilities, and a smart TV experience with built-in voice control.",
        price_code="PC03"
    )
]

# Home Appliances
home_appliances = [
    Product(
        name="Dyson V11 Absolute Cordless Vacuum Cleaner",
        image_url="https://example.com/dyson-vacuum.jpg",
        description="This cordless vacuum cleaner provides powerful suction, intelligent cleaning modes, and up to 60 minutes of runtime.",
        price_code="PC04"
    ),
    Product(
        name="Instant Pot Duo Nova 7-in-1 Electric Pressure Cooker",
        image_url="https://example.com/instant-pot.jpg",
        description="The Instant Pot Duo Nova combines seven appliances in one, offering pressure cooking, slow cooking, steaming, and more.",
        price_code="PC05"
    ),
    Product(
        name="Philips Hue White and Color Ambiance Smart Bulb Starter Kit",
        image_url="https://example.com/philips-hue.jpg",
        description="This smart bulb starter kit includes three color-changing bulbs and a bridge, allowing you to create personalized lighting at home.",
        price_code="PC06"
    )
]

# Fashion
fashion = [
    Product(
        name="Nike Air Zoom Pegasus 38 Running Shoes",
        image_url="https://example.com/nike-shoes.jpg",
        description="These running shoes feature responsive cushioning, a lightweight design, and a breathable upper for enhanced comfort.",
        price_code="PC07"
    ),
    Product(
        name="Kate Spade New York Cameron Medium Satchel",
        image_url="https://example.com/kate-spade-bag.jpg",
        description="This stylish medium-sized satchel is crafted from durable crossgrain leather and offers multiple pockets for organization.",
        price_code="PC08"
    ),
    Product(
        name="Casio G-Shock Analog-Digital Watch",
        image_url="https://example.com/casio-watch.jpg",
        description="This rugged G-Shock watch combines analog and digital displays, shock resistance, and water resistance up to 200 meters.",
        price_code="PC09"
    )
]

# Displaying products
for product in electronics:
    print("Product:", product.name)
    print("Image:", product.image_url)
    print("Description:", product.description)
    print("Price Code:", product.price_code)
    print()

for product in home_appliances:
    print("Product:", product.name)
    print("Image:", product.image_url)
    print("Description:", product.description)
    print("Price Code:", product.price_code)
    print()

for product in fashion:
    print("Product:", product.name)
    print("Image:", product.image_url)
    print("Description:", product.description)
    print("Price Code:", product.price_code)
    print()
