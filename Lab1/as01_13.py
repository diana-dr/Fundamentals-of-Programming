'''
Determine the n-th element of the sequence 1,2,3,2,5,2,3,7,2,3,2,5,...
obtained from the sequence of natural numbers by replacing composed numbers
with their prime divisors, without memorizing the elements of the sequence.
'''

def IsPrime(number):
    if (number < 2):
        return False
    if (number % 2 == 0 and number != 2):
        return False
    else:
        for i in range(3, int(number/2), 2):
            if (number % i == 0):
                return False
        return True

def FindElement(n):
    '''
    Check every natural number and finds it's prime divisors, counting them.
    Input:  -the n-th position of the sequence
    Output: -the number which is find on the n-th position
    '''
    number = 1
    j = 1
    new_number = 1

    while (j != n):
        for i in range(2, int(number/2) + 1):
            if (IsPrime(i) and number%i == 0):
                j += 1
                new_number = i

                if (j == n):
                    return(new_number)
            
        if (IsPrime(number)):
            j += 1
            new_number = number
            
        if (j == n):
            return(new_number)
            
        number += 1

n = int(input("Enter the element's number: "))
print(FindElement(n))



        
