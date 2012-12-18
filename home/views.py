from datetime import date, datetime

from dateutil.relativedelta import relativedelta
from flask import render_template, request
from humanize import apnumber

from home import app

DATE_STARTED_PROGRAMMING = date(2004, 4, 4)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    now = datetime.utcnow()

    years_programming = relativedelta(now, DATE_STARTED_PROGRAMMING)
    years_programming = years_programming.years
    years_programming = apnumber(years_programming)

    return render_template('about.html', years_programming=years_programming)

@app.errorhandler(404)
def page_not_found(error):
    path = request.path
    path = path.strip('/')

    return render_template('404.html', path=path), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500
