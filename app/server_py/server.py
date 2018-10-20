from flask import Flask, jsonify, abort, request, make_response, url_for
from flask_cors import CORS

app = Flask(__name__, static_url_path = "")
CORS(app)

@app.route('/', methods = ['GET'])
def get_json_from_frontend():
    return jsonify({"orig": "loc1", "dest":"loc2"})


@app.route('/', methods = ['POST'])
def post_json_to_frontend():
    if request.json:
        print(request.json)
    return jsonify("fetch from frontend to python")

if __name__ == '__main__':
    app.run(debug = True)
