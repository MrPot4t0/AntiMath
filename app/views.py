from app import app 
from flask import render_template, request

@app.route("/")
def index():    
    return render_template("public/index.html")

@app.route("/about")
def about():
    return render_template("public/about.html") 
    
@app.route("/login")
def sign_up():
    return render_template("public/login.html")



