L=[1,2,3,4,5,6,7]
def func1():
    try:
        L = input("input list please: ").strip().split(",")
        if len(L) <= 4:
            return
        L = list(map(lambda x: int(x), L))
        print(L)

        return sum(L[0:4]) == 9
    except BaseException as e:
        print(e)

#func1()

def func2(L):
    s = set(L)
    return set([1,2,3,4]).issubset(s)
#print(func2(L))

def func3(L):
    return L[0]==6 and L[-1]==6
def func4(L1,L2):
    return L1[0]==L1[-1] and L2[0]==L2[-1]
def func5(L1,L2,L3):
    return sum(L1)+sum(L2)+sum(L3)
def func6(L):
    L.reverse()
def func7(L):
    if len(L)>5:
        return
    i = 0
    a=max(L)
    while i < len(L):
        L[i]=a
        i+=1
#func7(L)
#print(L)
def func8(L):
    leng = len(L)
    if leng > 1:
        return L[1] + L[0]
    elif leng == 0:
        return 0
    else:
        return L[0]
a = [1,2,3]
b = [4,5,6]
def func9(L1,L2):
    return [sum(L1)/len(L1),sum(L2)/len(L2)]

def func10(L):
    return {1,2}.issubset(L)

def func11():
    L = [1,2,3,1,2]
    return len(set(L))

def func12():
    a=[1,3,2]
    b=[4,3,2]
    #print (len(set(a).union(b)))
    print(len(a)+len(b))
#func12()

def func13():
    print(sorted([1, 2, 6, 4, 5, 7] + [1, 2, 6, 4, 5, 7]))
#func13()

def func14():
    str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque tempus fringilla dictum. Suspendisse consectetur, velit at tincidunt gravida, lacus nisl pharetra lorem, nec ultrices mauris enim ut lectus. Donec vitae libero quis enim sagittis bibendum. Praesent scelerisque eget nisl et bibendum. Ut pretium ante non fringilla pharetra. Ut ex mauris, feugiat ut orci eu, volutpat laoreet tellus. Praesent sollicitudin purus mauris, eu dignissim ipsum sollicitudin ut. Etiam dapibus, metus vel fermentum tincidunt, dolor ex aliquet felis, ac tempus nisl nunc eu lorem. Nullam lobortis nulla ut ipsum mollis, vel iaculis odio ultrices. Pellentesque vehicula est sed est auctor consectetur. Aliquam erat volutpat. Integer luctus, augue quis suscipit ultricies, velit dolor fermentum felis, vel fringilla tortor est interdum massa. Donec fermentum blandit elementum. Praesent cursus ultrices felis sed rutrum. Sed tortor eros, ultricies sed sem nec, bibendum dapibus est. Suspendisse molestie, urna ut pretium hendrerit, tellus nisi viverra orci, vitae cursus dui tortor at dui."
    print(len(str.split(" ")))
#func14()

import random
def home_1_FromBeetroot():
    a = list(map(lambda x1: random.randint(1,10),range(0,10)))
    b = list(map(lambda x1: random.randint(1,10),range(0,10)))
    c = list(set(a).intersection(b))
    print("first list: "+str(a))
    print("second list: "+str(b))
    print("set: "+str(c))
    #print(set(a).intersection(b))
#home_1_FromBeetroot()

def func_(a):
    if a%7==0 and a%5!=0:
        return a
    else:
        return 7
def home_2_FromBeetroot():
    a = list(range(1,100))
    a = set(map(func_,a))
    print(a)
#home_2_FromBeetroot()


i=0
L = [1,2,3,4]
while i<len(L):
    i+=1
    if i==1:
        continue
    print(i)
    #print(L[i])