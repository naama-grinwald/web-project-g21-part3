from flask import Blueprint, render_template
from flask import Flask, redirect, url_for , render_template, request , session ,  flash
from utilities.db.interact_with_DB import interact_db


# SignIn blueprint definition
SignIn = Blueprint('SignIn', __name__, static_folder='static', static_url_path='/SignIn', template_folder='templates')


# Routes
@SignIn.route('/')
def login():
    return render_template('SignIn.html')

@SignIn.route('/SignIn', methods=[ 'POST'])
def index():
    if request.method == 'POST':
        user_email = request.form['user_email']
        password = request.form['password']
        found = val_email_pas(user_email,password)
        if found:

            session['user_email'] = get_username(user_email)
            session['password'] = password
            return redirect('/main')
        else:
            return redirect('/')

def val_email_pas(user_email,form_password):
    #naama.grinwald@gmail.com 1234
    # list of all the users
    users_query = 'select email from staff;'
    users_list = interact_db(query=users_query, query_type='fetch')
    users_list_int = []
    for row in users_list:
        users_list_int.append(str(row.email))
    #get password from DB
    user_password_query = "select password from staff where email='%s';" % user_email
    user_password_db=interact_db(query=user_password_query, query_type='fetch')
    # validation:
    global found
    if str(user_email) not in users_list_int:
        flash(f'המשתמש אינו קיים')
        found= False
    elif user_password_db[0][0] != form_password:
        flash(f'הסיסמה אינה נכונה, נסה שנית')
        found = False
    else:
        found= True
    return found


def get_username(user_email):
    user_name_query = "select first_name from staff where email='%s';" % user_email
    user_name_db = interact_db(query=user_name_query, query_type='fetch')
    return user_name_db[0][0]


@SignIn.route('/logout')
def logout_func():
    session['user_email'] = ''
    session['password'] = ''
    return redirect('/')
