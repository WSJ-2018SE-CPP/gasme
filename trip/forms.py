from flask_wtf import FlaskForm
from wtforms import widgets,TextField, SubmitField, SelectField, SelectMultipleField, DecimalField
from wtforms.validators import DataRequired

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class TripForm(FlaskForm):
	brandString = ['Any\r\nMobil\r\nArco\r\n']
	brandList = brandString[0].split()
	brands = [(x,x) for x in brandList]
	origin = TextField('Starting Point', validators=[DataRequired()])
	destination = TextField('Destination', validators=[DataRequired()])
	
	brand = MultiCheckboxField('Brand', choices=brands)
	currentTankLevel = DecimalField('Current Tank Level', default = 100)
	
	carBrandString = ['NA\r\nToyota\r\nHonda\r\n']
	carBrandList = carBrandString[0].split()
	carBrands = [(x,x) for x in carBrandList]
	carBrand = SelectField('Car Brand', choices=carBrands)
	
	'''Need to get from database based on carBrand'''
	carModelString = ['NA\r\n']
	carModelList = carModelString[0].split()
	carModels = [(x,x) for x in carModelList]
	carModel = SelectField('Car Model', choices=carModels)
	
	'''Need to get from database based on carModel'''
	carYearString = ['NA\r\n']
	carYearList = carYearString[0].split()
	carYears = [(x,x) for x in carYearList]
	carYear = SelectField('Car Year', choices=carYears)
	
	'''Depends on car Model, but users can insert it themselves'''
	cityMPG = DecimalField('City MPG', default = 25)
	highwayMPG = DecimalField('Highway MPG', default = 50)
	tankCapacity = DecimalField('Tank Capacity', default = 10)
	
	submit = SubmitField('Submit')