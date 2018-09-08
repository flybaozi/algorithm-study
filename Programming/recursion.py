# def fact(x):
#     if x == 1:
#         return 1
#     else:
#         return x * fact(x - 1)
#
#
# fact(4)
#


def sum_one(nums):
    if type(nums) is list:
        if not nums:
            return 0
        return nums[0] + sum_one(nums[1:])
    return "不是数组"


print(sum_one([1, 2, 3]))


def count(nums):
    if type(nums) is list:
        if not nums:
            return 0
        return 1 + count(nums[1:])
    return "不是数组"


print(count([1, 2, 3]))


def max_three(nums):
    if type(nums) is list:
        return nums[0] if nums[0] > nums[1] else nums[1]
    sub_max = max_three(nums[1:])
    return nums[0] if nums[0] > sub_max else sub_max
