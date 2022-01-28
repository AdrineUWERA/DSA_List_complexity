import random
import timeit
import string
import numpy as np
import matplotlib.pyplot as plt


def convert_to_lowercase(my_string):
    string_list = list(my_string)
    return_string = ""
    for letter in string_list:
        return_string += letter.lower()

    return return_string


size_array = []
runtime_array = []


for string_size in range(1, 100000, 20000):
    # printing uppercase
    letters = string.ascii_uppercase
    mystring = ''.join(random.choices(letters, k=string_size))
    start_time = timeit.default_timer()
    print(f"Lowercase string: {convert_to_lowercase(mystring)}")
    end_time = timeit.default_timer()
    runtime = end_time - start_time
    size_array.append(string_size)
    runtime_array.append(runtime)
    print(f"List size: {string_size} --> Runtime: {runtime}")


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