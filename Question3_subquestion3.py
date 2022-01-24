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
