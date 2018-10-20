from context import trip
from trip.trip_calculator.trip_calculator import calculate_trip
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
	route = calculate_trip(args.password, origin, destination)
	for location in route:
		print(location.address)
