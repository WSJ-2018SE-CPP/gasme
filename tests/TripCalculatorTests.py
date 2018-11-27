from context import trip
from trip.trip_calculator.trip_calculator import calculateTrip, getCostOfTrip, getRemainingTankLevel
from trip.location import GasStation
from trip.trip_calculator.database.filters import *
import argparse

# argument parser for password
parser = argparse.ArgumentParser(description='Supply the password.')
parser.add_argument('-p',
            dest='password',
            required=True,
            type=str,
            help='the rds password')
args = parser.parse_args()

if __name__ == '__main__':
	origin = "1000 Vin Scully Ave, Los Angeles, CA 90012"
	destination = "4 Yawkey Way, Boston, MA 02215"
	#origin = "AT&T Park, San Francisco"
	#destination = "Oracle, Oakland 02215"
	#origin = "Anaheim, CA, USA"
	#destination = "New York, NY, USA"
	#origin = "Cal Poly Pomona, Pomona, CA"
	#destination = "3421 Loreto Drive, San Ramon, CA"
	mpg = 30
	tankCapacity = 12
	filters = [GasStationBrandMultipleFilter(["Shell", "76", "ARCO"])]
	route = calculateTrip(args.password, origin, destination, mpg, tankCapacity, 5, filters)
	for location in route:
		print(("%s --> $%.2f, %s" % (location.address, location.gasPrice, location.brand)
				if isinstance(location, GasStation) else location.address))
	print(getCostOfTrip(route, mpg, tankCapacity, tankCapacity))
	print(getRemainingTankLevel(route, mpg, tankCapacity, tankCapacity))
