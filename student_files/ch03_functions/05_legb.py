x = 10
def f1():
    x = 20

    def f2():
        x = 30
        print(x)
    f2()

f1()