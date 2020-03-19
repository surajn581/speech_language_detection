import flask
from flask import Flask, request
import requests
import json
import os
import io

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
	return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/audio', methods=["GET", "POST"])
def audio_process():
	if request.method == "POST":
		if request.files:
			audio = request.files['file']
			print('audio received')
			print(audio)
			with io.BufferedReader(audio) as r:
				lines = [str(line,'utf-8') for line in r]
			print(lines)
			# audio.save('C:/Users/hp/AnneMe/','this.wav')
			# # with open("audio_file.wav", "wb") as file:
			# # 	file.write(audio.frame_data())
			# print('audio saved')

			return 'hogaya'

	return 'kuch'

app.run()