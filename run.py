"""
Run.py enables quick prototyping for development.
Run this to create a debug flask server.
"""
from upr import app
app.run(host='0.0.0.0', port=8080, debug=True)
