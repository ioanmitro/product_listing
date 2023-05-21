'''
An updated version of the code that allows users to click on a product to 
view more details. It shows a larger image, detailed description, additional information,
and prominently displayes the price code.
Additional information can be added
'''

class Product:
    def __init__(self, name, image_url, description, price_code, additional_info):
        self.name = name
        self.image_url = image_url
        self.description = description
        self.price_code = price_code
        self.additional_info = additional_info

# Electronics
electronics = [
    Product(
        name="iPhone 12",
        image_url="https://example.com/iphone12.jpg",
        description="The iPhone 12 features a stunning Super Retina XDR display, A14 Bionic chip, advanced dual-camera system, and 5G capability.",
        price_code="PC01",
        additional_info="Additional information about the iPhone 12."
    ),
    Product(
        name="Sony WH-1000XM4 Wireless Noise-Canceling Headphones",
        image_url="https://example.com/sony-headphones.jpg",
        description="These wireless headphones offer industry-leading noise cancellation, exceptional sound quality, and smart listening features.",
        price_code="PC02",
        additional_info="Additional information about the Sony headphones."
    ),
    Product(
        name="Samsung QLED Q80T 4K Smart TV",
        image_url="https://example.com/samsung-tv.jpg",
        description="This QLED TV delivers stunning picture quality, enhanced gaming capabilities, and a smart TV experience with built-in voice control.",
        price_code="PC03",
        additional_info="Additional information about the Samsung QLED TV."
    )
]

# Home Appliances
home_appliances = [
    Product(
        name="Dyson V11 Absolute Cordless Vacuum Cleaner",
        image_url="https://example.com/dyson-vacuum.jpg",
        description="This cordless vacuum cleaner provides powerful suction, intelligent cleaning modes, and up to 60 minutes of runtime.",
        price_code="PC04",
        additional_info="Additional information about the Dyson vacuum cleaner."
    ),
    Product(
        name="Instant Pot Duo Nova 7-in-1 Electric Pressure Cooker",
        image_url="https://example.com/instant-pot.jpg",
        description="The Instant Pot Duo Nova combines seven appliances in one, offering pressure cooking, slow cooking, steaming, and more.",
        price_code="PC05",
        additional_info="Additional information about the Instant Pot pressure cooker."
    ),
    Product(
        name="Philips Hue White and Color Ambiance Smart Bulb Starter Kit",
        image_url="https://example.com/philips-hue.jpg",
        description="This smart bulb starter kit includes three color-changing bulbs and a bridge, allowing you to create personalized lighting at home.",
        price_code="PC06",
        additional_info="Additional information about the Philips Hue smart bulb kit."
    )
]

# Fashion
fashion = [
    Product(
        name="Nike Air Zoom Pegasus 38 Running Shoes",
        image_url="https://example.com/nike-shoes.jpg",
        description="These running shoes feature responsive cushioning, a lightweight design, and a breathable upper for enhanced comfort.",
        price_code="PC07",
        additional_info="Additional information about the Nike running shoes."
    ),
    Product(
        name="Kate Spade New York Cameron Medium Satchel",
        image_url="https://example.com/kate-spade-bag.jpg",
        description="This stylish medium-sized satchel is crafted from durable crossgrain leather and offers multiple pockets for organization.",
        price_code="PC08",
        additional_info="Additional information about the Kate Spade satchel."	