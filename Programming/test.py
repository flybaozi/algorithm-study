import json

# num = []
# i = 2
# for i in range(2, 100):
#     j = 2
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         num.append(i)
# print(num)

a = {"apple": "123", "banana": "234"}
# b = json.dumps(a)
# print(a["apple"])
# print(type(a))
# h = json.loads(b)
print(a["apple"])


def mm(num, arr):
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = (low + high) / 2
        guess = arr[mid]
        if num == guess:
            return mid
        elif num > guess:
            low = mid + 1
        elif num < guess:
            high = mid - 1
    return "未找到"


def bubble():
    arr = [2, 3, 51, 2, 1, 0]
    times = len(arr) - 1
    for i in range(times):
        times_two = times - i
        for j in range(times_two):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)


bubble()


def frog_jump(n=10):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return frog_jump(n - 1) + frog_jump(n - 2)


print(frog_jump())


def findsmallest(arr):
    smallest = arr[0]
    smallest_index = 1
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def two(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = findsmallest(arr)
        new_arr.append(arr.pop[smallest])
    return new_arr


import re


def aaa(nums):
    str = nums
    n = re.split("\D", str)
    m = 0
    l = 0
    while m != len(n):
        if len(n[m]) != 0:
            if len(n[m]) > len(n[l]):
                l = m
        m = m + 1
    print(n[l])


aaa("123456addd789")


def bubble(arr):
    times = len(arr) - 1
    for i in range(times):
        times_two = times - i
        for j in range(times_two):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)


bubble([1, 3, 2, 5, 3, 7, 8, 5, 4])


def frog_jump(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return frog_jump(n - 1) + frog_jump(n - 2)


print(frog_jump(10))


def mid(arr, item):
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = (low + high) / 2
        guess = arr[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        elif guess < item:
            low = mid + 1
    return mid


def query_first(arr):
    dic = {}
    for i in range(len(arr)):
        if arr[i] in dic:
            dic[arr[i]] += 1
        else:
            dic[arr[i]] = 1
    for i in range(len(arr)):
        if dic[arr[i]] == 1:
            return arr[i]




def frog_jump(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        frog_jump(n - 1) + frog_jump(n - 2)


def bubble(arr):
    times = len(arr) - 1
    for i in range(times):
        times_two = times - i
        for j in range(times_two):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)


def frog(high):
    day = 0
    current = 0
    up = 7
    down = 5
    while True:
        day = day + 1
        current = current + up
        if current >= high:
            break
        current -= down


def query_first(words):
    dic = {}
    for i in range(len(words)):
        if words[i] in dic:
            dic[words[i]] += 1
        else:
            dic[words[i]] = 1
    for i in range(len(words)):
        if dic[words[i]] == 1:
            return words[i]


def quick_search(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        low = [i for i in arr[1:] if i <= pivot]
        high = [i for i in arr[1:] if i > pivot]
        
