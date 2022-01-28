# importing pythonds to use stack and memory_profiler to track memory
from pythonds import Stack
from memory_profiler import profile


# program to reverse letters of a string

@profile  # a decorator which shows the function to be tracked
# method to reverse the string
def revstring(mystr):
    returnString = "" # a variable to hold the reversed string
    s = Stack()       # a stack to reverse the string
    chrsList = list(mystr)  # breaking the string into a list inorder to access individual characters
    for character in chrsList:  # looping through the list
        s.push(character)  # Adding the characters to the stack hence reversing them
    for counter in range(s.size()):  # looping till the size of the stack
         # removing the characters from stack and then assigning them to a string hence concatenating(combining) them again.
        returnString += (s.pop())

    return returnString # returning the reversed string.

# passing a string to reverse
mystring = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc at purus lobortis, finibus quam sit amet, euismod sapien. Morbi gravida venenatis tincidunt. Integer leo turpis, accumsan sit amet ultrices non, accumsan eu erat. Vestibulum tempus porttitor pellentesque. In quis neque vel velit ultrices tincidunt. Aenean a consequat purus. Praesent maximus tortor eu ante varius hendrerit. Nulla auctor sagittis lorem, sed dictum nibh semper eget. Nunc ac interdum nulla, eget porttitor massa. Nullam qu"
# printing the reversed string
print(revstring(mystring))


