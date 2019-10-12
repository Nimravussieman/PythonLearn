import sys
def func1(temp):
    return (temp - 32) * (5 / 9)


def func2(*args):
    return print(min(args))


def m_min(*args):
    res = 9223372036854775807
    # print(args)
    for x in args:
        # print(x)

        if res > x:
            res = x
    return res


def m_max(*args):
    res = -9223372036854775807
    for x in args:
        if res < x:
            res = x
    return res


def func3(choice, *args):
    d = {"min": m_min, "max": m_max}
    return d[choice](*args)


# print(func3('max',2,2,3,4,5))

def func4_append(*args):
    i = 1
    while i < len(args):
        for x in args[i]:
            if x not in args[0]:
                args[0].append(x)
        i += 1
    return args[0]


def func4_per(*args):
    L = []
    # print(args)
    for x in args[0]:
        # print(x)
        i = 1
        q = True
        while i < len(args):
            # print(args[i])

            if x not in args[i]:
                q = False
                break
            i += 1
        if q:
            L.append(x)
    return L


# print(func4_per([1,2,3,5],[234,56,78,1,3], [3,7,5]))

def func5(*args, sep, end):
    i = 0
    l = len(args) - 1
    str = ""
    while i < l:
        str += args[i] + sep
        i += 1
    #return str + args[l] + end
    sys.stdout.write(str + args[l] + end)



# print(func5("1","2","3",sep="o", end='<'))

def func6(str):
    l = -len(str)
    i = -1
    new_str = ""
    while i >= l:
        new_str += str[i]
        i -= 1
    # print(new_str)
    sys.stdout.write(new_str)


#func6("12345")

def func7(fig,*args):
    d = {'_':sum,"circle":lambda D: D[0] * 3.14}
    if fig != "circle":
        fig = "_"
        if len(args)<3:
            return
    return d[fig](args)
print(func7("c",7,7))

#print(func7(1, 2, 3))
import random
def func8():
    n = int(input("input size: "))
    #random.sample(range(100), k=n)
    L = [random.sample(range(n*n), k=n) for x in range(n)]
    print(L)
    return L
L = func8()

def func9(L):
    res = -9223372036854775807
    for x in L:
        s = sum(x)
        if res < s:
            res = s
    print(res)
func9(L)