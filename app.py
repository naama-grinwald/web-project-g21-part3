from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('settings.py')

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
