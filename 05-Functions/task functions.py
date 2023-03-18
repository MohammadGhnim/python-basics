
#Python Functions Tasks:

#1- Create a simple function that takes 2 numbers and print their values.

def num(x, y):
    print('num')

print(1, 2)
#2- Create a simple function that takes 2 numbers and return their values.
print('-------------------------------------')


def num(x, y):
    print('num')
    return

print(2, 3)
#3- In the above return function , use keyword arguments when calling the function.
print('-------------------------------------')


def sum(x, y = 1):
    result = x + y
    return result
m = sum(7)
   
print(m)

#4- In the above return function , give x and y default values of 0 and call the function with no arguments.
print('-------------------------------------')

def sum(x = 0, y = 0):
    result = x + y
    return result
n = sum()

print(n)
#5- Create a function that can take any number of arguments and print the sum of them.
print('-------------------------------------')


def mysum (x,y):
    result = x + y
    return(result)
l = mysum(5, 6)

print(l)

#6- Create the same sum function using the lambda.
print('-------------------------------------')

mysum = lambda x, y : x + y

#7- Call the lambda function at the same definition line.
print('-------------------------------------')
(lambda x, y: x + y)(2, 3)



#8- Write the difference between the local variable and global variable.
'''
Local variables: can only be accessed within the function or module in which they are defined,
global variables: can be used throughout the entire program
'''
