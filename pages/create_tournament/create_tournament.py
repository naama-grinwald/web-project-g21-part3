from flask import Blueprint, render_template, redirect, request
from utilities.db.interact_with_DB import interact_db
from utilities.db_objects.Tournaments import Tournaments

# create_tournament blueprint definition
create_tournament = Blueprint('create_tournament', __name__,
                  static_folder='static',
                  static_url_path='/create_tournament',
                  template_folder='templates')


# Routes
@create_tournament.route('/create_tournament', methods=['GET'])
def create_tournament_func():
    return render_template('create_tournament.html')


@create_tournament.route('/create_tournament_route', methods=['POST'])
def create_tournament_post_func():
    # get data
    name = request.form['name']
    date = request.form['date']
    location = request.form['location']
    type = request.form['type']
    Season = request.form['Season']
    details = request.form['details']

    # insert to DB
    Tournaments.create_tournament(name,date,location,type,Season,details)
    return redirect('/main')


@create_tournament.route('/tournament/<int:tournament_id>/update_tournament', methods=['GET', 'POST'])
def update_tournament_form_func(tournament_id):
    # get tournament table
    tournament = Tournaments.get_tournament(tournament_id)[0]
    return render_template('create_tournament.html', tournament=tournament)

@create_tournament.route('/tournament/<int:tournament_id>/update_tournament_route', methods=['POST'])
def update_tournament_func(tournament_id):
    # get data
    name = request.form['name']
    date = request.form['date']
    location = request.form['location']
    type = request.form['type']
    Season = request.form['Season']
    details = request.form['details']

    # update
    fields=['name','date','location','type','Season','details']
    results=[name,date,location,type,Season,details]
    zip_object = zip(fields, results)
    for field, result in zip_object:
        if result != "":
           # Tournaments.update_tournament(field, result, tournament_id)
            query = "UPDATE tournaments SET %s='%s' WHERE id = '%s';" % (field, result, tournament_id)
            interact_db(query=query, query_type='commit')

    return redirect('/tournament/%s' % tournament_id)
