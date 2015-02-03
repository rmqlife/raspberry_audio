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

@app.route('/pd')
def play_dir():
	play_file.play_dir("lijian-yiran")
	return 'playing dir'

@app.route('/user/<username>')
def show_user_profile(username):
	#show the user profile for that user
	return 'User %s' % username

#print "name is", __name__ 
if __name__ == '__main__':
	app.run(host="0.0.0.0",debug=True)

