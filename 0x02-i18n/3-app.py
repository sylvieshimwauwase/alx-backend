#!/usr/bin/env python3
"""setting up basic flask app"""

from flask import Flask, render_template, request
from flask_babel import  Babel, gettext


app = Flask(__name__)
babel = Babel(app)

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)

@babel.localeselector
def get_locale():
    """getting locale"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """returning index page"""
    return render_template('3-index.html', home_title=gettext('home_title'),
                           home_header=gettext('home_header'))

if __name__ == '__main__':
    app.run(debug=True)
