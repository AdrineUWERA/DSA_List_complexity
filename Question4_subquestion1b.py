# import all necessary modules
from random import randrange  # module for generating random variables
import matplotlib.pyplot as plt  # module for plotting graphs
from memory_profiler import memory_usage  # module for tracking memory usage


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

# array to store memory usage of the program
memory_usage_array = []

# creates a loop to execute and track the runtime of the program for different list size
for list_size in range(1, 100, 20):
    # creating random list
    random_list = [randrange(1000) for x in range(list_size)]

    # display output for the maximum value in the list
    print(f"Maximum value: {find_max(random_list)}")

    # records the list size to the size_array
    size_array.append(list_size)

    # calculates the memory usage of the program
    mem_usage = memory_usage(-1, interval=.2, timeout=1)

    # records the total memory space used by the program
    memory_usage_array.append(mem_usage[-1])

    # displays the arr
    print(f"List size: {list_size} --> Memory space used: {mem_usage[-1]}")

# plotting the points
plt.plot(size_array, memory_usage_array)

# naming the x axis
plt.xlabel('Input size')
# naming the y axis
plt.ylabel('Memory usage')

# giving a title to my graph
plt.title('Graph')

# function to show the plot
plt.show()