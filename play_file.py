#!/usr/bin/env python
import os
import sys
# coding=utf8
reload(sys)
sys.setdefaultencoding('utf-8')

def play_dir(target_dir):
	print target_dir
	for i in os.listdir(target_dir):
		if i.lower().endswith('mp3'):
			print i.encode('utf8')
			try:
				os.system("omxplayer "+os.path.join(target_dir,i.encode('utf8')))
			except KeyboardInterrupt:
				print 'cancel play'
				try:
					sys.exit(0)
				except SystemExit:
					os._exit(0)

if __name__=="__main__":
	play_dir(sys.argv[1])
