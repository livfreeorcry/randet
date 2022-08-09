import os
from urllib import request
import json
import flask
import ety

app = flask.Flask(__name__)

wiktionary = "https://en.wiktionary.org/wiki/"
etymonline = "https://www.etymonline.com/word/"


@app.route('/', methods=['GET','POST'])
def randet():
	count = 0
	while count < 10:
		blob = request.urlopen("https://random-word-api.herokuapp.com/word").read()
		word = json.loads(blob)[0]
		et = ety.origins(word, recursive=True)
		if len(et) > 0:
			return("<h2>" + word + ":</h2><p>" + str(et) + 
				"</p><p>Wiktionary: <a href=\""+wiktionary+"\">" + word + "</a>" +
				"</p><p>Etymonline: <a href=\""+etymonline+"\">" + word + "</a>" )
		else:
			count += 1
	return("<h3>Tried ten words, none had an etymology listed. Please try again.</h3")