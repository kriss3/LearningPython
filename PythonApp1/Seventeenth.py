#9.4 Write a program to read through the mbox-short.txt and figure out who has the sent 
#the greatest number of mail messages. The program looks for 'From ' lines and takes the second 
#word of those lines as the person who sent the mail. 
#The program creates a Python dictionary that maps the sender's mail address to a count of 
#the number of times they appear in the file. 
#After the dictionary is produced, the program reads through the dictionary using a maximum 
#loop to find the most prolific committer.

myFile = raw_input('Enter File Name: ')
if myFile == '':
    myFile = 'txtFiles/mbox-short.txt'

try:
    fileHook = open(myFile, 'r')
except:
    print 'File not found...'
    exit()

emailList = list()
for line in fileHook:
    line = line.strip()
    if 'From:' not in line: 
        continue
    else:
        words = line.split()
        emailList.append(words[1])

emailDict = dict()
for key in emailList:
    emailDict[key] = emailDict.get(key, 0) + 1

for key, value in emailDict.items():
    if value == max(emailDict.values()):
        print key, value


    