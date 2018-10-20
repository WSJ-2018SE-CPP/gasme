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
	origin = "3421 Loreto Drive, San Ramon, CA 94583"
	destination = "270 E Orlando Way, Covina, CA, 91723"
	calculate_trip(args.password, origin, destination)
