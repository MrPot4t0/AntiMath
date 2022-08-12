from app import app
from flask import render_template
from flask import request

@app.route("/")
def index():    
    return render_template("public/index.html")

@app.route("/about")
def about():
    return render_template("public/about.html") 
    
@app.route("/login")
def sign_up():
    return render_template("public/login.html")

@app.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('index'))
    return render_template("public/singup_form.html")


