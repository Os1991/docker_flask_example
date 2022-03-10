#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dill
import pandas as pd
import os
dill._dill._reverse_typemap['ClassType'] = type
#import cloudpickle
import flask
import logging
from logging.handlers import RotatingFileHandler
from time import strftime

app = flask.Flask(__name__)
model = None

handler = RotatingFileHandler(filename='app.log', maxBytes=100000, backupCount=10)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

def load_model(model_path):
	# load the pre-trained model
	global model
	with open(model_path, 'rb') as f:
		model = dill.load(f)
	print(model)

model_path = r"C:/Users/okruz/cat1.dill"
load_model(model_path)

@app.route("/", methods=["GET"])
def general():
	return """Welcome to value prediction process. Please use 'http://192.168.0.108:8180/predict' to POST"""

@app.route("/predict", methods=["POST"])
def predict():
	# initialize the data dictionary that will be returned from the
	# view
	data = {"success": False}
	dt = strftime("[%Y-%b-%d %H:%M:%S]")
	# ensure an image was properly uploaded to our endpoint
	if flask.request.method == "POST":
		age, position, citizenship, club, national_team = 0, "", "", "", ""
		request_json = flask.request.get_json()
		if request_json["age"]:
			age = request_json['age']
		if request_json["position"]:
			position = request_json['position']
		if request_json["citizenship"]:
			citizenship = request_json['citizenship']
		if request_json["club"]:
			club = request_json['club']
		if request_json["national_team"]:
			national_team = request_json['national_team']
		logger.info(f'{dt} Data: age={age}, position={position}, citizenship={citizenship}, club={club},'
					f' national_team={national_team}')
		try:
			preds = model.predict(pd.DataFrame({"age": [age], "position": [position], "citizenship": [citizenship],
													  "club": [club], "national_team": [national_team],}))
		except AttributeError as e:
			logger.warning(f'{dt} Exception: {str(e)}')
			data['success'] = False
			return flask.jsonify(data)

		data["predictions"] = preds[0]
		# indicate that the request was a success
		data["success"] = True

	# return the data dictionary as a JSON response
	return flask.jsonify(data)

# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
	print(("* Loading the model and Flask starting server..."
		"please wait until server has fully started"))
	port = int(os.environ.get('PORT', 8180))
	app.run(host='0.0.0.0', debug=True, port=port)
