import random
import turtle as t
def funcFild(n=4):
    L = list(range(0,n*n))
    fild = []
    print(L)
    while 0<len(L):
        i=0
        tempL = []
        while i < n:
            digit = L.pop(L.index(random.choice(L)))
            if not digit:
                digit = ""
            else:
                digit = str(digit)
            tempL.append(digit)
            i+=1
        fild.append(tempL)
#print(fild[0][0])

def fPrint(L):
    while True:
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.forward(100)
fPrint([])