from random import randrange
import time
import matplotlib.pyplot as plt

def sort_list(str):
    list2 = str.split()

    for i in range(0, len(list2)):
        list2[i] = int(list2[i])

    list2.sort()
    return list2


print(sort_list(input("Enter a list of integers separated by space: ")))


def sort_list(list2):
    list2.sort()
    return list2


print(sort_list([1, 2, 5, 6, 3, 4]))

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
    print(f"List size: {list_size} --> Runtime: {runtime}")


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
