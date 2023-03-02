from flask import render_template, flash, redirect
from app import app
from app.forms import RegisterForm, LoginForm, HomeSearchGames
from app.models import User, GameLibrary
from flask_login import current_user, login_user

@app.route('/', methods=['GET', 'POST'])
def index():
    form = HomeSearchGames()
    game_title = form.game_title.data
    genre = form.genre.data
    rating = form.rating.data
    games = {
        'coming_soon': ['Flower Picking Sim', 'Frog Stomp'],
        'out_now': ['Tank Busters', 'Kitty with a Kite']
    }
    # game_match = GameLibrary.query.filter_by(game_title=game_title).first()
    g = GameLibrary(game_title=game_title, genre=genre, rating=rating)
    if form.validate_on_submit():
        g.commit()
        # if not game_match:
        #     flash(f'Sorry, there is no {game_title} in our library.')
        #     return redirect('/')
        flash(f'Your search for "{game_title}" successful')
        return redirect('/')
    return render_template('home.jinja', games=games, form=form, title='Home')

@app.route('/about')
def about():
    return render_template('about.jinja')

@app.route('/register', methods=['GET', 'POST'])
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

@app.route('/login', methods=['GET', 'POST'])
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
        return redirect('/')
    return render_template('/login.jinja', form=form)

@app.route('/blog')
def blog():
    return render_template('/blog.jinja')