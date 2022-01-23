from flask import Blueprint, render_template
from utilities.db.interact_with_DB import interact_db

# default blueprint definition
default = Blueprint('default', __name__,
                  static_folder='static',
                  static_url_path='/default',
                  template_folder='templates')


# Routes
@default.route('/default')
def default_func():
    return render_template('results.html')
