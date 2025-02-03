from flask import render_template
from app.services.sanity_service import SanityService

class HomeController:
    @staticmethod
    def index():
        return render_template('home.html')
