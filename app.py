from flask import Flask, url_for

# App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

# Pages
# Default
from pages.default.default import default
app.register_blueprint(default)

# Main
from pages.main.main import main
app.register_blueprint(main)

# Tournament
from pages.tournament.tournament import tournament
app.register_blueprint(tournament)

# Results
from pages.results.results import results
app.register_blueprint(results)

# Judgment
from pages.judgment.judgment import judgment
app.register_blueprint(judgment)

# Page error handlers
from pages.page_error_handlers.page_error_handlers import page_error_handlers
app.register_blueprint(page_error_handlers)


# Components
# Navbar
#from components.navbar.navbar import navbar
#app.register_blueprint(navbar)

# Footer
#from components.footer.footer import footer
#app.register_blueprint(footer)

# Headline
from components.headline.headline import headline
app.register_blueprint(headline)

if __name__ == '__main__':
    app.run()
