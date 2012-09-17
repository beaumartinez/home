from datetime import date, datetime

from dateutil.relativedelta import relativedelta
from flask import render_template, request

from home import app

BIRTHDAY = date(1990, 4, 4)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    now = datetime.utcnow()
    now = now.date()

    age = relativedelta(now, BIRTHDAY)
    age = age.years

    return render_template('about.html', age=age)

@app.errorhandler(404)
def page_not_found(error):
    path = request.path
    path = path[1:]

    return render_template('404.html', path=path), 404
