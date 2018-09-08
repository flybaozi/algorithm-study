import math


def binary_search(nums, num):
    list_low = 0
    list_high = len(nums) - 1
    print("数组最大下标为%d" % list_high)
    # print(list_high)
    while list_low <= list_high:
        mid = math.floor((list_low + list_high) / 2)
        # math.floor()向下取整
        # math.cell()向上取整
        print("中间长度是%d" % mid)
        guess = nums[mid]
        if guess == num:
            print("已查找到被猜测数字，下标为%d" % mid)
            return mid
        if guess > num:
            list_high = mid - 1
        else:
            list_low = mid + 1
    return "查找元素不在指定的list中"


my_list = [1, 3, 10, 2, 4]
# 必须有序
binary_search(my_list, 3)
