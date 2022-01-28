# importing random library to generate random lists , timeit to track time and matplotlib to make graphs.
from random import randrange
import timeit
import matplotlib.pyplot as plt

# method to sort the lists.
def sort_list(list2):
    list2.sort()
    return list2

# creating array that will hold the different input-size and time taken.
size_array = []
runtime_array = []

# Generating random lists with input size between 1 and 100.
for list_size in range(1, 100, 20):
    list1 = [randrange(1000) for x in range(list_size)]
# Generating the start time of the process
    start_time = timeit.default_timer()
# printing the sorted list
    print(f"sorted list: {sort_list(list1)}")
# Recording the end time of the process
    end_time = timeit.default_timer()
# Calculating how long the process too by getting the difference between start and end time.
    runtime = end_time - start_time
# appending the size of the list and corresponding time taken
    size_array.append(list_size)
    runtime_array.append(runtime)
# displaying the information
    print(f"List size: {list_size} --> Runtime: {runtime}")


# plotting the points
plt.plot(size_array, runtime_array)

# naming the x axis
plt.xlabel('Input size')

# naming the y axis
plt.ylabel('Time')

# giving a title to my graph
plt.title('Graph')

# function to show the plot
plt.show()
