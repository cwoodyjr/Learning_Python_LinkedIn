# 
# Example file for variables
# LinkedIn Learning Python course by Joe Marini
#


# Basic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries
myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, 1, 2)
mydict = {"one" : 1, "two" : 2}

print(myint)
print(myfloat)
print(mystr)
print(mybool)
print(mylist)
print(mytuple)
print(mydict)

# re-declaring a variable works
myint = "abc"
print(myint)
# to access a member of a sequence type, use []
print(mylist[2])

# use slices to get parts of a sequence
print(mylist[1:4])
print(mylist[0:5:2])

# you can use slices to reverse a sequence
print(mylist[::-1]) #prints lst in reverse

# dictionaries are accessed via keys
print(mydict)
print(mydict["two"])
# ERROR: variables of different types cannot be combined
print("this is a string"+ str(123))
# Global vs. local variables in functions

def thisIsAFunction():
    global mystr  #this line makes mystr a global variable so it can be accessed from anywhere in the file
    mystr = "def"
    print(mystr)

thisIsAFunction()
print(mystr)

del(mystr) #this line deletes the variable
print(mystr) #this line throws an error as the variable no longer exists