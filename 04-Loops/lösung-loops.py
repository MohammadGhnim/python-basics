# Python Loops Tasks


# 1- Print numbers from 0 to 10 using while

x = 0
while x < 11 :
    print(x)
    x += 1
    
# 2- Print numbers from 0 to 1o using for

for x in range (11):
    print (x)

# 3- Stop the loop if the number = 5

for x in range (11):
    if x == 5:
        break
    print (x)

# 4- Skip the 5 iteration from print

for x in range (11):
    if x == 5:
        continue
    print (x)
    
# 5- Print multiplication table from 1 to 5

for x in range (1,6):
    for y in range(1,11):
        print (f"{x}X{y} = \t{x*y}")
        
# 6- How to get numbers from 10 to 20 using range

for x in range(10, 21):
    print(x)
    
# 7- How to get numbers from 10 to 100 with 3 at each step using range

for x in range(10, 101, 3):
    print(x)
    
# 8- Get a list of even numbers from 1 to 100 using for
# (don't understand this question)

for x in range(1, 100 + 1):
    print(x)
    
# 9- Get a list of even numbers from 1 to 100 using while
# (don't understand this question)
x = 0
while x < 101 :
    print(x)
    x += 1
    
# 10- Get a list of even numbers from 1 to 100 using range
# (don't understand this question)
for x in range(1, 100 + 1):
    print(x)
