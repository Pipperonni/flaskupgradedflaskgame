from . import bp as auth_bp
from app.forms import RegisterForm, LoginForm
from app.blueprints.auth.models import User
from flask_login import login_user, logout_user, login_required, current_user
from flask import render_template, redirect, flash

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        username=form.username.data
        email=form.email.data
        password=form.password.data
        u = User(first_name=first_name, last_name=last_name, username=username, email=email, password_hash='')
        user_match = User.query.filter_by(username=username).first()
        email_match = User.query.filter_by(email=email).first()
        if user_match:
            flash(f'{username} already exists, please try again.')
            return redirect('/register')
        elif email_match:
            flash(f'{email} already exists, please try again.')
            return redirect('/register')
        else:
            u.hash_password(password)
            u.commit()
            flash(f'Request to register {username} successful')
            return redirect('/')
    return render_template('/register.jinja', form=form)

@auth_bp.route('/login', methods=['GET', 'POST'])
def sign_in():
    form = LoginForm()
    email = form.email.data
    password = form.password.data
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user_match = User.query.filter_by(email=email).first()
        if not user_match or not user_match.check_password(password):
            flash(f'Username or password are incorrect, try again')
            return redirect('/login')
        flash(f'{email} sign in was successful')
        login_user(user_match, remember=form.remember_me.data)
        return redirect('/')
    return render_template('/login.jinja', form=form)

@auth_bp.route('/blog/<username>')
def user(username):
    user_match = User.query.filter_by(username=username).first()
    if not user_match:
        redirect('/')
    return render_template('blog.jinja', user=user_match)

@auth_bp.route('/signout')
@login_required
def sign_out():
    logout_user()
    return redirect('/')

