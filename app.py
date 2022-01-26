from flask import Flask, url_for

# App setup
app = Flask(__name__)
app.secret_key= '123'
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

# Create Tournament
from pages.create_tournament.create_tournament import create_tournament
app.register_blueprint(create_tournament)

# Page error handlers
from pages.page_error_handlers.page_error_handlers import page_error_handlers
app.register_blueprint(page_error_handlers)

# Create_Staff
from pages.Create_Staff.Create_Staff import Create_Staff
app.register_blueprint(Create_Staff)

# Create_Player
from pages.Create_Player.Create_Player import Create_Player
app.register_blueprint(Create_Player)

# staff
from pages.staff.staff import staff
app.register_blueprint(staff)

# staff
from pages.Players.Players import Players
app.register_blueprint(Players)
## SignIn
from pages.SignIn.SignIn import SignIn
app.register_blueprint(SignIn)

# Components
# Navbar
from components.navbar.navbar import navbar
app.register_blueprint(navbar)

# Footer
from components.footer.footer import footer
app.register_blueprint(footer)

# Headline
from components.headline.headline import headline
app.register_blueprint(headline)

if __name__ == '__main__':
    app.run()
