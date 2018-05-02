def frog(high=None):
    day = 0
    current = 0
    up = 7
    down = 5
    while True:
        day += 1
        current += up
        print("上升了 %d 米" % current)
        if current >= high:
            break
        current -= down
        print("下降后 %d 米" % current)
    print("共花费%d" % day)


frog(30)
