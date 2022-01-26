from flask import Blueprint, render_template
from utilities.db.interact_with_DB import interact_db

# results blueprint definition
results = Blueprint('results', __name__,
                  static_folder='static',
                  static_url_path='/results',
                  template_folder='templates')


# Routes
@results.route('/tournament/<int:tournament_id>/results')
def results_func(tournament_id):
    # get tournament table
    id_query = 'select * from tournaments where id=%s;' % tournament_id
    tournament = interact_db(query=id_query, query_type='fetch')[0]

    # get scores tables
    score_query = 'select id_player, concat(P.first_name," ", P.last_name) AS name, score, ROW_NUMBER() OVER(ORDER BY score desc) RowNumber from(select id_player1 as id_player, sum(score_player1) as score from((select id_player1,score_player1 from gamescores where id_tournament=%s) union all (select id_player2,score_player2 from gamescores where id_tournament=%s)) as scores group by id_player1) as S join Players AS P ON S.id_player = P.id  order by Score desc;' % (tournament_id, tournament_id)
    score_table = interact_db(query=score_query, query_type='fetch')
    return render_template('results.html', tournament=tournament, score_table=score_table)
