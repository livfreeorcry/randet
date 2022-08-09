import os
from urllib import request
import json
from flask import Flask, render_template
import ety

app = Flask(__name__)

wiktionary = "https://en.wiktionary.org/wiki/"
etymonline = "https://www.etymonline.com/word/"

# Wiktionary Extract Pull

def extract(word=test):
	try:
		url= "https://en.wiktionary.org/w/api.php?action=query&prop=extracts&format=json&titles="
		extBlob = request.urlopen(url+word)
		extText = extBlob.read()
		jsonPages = json.loads(extText['query']['pages'])
		for page in jsonPages:
			return(jsonPages[page]['extract'])
	except:
		return "No Wiktionary Extract Available"

@app.route('/')
def randet():
	count = 0
	while count < 10:
		blob = request.urlopen("https://random-word-api.herokuapp.com/word").read()
		word = json.loads(blob)[0]
		et = ety.origins(word, recursive=True)
		extract = extract(word)
		if len(et) > 0:
			#return render_template("template.html", word=word, et=str(et), extract=extract)
			return("<h2>" + word + ":</h2><p>" + str(et) + 
				"</p><p>Wiktionary: <a href=\"" + wiktionary + word + "\">" + word + "</a>" +
				"</p><p>Etymonline: <a href=\"" + etymonline + word + "\">" + word + "</a>" +
				"<h4>Wiktionary Extract:</h4>")
		else:
			count += 1
	return("<h3>Tried ten words, none had an etymology listed. Please try again.</h3")

