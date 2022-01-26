from flask import Blueprint, render_template
from utilities.db.interact_with_DB import interact_db
from flask import request, redirect, flash

# Players blueprint definition
Players = Blueprint('Players', __name__,
                  static_folder='static',
                  static_url_path='/Players',
                  template_folder='templates')


# Routes
@Players.route('/Players')
def Players_func():
    # get Players table
    Players_query = 'select id, concat(first_name," ", last_name) AS name, level, age, school from Players;'
    Players_table = interact_db(query=Players_query, query_type='fetch')
    return render_template('Players.html', Players_table=Players_table)


@Players.route('/Players/delete_Players/<int:Players_id>')
def delete_Players(Players_id):
    query= "delete from Players where id='%s';" % Players_id
    interact_db(query=query, query_type='commit')
    flash('השחקן נמחק בהצלחה!')
    return redirect('/Players')

@Players.route('/Players/update_player' , methods=['post'])
def update_player_func():
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
    players_list_int = []
    for row in players_list:
        players_list_int.append(str(row.id))

    # validations
    if str(id) not in players_list_int:
        flash(f'  שחקן מספר  {id}  לא קיים במערכת...  ')
    else:
        # update DB
        if first_name != "":
            query = "UPDATE Players SET first_name = '%s' where id='%s' ; " % (first_name, id)
            interact_db(query=query, query_type='commit')
        if last_name != "":
            query = "UPDATE Players SET last_name = '%s' where id='%s' ; " % (last_name, id)
            interact_db(query=query, query_type='commit')
        if level != "":
            query = "UPDATE Players SET level = '%s' where id='%s' ; " % (level, id)
            interact_db(query=query, query_type='commit')
        if age != "":
            query = "UPDATE Players SET age = '%s' where id='%s' ; " % (age, id)
            interact_db(query=query, query_type='commit')
        if school != "":
            query = "UPDATE Players SET age = '%s' where id='%s' ; " % (age, id)
            interact_db(query=query, query_type='commit')
        if first_name == "" and last_name == "" and age == "" and level == "" and school == "":
            flash(f'לא הוכנסו פרטים לעידכון!')
        else:
            flash(f' השדות עודכנו בהצלחה!')
        # come back to Create_Player
        return redirect('/Players')
