def sub_sort(array, low, high):
    key = array[low]
    # 判断数组的第一个
    while low < high:
        # 判断数组组大最小是否有区间
        while low < high and array[high] >= key:
            print("此时key array[low] %d array[high] % d low是 %d high是%d" % (key, array[high], low, high))
            high -= 1
            print("处理后变换%s" % array)

        while low < high and array[high] < key:
            print("此时key array[low] %d array[high] % d low是 %d high是%d" % (key, array[high], low, high))
            array[low] = array[high]
            low += 1
            array[high] = array[low]
            print("处理后变换%s" % array)
    array[low] = key
    return low


def quick_sort(array, low, high):
    if low < high:
        key_index = sub_sort(array, low, high)
        quick_sort(array, low, key_index)
        quick_sort(array, key_index + 1, high)


if __name__ == '__main__':
    array = [5, 6, 4, 2, 3, 1]
    print('原：', array)
    quick_sort(array, 0, len(array) - 1)
    print('现：', array)


# 递归
def quick_search(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        low = [i for i in arr[1:] if i <= pivot]
        high = [i for i in arr[1:] if i > pivot]
        return quick_search(low) + [pivot] + quick_search(high)

