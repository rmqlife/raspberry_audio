from flask import Flask
from flask import render_template
from flask import request
# -*- coding: utf-8 -*-
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')
LIB_FOLDER="./Music"
UPLOAD_FOLDER="upload"
app = Flask(__name__)
app.config['LIB_FOLDER'] = LIB_FOLDER
app.config['UPLOAD_FOLDER'] = os.path.join(LIB_FOLDER,UPLOAD_FOLDER)
if not os.path.exists(app.config['UPLOAD_FOLDER']):
	os.mkdir(app.config['UPLOAD_FOLDER'])

with app.test_request_context('/hello'):
	assert request.path == '/hello'

@app.route('/upload/',methods=['GET','POST'])
def upload_file():
	if request.method == 'POST':
		f =  request.files['file']
		f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))	
	return render_template("upload.html")
		
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template("hello.html",name=name)

@app.route('/')
def index():
	return render_template("index.html")


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
	filepath_list=list()
	for root,dirs,files in os.walk(app.config['LIB_FOLDER']):
		for filepath in files:
			if filepath.endswith('.mp3'):
				print os.path.join(root,filepath)
				filepath_list.append(os.path.join(root,filepath))
	output=""
	for path in filepath_list:
		link="/pl/%s"% (path)
		output = output + '''<p><a href="%s">%s</a></p>'''%(link , path)
	return output

@app.route('/user/<username>')
def show_user_profile(username):
	#show the user profile for that user
	return 'User %s' % username

#print "name is", __name__ 
if __name__ == '__main__':
	app.run(host="0.0.0.0",port=5000,debug=True)
