#!/usr/bin/env python
import os
import sys
# coding=utf8
reload(sys)
sys.setdefaultencoding('utf-8')

def play_single(file_path):
	cmd="omxplayer %s"%file_path.encode('utf8')
	print cmd
	os.system(cmd)


def play_dir(target_dir):
	print target_dir
	for i in os.listdir(target_dir):
		if i.lower().endswith('mp3'):
			play_single(os.path.join(target_dir,i))

if __name__=="__main__":
	play_dir(sys.argv[1])
