"""
These are the base controlers that render pages attatched to the homepage.
"""
from upr import app
from upr.forms import LoginForm, RegistrationForm
from upr.models import User
from flask import url_for, render_template, flash, redirect
from flask_login import login_user, login_required

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


@app.route("/register_user", methods = ["GET", "POST"])
def register_user():
    """
    displays the register user page.
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(form.email.data, form.password.data)
        #values to copy
        values = ['first_name', 'last_name', 'address', 'postal_code',\
        'province', 'country', 'phone']
        for field in values:
            setattr(user, field, getattr(form, field).data)
        user.is_authenticated = True
        user.commit()
        login_user(user)
        flash("Registration successful. Welcome, %s." %(user.first_name))
        return redirect(url_for('landing'))
    return render_template('register_user.html', form=form)


@app.route("/login", methods = ["GET", "POST"])
def login():
    """
    displays the account login page.
    """
    form = LoginForm()
    if form.validate_on_submit():
        user = User.find_by_email(form.email.data)
        if not user or not user.password == form.password.data:
            flash('Invalid user or password.')
            return render_template('login', form = form)
        user.is_authenticated = True
        user.commit()
        login_user(user)
        return redirect(url_for('landing'))
    return render_template('login.html', form = form)

@app.route('/logout')
def logout():
    user = current_user
    if user:
        user.is_authenticated = False
        user.commit()
        logout_user()
    return render_template('index')


@app.route("/edit")
def edit():
    """
    displays the edit page.
    """
    return render_template('edit.html')


@app.route("/landing")
@login_required
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
