from flask import Blueprint

# navbar blueprint definition
navbar = Blueprint('navbar', __name__, static_folder='static', static_url_path='/navbar', template_folder='templates')
