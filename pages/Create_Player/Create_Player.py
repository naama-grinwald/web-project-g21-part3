from flask import Blueprint, render_template
from utilities.db.interact_with_DB import interact_db
from flask import request, redirect, flash

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
    players_query = 'select id from Players;'
    players_list = interact_db(query=players_query, query_type='fetch')
    players_list_int=[]
    for row in players_list:
        players_list_int.append(str(row.id))

    # validations
    if str(id) in players_list_int:
        flash(f'  שחקן מספר  {id}  כבר קיים במערכת...  ')
    else:
        # insert to DB
        query = "insert into Players(id, first_name, last_name, level, age, school) values ('%s','%s','%s','%s','%s','%s'); " % (id, first_name, last_name, level, age, school)
        interact_db(query=query, query_type='commit')
        flash(f'השחקן נוסף בהצלחה!')

    # come back to Create_Player
    return redirect('/Create_Player')
