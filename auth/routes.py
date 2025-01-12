from flask import Blueprint, render_template

# from config import db

auth = Blueprint("auth", __name__, template_folder="templates", static_folder="static")


@auth.route("/", methods=["GET", "POST"])
def login():
    return render_template("auth/login.html")


@auth.route("/signup")
def signup():
    return "Signup"


@auth.route("/logout")
def logout():
    return "Logout"
