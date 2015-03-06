#8.4 
#Open the file romeo.txt and read it line by line. For each line, split the line into a list of 
#words using the split() function. The program should build a list of words. 
#For each word on each line check to see if the word is already in the list and if not 
#append it to the list. When the program completes, sort and print the resulting words 
#in alphabetical order.
#You can download the sample data at http://www.pythonlearn.com/code/romeo.txt

myList = list()

myFile = raw_input('Enter File Name: ')
if myFile == '':
    myFile = 'txtFiles/remeo.txt'

try:
    myFile = open('txtFiles/romeo.txt')
except:
    print('File not found')
    exit()


for line in myFile:
    line = line.strip()
    lineWords = line.split()
    for word in lineWords:
        if word not in myList:
            myList.append(word)

myList.sort()
print myList
