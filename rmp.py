from flask import Flask,render_template,url_for,request,redirect
# -*- coding: utf-8 -*-
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')
LIB_FOLDER="./Music"
UPLOAD_FOLDER="upload"
ALLOWED_EXTENSIONS=set(['mp3','aac','wav'])
app = Flask(__name__)
app.config['LIB_FOLDER'] = LIB_FOLDER
app.config['UPLOAD_FOLDER'] = os.path.join(LIB_FOLDER,UPLOAD_FOLDER)
if not os.path.exists(app.config['UPLOAD_FOLDER']):
	os.mkdir(app.config['UPLOAD_FOLDER'])
with app.test_request_context('/hello'):
	assert request.path == '/hello'

def allowed_file(filename):
	return '.' in filename and \
		filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

@app.route('/upload/',methods=['GET','POST'])
def upload_file():
	if request.method == 'POST':
		f =  request.files['file']
		f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))	
	return render_template("upload.html")

@app.route('/hello/')
@app.route('/hello/<name>')
def say_hello(name=None):
	return render_template("hello.html",name=name)

#@app.errorhandler(404)
#def page_not_found(error):
#	pass

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/aloha/')
def aloha():
	return redirect(url_for("say_hello",name="Hawaii"))

@app.route('/kill/')
def kill():
	from play_file import kill_all
	kill_all()
	return list_file()
	
@app.route('/play/<path:file_path>')
def play_single(file_path):
	from play_file import play_single 
	from flask import render_template
	p=play_single(file_path)
	return render_template("play.html",pid=p.pid,file_path=file_path)

@app.route('/ls/')
@app.route('/ls/<path:subdir>')
def list_file(subdir=app.config['LIB_FOLDER']):
	if subdir==None or not os.path.exists(subdir):
		return redirect(url_for('list_file'))
	output=render_template("ls.html")
	for root,dirs,files in os.walk(subdir):
		for filepath in files:
			if allowed_file(filepath):
				full_path=os.path.join(root,filepath)
				link=url_for('play_single',file_path=full_path)
				output = output + '''<p><a href="%s">%s</a></p>'''%(link , filepath)
	return output

@app.route('/lsdir/')
@app.route('/lsdir/<path:subdir>')
def list_dir(subdir=app.config['LIB_FOLDER']):
	if subdir==None or not os.path.exists(subdir):
		return redirect(url_for('list_dir'))
	output=render_template("ls.html")
	for d in os.listdir(subdir):
		full_path=os.path.join(app.config['LIB_FOLDER'],d)
		if os.path.isdir(full_path):
			print d
			link=url_for('list_file',subdir=full_path)
			output = output + '''<p><a href="%s">%s</a></p>'''%(link , full_path)
	return output

@app.route('/user/<username>')
def show_user_profile(username):
	#show the user profile for that user
	return 'User %s' % username

#print "name is", __name__ 
if __name__ == '__main__':
	app.run(host="0.0.0.0",port=5000,debug=True)
