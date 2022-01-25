from random import randrange
from memory_profiler import memory_usage
import matplotlib.pyplot as plt


# def sort_list(str):
#     list2 = str.split()
#
#     for i in range(0, len(list2)):
#         list2[i] = int(list2[i])
#
#     list2.sort()
#     return list2
#
#
# print(sort_list(input("Enter a list of integers separated by space: ")))


def sort_list(list2):
    list2.sort()
    return list2


size_array = []
memory_usage_array = []

for list_size in range(1, 100, 20):
    list1 = [randrange(1000) for x in range(list_size)]
    print(f"Sorted list: {sort_list(list1)}")
    size_array.append(list_size)
    mem_usage = memory_usage(-1, interval=.2, timeout=1)
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
