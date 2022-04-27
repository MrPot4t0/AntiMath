from app import app
from flask import render_template

@app.route("/")
def index():    
    return render_template("public/index.html")

@app.route("/about")
def about():
    return render_template("public/about.html") 
    
@app.route("/jinja")
def jinja():
    # Strings
    my_name = "Cristopher"

    # Integers
    my_age = 5000

    # Lists
    langs = ["Python", "C Tic-Tac-Toe", "Spanish"]

    # Dictionaries
    friends = {
        "The Guru": 43,
        "The K3n": 28,
        "Mr. Pot4t0": 26,
    }

    # Tuples
    colors = ("Red", "Blue")

    # Booleans
    cool = True

    # Classes
    class GitRemote:
        def __init__(self, name, description, domain):
            self.name = name
            self.description = description 
            self.domain = domain

        def pull(self):
            return f"Pulling repo '{self.name}'"

        def clone(self, repo):
            return f"Cloning into {repo}"

    my_remote = GitRemote(
        name="Learning Flask to exploit Flask an create AntiMath",
        description="AntiMath is a ransomware disguised as a calulator",
        domain="https://github.com/Mr. Pot4t0"
    )

    # Functions
    def repeat(x, qty=1):
        return x * qty

    return render_template(
        "public/jinja.html", my_name=my_name, my_age=my_age, langs=langs,
        friends=friends, colors=colors, cool=cool, GitRemote=GitRemote, 
        my_remote=my_remote, repeat=repeat
    )

    @app.route("/login")
    def sign_up():
        return render_template("public/login.html")


