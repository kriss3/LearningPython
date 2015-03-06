#Exercise 2    (7.2 Assignment)

#Write a program to prompt for a file name, and then read through the file
# and look for lines of the form: 

#X-DSPAM-Confidence:  0.8475 

#When you encounter a line that starts with "X-DSPAM-Confidence:" 
#pull apart the line to extract the floating point number on the line. 
#Count these lines and the compute the total of the spam confidence values from these lines. 
#When you reach the end of the file, print out the average spam confidence. 
#Enter the file name: mbox.txt Average spam confidence: 0.894128046745
#Enter the file name: mbox-short.txt 
#Average spam confidence: 0.750718518519 

#Test your file on the mbox.txt and mbox-short.txt files.

import os

x = 'Confidence'
counter=0
total = 0

#Example of the line: X-DSPAM-Confidence: 0.8475
def lineAnalysis(line):
    value = 0
    line = line.split(' ')
    value = float(line[1])
    return value

firstPrompt = raw_input('Enter file name: ')

#Directory:
directory = os.path.dirname('txtFiles/mbox.txt')

if firstPrompt == '':
    fileName = 'txtFiles/mbox.txt'
else:
    fileName = firstPrompt

try:
    fHandle = open(fileName, 'r')
except:
    print('File not Found...')

testTxt = ''

for line in fHandle:
    line = line.strip()
    if x in line:
        counter +=1
        lineValue = lineAnalysis(line)
        total = total + lineValue
        print lineValue

print '\n', counter
avg = total / counter
print ('%.2f' % total)
print ('%.2f' % avg) 