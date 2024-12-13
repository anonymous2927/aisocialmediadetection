from flask import render_template, url_for, flash, redirect, request
from app import app, db, mail
from flask_mail import Message
from flask_login import login_user, login_required, logout_user
from app.models import User
from flask_login import current_user

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Find user by email and check password
        user = User.query.filter_by(email=email).first()
        if user and user.password == password:  # In production, use hashed passwords!
            login_user(user)
            return redirect(url_for('dashboard'))  # Redirect to dashboard or protected page

    return render_template('login.html')

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()

        flash('Account created successfully!', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route("/dashboard")
@login_required  # Protect the dashboard route
def dashboard():
    return render_template('dashboard.html')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
