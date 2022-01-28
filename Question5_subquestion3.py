from random import randrange
import timeit
import matplotlib.pyplot as plt
import math


def sort_list(list2):
    list2.sort()
    return list2


size_array = []
runtime_array = []


for list_size in range(1, 100000, 20000):
    list1 = [randrange(1000) for x in range(list_size)]
    start_time = timeit.default_timer()
    print(f"Maximum value: {sort_list(list1)}")
    end_time = timeit.default_timer()
    runtime = end_time - start_time
    size_array.append(list_size)
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

n1 = 80001
runtime_eighty_one_input_size = runtime_array[4]
# T(n) = C.nlogn
C = runtime_eighty_one_input_size / (n1 * math.log(n1, 2))
n = 1000000
time_complexity = C * n * math.log(n, 2)
print(f"{time_complexity}")

# function to show the plot
plt.show()
