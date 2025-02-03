from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models.article import Article
from app.services.sanity_service import SanityService

class DashboardController:
    @staticmethod
    @login_required
    def index():
        sanity_service = SanityService()
        try:
            articles = sanity_service.get_articles_by_user(current_user.username)
            return render_template('dashboard.html', articles=articles)
        except Exception as e:
            flash(f'Error fetching articles: {str(e)}', 'error')
            return redirect(url_for('dashboard'))

    @staticmethod
    @login_required
    def create_article():
        if request.method == 'POST':
            title = request.form['title']
            description = request.form['description']
            price = float(request.form['price'])
            quantity = int(request.form['quantity'])
            image_file = request.files['image']

            sanity_service = SanityService()
            try:
                image_url = sanity_service.upload_image(image_file)
                article = Article(title, description, price, quantity, image_url, current_user.username)
                sanity_service.create_article(article)
                flash('Article published successfully!', 'success')
                return redirect(url_for('dashboard'))
            except Exception as e:
                flash(f'Error publishing article: {str(e)}', 'error')
                return redirect(url_for('dashboard'))
        return render_template('dashboard.html')

    @staticmethod
    @login_required
    def upload_profile_image():
        if request.method == 'POST':
            profile_image = request.files['profile_image']
            if profile_image:
                sanity_service = SanityService()
                try:
                    profile_image_url = sanity_service.upload_image(profile_image)
                    # Aquí debes actualizar la imagen de perfil del usuario en tu base de datos
                    # Por ejemplo:
                    # current_user.profile_image_url = profile_image_url
                    # db.session.commit()
                    flash('Profile image uploaded successfully!', 'success')
                except Exception as e:
                    flash(f'Error uploading profile image: {str(e)}', 'error')
            else:
                flash('No image selected.', 'error')
        return redirect(url_for('dashboard'))