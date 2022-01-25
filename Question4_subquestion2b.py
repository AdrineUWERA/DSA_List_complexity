from memory_profiler import memory_usage
import random
import string
import matplotlib.pyplot as plt


def convert_to_lowercase(my_string):
    string_list = list(my_string)
    return_string = ""
    for letter in string_list:
        return_string += letter.lower()

    return return_string


size_array = []
memory_usage_array = []

for string_size in range(1, 100, 20):
    # printing uppercase
    letters = string.ascii_uppercase
    mystring = ''.join(random.choices(letters, k=string_size))
    print(f"Lowercase string: {convert_to_lowercase(mystring)}")
    size_array.append(string_size)
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
