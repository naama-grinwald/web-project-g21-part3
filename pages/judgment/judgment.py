from flask import Blueprint, render_template
from utilities.db.interact_with_DB import interact_db

# judgment blueprint definition
judgment = Blueprint('judgment', __name__,
                  static_folder='static',
                  static_url_path='/judgment',
                  template_folder='templates')


# Routes
@judgment.route('/<int:tournament_id>/judgment',methods=['GET', 'POST'])
def judgment_func(tournament_id):
    # get tournament table
    id_query = 'select * from tournaments where id=%s;' % tournament_id
    tournament = interact_db(query=id_query, query_type='fetch')[0]
    return render_template('judgment.html', tournament=tournament)


@judgment.route('/<int:tournament_id>/judgment/insert', methods=['POST'])
def insert_judgment_func(tournament_id):
    # get data

    # insert to DB

    # back to judgment
    return redirect('/<int:tournament_id>/judgment')
