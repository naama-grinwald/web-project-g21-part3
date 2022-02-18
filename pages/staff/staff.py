from flask import Blueprint, render_template
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
    staff_list = Staff.get_staff_email()
    staff_list_emails=[]
    for row in staff_list:
        staff_list_emails.append(str(row.email))

    # validations
    if str(email) not in staff_list_emails:
        flash(f'  האימייל  {email}  לא קיים במערכת...  ')
    else:
        # update DB
        fields = ['first_name','last_name','phone','role','password']
        results =  [first_name,last_name,phone,role,password]
        zip_object = zip(fields, results)
        for field, result in zip_object:
            if result != "":
                Staff.update_staff(field, result, email)

        if first_name == "" and last_name == "" and phone == "" and role == "" and password == "":
            flash(f'לא הוכנסו פרטים לעידכון!')
        else:
            flash(f' השדות עודכנו בהצלחה!')

        # come back to Create_Player
        return redirect('/staff')
