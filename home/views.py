from flask import render_template, request

from home import app

@app.route('/')
def home():
    return render_template('home.html')

@app.errorhandler(404)
def page_not_found(error):
    path = request.path
    path = path[1:]

    return render_template('404.html', path=path), 404
