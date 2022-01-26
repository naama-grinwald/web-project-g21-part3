from flask import Blueprint, render_template
from utilities.db_objects.Tournaments import Tournaments

# tournament blueprint definition
tournament = Blueprint('tournament', __name__,
                  static_folder='static',
                  static_url_path='/tournament',
                  template_folder='templates')


# Routes
@tournament.route('/tournament/<int:tournament_id>')
def tournament_func(tournament_id):
    # get tournament table
    tournament = Tournaments.get_tournament(tournament_id)[0]

    # get number of ranked tables
    ranked_tables=Tournaments.get_ranked_tables(tournament_id)[0]

    # get number of rounds
    rounds = Tournaments.get_num_of_rounds(tournament_id)[0]

    # get number of players
    players = Tournaments.get_num_of_players(tournament_id)[0]

    return render_template('tournament.html',tournament=tournament, ranked_tables=ranked_tables, rounds=rounds, players=players, back_tournament=True)
