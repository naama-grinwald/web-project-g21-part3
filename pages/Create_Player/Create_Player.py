from flask import Blueprint, render_template
from flask import request, redirect, flash
from utilities.db_objects.Players import Players

# Create_Player blueprint definition
Create_Player = Blueprint('Create_Player', __name__,
                  static_folder='static',
                  static_url_path='/Create_Player',
                  template_folder='templates')


# Routes
@Create_Player.route('/Create_Player')
def Create_Player_func():
    return render_template('Create_Player.html')


@Create_Player.route('/Create_Player/insert_player', methods=['post'])
def insert_player_func():
    # get the data
    id = request.form['id']
    first_name = request.form['name']
    last_name = request.form['LastName']
    level = request.form['level']
    age = request.form['age']
    school = request.form['school']

    # existing players
    players_list = Players.get_players_id()
    players_list_int=[]
    for row in players_list:
        players_list_int.append(str(row.id))

    # validations
    if str(id) in players_list_int:
        flash(f'  שחקן מספר  {id}  כבר קיים במערכת...  ')
    else:
        # insert to DB
        Players.insert_player(id, first_name, last_name, level, age, school)
        flash(f'השחקן נוסף בהצלחה!')

    # come back to Create_Player
    return redirect('/Create_Player')
