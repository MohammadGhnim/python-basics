#Python Data Types Tasks

#1- Wich is the differences between ‘ ’ “ ” ‘’’ ‘’’

'''
a- Single & Double Quotes
Enclose strings. Either single or double quotes are fine.
Use single quotes as enclosing quotes to eliminate the need of escaping double quotes in a string, and vice versa.
b- Triple Quotes
Enclose strings containing both single and double quotes such that no escaping is needed.
Enclose multi-line strings.
'''
#2- Create a string with the name ‘mystro’
print('------------------------------------')

name = 'mystro'
#3- Make the string letters capital
print('------------------------------------')


name = 'mystro'
print(name.upper())

#4- Create a list of values from 10 to 20
print('------------------------------------')

l = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#5- Add 30 to the end of the list
print('------------------------------------')


l = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
l.append(30)
print(l)

#6- Add 40 as the second element of the list
print('------------------------------------')


l = [10,11,12,13,14,15,16,17,18,19,20]
l.append(30)
l.insert(1,40)
print(l)

#7- Print how many elements in the list
print('------------------------------------')


l = [10,11,12,13,14,15,16,17,18,19,20]
l.append(30)
l.insert(1,40)
print(len(l))

#8- replace the second element in the list with 100
print('------------------------------------')



l=[10,11,12,13,14,15,16,17,18,19,20]
l[1] = 100
print(l)

#9- Create a tuple with values from 1 to 5
print('------------------------------------')


t = (1, 2, 3, 4, 5)

#10- Can we add 10 to the end of the tuple?
print('------------------------------------')

# no, we can not

#11- Create a dict of value Mahmoud:28 , ahmed:30
print('------------------------------------')

d = {"Mahmod": 28, "ahmed": 30}

#12- Print Mahmoud age from the dict
print('------------------------------------')

d = {"Mahmod": 28, "ahmed": 30}
print(d['Mahmod'])

#13- What is the differences between mutable and immutable data types ?
print('------------------------------------')


'''
An object whose internal state can be changed is mutable.
On the other hand, immutable doesn't allow any change in the object once it has been created.
'''
