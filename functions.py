def func(n):
    def func1 ():
        return "Demo"
    def func2 ():
        return "python"
    if n == 1:
        return func1
    else:
            return func2
    a = func1()
    b = func2()
    print(a())
    print(b())