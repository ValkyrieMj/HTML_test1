# global a
a = 0

def test():
    global a
    a += 1
    return a

if __name__ == '__main__':
    for i in range(10):
        b = test()
        print b