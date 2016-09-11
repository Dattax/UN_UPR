"""
These are the base controlers attached to the homepage.
"""
from upr import app, render_template

@app.route("/")
def index():
    """    
    displays the index page.
    """
    return render_template('index.html')
