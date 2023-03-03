from . import bp as main_bp
from flask import render_template, flash, redirect
from app.forms import HomeSearchGames
from app.blueprints.main.models import GameLibrary
from flask_login import login_required

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    form = HomeSearchGames()
    game_title = form.game_title.data
    # genre = form.genre.data
    # rating = form.rating.data
    games = {
        'coming_soon': ['Flower Picking Sim', 'Frog Stomp'],
        'out_now': ['Tank Busters', 'Kitty with a Kite']
    }
    game_match = GameLibrary.query.filter_by(game_title=game_title).first()
    # g = GameLibrary(game_title=game_title, genre=genre, rating=rating)
    if form.validate_on_submit():
        # g.commit()
        if not game_match:
            flash(f'Sorry, there is no {game_title} in our library.')
            return redirect('/')
        flash(f'Your search for "{game_title}" successful')
        return redirect('/')
    return render_template('home.jinja', games=games, form=form, title='Home')

@main_bp.route('/about')
def about():
    return render_template('about.jinja')

@main_bp.route('/blog')
@login_required
def blog():
    return render_template('/blog.jinja')
