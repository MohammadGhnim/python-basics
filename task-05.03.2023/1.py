



# 1- for:

for x in range(1,51):
    if x == 40:
        continue
    print(x)




# 2- while:

x = 0
while x < 51:
    if x == 40:
        break
    print(x)
    x += 1

# 3-
# iterating each number in list

# 1- using for: 
for num in range(0, 200 + 1):
    if num % 2 == 0:
        print(num, end = " ")

# (not in list):
for i in range(201): 
    if i%2 == 0:
        print(i)

# 1- another way:
for even_numbers in range(4,201,2):
    print(even_numbers,end=' ')

# 2- using while:
max = 100
print('-------------------------')
max = 100
num = 1

while num <= max:
    if(num % 2 == 0):
        print("{0}".format(num))
    num = num + 1

# names = ['ahmed','mahmoud','ali'] 

# [5,7,3]
names = ['ahmed','mahmoud','ali']
for letter in 'names':
    print(letter)


print('********************')

items = ['ahmed','mahmoud','ali']

for item in items:
    if isinstance(item, int):
        print(len(str(item)))
    else:
        print(len(item))
