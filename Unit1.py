import time

L = {2}
global globRange

def f_(numb):

    List = [numb]

    num = [ch for ch in str(numb)]

    i=0
    n=len(num)
    while i<n-1:
        save = num[0]
        num[0:-1]=num[1:n]
        num[-1] = save

        integ = int("".join(num))
        if not integ % 2 or integ in L:
            return []
        List.append(integ)

        #L.append(int("".join(num)))
        i+=1

    if sum(List)/n == numb:
        return [numb]
    #print(sum(L)/n)
    return List
#print(f_(919))

def func1_1(i):
    #print(range[2:i-1])
    #ii=i-1
    #for ii in [x for x in range(2,i-1) if x % 2]:
    try:
        newRange = globRange[0:globRange.index(i)]
    except ValueError:
        newRange = [x for x in range(2,i-1) if x % 2]

    for ii in newRange:

    #while ii > 2:
        if not i % ii:
            return False
     #   ii -= 1
    return True

def func1(n):
    old = time.time()
    global globRange
    globRange = [x for x in range(2,n) if x % 2]
    i=2
    for i in globRange:
    #while i < n:
            L2 = f_(i)
            for x in L2:
                if x in L or not func1_1(x):
                    break
            else:
                L.update(L2)

      #      i += 1



    new = time.time()
    print(sorted(L))
    print(len(L))
    print(new - old)
func1(1000000)
#print(list(range(1,1000,2)))

#print([x for x in range(2,1000) if (x % 10) % 2])

def func2():
    with open("Unit_words_dict","r") as f:
        #L = f.read()#.lower().split(" ")
        print(f.read())
#func2()

