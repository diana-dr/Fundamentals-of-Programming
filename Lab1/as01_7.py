'''
Determine a calendar data (as year, month, day) starting
from two integer numbers representing the year and the day
number inside that year.
'''


def leapYear(number):
    '''
    Checks if the year is a leap year.
    Input:  -number - the year
    Output: -True - if the year is a leap year
            -False - the year is not a leap year
    '''
    if (number % 4 == 0):
        return True
    return False


def checkDay(number):
    '''
    Checks if the given day is a valid one.
    Input:  -number - the day of the year
    Output: -True - if the day is valid
            -False - the day is not valid
    '''
    if ((leapYear and number <= 366) or (leapYear == False and number <= 365)):
        return True
    else:
        return False


def findDate(number1, number2):
    '''
    Finds the month and day of the year.
    Outputs the date.
    '''
    if (leapYear(number1)):
        lst = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        lst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    i = 0
    j = 1
    if (checkDay(number2)):
        while (number2 - lst[i] > 0):
            number2 = number2 - lst[i]
            j += 1
            i += 1
        return (str(number1) + '/' + str(j) + '/' + str(number2))
    else:
        return ('Invalid date')


number2 = 0

while (number2 != 1):
    number1 = int(input("Enter the year: "))
    number2 = int(input("Enter the day: "))
    print(findDate(number1, number2))
