# Importar controladores (esto debe hacerse después de definir `app` para evitar importaciones circulares)
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_login import LoginManager, login_required, current_user
from config import Config
from app.utils import generate_session_id
from app.controllers.home_controller import HomeController
from app.controllers.dashboard_controller import DashboardController
from app.controllers.articles_controller import ArticlesController
from app.controllers.payment_controller import PaymentController
from app.controllers.auth_controller import AuthController
from app.controllers.cart_controller import CartController
# Crear la aplicación Flask
app = Flask(__name__)
app.config.from_object(Config)

# Configurar Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Ruta a la que se redirige si el usuario no está autenticado

# Función para cargar el usuario (esto es un ejemplo básico)
@login_manager.user_loader
def load_user(user_id):
    from app.models.user import User  # Importa el modelo de usuario
    return User(user_id, "username", "password")



# Rutas de la aplicación
@app.route('/')
def home():
    return HomeController.index()

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    if request.method == 'POST':
        # Llama a create_article() y maneja su respuesta
        response = DashboardController.create_article()
        return response  # Devuelve la respuesta directamente (puede ser una redirección o un renderizado)
    else:
        # Llama a index() y maneja su respuesta
        response = DashboardController.index()
        return response  # Devuelve la respuesta directamente (puede ser un renderizado o una redirección)

@app.route('/upload_profile_image', methods=['POST'])
@login_required  # Requiere autenticación para subir la imagen de perfil
def upload_profile_image():
    return DashboardController.upload_profile_image()

@app.route('/articles')
def articles():
    return ArticlesController.index()

@app.route('/add_to_cart', methods=['POST'])
@login_required  # Requiere autenticación para añadir al carrito
def add_to_cart():
    return ArticlesController.add_to_cart()

@app.route('/cart')
@login_required  # Requiere autenticación para ver el carrito
def cart():
    return CartController.index()

@app.route('/remove_from_cart', methods=['POST'])
@login_required  # Requiere autenticación para eliminar del carrito
def remove_from_cart():
    return CartController.remove_from_cart()

@app.route('/payment', methods=['GET', 'POST'])
@login_required  # Requiere autenticación para pagar
def payment():
    if request.method == 'POST':
        return PaymentController.create_payment()
    return PaymentController.index()

@app.route('/payment/success')
@login_required  # Requiere autenticación para ver la página de éxito
def payment_success():
    return PaymentController.payment_success()

@app.route('/payment/failure')
@login_required  # Requiere autenticación para ver la página de fallo
def payment_failure():
    return PaymentController.payment_failure()

@app.route('/payment/pending')
@login_required  # Requiere autenticación para ver la página de pendiente
def payment_pending():
    return PaymentController.payment_pending()

@app.route('/register', methods=['GET', 'POST'])
def register():
    return AuthController.register()

@app.route('/login', methods=['GET', 'POST'])
def login():
    return AuthController.login()

@app.route('/logout')
@login_required  # Requiere autenticación para cerrar sesión
def logout():
    return AuthController.logout()

# Manejo de errores global
@app.errorhandler(Exception)
def handle_error(e):
    # Registra el error en un archivo de log (opcional)
    app.logger.error(f"Error: {str(e)}")
    # Devuelve un mensaje de error al usuario
    return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)