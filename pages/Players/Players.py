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
    Players_query = 'select email, concat(first_name," ", last_name) AS name, phone, role, password from Players;'
    Players_table = interact_db(query=Players_query, query_type='fetch')
    return render_template('Players.html', Players_table=Players_table)


@Players.route('/Players/delete_Players/<Players_email>')
def delete_Players(Players_email):
    print('hi')
    print(Players_email)
    print(type(Players_email))

    email = Players_email
    query= "delete from Players where email='%s';" % email
    interact_db(query=query, query_type='commit')
    flash('איש הצוות נמחק בהצלחה!')
    return redirect('/Players')
