from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user  # Importa login_required y current_user
from app.services.mercadopago_service import MercadoPagoService

class PaymentController:
    @staticmethod
    @login_required  # Requiere autenticación
    def index():
        return render_template('payment.html')

    @staticmethod
    @login_required  # Requiere autenticación
    def create_payment():
        if request.method == 'POST':
            items = [
                {
                    "title": request.form['title'],
                    "quantity": int(request.form['quantity']),
                    "unit_price": float(request.form['price'])
                }
            ]
            mercadopago_service = MercadoPagoService()
            try:
                payment_url = mercadopago_service.create_preference(items)
                return redirect(payment_url)
            except Exception as e:
                flash(f'Error creating payment: {str(e)}', 'error')
                return redirect(url_for('payment'))
        return render_template('payment.html')

    @staticmethod
    @login_required  # Requiere autenticación
    def payment_success():
        flash('Payment successful!', 'success')
        return render_template('payment_success.html')

    @staticmethod
    @login_required  # Requiere autenticación
    def payment_failure():
        flash('Payment failed. Please try again.', 'error')
        return render_template('payment_failure.html')

    @staticmethod
    @login_required  # Requiere autenticación
    def payment_pending():
        flash('Payment pending. We will notify you once it is completed.', 'warning')
        return render_template('payment_pending.html')