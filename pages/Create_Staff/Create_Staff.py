from flask import Blueprint, render_template
from flask import request, redirect, flash
from utilities.db_objects.Staff import Staff

# Create_Staff blueprint definition
Create_Staff = Blueprint('Create_Staff', __name__,
                  static_folder='static',
                  static_url_path='/Create_Staff',
                  template_folder='templates')


# Routes
@Create_Staff.route('/Create_Staff')
def Create_Staff_func():
    return render_template('Create_Staff.html')


@Create_Staff.route('/Create_Staff/insert_staff', methods=['post'])
def insert_staff_func():
    # get the data
    first_name = request.form['staffName']
    last_name = request.form['staffLastName']
    email = request.form['staffEmail']
    phone = request.form['staffPhone']
    role = request.form['staffRole']
    password = request.form['staffPassword']

    # existing staff
    staff_list = Staff.get_staff_email()
    staff_list_emails=[]
    for row in staff_list:
        staff_list_emails.append(str(row.email))

    # validations
    if str(email) in staff_list_emails:
        flash(f'  האימייל {email}  כבר קיים במערכת...  ')
    else:
        # insert to DB
        Staff.insert_staff(email, first_name, last_name, phone, role, password)
        flash(f'איש הצוות נוסף בהצלחה!')

    # come back to Create_Staff
    return redirect('/Create_Staff')
