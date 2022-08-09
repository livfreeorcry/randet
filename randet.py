import os
from urllib import request
import json
import flask
import ety

app = flask.Flask(__name__)

@app.route('/', methods=['GET','POST'])
def randet():
	count = 0
	while count < 10:
		blob = request.urlopen("https://random-word-api.herokuapp.com/word").read()
		word = json.loads(blob)[0]
		et = ety.origins(word, recursive=True)
		if len(et) > 0:
			return("<h2>" + word + ":</h2><br>" + str(et))
			break
		else:
			count += 1
	return("<h2>Tried ten words, none had an etymology to provide. Please try again.</h2")