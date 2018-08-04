def merge_list(list1, list2):
    result = []
    while list1 and list2:
        if list1[0] < list2[0]:
            result.append(list1.pop(0))
        else:
            result.append(list2.pop(0))

    result.extend(list1)
    result.extend(list2)
    print(result)
    return result


# def merge_sort(list_one, list_two):
#     ret = []
#     i = 0
#     j = 0
#     while len(list_one) > i + 1 and len(list_two) > j + 1:
#         if list_one[i] <= list_two[j]:
#             ret.append(list_one[i])
#             i += 1
#         else:
#             ret.append(list_two[j])
#             j += 1
#     if len(list_one) > i + 1:
#         ret += a[i:]
#     if len(list_two) > j + 1:
#         ret += list_two[j:]
#     return ret
#
#
def get_median(data):
    half = len(data) // 2
    print(data[half])
    print(data[~half])
    return (data[half] + data[~half]) / 2


if __name__ == '__main__':
    a = merge_list(list1=[5, 6, 10, 13,  30], list2=[3, 7, 8, 9, 12])
    print(get_median(data=a))
#
# if __name__ == '__main__':
#     a = [1, 3, 4, 6, 7, 78, 97, 190]
#     b = [2, 5, 6, 8, 10, 12, 14, 16, 18]
#     print(merge_sort(a, b))
