#4.6 
# Write a program to prompt the user for hours and rate per hour using
# raw_input to compute gross pay. Award time-and-a-half for the hourly rate for all hours
# worked above 40 hours. Put the logic to do the computation of time-and-a-half in a function
# called computepay() and use the function to do the computation. 
# The function should return a value. Use 45 hours and a rate of 10.50 per hour to
# test the program (the pay should be 498.75). 
# You should use raw_input to read a string and float() to convert the string to a number. 
# Do not worry about error checking the user input unless you want to - you can assume
# the user types numbers properly.

# Initial Code:
#     def computepay(h,r):
#    return 42.37

# hrs = raw_input("Enter Hours:")
# p = computepay(10,20)
# print "Pay",p


#if h <= 40:
#    result = h * r
#    print result
#else:
#    #establish hours above standar rate 
#    h_standard = 40
#    h_above = h - h_standard
#    r_above  = r_standard *1.5

#    standard_result = float(h_standard) * r_standard

#    above_result = float(h_above) * r_above
    
#    result = (h_standard * r_standard) + (h_above * r_above)

def computepay(hrs, rate, hrs_above, rate_above):
    result = 0
    result = (hrs * rate) + (hrs_above * rate_above)
    return result

try:
    hrs_input = raw_input("Enter Hours:\t")
    hrs_input = float(hrs_input)

    rate_input = raw_input("Enter Rate:\t")
    rate_input = float(rate_input)
except:
    print "Enter numeric value..."
    quit()

hrs_std = 0;
rate_above = 0
hrs_above = 0
if (hrs_input > 40):
    hrs_std = 40
    hrs_above = hrs_input - hrs_std
    rate_above = rate_input * 1.5
    
result = computepay(hrs_std, rate_input, hrs_above, rate_above)

print result;

