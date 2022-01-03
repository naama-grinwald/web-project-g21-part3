from flask import Blueprint, render_template

# tournament blueprint definition
tournament = Blueprint('tournament', __name__,
                  static_folder='static',
                  static_url_path='/tournament',
                  template_folder='templates')


# Routes
@tournament.route('/tournament')
def tournament_func():
    return render_template('tournament.html')
