"""
These are the base controlers that render pages attatched to the homepage.
"""
from upr import app
from flask import url_for, render_template


@app.route("/")
def index():
    """
    displays the index page.
    """
    return render_template('index.html')


@app.route("/register_org")
def register_org():
    """
    displays the organization registration page.
    """
    return render_template('register_org.html')


@app.route("/register_user")
def register_user():
    """
    displays the register user page.
    """
    return render_template('register_user.html')


@app.route("/login")
def login():
    """
    displays the account login page.
    """
    return render_template('login.html')


@app.route("/edit")
def edit():
    """
    displays the edit page.
    """
    return render_template('edit.html')


@app.route("/landing")
def landing():
    """
    displays the landing page.
    """
    return render_template('landing.html')

@app.route("/about")
def about():
    """
    displays the landing page.
    """
    return render_template('about.html')


@app.route("/status")
def status():
    """
    displays the status page.
    """
    return render_template('status.html')


@app.route("/submission")
def submission():
    """
    displays the submission page.
    """
    return render_template('submission.html')


@app.route("/thanks")
def thanks():
    """
    displays the thanks page.
    """
    return render_template('thanks.html')
