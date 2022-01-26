from flask import Blueprint, render_template
from utilities.db.interact_with_DB import interact_db
from flask import request, redirect, flash

# staff blueprint definition
staff = Blueprint('staff', __name__,
                  static_folder='static',
                  static_url_path='/staff',
                  template_folder='templates')


# Routes
@staff.route('/staff')
def staff_func():
    # get staff table
    staff_query = 'select email, concat(first_name," ", last_name) AS name, phone, role, password from staff;'
    staff_table = interact_db(query=staff_query, query_type='fetch')
    return render_template('staff.html', staff_table=staff_table)


@staff.route('/staff/delete_staff/<staff_email>')
def delete_staff(staff_email):
    print('hi')
    print(staff_email)
    print(type(staff_email))

    email = staff_email
    query= "delete from staff where email='%s';" % email
    interact_db(query=query, query_type='commit')
    flash('איש הצוות נמחק בהצלחה!')
    return redirect('/staff')
