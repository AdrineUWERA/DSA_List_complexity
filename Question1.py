# Code to Measure time taken by program to execute.
import timeit
from pythonds import Stack

# store starting time
begin = timeit.default_timer()


# program body starts
# sample program
def revstring(mystr):
    returnString = ""
    s = Stack()
    chrsList = list(mystr)
    for character in chrsList:
        s.push(character)
    for counter in range(s.size()):
        returnString += (s.pop())

    return returnString


mystring = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc at purus lobortis, finibus quam sit amet, euismod sapien. Morbi gravida venenatis tincidunt. Integer leo turpis, accumsan sit amet ultrices non, accumsan eu erat. Vestibulum tempus porttitor pellentesque. In quis neque vel velit ultrices tincidunt. Aenean a consequat purus. Praesent maximus tortor eu ante varius hendrerit. Nulla auctor sagittis lorem, sed dictum nibh semper eget. Nunc ac interdum nulla, eget porttitor massa. Nullam qu"
print(revstring(mystring))
# program body ends

# store end time
end = timeit.default_timer()

# total time taken
print(f"Total runtime of the program is {end - begin}")
