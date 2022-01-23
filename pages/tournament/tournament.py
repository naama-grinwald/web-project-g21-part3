from flask import Blueprint, render_template
from utilities.db.interact_with_DB import interact_db

# tournament blueprint definition
tournament = Blueprint('tournament', __name__,
                  static_folder='static',
                  static_url_path='/tournament',
                  template_folder='templates')


# Routes
@tournament.route('/tournament/<int:tournament_id>')
def tournament_func(tournament_id):
    query = 'select * from tournaments where id=%s;' % tournament_id
    tournaments = interact_db(query=query, query_type='fetch')
    return render_template('tournament.html',tournaments=tournaments)
