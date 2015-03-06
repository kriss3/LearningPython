#Exercise 1   (7.1 Assignment)

#Write a program to read through a file and print the contents of the file (line by line) all in upper case. 
#Executing the program will look as follows: 
#python shout.py 
#Enter a file name: mbox-short.txt 
#FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN  5 09:14:16 2008 
#RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG> 
#RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])   
#BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;   
#SAT, 05 JAN 2008 09:14:16 -0500 

#You can download the file from www.py4inf.com/code/mbox-short.txt 
# Use words.txt as the file name
import sys

fname = raw_input("Enter file name: ")

if fname == '':
    fname = 'txtFiles\words.txt'

try:
    fh = open(fname)
except:
    print('File does not exist...')
    exit()
    

for line in fh:
    line = line.upper()
    print line