import numpy as np #the use of numpy shall be determined later

def main():
    i = 0 #i is an integer
    n = 10 #n is another integer
    x = 119.0 #x is a float

    #numpy can be used to declare arrays quickly


    y = np.zeros(n, dtype= float)

    #for loops are the typical looping operator to iterate through a variable

    for i in range(n):
        y[i] = 2.0 * float(i) + 1
    
    #this for loop iterates through i until it finally reaches the value n-1
    #it then assigns a second matrix variable on top of i

    #iterating througha variable array is done as such
    for y_element in y: #loops through each value of y
        print(y_element) #prints out the values taken from y in y_element

#to execute the function, we need to call the function outside of itself
if __name__ == "__main__":
    main()