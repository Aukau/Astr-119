#stringsssss

s = "I am a string."
print(type(s))

#boolean

yes = True      #Is this also equivalent to a 1 or 0 within the core processing?  ---> From what Brant said, it seems to be a yes
print(type(yes))

no = False
print(type(no))

#list -- ordered and changeable  (Why do we have changeable here? Are there data types that are unchangeable?)

alpha_list = ["a", "b", "c"]
print(type(alpha_list))     #will say tuple --> a tuple is a collection of variables?
print(type(alpha_list[0]))  #will say a string because of the quotation marks?
alpha_list.append("d")      #appends a new variable onto the end of the string ---> How do you append the variable to a specific point in the list
print(alpha_list)

#Tuple  --  ordered and unchangeable        --->        Because these are unchangeable, what are the benefits compared to a list?

alpha_tuple = ("a", "b", "c")
print(type(alpha_tuple))

try:            #Try should check for a certain exception that you either want or don't want, and will throw an exception if this is not allowed, allowing you to give a personalised failure comment on the program
    alpha_tuple[2] = "d"        #Remember that groups of variables start from [0] so [2] is the third variable of the grouping
except TypeError:
    print("We can't add elements to a tuple")
print(alpha_tuple)