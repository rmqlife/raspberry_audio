#!/usr/bin/env python
import os
import sys
# coding=utf8
reload(sys)
sys.setdefaultencoding('utf-8')
def kill_all():
	os.system("killall omxplayer.bin")	

def play_single(file_path):
	cmd="omxplayer %s"%file_path.encode('utf8')
	print cmd
	import subprocess
	kill_all()
	import time
	time.sleep(1)
	p=subprocess.Popen(cmd,shell=True)
	return p

def play_dir(target_dir):
	print target_dir
	for i in os.listdir(target_dir):
		if i.lower().endswith('mp3'):
			play_single(os.path.join(target_dir,i))

if __name__=="__main__":
	play_single("lake.mp3")
	#play_dir(sys.argv[1])
