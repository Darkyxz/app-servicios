from flask import render_template, request, redirect, url_for, session, flash
from flask_login import login_required, current_user
from app.services.sanity_service import SanityService

class ArticlesController:
    @staticmethod
    def index():
        sanity_service = SanityService()
        try:
            articles = sanity_service.get_articles()
            return render_template('articles.html', articles=articles)
        except Exception as e:
            # Renderiza una plantilla de error en lugar de devolver una cadena
            flash(f'Error fetching articles: {str(e)}', 'error')
            return render_template('error.html'), 400

    @staticmethod
    @login_required  # Requiere autenticación
    def add_to_cart():
        if request.method == 'POST':
            article_id = request.form.get('article_id')
            if not article_id:
                flash('No article ID provided', 'error')
                return redirect(url_for('articles'))

            # Inicializa el carrito en la sesión si no existe
            if 'cart' not in session:
                session['cart'] = []

            # Añade el artículo al carrito
            session['cart'].append(article_id)
            session.modified = True  # Asegura que la sesión se guarde

            flash('Article added to cart successfully!', 'success')
            return redirect(url_for('articles'))

        # Si no es una solicitud POST, redirige al usuario a la página de artículos
        return redirect(url_for('articles'))