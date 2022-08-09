import os
import re
from random import randint
from json import loads
from urllib import request
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def randet():
	blob = request.urlopen("https://random-word-api.herokuapp.com/word").read()
	word = json.loads(blob)[0]
	return(word)