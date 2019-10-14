import random

def func1_1(x):
    return random.randint(0,x)

L = [func1_1(x) for x in range(30)]


def func1():
    #D={key: value for key, value }
    D={}
    for x in L:
        if x in D:
            D[x]+=1
        else:
            D.setdefault(x, 1)
    print(L)
    print(D)

def func2():
    D={"chet":0,"nechet":0}
    for x in L:
        if x%2==0:
            D["chet"]+=1
        else:
            D["nechet"]+=1
    print(L)
    print(D)
#func2()

def func3():
    str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis at vulputate lacus. Integer odio justo, dignissim eu efficitur efficitur, imperdiet eget magna. Cras sed ultricies augue. Ut tortor est, suscipit quis convallis eget, posuere sit amet eros. Vestibulum id nisl et neque pulvinar pulvinar non at neque. Nullam dignissim tincidunt euismod. Phasellus in purus diam. Nulla ullamcorper tellus felis, quis tempor libero elementum quis. Nunc vulputate efficitur justo, sed mattis velit rutrum ac.".split(" ")
    D = {}
    for x in str:
        if x in D:
            D[x] += 1
        else:
            D.setdefault(x, 1)
    print(L)
    print(D)

#func3()


def func4():
    D={"Hello": "Hi", "Bye": "Goodbye", "List": "Array"}
    word = input("input word: ")
    for key, value in D.items():
        if value == word:
            print(key)
            break
#func4()

def func5():
    str = input("input some digits: ").split()
    print([int(x)*2 for x in str])
#func5()

def func6():
    str = input("input some digits: ").split()
    print([x for x in str if int(x)%2==0])
#func6()


def func7():
    L=list(range(7,32,7))
    #print(L)
    print([x for x in range(1,32) if x not in L and (x+1) not in L])
#func7()


def func8():
    n=0
    while True:
        n = random.randint(2,5)
        if n%2!=0:
            break
    res = 0
    i=0
    ii=0
    L = [list(range(n)) for x in list(range(n))]
    while True:
        res+=L[i][ii]
        if i == n-1:
            break
        i+=1
        ii+=1
    while i>=0:
        res+=L[i][ii]
        i-=1
        ii-=1

    print(L)
    print(res)
#func8()

def func9():
    L=[]

    try:
        while 'y' == input("Want to talk about your family? y/n: ").lower():
            name = input("input name: ")
            age = int(input("input age: "))
            L.append({name:age})
        a={0:0}
        for d in L:
            if list(list(d.values()))[0] > list(a.values())[0]:
                a = d
        print("имя самого пожилого человека в семье: {}".format([*a.keys()][0]))


    except BaseException as ex:
        print(ex)

#func9()

def func10_1(*tup):
    return tup
def func10():
    d1 = {'aaa':10,'bbb':20,'ccc':40}
    d2 = {'ccc':100,'fff':93,'dfwjsf':19,'ooo':1}
    print("d1: {}".format(d1))
    print("d2: {}".format(d2))

    d1.update({key: value for key, value in d2.items() for k, v in d1.items() if (key == k and value > v) or key not in d1}.items())

    #[d1.setdefault(kk , vv) for kk,vv in {key: value for key, value in d2.items() for k, v in d1.items() if (key == k and value > v) or key not in d1}.items()]
    #print( *{key: value for key, value in d2.items() for k, v in d1.items() if (key == k and value > v) or key not in d1}.items())

    print("d1 new: {}".format(d1))
#func10()

def func11():
    D = {"Igor":['192.168.250.1', '192.168.250.2', '10.236.43.2'],"Denis":['193.168.250.2', '10.250.43.2']}
    ip = input("input ip: ")
    for name, ips in D.items():
        if ip in ips:
            print(name)
            break
func11()














 #   def func7_(x,xi):
 #       xi+=7
 #       print(xi)
 #       return x

 #   def func7_2():
 #       i=[7]
 #       #print(id(L))
 #       print([func7_(x,i) for x in range(1,32) if x != i[0] and x!= i[0]-1])
    #func7_2()

 #   def pr(x):
 #       print(x)
 #       return x

 #   def func7_1():
 #       L={k:v for k,v in zip(range(7,32,7),range(7,32,7))}
        #print(L.get(7))
 #       print([x for x in range(1,32) if x != [x for xx in range(7,32,7)] ])
    #func7_1()

