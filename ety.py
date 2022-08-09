import os
from urllib import request
import json
import flask
import ety

app = flask.Flask(__name__)

@app.route('/', methods=['GET','POST'])
def randet():
	blob = request.urlopen("https://random-word-api.herokuapp.com/word").read()
	word = json.loads(blob)[0]
	return(ety.origins(word, recursive))