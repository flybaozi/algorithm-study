def test1():
    arr = [["我", "你好"], ["你在干嘛", "你干啥呢"], ["吃饭呢", "打球呢", "看电视呢"]]
    new_arr = []
    for i in arr[0]:
        print(i)
        for j in arr[1]:
            new_arr.append(i + j)
    print(new_arr)

#
# def test():
#     while True:
#         test1(arr)


test1()
