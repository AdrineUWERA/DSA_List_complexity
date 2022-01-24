def find_max(list1):
    max_so_far = list1[0]
    for i in list1:
        if i > max_so_far:
            max_so_far = i
    return max_so_far


print(find_max([10, 26, 3000000, 474, 50, 123]))
