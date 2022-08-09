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
		url= "https://en.wiktionary.org/w/api.php?action=query&prop=extracts&exsentences=10&format=json&titles="
		request = requests.get(url+word).text
		pages = json.loads(str(request))['query']['pages']
		for page in pages:
			return(pages[page]['extract'])
	except Exception as e:
		print("[EXCEPT] wiki extraction: " + e)
		return "No Wiktionary Extract Available"

@app.route('/')
def randet():
	count = 0
	while count < 25:
		word = randWord()
		et = ety.origins(word, recursive=True)
		if len(et) > 0:
			return render_template("template.html", word=word, et=str(et), extract="")
		else:
			count += 1
	return(render_template( "template.html", 
		word="Lookup Failed.", 
		et="Tried twentyfive words, none had an etymology in the database. Halting to reduce spamming the API. Please try again in a few seconds.", 
		extract="")
	)

@app.route('/test')
def test():
	count = 0
	while count < 10:
		word = "test"
		et = "Testing the wiktionary lookup."
		if len(et) > 0:
			return render_template("template.html", word=word, et=str(et), extract=wikiExtract(word))
		else:
			count += 1
	return("Something Very Bad Happened Here.")