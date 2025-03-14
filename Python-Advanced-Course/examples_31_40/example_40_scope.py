# Example 40 - Variables scope and scope resolution

def func1():
    print(x)


def func2():
    x = 2
    print(x)


x = 4

func1()
func2()