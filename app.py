from flask import Flask

# App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')


# Pages
# Default
from pages.default.default import default
app.register_blueprint(default)

# Page error handlers
from pages.page_error_handlers.page_error_handlers import page_error_handlers
app.register_blueprint(page_error_handlers)

# Components
# navbar
#from components.navbar.navbar import navbar
#app.register_blueprint(navbar)

# footer
#from components.footer.footer import footer
#app.register_blueprint(footer)


if __name__ == '__main__':
    app.run()
