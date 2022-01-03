from flask import Blueprint, render_template

# headline blueprint definition
headline = Blueprint('headline', __name__,
                  static_folder='static',
                  static_url_path='/headline',
                  template_folder='templates')

