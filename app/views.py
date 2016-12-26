from flask import render_template
from app import app
from app import scraper


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', schedules=scraper.schedules)

@app.route('/schedule/<date>')
def schedule(date):
    # TODO: date is from : 1 to 112 (date % 4 = Day of Month, date / 4 = season)
    return render_template('index.html', title='Home', schedules=scraper.schedules)
