from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, username, password, profile_image_url=None):
        self.id = id
        self.username = username
        self.password = password
        self.profile_image_url = profile_image_url