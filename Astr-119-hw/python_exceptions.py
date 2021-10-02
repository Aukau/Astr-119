#python exceptions let you deal with unexcpected results

try:
    print(a)        #remember a is not defined yet
except:
    print("a has not been defined yet!")

    #there are specific errors to help with cases
try:
    print(a)    #another exception is thrown
except NameError:
    print("a is still not defined!")    #tells the nature of the problem
except:
    print("Something else went wrong?")

#This will break our program out of its function because a is not defined
print(a)

#It is very annoying to see the yellow bar up top telling me that there are problems
#Thank you VSC, very cool

#Remember using exception makes sure that you properly understand what can go wrong with your program

#Can you try something like this
#   a = "I am a string"
#   try:
#       a == type(float)   ---> this might also be pseudo code but eh
#   except:
#       print("a should be a float")