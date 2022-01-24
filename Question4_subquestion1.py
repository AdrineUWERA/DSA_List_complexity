from random import randrange
import time


def find_max(list1):
    max_so_far = list1[0]
    for i in list1:
        if i > max_so_far:
            max_so_far = i

    return max_so_far


for list_size in range(1,100000, 10000):
    list1 = [randrange(1000) for x in range(list_size)]
    start_time = time.time()
    print(start_time)
    print(find_max(list1))
    end_time = time.time()
    print(end_time)
    print(f"List size: {list_size} --> Run time: {end_time - start_time}")
    # print("size %d time: %f % (list_size, (end_time - start_time))")

