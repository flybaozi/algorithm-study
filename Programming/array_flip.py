import random
def abc():
    a = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    new_list = []
    for i in a:
        new_list.append([1 - val for val in i[::-1]])
    return new_list


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(random.sample(a,4))
print(random.sample(a,4))

print(random.sample(a,4))

print(random.sample(a,4))


print(random.sample(a,4))