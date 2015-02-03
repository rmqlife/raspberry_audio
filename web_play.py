from flask import Flask
import play_file
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app =  Flask(__name__)

@app.route('/')
def index():
	return 'Index Page'

@app.route('/pl/')
def play_lake():
	play_file.play_single("lake.mp3")
	return 'playing lake.mp3'

@app.route('/user/<username>')
def show_user_profile(username):
	#show the user profile for that user
	return 'User %s' % username

#print "name is", __name__ 
if __name__ == '__main__':
	app.run(host="0.0.0.0",port=80,debug=True)

