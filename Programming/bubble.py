def bubble(nums):
    times = len(nums) - 1
    for i in range(times):  # 这个循环负责设置冒泡排序进行的次数
        # 将数组最大的值放大最后 :5 跟 2比较 然后 跟 45 比较 依次替换  45替换到了最后
        times_two = len(nums) - i - 1
        for j in range(times_two):  # ｊ为列表下标
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    print(nums)


bubble([5, 2, 45, 6, 8, 2, 1])


