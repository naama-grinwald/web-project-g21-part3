from flask import Blueprint, render_template
from flask import Flask, redirect, url_for , render_template, request , session ,  flash
from utilities.db_objects.Staff import Staff

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

            session['user_name'] = get_username(user_email)
            session['password'] = password
            return redirect('/main')
        else:
            return redirect('/')

def val_email_pas(user_email,form_password):
    #naama.grinwald@gmail.com 1234
    # list of all the users
    users_list = Staff.get_staff_email()
    users_list_int = []
    for row in users_list:
        users_list_int.append(str(row.email))
    #get password from DB
    user_password_db = Staff.get_staff_password(user_email)
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
    user_name_db = Staff.get_staff_name(user_email)
    return user_name_db[0][0]


@SignIn.route('/logout')
def logout_func():
    session['user_name'] = ''
    session['password'] = ''
    return redirect('/')
