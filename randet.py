import os
import requests
import json
from flask import Flask, render_template, request
import ety

app = Flask(__name__)

wiktionary = "https://en.wiktionary.org/wiki/"
etymonline = "https://www.etymonline.com/word/"

# Wiktionary Extract Pull

def randWord():
	request = requests.get("https://random-word-api.herokuapp.com/word").text
	word = json.loads(str(request))[0]
	return word

def wikiExtract(word, depth=10):
	try:
		url= "https://en.wiktionary.org/w/api.php?action=query&prop=extracts&exsentences={depth}&format=json&titles={word}".format(
			word=word,
			depth=depth)
		request = requests.get(url).text
		pages = json.loads(str(request))['query']['pages']
		for page in pages:
			return(pages[page]['extract'])
	except Exception as e:
		print("[EXCEPT] wiki extraction:")
		print(e)
		return "No Wiktionary Extract Available"

@app.route('/')
def randet():
	count = 0
	while count < 25:
		word = randWord()
		et = ety.origins(word, recursive=True)
		if len(et) > 0:
			extract = wikiExtract(word)
			return render_template("template.html", word=word, et=str(et), extract=extract)
		else:
			count += 1
	return(render_template( "template.html", 
		word="Lookup Failed.", 
		et="Tried twentyfive words, none had an etymology in the database. Halting to reduce spamming the API. Please try again in a few seconds.", 
		extract="")
	)

@app.route('/<word>')
def specificLookup(word):
	et = ety.origins(word, recursive=True)
	extract = wikiExtract(word)
	return render_template("template.html", word=word, et=str(et), extract=extract)