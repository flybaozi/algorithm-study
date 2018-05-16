import math


def binary_search(list, item):
    low = 0
    high = len(list) - 1
    print("low是%d,high是%d" % (low, high))
    # print(high)
    while low <= high:
        mid = math.floor((low + high) / 2)
        # math.cell()向上取整
        print("mid是%d" % mid)
        guess = list[mid]
        print("猜测数字是多少%d" % guess)
        if guess == item:
            print("在数组的第%d位" % mid)
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9]

binary_search(my_list, 3)
