from flask import Blueprint, render_template, url_for
from utilities.db_objects.Tournaments import Tournaments

# main blueprint definition
main = Blueprint('main', __name__,
                static_folder='static',
                static_url_path='/main',
                template_folder='templates')


# Routes
@main.route('/main')
def main_func():
    tournaments = Tournaments.get_all_tournaments()
    return render_template('main.html', tournaments=tournaments)


