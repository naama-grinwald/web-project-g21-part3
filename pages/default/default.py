from flask import Blueprint, render_template

# default blueprint definition
default = Blueprint('default', __name__,
                  static_folder='static',
                  template_folder='templates')


# Routes
@default.route('/default')
def default_func():
    return render_template('default.html')
