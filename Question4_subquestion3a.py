from random import randrange
import timeit
import matplotlib.pyplot as plt


def sort_list(list2):
    list2.sort()
    return list2


size_array = []
runtime_array = []


for list_size in range(1, 100, 20):
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

# function to show the plot
plt.show()
