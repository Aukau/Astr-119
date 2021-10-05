#define a dictionary data structure
#Dictionaries again allow for a correlation between a key and a value

example_dict = {
    "class"     :   "Astr 119",
    "prof"      :   "Brant",
    "awesomeness"       :   10
}
print(type(example_dict))       #this will print <class 'dict'>

example_dict_array_test = {
    "person"     :   "Me",
    "prime"      :   [1, 3, 5, 7, 11],
    "awesomeness"       :   10
}
for cool in example_dict_array_test.keys():
    print(cool, example_dict_array_test[cool])

print(type(example_dict_array_test["prime"]))

course = example_dict["class"]
print(course)

example_dict["awesomeness"] += 1