import os
import re
from random import randint
from flask import Flask, render_template, requests, redirect, url_for, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def randet():
	return("Hello")