from flask import Blueprint, render_template, url_for

# main blueprint definition
main = Blueprint('main', __name__,
                static_folder='static',
                static_url_path='/main',
                template_folder='templates')


# Routes
@main.route('/main')
def main_func():
    return render_template('main.html')
