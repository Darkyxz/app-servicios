from flask import render_template, request, redirect, url_for, session
from app.services.sanity_service import SanityService

class CartController:
    @staticmethod
    def index():
        if 'cart' not in session:
            session['cart'] = []
        sanity_service = SanityService()
        cart_items = []
        total = 0
        for article_id in session['cart']:
            article = sanity_service.get_article_by_id(article_id)
            if article:
                cart_items.append(article)
                total += article['price']
        return render_template('cart.html', cart_items=cart_items, total=total)

    @staticmethod
    def remove_from_cart():
        if request.method == 'POST':
            article_id = request.form.get('article_id')
            if 'cart' in session and article_id in session['cart']:
                session['cart'].remove(article_id)
                session.modified = True
            return redirect(url_for('cart'))
        return redirect(url_for('cart'))