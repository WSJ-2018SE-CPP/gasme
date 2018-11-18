from flask import Flask, jsonify, abort, request, make_response, url_for
from flask_cors import CORS
import json, os

app = Flask(__name__, static_url_path = "")
CORS(app)

def get_json_file(path):
    with open(path) as data_file:
        return json.load(data_file)
    return 0


def decode_json(json_data):
    if json_data:
        #car
        car = dict()
        car["car_brand"] = json_data["car"]["car_brand"]
        car["car_model"] = json_data["car"]["car_model"]
        car["car_year"] = json_data["car"]["car_year"]
        car["highway_consumption"] = json_data["car"]["highway_consumption"]
        car["city_consumption"] = json_data["car"]["city_consumption"]
        car["tank_capacity"] = json_data["car"]["tank_capacity"]
        car["initial_gas_level"] = json_data["car"]["initial_gas_level"]
        car["default"] = json_data["car"]["default"]
        #gas
        gas = dict()
        gas["brand"] = json_data["gas"]["brand"]
        #trip
        trip = []
        for one in json_data["trip"]:
            trip.append({"long": one["long"], "lat": one["lat"]})
        return car, gas, trip

    return 0


#@app.route('/', methods = ['POST'])
#def from_jsonfile():
#    jdata = get_json_file(os.path.join(os.path.dirname(__file__), 'user_input.json'))
#    car, gas, trip = decode_json(jdata)
#    print("car: " + str(car))
#    print("gas " + str(gas))
#    print("trip " + str(trip))
#    return jsonify("fetch from a json file, check python terminal")


@app.route('/', methods = ['GET'])
def json_to_frontend():
    return jsonify({"orig": "loc1", "dest":"loc2"})


@app.route('/', methods = ['POST'])
def json_from_frontend():
    if request.json:
        print(request.json)
    return jsonify("fetch from frontend to python")

if __name__ == '__main__':
    app.run(debug = True)
