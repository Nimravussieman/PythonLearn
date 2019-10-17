import random

def func1():
    """
    Создать файл nums.txt с рандомными цифрами и нужно среди них найти самую большую цифру и написать его уже в новый max_num.txt файл

    :return:
    """
    L = random.sample(range(100), k=random.randint(1,100))
    #print(L)

    with open("nuts.txt", "r+") as f:
        f.write(" ".join(str(x) for x in L).rstrip())

        L = f.read().split(" ")
        n = -9223372036854775807
        print(L)
        for x in L:
            xx = int(x)
            if xx > n:
                n = xx
    with open("max_num.txt","w") as f:
        f.write(str(n))
#func1()

def func2():
    """
    Создайте файл nums.txt, содержащий несколько чисел, записанных через пробел.
     Напишите программу, которая подсчитывает и выводит на экран общую сумму чисел, хранящихся в этом файле
    :return:
    """
    with open("nuts.txt","r") as f:
        L = f.read().split(" ")
        n = 0
        print(L)
        for x in L:
            n += int(x)
    print(n)
#func2()

def func3():
    """
    Посчитать количество строк в файле и количество слов и символов в каждой строке
    :return:
    """
    with open("Lorem.txt", "r") as f:
        s = f.read().rstrip().lstrip().split("\n")
    print("strings: {}".format(len(s)))
    i=1
    while i <= len(s):
        print("words in string № {}: {}".format(i, len(s[i-1].split(" "))))
        i+=1
#func3()

def func4():
    """
    Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
    Окончанием ввода пусть служит пустая строка.
    :return:
    """
    with open("Practice4.txt","w") as f:
        while True:
            s = input("input your string: ")
            if s == "":
                return
            f.write(s+"\n")
#func4()
import json
def func5_1():
    while True:
        klas = input("input class NAME or press enter: ")
        L=[]
        if klas=="":
            break

        with open("_{}.txt".format(klas), "w") as f:
            while True:
                first = input("input first name or press enter: ")
                if first=='':
                    break
                last = input("input last name or press enter: ")
                if last=='':
                    break
                score = input("input score or press enter: ")
                if score=='':
                    break
                f.write("{} {} {}\n".format(first.replace(" ",""),last.replace(" ",""),score.replace(" ","")))

                #L.append({"first": first,"last": last,"score": score})
        #if len(L)==0:
            #break
        #with open("_{}.txt".format(klas),"w") as f:
            #f.write(json.dumps(L))

#func5_1()

def func5(string="8a"):
    with open("_{}.txt".format(string),"r") as f:
        L=f.read().splitlines()
        res = 0
        for x in L:
            score = int(x.split(' ')[2])
            res+=score
            if score<3:
                print(x)
        print("averrage: "+str(res))
#func5()

def func6():
    with open("Practice_9_6","r") as f:
        L1 = json.loads(f.read())
        L2=[]
        for x in L1:
            if x["completed"]:
                L2.append(x)
    with open("Practice_9_6_2.txt",'w') as f:
        f.write(json.dumps(L2))

#func6()

def func7():
    with open("Lorem.txt","r") as f:
        l=f.read().splitlines()[0].replace(",",'').replace('.','').split(" ")
        d={}
        for x in l:
            if x in d:
                d[x]+=1
            else:
                d[x]=1
    count=0
    for x in d.items():
        if x[1]>1:
            count+=1
            print(x)
    print("\ncount:",count,"words")
#func7()

def func8():
    with open("Practice_9_6","r") as f:
        L = json.loads(f.read())
        id_title = []
        id_completed = []
        for x in L:
            #print(list(x.items()))
            id_completed.append({"id":x["id"],"completed":x["completed"]})
            id_title.append({"id":x["id"],"title":x["title"]})
        #print(id_title)
    with open("id_completed.txt", "w") as f:
        f.write(json.dumps(id_completed))
    with open("id_title.txt", "w") as f:
        f.write(json.dumps(id_title))
    #############################################################

    with open("id_completed.txt", "r") as f:
        id_completed = json.loads(f.read())
    with open("id_title.txt", "r") as f:
        id_title = json.loads(f.read())
    with open("id_title_completed.txt","w") as f:
        n = len(id_completed)
        i = 0
        while i<n:
            id_completed[i]["title"]=id_title[i]["title"]
            i+=1
        f.write(json.dumps(id_completed))
func8()
