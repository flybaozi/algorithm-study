# def jumpFloor(number):
#     if number == 1:
#         return 1
#     elif number == 2:
#         return 2
#     else:
#         temp1 = 1  # 临时变量，保存f(n-2)的结果
#         temp2 = 0  # 中间变量，用于传递数据
#         result = 2  # f(n)结果值
#         for i in range(3, number + 1):
#             temp2 = result  # 保存下一波f(n-2)的值
#             result = result + temp1  # 计算当前f(n)的值
#             temp1 = temp2  # 将下一波f(n-2)的值从temp2传递给temp1
#         return result  # 得出结果
#
#
# print(jumpFloor(14))


def climbStairs(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return climbStairs(n - 1) + climbStairs(n - 2)


print(climbStairs(14))
