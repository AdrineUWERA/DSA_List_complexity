from random import randrange
import time
import matplotlib.pyplot as plt


def find_max(my_list):
    max_so_far = my_list[0]
    for i in my_list:
        if i > max_so_far:
            max_so_far = i

    return max_so_far


size_array = []
runtime_array = []


for list_size in range(1, 100, 20):
    list1 = [randrange(1000) for x in range(list_size)]
    start_time = time.time()
    # print(start_time)
    print(f"Maximum value: {find_max(list1)}")
    end_time = time.time()
    # print(end_time)
    runtime = end_time - start_time
    size_array.append(list_size)
    runtime_array.append(runtime)
    print(f"List size: {list_size} --> Run time: {runtime}")
    # print("size %d time: %f % (list_size, (end_time - start_time))")

# print(size_array)
# print(runtime_array)

# plotting the points
plt.plot(size_array, runtime_array)

plt.axis([0, 100, 0, 0.1])
# naming the x axis
plt.xlabel('Input size')
# naming the y axis
plt.ylabel('Time')

# giving a title to my graph
plt.title('Graph')

# function to show the plot
plt.show()
