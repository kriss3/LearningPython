#!usr/bin/python

hrs = raw_input("Enter Hours:\t")
h = float(hrs)

r = raw_input("Enter Rate:\t")
r_standard = float(r)

if h <= 40:
    result = h * r
    print result
else:
    #establish hours above standar rate 
    h_standard = 40
    h_above = h - h_standard
    r_above  = r_standard *1.5

    standard_result = float(h_standard) * r_standard

    above_result = float(h_above) * r_above
    
    result = (h_standard * r_standard) + (h_above * r_above)

    print 'Hours above standard: ' +str(h_above)
    print 'Rate above standard:  ' + str(r_above)
    print 'Standard hours * standard rate: ' + str(standard_result)
    print 'Hours above * rate above:  ' + str(above_result)

    print result
    