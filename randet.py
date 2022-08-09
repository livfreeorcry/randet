import os
import requests
import json
from flask import Flask, render_template
import ety

app = Flask(__name__)

wiktionary = "https://en.wiktionary.org/wiki/"
etymonline = "https://www.etymonline.com/word/"

# Wiktionary Extract Pull

def randWord():
	request = requests.get("https://random-word-api.herokuapp.com/word").text
	word = json.loads(str(request))[0]
	return word

def wikiExtract(word='test'):
	try:
		url= "https://en.wiktionary.org/w/api.php?action=query&prop=extracts&format=json&titles="
		request = requests.get(url+word).text
		pages = json.loads(str(request)['query']['pages'])
		for page in pages:
			return(pages[page]['extract'])
	except:
		return "No Wiktionary Extract Available"

@app.route('/')
def randet():
	count = 0
	while count < 10:
		word = randWord()
		et = ety.origins(word, recursive=True)
		if len(et) > 0:
			#return render_template("template.html", word=word, et=str(et), extract=extract)
			return("<h2>" + word + ":</h2><p>" + str(et) + 
				"</p><p>Wiktionary: <a href=\"" + wiktionary + word + "\">" + word + "</a>" +
				"</p><p>Etymonline: <a href=\"" + etymonline + word + "\">" + word + "</a>")
		else:
			count += 1
	return("<h3>Tried ten words, none had an etymology listed. Please try again.</h3")

@app.route('/test')
def test():
	count = 0
	while count < 10:
		word = randWord()
		et = ety.origins(word, recursive=True)
		extract = wikiExtract(word)
		if len(et) > 0:
			return render_template("template.html", word=word, et=str(et), extract=extract)
		else:
			count += 1
	return("<h3>Tried ten words, none had an etymology listed. Please try again.</h3")