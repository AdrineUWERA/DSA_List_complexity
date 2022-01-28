# Program to convert a string passed to it to lower case

# Function to convert a string to lower case
def convert_to_lowercase(my_string):
    string_list = list(my_string)  # Converts the string into a list of characters
    return_string = ""     # initialize string to be returned by the function
    for letter in string_list:    # iterates through every character of the string
        return_string += letter.lower()  # append each character after turning it into lower case

    return return_string      # returns the original string but now in lower case


print(convert_to_lowercase("Data Structure And Algorithms"))  # passes the string to the function and prints the returned string
