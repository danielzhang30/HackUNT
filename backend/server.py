# import Python modules
import requests
from datetime import date

from flask import Flask, jsonify
app = Flask(__name__)

# route HTTP request to 'get_flights()' function
@app.route('/get_flights')
def get_flights():
	# api-endpoint
	URL = "http://localhost:3030/flights"

	#date
	today = date.today().strftime("%Y-%m-%d")

	#parameters (hard-coded for now)
	PARAMS = {'date':today, 'origin':"DFW"}

	# sending get request and saving the response object
	r = requests.get(url = URL, params = PARAMS)

	# extracting data in json format
	data = r.json()

	return jsonify(data)

# route HTTP request to 'get_hotels()' function
@app.route('/get_hotels')
def get_hotels():
	URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

	# DFW airport location
	location = "32.8998, -97.0403"

	# search radius in meters
	radius = "1500"

	PARAMS = {'location':location, 'radius':radius, 'type':"lodging", 'key':"AIzaSyAKJueIwi6A6oLMrGaNSSsx561bMzOKJEg"}

	r = requests.get(url = URL, params = PARAMS)

	data = r.json()

	return jsonify(data)

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port=5001)
