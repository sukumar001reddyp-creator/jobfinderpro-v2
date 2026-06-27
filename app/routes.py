from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models.user import User

def register_routes(app):
    
    @app.route("/")
    def home():
        return render_template("home/index.html")

    @app.route("/jobs")
    def jobs():
        return render_template("jobs/index.html")

    @app.route("/companies")
    def companies():
        return render_template("companies/index.html")

    @app.route("/resume-builder")
    def resume_builder():
        return render_template("resume_builder/index.html")

    @app.route("/ai-tools")
    def ai_tools():
        return render_template("ai_tools/index.html")

    @app.route("/login", methods=['GET', 'POST'])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('dashboard'))
        
        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')
            user = User.query.filter_by(email=email).first()
            
            if user and user.check_password(password):
                login_user(user)
                flash('Login successful!', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid email or password', 'danger')
        
        return render_template("auth/login.html")

    @app.route("/register", methods=['GET', 'POST'])
    def register():
        if current_user.is_authenticated:
            return redirect(url_for('home'))
        
        if request.method == 'POST':
            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')
            
            if User.query.filter_by(email=email).first():
                flash('Email already registered!', 'danger')
            else:
                user = User(username=username, email=email)
                user.set_password(password)
                db.session.add(user)
                db.session.commit()
                
                flash('Registration successful! Please login.', 'success')
                return redirect(url_for('login'))
        
        return render_template("auth/register.html")

    @app.route("/logout")
    @login_required
    def logout():
        logout_user()
        flash('Logged out successfully!', 'success')
        return redirect(url_for('home'))

    @app.route("/dashboard")
    @login_required
    def dashboard():
        return render_template("dashboard/index.html")     

    return app