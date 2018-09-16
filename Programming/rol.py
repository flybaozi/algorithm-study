# def LeftRotateString(s, n):
#     # write code here
#     ans = []
#     if s:
#         lists = list(s)
#         print(lists)
#         ind = n % len(lists)
#         # 2 除 11 的长度
#         print(ind)
#         ans = lists[ind:]
#         print(ans)
#         ans.extend(lists[0:ind])
#     return ''.join(ans)
# print(LeftRotateString("ASDASDEEQCV",2))


def LeftRotateString(s, n):
    return s[n:] + s[:n]


def LeftRotateString(s, n):
    # write code here
    if s == '':
        return s
    list_arr = list(s)
    list_arr_2 = []

    for i in range(n):
        list_arr_2.extend(list_arr.pop(-1))
        list_arr.insert(0, list_arr_2.pop(0))
        # list_arr_2.extend(list_arr.pop(0))
        # list_arr.extend(list_arr_2.pop(0))

    s1 = ''.join(list_arr)
    return s1


print(LeftRotateString('123123ASDBBCC', 2))

# def rotateString(s, offset):
#     # write you code here
#     if not offset:
#         return
#     if not s:
#         return
#
#     n = len(s)
#     offset = offset % n
#
#     for i in range(offset):
#         t = s.pop()
#         s.insert(0, t)


# rotateString('123123ASDBBCC', 2)
#
#
# def LeftRotateString(s, n):
#     if not s:
#         return ''
#     res1 = list(reversed(s[:n]))
#     res2 = list(reversed(s[n:]))
#     res = res1 + res2
#     res = list(reversed(res))
#     return ''.join(res)
#

#
#
# class Solution:
#     def reverse(self, s, l, r):
#         while l < r:
#             s[l], s[r] = s[r], s[l]
#             l += 1
#             r -= 1
#
#     def LeftRotateString(self, s, n):
#         if not s:
#             return s
#         s = list(s)  # str转成list处理
#         self.reverse(s, 0, n - 1)
#         self.reverse(s, n, len(s) - 1)
#         self.reverse(s, 0, len(s) - 1)
#         return ''.join(s)  # 直接join列表就变成str了
