def find_smallest(arr):  # 函数是找到数组中最小的元素
    smallest = arr[0]  # 用于存储最小的值，同时假定第一个元素是最小的
    smallest_index = 0  # 最小的值的索引，同时也假定最小值的索引是0
    for i in range(1, len(arr)):  # 遍历数组中每一个元素，从第二个开始
        if arr[i] < smallest:  # 如果第二个元素小于第一个元素
            smallest = arr[i]  # 那么赋值给smallest
            smallest_index = i  # 索引同样操作
    print(smallest_index)
    return smallest_index  # 返回数组中最小值的索引


def selection_sort(arr):  # 选择排序函数
    newArr = []  # 一个列表用于保存
    for i in range(len(arr)):  # 遍历每一个元素
        smallest = find_smallest(arr)  # 用上面的函数找到最小值
        newArr.append(arr.pop(smallest))
    return newArr


print(selection_sort([5, 3, 6, 2, 10]))
