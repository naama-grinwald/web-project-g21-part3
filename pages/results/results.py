from flask import Blueprint, render_template
from utilities.db_objects.Tournaments import Tournaments

# results blueprint definition
results = Blueprint('results', __name__,
                  static_folder='static',
                  static_url_path='/results',
                  template_folder='templates')


# Routes
@results.route('/tournament/<int:tournament_id>/results')
def results_func(tournament_id):
    # get tournament table
    tournament=Tournaments.get_tournament(tournament_id)[0]

    # get results tables
    score_table = Tournaments.get_results(tournament_id)
    return render_template('results.html', tournament=tournament, score_table=score_table)
