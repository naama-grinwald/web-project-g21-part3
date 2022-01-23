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
    # get tournament table
    id_query = 'select * from tournaments where id=%s;' % tournament_id
    tournament = interact_db(query=id_query, query_type='fetch')[0]

    # get number of ranked tables
    ranked_tables_query = 'select count(*) as tables from GameScores where id_tournament=%s;' % tournament_id
    ranked_tables = interact_db(query=ranked_tables_query, query_type='fetch')[0]

    # get number of rounds
    rounds_query = 'select count(distinct round) as rounds from GameScores where id_tournament=%s;' % tournament_id
    rounds = interact_db(query=rounds_query, query_type='fetch')[0]

    # get number of players
    players_query = 'select count(distinct player) as players from ((select id_player1 as player from GameScores where id_tournament=%s) union (select id_player2 as player from GameScores where id_tournament=%s)) as a;' % (tournament_id,tournament_id)
    players = interact_db(query=players_query, query_type='fetch')[0]

    return render_template('tournament.html',tournament=tournament, ranked_tables=ranked_tables, rounds=rounds, players=players)
