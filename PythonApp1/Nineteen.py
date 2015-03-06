#Working with files and file systems:

import os
import sys

temp1 = os.path.join('D:\\','torrent')
print type(temp1)

try:
	temp2 = os.listdir(temp1)
except:
	print 'No such file' + temp1
	exit;

print type(temp2)

for item in temp2:
	print item

print sys.platform


temp3 = list(os.environ.items())
for item3 in temp3:
	if 'COMPUTERNAME' in item3:
		print item3

for param in os.environ.keys():
	print (param, os.environ[param])

print "--------------"
print temp3[1]

try:
	mf = open('txtFiles/mbox-short.txt')
except:
	print 'File not found ...'
	exit()

myLineList = mf.readlines()
for line in myLineList:
	line = line.strip()
	if line in ['\n', '\r\n']: continue
	print line
