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


@app.route("/account")
def account_details():
    """
    displays the account details page.
    """
    return render_template('accountdetails.html')


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
