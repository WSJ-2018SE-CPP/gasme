# run.py
import json
from trip.forms import TripForm
from trip.trip import Trip
from flask import Flask, render_template, flash, redirect, request
from config import Config
import argparse

# argument parser for password
parser = argparse.ArgumentParser(description='Supply the password.')
parser.add_argument('-p',
            dest='password',
            required=True,
            type=str,
            help='the rds password')
args = parser.parse_args()

app = Flask(__name__)
app.config.from_object(Config)

#Main page, produce form, receive value inserted in form, pass the result.html
@app.route('/', methods = ['GET', 'POST'])
def index():
    form = TripForm()
    if form.validate_on_submit():
    	result = request.form
    	form = TripForm()
    	
    	origin = request.form.get('origin')
    	destination = request.form.get('destination')
    	gb = request.form.get('brand')
    	cb = request.form.get('carBrand')
    	cm = request.form.get('carModel')
    	cy = request.form.get('carYear')
    	hc = request.form.get('highwayMPG')
    	cc = request.form.get('cityMPG')
    	tc = request.form.get('tankCapacity')
    	igl = request.form.get('currentTankLevel')

    	t = Trip(origin, destination, "", gb, cb, cm, cy, hc, cc, tc, igl)
    	stops = t.findRoute(t.origin, t.dest)
    	return render_template('result.html', result=result, form=form,
    		origin=t.origin, destination=t.dest, distance=t.distance, duration=t.duration, 
    		route=stops)
    return render_template("index.html", title='Trip Form', form=form)


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contactus.html")
    
if __name__ == '__main__':
    app.run()
