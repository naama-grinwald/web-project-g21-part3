from flask import Blueprint, render_template
from utilities.db.interact_with_DB import interact_db

# results blueprint definition
results = Blueprint('results', __name__,
                  static_folder='static',
                  static_url_path='/results',
                  template_folder='templates')


# Routes
@results.route('/<int:tournament_id>/results')
def results_func(tournament_id):
    # get tournament table
    id_query = 'select * from tournaments where id=%s;' % tournament_id
    tournament = interact_db(query=id_query, query_type='fetch')[0]
    return render_template('results.html', tournament=tournament)

