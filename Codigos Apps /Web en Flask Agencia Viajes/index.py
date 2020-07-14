from flask import Flask, render_template

app = Flask(__name__)

# Routes to Render Something
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about', strict_slashes=False)
def about():
    return render_template("about.html")

@app.route('/services', strict_slashes=False)
def services():
    return render_template("services.html")

@app.route('/projects', strict_slashes=False)
def projects():
    return render_template("projects.html")

@app.route('/contacts', strict_slashes=False)
def contacts():
    return render_template("contacts.html")

# Make sure this we are executing this file
if __name__ == '__main__':
    app.run(debug=True)
