from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    first_name = request.args.get('first_name')
    signed_in = True # we are hardcoding this just to demonstrate how we can do conditionals in our template files, in future we won't be hardcoding this.
    return render_template('index.html', signed_in=signed_in)

@app.route("/<name>")
def user_page(name):
    name = name.capitalize()
    signed_in = True
    return render_template('hello.html', name = name, signed_in=signed_in)
    # by default looks for index.html inside a templates folder in the same directory as this script.

@app.route("/contact")
def contact():
    signed_in = True
    return render_template('contact.html', signed_in=signed_in)

if __name__ == '__main__':
    app.run(debug = True)