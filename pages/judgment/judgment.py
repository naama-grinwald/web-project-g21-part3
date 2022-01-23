from flask import Blueprint, render_template
from utilities.db.interact_with_DB import interact_db
from flask import request, redirect, flash


# judgment blueprint definition
judgment = Blueprint('judgment', __name__,
                  static_folder='static',
                  static_url_path='/judgment',
                  template_folder='templates')

# Routes
@judgment.route('/tournament/<int:tournament_id>/judgment',methods=['GET', 'POST'])
def judgment_func(tournament_id):
    # get tournament table
    id_query = 'select * from tournaments where id=%s;' % tournament_id
    tournament = interact_db(query=id_query, query_type='fetch')[0]
    return render_template('judgment.html', tournament=tournament)


@judgment.route('/tournament/<int:tournament_id>/judgment/insert_score', methods=['POST'])
def insert_judgment_func(tournament_id):
    # get data
    id_tournament = tournament_id
    Round = request.form['Round']
    desk = request.form['desk']
    id_player1 = request.form['id_player1']
    id_player2 = request.form['id_player2']
    score=request.form['score']
    if score == "draw":
        score_player1=0.5
        score_player2=0.5
    elif score == "player1_won":
        score_player1=1
        score_player2=0
    else:
        score_player1=0
        score_player2=1

    # list of users
    players_query = 'select id from Players;'
    players_list = interact_db(query=players_query, query_type='fetch')
    players_list_int=[]
    for row in players_list:
        players_list_int.append(str(row.id))

    # existing game scores
    scores_query = 'select * from GameScores;'
    scores = interact_db(query=scores_query, query_type='fetch')
    inputOK= True
    for row in scores:
        if (id_tournament == row.id_tournament) and (int(Round) == row.Round) and (int(desk) == row.desk):
            inputOK = False

    # validations
    if str(id_player1) not in players_list_int:
        flash(f'שחקן { id_player1 } אינו קיים ')
    elif str(id_player2) not in players_list_int:
        flash(f'שחקן {id_player2} אינו קיים ')
    elif id_player1 == id_player2:
        flash(f'הזנת שני מספרי שחקן זהים, כדאי לנסות שוב...')
    elif not inputOK:
        flash(f'כבר קיים ניקוד עבור שולחן זה...')
    else:
        # insert to DB
        query = "INSERT INTO GameScores(id_tournament,Round,desk,id_player1,id_player2,score_player1,score_player2) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (id_tournament,Round,desk,id_player1,id_player2,score_player1,score_player2)
        interact_db(query=query, query_type='commit')
        flash(f'הניקוד הוזן בהצלחה!')

    # back to judgment
    return redirect('/tournament/%s/judgment' % tournament_id)
