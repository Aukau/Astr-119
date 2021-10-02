import numpy as np
import sys

#define a function that returns a value

def expo(x):
    return np.exp(x) #returns the exponent of x

#define a subroutine that does not return a value
def show_expo(n):
    for i in range(n):
        print(expo(float(i)))   #brings the exponential for the value inputted for n for each value of n

#define a main function
def main():
    n = 10 #default value

    #check for any other system arguments in the cmd line
    if(len(sys.argv)>1):
        n = int(sys.argv[1])

    show_expo(n)


#time to run the function!! :)
if __name__ == "__main__":
    main()

#Flow of the program
#Step 1:
#   defining a function to return an exponent for a value of x
#Step 2:
#   