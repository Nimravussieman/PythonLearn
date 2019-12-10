import random
#l = random.shuffle(range(10))
#l = [8,9,3,0,10,1]
l=[10,9,8,7,6,5,4,3,2,1]
def funcBub(l):
    leng = len(l)-1
    while leng:
        j = 0
        while j < leng:
            if l[j] > l[j+1]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
            j += 1
        leng -= 1
    return l


def funcMer(l):
    leng = len(l)
    if leng > 2:
        newL = leng//2
        resL = funcMer(l[:newL])
        resR = funcMer(l[newL:])
        res = list(range(leng))
        i=0
        while resL or resR:
            if resL and resR:
                if resL[0] > resR[0]:
                    res[i] = resR.pop(0)
                else:
                    res[i] = resL.pop(0)
            else:
                if resL:
                    res[i] = resL.pop(0)
                else:
                    res[i] = resR.pop(0)
            i+=1
        return res

    elif leng == 2:
        if l[0] > l[1]:
            l[0],l[1] = l[1],l[0]
        return l
    return l


def funcQick(l):
    leng = len(l) - 1
    if leng < 1:
        return l
    resL = []
    resR = []
    i=0
    while i < leng:
        if l[-1]>l[i]:
            resL.append(l[i])
        else:
            resR.append(l[i])
        i+=1
    resL=funcQick(resL)
    resR=funcQick(resR)
    leng = len(resL)
    l[:leng] = resL
    l[leng] = l[-1]
    l[leng+1:] = resR
    return l

#print(funcQick(l))


# def funcSer(l,var):
#     i=0
#     x=len(l)
#     while x:
#         index = (x+i)//2
#         if i==index:
#             return False
#         if l[index] < var:
#             i=index
#         elif l[index] > var:
#             x=index
#         else:
#             return True
#     return False
#
# print(funcSer(funcQick(l),1))

def f(l,var):

    index = len(l) // 2

    if l[index] == var:
        return True
    elif len(l) == 1:
        return False
    elif l[index] < var:
        res=f(l[index:], var)
    else:# l[index] > var:
        res=f(l[:index], var)

    return res
#print(f(funcQick(l),2))