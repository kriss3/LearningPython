#10.2 

#Write a program to read through the mbox-short.txt and figure out the 
#distribution by hour of the day for each of the messages. You can pull the
#hour out from the 'From ' line by finding the time and then splitting the string a 
#second time using a colon.

# 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
#Once you have accumulated the counts for each hour, print out the counts, sorted 
#by hour as shown below. Note that the autograder does not have support 
#for the sorted() function.

file = raw_input('Enter file name: ')
if (file == ''):
	file = 'txtFiles/mbox-short.txt'

try:
	fHandler = open(file, 'r')
except:
	print 'File not found ...'
	exit()

#get lines from mailbox-short.txt
listLine = list()
for line in fHandler:
	line = line.strip()
	if 'From ' not in line: continue	
	listLine.append(line)

# I got list of lines 
# go through each line and get second item from the end

listTimes = list()
for line in listLine:
	words = line.split();
	time = words[-2:-1]
	listTimes.append(time)

# now u got a list of times only  - do the histogram based on an hour, split by ':'
myList = list()
myDict = dict()
for item in listTimes:
	myList = item[0].split(':')
	myDict[myList[0]] = myDict.get(myList[0], 0) +1

#use tuple to sort and print items
t = tuple()
t = myDict.items()
t.sort()

for key, value in t:
	print key, value
