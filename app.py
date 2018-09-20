# run.py

from webtest.forms import TripForm
from webtest.geo import getInfo, getRoute
from flask import Flask, render_template, flash, redirect, request

from config import Config

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
    
if __name__ == '__main__':
    app.run()