from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
   return render_template('index.html')
   # by default looks for index.html inside a templates folder in the same directory as this script.

@app.route("/another")
def show():
    return '<h1>Yo</h1>'

@app.route('/user/<username>')
def show_name(username):
    return f'<h1>Hi {username}</h1>'

if __name__ == '__main__':
    app.run(debug = True)