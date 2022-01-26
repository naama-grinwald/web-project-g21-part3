from flask import Blueprint, render_template
from flask import request, redirect, flash
from utilities.db_objects.Tournaments import Tournaments
from utilities.db_objects.Players import Players


# judgment blueprint definition
judgment = Blueprint('judgment', __name__,
                  static_folder='static',
                  static_url_path='/judgment',
                  template_folder='templates')

# Routes
@judgment.route('/tournament/<int:tournament_id>/judgment',methods=['GET', 'POST'])
def judgment_func(tournament_id):
    # get tournament table
    tournament=Tournaments.get_tournament(tournament_id)[0]
    # get game scores
    scores=Tournaments.get_scores(tournament_id)
    return render_template('judgment.html', tournament=tournament, scores=scores)


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

    # get players id from DB
    players_list = Players.get_players_id()
    players_list_int=[]
    for row in players_list:
        players_list_int.append(str(row.id))

    # get game scores
    scores=Tournaments.get_scores(tournament_id)
    inputOK= True
    for row in scores:
        if (int(Round) == row.Round) and (int(desk) == row.desk):
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
        Tournaments.insert_scores(id_tournament, Round, desk, id_player1, id_player2, score_player1, score_player2)
        flash(f'הניקוד הוזן בהצלחה!')

    # back to judgment
    return redirect('/tournament/%s/judgment' % tournament_id)


@judgment.route('/tournament/<int:tournament_id>/judgment/delete_score', methods=['POST'])
def delete_judgment_func(tournament_id):
    # get data
    id_tournament = tournament_id
    Round = request.form['Round']
    desk = request.form['desk']

    # delete scores
    Tournaments.delete_scores(tournament_id,Round,desk)
    return redirect('/tournament/%s/judgment' % tournament_id)

