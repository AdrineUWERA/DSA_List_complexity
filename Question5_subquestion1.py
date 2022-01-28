from random import randrange
import matplotlib.pyplot as plt
import timeit
import numpy as np


def find_max(my_list):
    max_so_far = my_list[0]
    for i in my_list:
        if i > max_so_far:
            max_so_far = i

    return max_so_far


size_array = []
runtime_array = []


for list_size in range(1, 100000, 20000):
    list1 = [randrange(1000) for x in range(list_size)]
    start_time = timeit.default_timer()
    print(f"Maximum value: {find_max(list1)}")
    end_time = timeit.default_timer()
    runtime = end_time - start_time
    size_array.append(len(list1))
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

x = np.array(size_array)
y = np.array(runtime_array)

# find line of best fit
a, b = np.polyfit(x, y, 1)

# add points to plot
plt.scatter(x, y)

# add line of best fit to plot
plt.plot(x, a*x+b)

print(f"\nGradient: {a}")
# T(n) = a*x+b
# drop the constant

x = 1000000
time_complexity = a * x
print(f"Time complexity when input size = 1000000 is {time_complexity}")

# function to show the plot
plt.show()
