# views.py

from flask import render_template, flash, redirect, request

from app import app
from app.forms import TripForm
from app.geo import getInfo, getRoute

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = TripForm()
    if form.validate_on_submit():
    	result = request.form
    	form = TripForm()
    	
    	origin = request.form.get('origin')
    	origin = getInfo(origin)
    	destination = request.form.get('destination')
    	destination = getInfo(destination)
    	trip = getRoute(origin['address'], destination['address'])
    	return render_template('result.html', result=result, form=form,
    		origin=origin, destination=destination, trip=trip)
    return render_template("index.html", title='Trip Form', form=form)


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contactus.html")

@app.route('/result')
def result():
	return render_template("result.html")