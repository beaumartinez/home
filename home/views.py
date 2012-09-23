from datetime import date, datetime

from dateutil.relativedelta import relativedelta
from flask import render_template, request

from home import app

AGE_STARTED_PROGRAMMING = 14
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

    years_programming = age - AGE_STARTED_PROGRAMMING

    return render_template('about.html', age=age, years_programming=years_programming)

@app.errorhandler(404)
def page_not_found(error):
    path = request.path
    path = path.strip('/')

    return render_template('404.html', path=path), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500
