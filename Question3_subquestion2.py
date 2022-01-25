def convert_to_lowercase(my_string):
    string_list = list(my_string)
    return_string = ""
    for letter in string_list:
        return_string += letter.lower()

    return return_string


print(convert_to_lowercase("Data Structure And Algorithms"))
