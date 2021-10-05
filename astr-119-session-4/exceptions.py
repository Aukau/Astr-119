#python exceptions

try:
    print(a)    #as we know a doesn't exist so the program will throw an exception

except:
    print("Please define 'a'")
    a = input("What shall the value of a be? ")
    print(a)

try:
    print(no)
except NameError:
    print("no is still not defined") #This is the whole issue, but even if we couldn't find the issue here...
except:
    print("Something else went wrong")  #...it would be caught here