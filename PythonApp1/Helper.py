import sys
import os

def PrintText(str):
    print str
    return

def CalculateWeeklyRate(hours, rate):
    result = hours * rate
    return result

#This will check whether what we pass to the method is a number
def CheckIfNumber(value):
    if (type(value) is int or type(value) is float):
        return True
    else:
        return False

#This will check the type of the parameter passed to the function using isinstance method
def CheckInstanceParam(value):
    if isinstance(value, int):
        return True
    elif isinstance(value, float):
        return True
    else:
        return False