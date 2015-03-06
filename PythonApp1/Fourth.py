#Week Two assignment 2.3
import os   #used to clear screen when another set of values are to be evaluated
import Helper

#Main loop for the whole script continuation purposes:
condition = True
while condition:

    #Getting input for Hours and Rates and casting to float for calculation purposes
    #Checking the type entered in case Non a Number entered
    while True:
        try:
            #Prompt for number of hours weekly:
            hours = raw_input('Enter number of hours per week: ')
            # check if valid variable type entered - checking for floats
            if(type(float(hours)) == float):
                print('The number is '+str(float(hours))+' is a valid number\n')
                hours = float(hours)
                break
        except ValueError:
            print('\nValue '+ hours +' is NOT a valid number, please correct it...\n')
    

    while True:
        try:
            #Prompt for available rate:
            rate = raw_input('Enter weekly rate: ')
            # check if valid variable type entered - checking for floats
            if(type(float(rate)) == float):
                print('The number is '+str(float(rate))+' is a valid number\n')
                rate = float(rate)
                break
        except ValueError:
            Helper.PrintText('\nValue '+ rate +' is NOT a valid number, please correct it...\n\n')

    print('\n')
    print('You have entered:\n')
    print('Hours:\t' + str(hours))
    print('Rate:\t' + str(rate))

    #============ Calculations ======

    Result = Helper.CalculateWeeklyRate(hours, rate)
    #Result = hours * rate

    #============ Output ========

    print('\n')
    print('======================================================================')
    print('= The weekly rate for ' +str(hours)+ ' hours at the rate of: ' +str(rate)+ ' is ' +str(Result)+'       =')
    print('======================================================================')

    print('\n')
    answer = True
    while answer:
        exitCondition = raw_input('Do you want to try again? [y/n] ')
        if exitCondition not in 'nNyY':
            print('Wrong answer, try again [y/n]')  
        else:
           answer = False

    #Let's clear the screen for the new set of values
    if exitCondition in 'yY':
        os.system('cls')
    
    #this condition check in case we want to finish the whole scrop, main condition variable
    if exitCondition in 'nN':
        condition = False
        print('OK! Bye, Bye!!!')