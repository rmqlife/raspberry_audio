from flask import Flask
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
app =  Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
	from flask import render_template
	return render_template("hello.html",name=name)

@app.route('/')
def index():
	return '''<h1>Air Music Player</h1> <h2><a href="/ls">list files</a></h2>'''

@app.route('/kill/')
def kill():
	from play_file import kill_all
	kill_all()
	return list_file()
	
@app.route('/pl/<path:file_path>')
def play_single(file_path):
	from play_file import play_single 
	from flask import render_template
	p=play_single(file_path)
	return render_template("play.html",pid=p.pid,file_path=file_path)

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

#fail to use
@app.route('/gen/')
def generate_url():
	with app.test_request_context():
		print url_for('login')

#print "name is", __name__ 
if __name__ == '__main__':
	app.run(host="0.0.0.0",port=5000,debug=True)
