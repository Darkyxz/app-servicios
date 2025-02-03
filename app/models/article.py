class Article:
    def __init__(self, title, description, price, quantity, image_url, owner_username):
        self.title = title
        self.description = description
        self.price = price
        self.quantity = quantity
        self.image_url = image_url
        self.owner_username = owner_username

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "quantity": self.quantity,
            "image_url": self.image_url,
            "owner_username": self.owner_username
        }