# importing random library to generate random lists , memory_profiler to track memory used and matplotlib to make graphs.

from random import randrange
from memory_profiler import memory_usage
import matplotlib.pyplot as plt

# method to sort the lists.
def sort_list(list2):
    list2.sort()
    return list2

# creating array that will hold the different input-size and memory taken.
size_array = []
memory_usage_array = []
# Generating random lists with input size between 1 and 100.
for list_size in range(1, 100, 20):
    list1 = [randrange(1000) for x in range(list_size)]
    print(f"Sorted list: {sort_list(list1)}")  # sorting the randomly generate list
    size_array.append(list_size)  # Recording the size of the list

# A memory_profiler method to track the memory usage where the first parameter (-1) to call the method to track
# current process and interval which specify to measure the memory every 0.2 seconds and
# timeout to stop measuring for one second to return the results
    mem_usage = memory_usage(-1, interval=.2, timeout=1)
# adding the calculated memory usage corresponding to the different sizes in an array and printing the memory used
    memory_usage_array.append(mem_usage[-1])
    print(mem_usage)


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
