#define a function
def flow_control(k):
    #define a string based on the value of k
    if(k==0):
        s = "Variable k = %d equals 0." % k #the %d in this sentence allows for a variable to be inserted into the program without creating a break in quotation

    elif(k==1):
        s = "Variable k = %d equals 1." % k

    else:
        s = "Variable k = %d does not equal either 0 or 1." % k

    print(s) #completes the goal of this program (therefore s is a string while k is an int)

#define a main function
def main():
    #declare an integer
    i = 0

    #try our function "flow_control" for 0, 1, 2
    flow_control(i)
    i = 1
    flow_control(i)
    i = 2
    flow_control(i)

#running the program goes here
if __name__ == "__main__":
    main()