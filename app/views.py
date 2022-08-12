from app import app 
from flask import render_template, request

@app.route("/")
def index():    
    return render_template("public/index.html")

@app.route("/profile")
def about():
    return render_template("public/about.html")

@app.route("/singup")
def singup():
    return render_template("public/singup.html")

@app.route("/login")
def login():
    return render_template("public/login.html")



