'''
Given the natural number n, determine the prime numbers
p1 and p2 such that n = p1 + p2 (check the Goldbach hypothesis).
'''

def IsPrime(number):
    '''
    Checks if the given number is prime.
    Input:  -number - integer
    Output: -True - if the number is prime
            -False - the number is not prime
    '''
    if (number < 2):
        return False
    if (number % 2 == 0 and number != 2):
        return False
    else:
        for i in range(3, int(number/2) + 1, 2):
            if (number % i == 0):
                return False
        return True

def FindNumbers(number):
    lst = []
    for i in range(1, int(number/2)):
        if(IsPrime(i) and IsPrime(number - i)):
            lst.append([i, number - i])
    return lst

number = int(input("Enter a number n: "))
print(FindNumbers(number))
    
