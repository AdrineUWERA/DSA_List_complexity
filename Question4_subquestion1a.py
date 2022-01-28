from random import randrange
import matplotlib.pyplot as plt
import timeit


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
    print(list1)
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

# function to show the plot
plt.show()
