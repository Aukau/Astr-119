x = [0.0, 3.0, 5.0, 2.5, 3.7]  #this has defined an array
print(type(x))      #what does this print out? ----> 'list'

print("Originally x = ", x)

#removing the third element
x.pop(2)
print("The new side of x = ", x)

#removing the element equal to 2.6
x.remove(2.5)
print(x)

#add an element to the end of the array
x.append(1.2)
print(x)

#you can make a copy of the array
y =x.copy()
print(y)

#finding the count of a specific variable in the array
print(y.count(0.0))

#print the index with the value of 3.7  --->   the location
print(y.index(3.7))

#sorting the list
y.sort()        #sorts in values lowest to highest
print(y)

#reversing the sort of the list
y.reverse()
print(y)

#removing all elements)
y.clear()
print(y)

#adding a variable to a specific location
x[0] = 5.9
print(x)