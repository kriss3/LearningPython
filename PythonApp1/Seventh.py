
try:
    inp = raw_input('Enter value between 0.0 and 1.0: ')
    inp = float(inp)
except:
    print 'Please enter correct value!!!'
    quit()

if (inp < 0.0 or inp > 1.0):
    print 'Input out of range'
elif (inp < 0.6):
    print 'F'
elif (inp >= 0.6 and inp < 0.7):
    print 'D'
elif (inp >= 0.7 and inp < 0.8):
    print 'C'
elif (inp >= 0.8 and inp < 0.9):
    print 'B'
elif (inp >= 0.9):
    print 'A'