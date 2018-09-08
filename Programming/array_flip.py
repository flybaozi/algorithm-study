def abc():
    a = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    new_list = []
    for i in a:
        new_list.append([1-val for val in i[::-1]])
    return new_list