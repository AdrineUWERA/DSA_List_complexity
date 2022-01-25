import random
import time
import string
import matplotlib.pyplot as plt


def convert_to_lowercase(my_string):
    string_list = list(my_string)
    return_string = ""
    for letter in string_list:
        return_string += letter.lower()

    return return_string


size_array = []
runtime_array = []


for string_size in range(1, 100, 20):
    # printing uppercase
    letters = string.ascii_uppercase
    mystring = ''.join(random.choices(letters, k=string_size))
    start_time = time.time()
    print(f"Lowercase string: {convert_to_lowercase(mystring)}")
    end_time = time.time()
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

# function to show the plot
plt.show()
