from flask import Blueprint, render_template
from utilities.db.interact_with_DB import interact_db

# create_tournament blueprint definition
create_tournament = Blueprint('create_tournament', __name__,
                  static_folder='static',
                  static_url_path='/create_tournament',
                  template_folder='templates')


# Routes
@create_tournament.route('/tournament/<int:tournament_id>/create_tournament')
def create_tournament_func(tournament_id):
    # get tournament table
    id_query = 'select * from tournaments where id=%s;' % tournament_id
    tournament = interact_db(query=id_query, query_type='fetch')[0]
    return render_template('create_tournament.html', tournament=tournament)
