a = 10


def something():
    global a
    a = 15
    print("local",a)
something()


print("global",a)
