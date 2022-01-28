# a function to find the maximum value in a list
def find_max(list1):
    # initiate the starting maximum value as the first element of the list
    max_so_far = list1[0]

    # iterate through the list
    for item in list1:
        # checks if the item is greater than the maximum value so far
        if item > max_so_far:
            # assigns the item as the maximum value so far if the element was greater than the previous maximum value
            max_so_far = item
    # returns the final maximum value after iterating in the list
    return max_so_far


# sample example
# display the maximum value in the sample list
print(f"The maximum value is: {find_max([10, 26, 3000000, 474, 50, 123])}")