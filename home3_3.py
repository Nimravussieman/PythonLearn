def func1():
    li = list(range(1, 5))
    l = iter(li)
    print(li)

    def sum(digit):
        try:
            d = next(digit)
        except StopIteration:
            d=0
            return d
        return d + sum(digit)

    print(f"sum = {sum(l)}")
# func1()

def func2(word):
    # i = iter(word)
    def comp(word,count,i):
        if i == count:
            return True
        if word[i] != word[count]:
            return False

        return comp(word, count-1, i+1)
    print(comp(word,len(word)-1,0))
# func2("wopow")
def func3(word):

    def new_word(new_w):
        if len(new_w)<=2:
            return f"({new_w})"
        return f"({new_w[0]}{new_word(new_w[1:-1])}{new_w[-1]})"

    print(new_word(word))
# func3("7oo4w")
def func4(x,y):

    if y==1:
        return x
    return x*func4(x,y-1)

# print(func4(5,8))
import os,logging
def func5(path,str=''):
    for root,dir,files in os.walk(path):
        old = str
        str += '\t'

        print(f"{old} curent path: {root}")

        print(f'{old}  files:')
        for _file in files:
            print(str + _file)
        print(f'{old}  dirs:')
        for _dir in dir:
            print(str+_dir)

        for _dir in dir:
            func5(_dir, str)

# func5("C:\Games")
def func5_1(path,str=''):
    str+='\t'
    logging.warning('|'+str+'|')
    for root,dir,files in os.walk(path):
        print(f"{str} curent path: {root}")

        print(f'{str}  files:')
        for _file in files:
            print(f'{str}\t f: {_file}')
        print(f'{str}  dirs:')
        for _dir in dir:
            print(f'{str}\t d: {_dir}')
            func5_1(_dir, str)
# func5_1("C:\Games")


def func6(n):
    if n == 1:
        print("yes")
    elif n < 1:
        print("no")
    else:
        func6(n-3)
# func6(4)
def func6_1(n):
    if n == 1:
        return "yes"
    elif n < 1:
        return"no"

    return func6(n-3)
# print(func6_1(5))