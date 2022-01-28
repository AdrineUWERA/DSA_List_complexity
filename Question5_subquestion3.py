# importing random library to generate random lists , timeit to track time , matplotlib to make graphs
# and math to perform log calculations

from random import randrange
import timeit
import matplotlib.pyplot as plt
import math


# method to sort the lists.
def sort_list(list2):
    list2.sort()
    return list2

# creating array that will hold the different input-size and time taken.
size_array = []
runtime_array = []

# Generating random lists with input size between 1 and 100.

for list_size in range(1, 100000, 20000):
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
    # displaying the information
    runtime_array.append(runtime)
    print(f"List size: {list_size} --> Runtime: {runtime}")

# plotting the points
plt.plot(size_array, runtime_array)

# naming the x axis
plt.xlabel('Input size')

# naming the y axis
plt.ylabel('Time')

# giving a title to my graph
plt.title('Graph')

# Taking one point on the graph to estimate the value for 1000000 input size
n1 = 80001
# retrieving the time taken at that point(80001)
runtime_eighty_one_input_size = runtime_array[4]
# The time complexity function will be :
# T(n) = C.nlogn
# finding the value of c:
C = runtime_eighty_one_input_size / (n1 * math.log(n1, 2))
# assigning the iput size to a variable
n = 1000000
# finding the time value for the value(1000000) and displaying it
time_complexity = C * n * math.log(n, 2)
print(f"Runtime when input size = 1000000 is {time_complexity} seconds")

# function to show the plot
plt.show()
