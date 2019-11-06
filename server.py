from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    signed_in = True # we are hardcoding this just to demonstrate how we can do conditionals in our template files, in future we won't be hardcoding this.
    return render_template('index.html', signed_in=signed_in)

@app.route("/<name>")
def user_page(name):
    name = name.capitalize()
    return render_template('hello.html', name = name)
    # by default looks for index.html inside a templates folder in the same directory as this script.

@app.route("/another")
def show():
    return '<h1>Yo</h1>'

@app.route('/user/<username>')
def show_name(username):
    return f'<h1>Hi {username}</h1>'

@app.route("/contact")
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug = True)