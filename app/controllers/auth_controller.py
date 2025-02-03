from flask import render_template, request, redirect, url_for, flash, session
from flask_login import login_user, logout_user, login_required
from app.models.user import User
from app.utils import generate_session_id  # Importa desde utils.py

class AuthController:
    @staticmethod
    def register():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            # Aquí debes guardar el usuario en tu base de datos
            user = User(1, username, password)  # Esto es un ejemplo básico
            flash('Registration successful!', 'success')
            return redirect(url_for('login'))
        return render_template('register.html')

    @staticmethod
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            # Aquí debes verificar las credenciales en tu base de datos
            user = User(1, username, password)  # Esto es un ejemplo básico
            login_user(user)
            session['user_session_id'] = generate_session_id()  # Usa la función desde utils.py
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        return render_template('login.html')

    @staticmethod
    @login_required
    def logout():
        logout_user()
        flash('Logout successful!', 'success')
        return redirect(url_for('home'))