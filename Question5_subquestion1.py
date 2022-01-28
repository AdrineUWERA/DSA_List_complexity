# import all necessary modules
from random import randrange  # module for generating random variables
import matplotlib.pyplot as plt  # module for plotting graphs
import timeit  # module for tracking time
import numpy as np  # imports numpy


# a function to find the maximum value in a list
def find_max(list1):
    # initiate the starting maximum value as the first element of the list
    max_so_far = list1[0]

    # iterate through the list
    for item in list1:
        # checks if the item is greater than the maximum value so far
        if item > max_so_far:
            # assigns the item as the maximum value so far if the element was greater than the previous maximum value
            max_so_far = item
    # returns the final maximum value after iterating in the list
    return max_so_far


# array to store input list sizes
size_array = []

# array to store runtime of the program
runtime_array = []

# creates a loop to execute and track the runtime of the program for different list size
for list_size in range(1, 100000, 20000):
    # creating random list
    random_list = [randrange(1000) for x in range(list_size)]

    # track starting time of the program
    start_time = timeit.default_timer()

    # display output for the maximum value in the list
    print(f"Maximum value: {find_max(random_list)}")

    # tracks the ending time of the program
    end_time = timeit.default_timer()

    # calculates the runtime of the program
    runtime = end_time - start_time

    # records the list size to the size_array
    size_array.append(len(random_list))

    # records the runtime to the runtime array
    runtime_array.append(runtime)

    # displays the list size and corresponding runtime of the program
    print(f"List size: {list_size} --> Runtime: {runtime}")

# plotting the points
plt.plot(size_array, runtime_array)

# naming the x axis
plt.xlabel('Input size')

# naming the y axis
plt.ylabel('Time')

# giving a title to my graph
plt.title('Graph')

# define data to plot
x = np.array(size_array)
y = np.array(runtime_array)

# find line of best fit
a, b = np.polyfit(x, y, 1)

# add points to plot
plt.scatter(x, y)

# add line of best fit to plot
plt.plot(x, a * x + b)

print(f"\nGradient: {a}")
# T(n) = a*x+b
# drop the constant

# size of the list
x = 1000000

# calculates the time complexity
runtime_for_x = a * x

# displays the time complexity of the program for input size of 1000000
print(f"Runtime when input size = 1000000 is {runtime_for_x} seconds ")

# function to show the plot
plt.show()
