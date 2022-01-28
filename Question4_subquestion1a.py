# import all necessary modules
from random import randrange  # module for generating random variables
import matplotlib.pyplot as plt  # module for plotting graphs
import timeit  # module for tracking time


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
for list_size in range(1, 100, 20):
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

# giving a title to the graph
plt.title('Graph')

# function to show the plot
plt.show()