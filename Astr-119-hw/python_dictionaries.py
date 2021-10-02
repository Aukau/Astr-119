#define a dictionary data structure

#dictionaries have key : value for the elements  ---> similar to a list but allowing for a correlation between two data types
example_dict = {
    "class"         :   "Astr 119",
    "prof"          :   "Brant",
    "awesomeness"   :   10
}
print(type(example_dict))   #What is this going to return?      --->    'dict'

#get a value via a key
course = example_dict["class"]      #creating course as the value of "class"
print(course)

#change a value via a key
example_dict["awesomeness"] +- 1    #increases awesomeness by 1

#print the dictionary
print(example_dict)

#print dictionary element
for x in example_dict.keys():
    print(x, " : ", example_dict[x])       #This prints out all of the values for keys of x