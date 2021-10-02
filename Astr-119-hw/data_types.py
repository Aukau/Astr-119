import numpy as np #thus we have the numpy library

#integers
i = 10      #this is an integer
print(type(i))  #print out the data type of the variable i

a_i = np.zeros(i, dtype=int) #this variable has called as an integer with "dtype=int"
print(type(a_i))        #What does this return? --->   'numpy.ndarray'
print(type(a_i[0]))     #What does this return? --->   'numpy.int32' - this is int32 rather than int64 because of windows?


                                    #####       Question for Jules Fowler       #####
            ####       What is the difference between int32 and int64 and what are the benefits and faults of each?        ####


#floats

x = 119.0   #this variable is a float
print(type(x))  #prints out the data type of x (float)

y = 1.19e2  #this variable is a float in scientific notation
print(type(y)) #What does this return? --->     'float'

z = np.zeros(i,dtype=float)
print(type(z))
print(type(z[0]))