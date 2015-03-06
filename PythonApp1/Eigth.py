

x = 0
if x < 2 :
    print 'Small'
elif x < 10 :
    print 'Medium'
else :
    print 'LARGE'
print 'All done'


astr = 'Hello Bob'
istr = 0
try:
    istr = int(astr)
except:
    istr = -1
    print istr

astr = 'Hello Bob'
istr = int(astr)
print 'First', istr
astr = '123'
istr = int(astr)
print 'Second', istr