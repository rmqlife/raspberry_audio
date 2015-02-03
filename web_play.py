from flask import Flask
import play_file
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
app =  Flask(__name__)

@app.route('/')
def index():
	return '''<h1>Air Music Player</h1> <h2><a href="/ls">list files</a></h2>'''

@app.route('/kill/')
def kill():
	play_file.kill_all()
	return list_file()
	
@app.route('/pl/<path:file_path>')
def play_single(file_path):
	p=play_file.play_single(file_path)
	return '<h2>playing %s</h2> <h2>pid=%d <a href="/kill">stop</a></h2> <h2><a href="/ls/">back to list</h2>'%(file_path,p.pid)

@app.route('/ls/')
def list_file():
	import os
	print "list"
	filepath_list=list()
	for root,dirs,files in os.walk("./Music"):
		for filepath in files:
			if filepath.endswith('.mp3'):
				print os.path.join(root,filepath)
				filepath_list.append(os.path.join(root,filepath))
	output=""
	for path in filepath_list:
		link="/pl/%s"% (path)
		output=output+'''<p><a href="%s">%s</a></p>'''%(link , path)
	return output


@app.route('/user/<username>')
def show_user_profile(username):
	#show the user profile for that user
	return 'User %s' % username

#print "name is", __name__ 
if __name__ == '__main__':
	app.run(host="0.0.0.0",port=5000,debug=True)
