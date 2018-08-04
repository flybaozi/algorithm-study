def first(words=None):
    dic = {}
    # 目的存储Key Value对应的次数
    # 分析字符串长度  循环
    for i in range(len(words)):
        # 根据长度进行循           环
        if words[i] in dic:
            dic[words[i]] += 1
        else:
            dic[words[i]] = 1
    for i in range(len(words)):
        if dic[words[i]] == 1:
            print(dic)
            return words[i]


print(first(words="9898cxzawedadadad123,;.../.wqe"))
