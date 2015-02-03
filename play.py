import os
import sys
# coding=utf8
reload(sys)
sys.setdefaultencoding('utf-8')

target_dir=sys.argv[1]


print target_dir
for i in os.listdir(target_dir):
	print i.encode('utf8')
	os.system("omxplayer "+os.path.join(target_dir,i.encode('utf8')))

