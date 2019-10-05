import random
L = random.sample(range(30), 10)

def func1():
    i=0
    for x in L:
        if x==9:
            i+=1
    return i
#print(func1())

L = list(map(lambda x: random.randint(0, 100), range(20)))

def func2():
    chet = 0
    nechet = 0
    for x in L:
        if x%2==0:
           chet+=1
        else:
            nechet+=1
    print(L)
    print("chet= "+str(chet)+"\npnechet= "+str(nechet))
#func2()

def func3():
    """
    Пользователь должен ввести последовательность чисел через пробел.Для каждого числа
    выведите слово YES (в отдельной строке), если это число ранее встречалось в последовательности
    или NO, если не встречалось.
    :return:
    """
    try:
        L = input("input range: ").strip().split(" ")
        S = set()
        if len(L)==0:
            return
        for x in L:
            if x in S:
                print("Yes "+ x)
            else:
                S.add(x)
                print("No "+x)
    except BaseException as ex:
        print(ex)
#func3()

def func4():
    """
    Написать функцию, которая будет принимать пароль. Если в пароле есть буквы и цифры и его
    длина не менее 10 символов вывести: “Your password is strong.” в противном случае
    “Your password is not strong enough.”
    :return:
    """
    L = input("input password: ")
    char = False
    digit = False
    di = 0
    for x in L:
        if not char and x.isupper():
            char = True
        elif not digit and x.isdigit():
            di += 1
            if di == 5:
                digit = True
        if char and digit:
            break

    if char and digit and len(L)>9:
        print("Your password is strong.")
    else:
        print("Your password is not strong enough.")
func4()

def func5():
    try:
        digit = int(input("input digit: "))
        i = 1
        fact = 1
        while i!=digit:
            i+=1
            fact*=i
        print(fact)

    except BaseException as ex:
        print(ex)
#func5()

def func6():
    score = 0
    while True:
        L = random.sample(range(30), 2)
        digit = input("sum of range {}: ".format(L))
        if digit == 'q':
            break
        elif digit.isdigit() and int(digit) == sum(L):
            score+=1
        print("your score: "+ str(score))
    print("your score: " + str(score))

#func6()

def func7(n):
    #n = random.randint(2, 5)
    while True:
        if n==1:
            break
        elif n%2==0:
            n /= 2
        else:
            n = 3*n+1
        print("n= " + str(n))


#func7(5)



def func8(x):
    i=2
    L = [0,1]
    while i<=x:
        L.append(L[i-2]+L[i-1])
        i+=1
    print(L)
#func8(25)


def pr(L):
    print("            <------>")
    for x in L:
        print(x)
def func9():
    """
    9) Дано нечетное число n. Создайте вложеный список из n×n элементов, заполнив его
    символами "."(каждый элемент массива является строкой из одного символа). Затем заполните
    символами "*" среднюю строку массива, средний столбец массива, главную диагональ и побочную
    диагональ. В результате должны образовывать изображение снежинки. Выведите полученный массив
     на экран, разделяя элементы массива пробелами.

    :return:
    """

    n=2
    while True:
        n = random.randint(2,5)
        if n%2!=0:
            break
    L = list(range(n))

    i=0
    while i < n:
        L[i] = list(range(n))
        ii = 0
        while ii < n:
            L[i][ii] = "."
            ii+=1
        i+=1
    pr(L)
    ###############################################################

    i = n//2
    ii = 0
    while ii<n:
        L[i][ii]="*"
        ii+=1

    pr(L)
##############################################################

    i=0
    ii=n//2
    while i<n:
        L[i][ii]="*"
        i+=1
    pr(L)
#############################################################
    i=0
    ii=0
    while i<n:
        L[i][ii]="*"
        i+=1
        ii+=1
    pr(L)
#################################################################
    i=0
    ii=-1
    while i<n:
        L[i][ii]="*"
        i+=1
        ii-=1
    pr(L)
#func9()