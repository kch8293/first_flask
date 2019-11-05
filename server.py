from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Why so easy</h1>'


@app.route("/another")
def show():
    return '<h1>Yo</h1>'

@app.route('/user/<username>')
def show_name(username):
    return f'<h1>Hi {username}</h1>'

if __name__ == '__main__':
    app.run(debug = True)