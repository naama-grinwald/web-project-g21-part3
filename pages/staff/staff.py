from flask import Blueprint, render_template
from utilities.db.interact_with_DB import interact_db
from flask import request, redirect, flash
from utilities.db_objects.Staff import Staff


# staff blueprint definition
staff = Blueprint('staff', __name__,
                  static_folder='static',
                  static_url_path='/staff',
                  template_folder='templates')


# Routes
@staff.route('/staff')
def staff_func():
    # get staff table
    staff_table = Staff.get_staff()
    return render_template('staff.html', staff_table=staff_table)


@staff.route('/staff/delete_staff/<staff_email>')
def delete_staff(staff_email):
    email = staff_email
    Staff.delete_staff(email)
    flash('איש הצוות נמחק בהצלחה!')
    return redirect('/staff')


@staff.route('/staff/update_staff' , methods=['post'])
def update_staff_func():
    # get the data
    first_name = request.form['staffName']
    last_name = request.form['staffLastName']
    email = request.form['staffEmail']
    phone = request.form['staffPhone']
    role = request.form['staffRole']
    password = request.form['staffPassword']

    # existing staff
    staff_query = 'select email from Staff;'
    staff_list = interact_db(query=staff_query, query_type='fetch')
    staff_list_emails=[]
    for row in staff_list:
        staff_list_emails.append(str(row.email))

    # validations
    if str(email) not in staff_list_emails:
        flash(f'  האימייל  {email}  לא קיים במערכת...  ')
    else:
        # update DB
        if first_name != "":
            query = "UPDATE staff SET first_name = '%s' where email='%s' ; " % (first_name, email)
            interact_db(query=query, query_type='commit')
        if last_name != "":
            query = "UPDATE staff SET last_name = '%s' where email='%s' ; " % (last_name, email)
            interact_db(query=query, query_type='commit')
        if phone != "":
            query = "UPDATE staff SET phone = '%s' where email='%s' ; " % (phone, email)
            interact_db(query=query, query_type='commit')
        if role != "":
            query = "UPDATE staff SET role = '%s' where email='%s' ; " % (role, email)
            interact_db(query=query, query_type='commit')
        if password != "":
            query = "UPDATE staff SET password = '%s' where email='%s' ; " % (password, email)
            interact_db(query=query, query_type='commit')
        if first_name == "" and last_name == "" and phone == "" and role == "" and password == "":
            flash(f'לא הוכנסו פרטים לעידכון!')
        else:
            flash(f' השדות עודכנו בהצלחה!')
        # come back to Create_Player
        return redirect('/staff')
