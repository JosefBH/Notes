from flask import Blueprint, render_template
views = Blueprint("views", __name__)

@views.route("/")
def root():
    return render_template("home.html", text='this is a test string')