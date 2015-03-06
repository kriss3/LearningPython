import sys
import Helper

#Lets Start:
print('This is my First Python App...Let' + "'s " + 'start' )
print("\nThis is nother start ")

stringArray = ['one','two','three','four','five', 'six','seven', 'eight', 'nine', 'ten']

intArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for test in intArray:
    print test

value1 = "This is my text"
value2 = 3
value3 = 4.5

print type(value2)

boolTest1 = Helper.CheckIfNumber(value1)
boolTest2 = Helper.CheckIfNumber(value2)
boolTest3 = Helper.CheckIfNumber(value3)

boolTest4 = Helper.CheckInstanceParam(value1)
boolTest5 = Helper.CheckInstanceParam(value2)
boolTest6 = Helper.CheckInstanceParam(value3)

print(boolTest1, boolTest2, boolTest3)
print(boolTest4, boolTest5, boolTest6)

Helper.PrintText('Good Bye, Press Any key ... ')


#while True:
#    char = sys.stdin.read(1)
#    if char == 'n':
#        break
#    else:
#        print char

#keyChar = raw_input('Do you want to continue? [y/n]')
#keyChar = keyChar.lower()
#while keyChar != 'n':
#    keyChar = raw_input('Insert character')
#    if(keyChar.lower == 'n'):
#        break
#    else:
#        continue


#condition = True
#while condition:
#    var = raw_input('Enter your name: ')
#    print('Hello ' + var+ '\n')
#    char = raw_input('Do you want to continue? [y/n] ')
#    while char not in 'ynYn':
#        print('Wrong answer, do you want to continue? [y/n]')
    
#    if char in 'nN':
#       condition = False
