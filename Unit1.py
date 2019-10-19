def f_(numb):
    if not (numb % 10) % 2:
        return []
    L = [numb]

    num = [ch for ch in str(numb)]

    i=0
    n=len(num)
    while i<n-1:
        save = num[0]
        if not (int(save) % 10) % 2:
            return []
        num[0:-1]=num[1:n]
        num[-1] = save
        L.append(int("".join(num)))
        i+=1
    return L
#print(f_(123))

def func1_1(i):
    ii=i-1
    while ii > 1:
        if not i % ii:
            return False
        ii -= 1
    return True

def func1(n):

    i=2
    L={2}

    while i < n:
        L2 = f_(i)
        for x in L2:
            if not func1_1(x):
                break
        else:
            L.update(L2)

        i+=1
    print(L)
func1(100000)

#print(list(range(1,1000,2)))

#print([x for x in range(2,1000) if (x % 10) % 2])

def func2():
    with open("Unit_words_dict","r") as f:
        #L = f.read()#.lower().split(" ")
        print(f.read())
#func2()

