import functools
import random
class Person:
    def __init__(self,permission):
        self.permission = permission
def func1():
    """
    Объявить словарь, в котором ключом будет permission (admin, loggedin, unknown etc)
    а значениями будут ссылки на функции, которые отображают доступный функционал данного
    пользователя. Объявить класс Person, у которого есть атрибут (свойство) permission.
    Создать экземпляры класса Person с различными permission и отобразить доступный функционал
    по словарю
    :return:
    """
    d = {"admin":lambda:print(["add user","delete user","etc"]),
        "loggedin":lambda: print(["send messege","add friend"]),
        "unknown":lambda: print(["register"])}

    l = [Person("admin"),Person("loggedin"),Person("unknown")]
    for x in l:
        d.get(x.permission)()
#func1()

def func2():
    """
    Пользователь вводить возраст. Написать функцию, если возраст больше 16 то объявить
    внутри функции функцию show_available_content, которая будет показывать доступные
    фильмы, вызвать show_available_content которая показывает скрытые данные. Если возраст
    меньше 16, вернуть сообщение что пользователю информация недоступна
    :return:
    """
    age = int(input("enter age: "))
    if age > 16:
        def show_available_content():
            print(" Friend of the Family","Cui hua kuang mo","Passion's Desire","Forbidden","Seduce Me: Pamela Principle 2")

        return show_available_content()
    else:
        return print("информация недоступна")
def func3(numList):
    """
Объявить две функции: 1 - принимает список чисел как аргумент и сортирует его по убыванию,
2 - принимает список чисел как аргумент и сортирует его по возрастанию. Отсортировать список
чисел по убыванию или по возрастанию, в зависимости от того что выберет пользователь.
 Реализовать с помощью функции, которая передается как аргумент    :return:
    """
    def func3_1(numList):
        numList.sort(reverse=True)
    def func3_2(numList):
        numList.sort()
    def action(numList,func):
        func(numList)
    d = {"<":func3_1,">":func3_2}
    act = input("enter action of list < or >: ")
    action(numList,d.get(act))
    return numList
#print(func3([1,2,9,4,0]))

import datetime as t
import time as t2
def func4(action):
    """
    Написать функцию таймер, которая будет принимать функцию как аргумент и вычислять время
    выполнения этой функции.

    :return:
    """
    time = t.datetime.now().time()
    action()
    newTime = t.datetime.now().time()

        #return "{}:{}:{}.{}".format(newTime.hour - time.hour,newTime.minute - time.minute,newTime.second - time.second,newTime.microsecond - time.microsecond)
    return print(t.timedelta(hours=newTime.hour - time.hour,
                                 minutes=newTime.minute - time.minute,
                                 seconds=newTime.second - time.second,
                                 microseconds=newTime.microsecond - time.microsecond))


#func4(lambda : [t2.sleep(1) for x in range(20)])


def func5():
    """
    Создать функцию create_adder, внутри которой будет объявлена функция add_elems(list_of_elems)
    и будет возвращаться эта функция. Вызвать функцию create_adder и сложить несколько рандомных
    чисел (произвольное количество) с помощью add_elems.

    :return:
    """
    def create_adder():

        def add_elems(list_of_elems):
            return sum(list_of_elems)
        return add_elems

    create = create_adder()
    return create([1,2,3])
#print(func5())

def func6():
    """
    Написать функцию create_counter, в которой будет объявлена переменная counter и
    функция generate_password, вернуть функцию generate_password. Функция generate_password
    должна генерировать пароль и увеличивать counter на 1. Вызвать функцию для генерации
    пароля несколько раз и посмотреть как изменится счетчик.

    :return:
    """
    def create_counter():
        counter = 0
        def generate_password():
            nonlocal counter
            counter +=1
            return "password{}".format(counter)
        return generate_password

    password = create_counter()
    [print(password()) for x in range(5)]
#func6()

    """
    Изменить пример make_averager, так чтоб функция хранила результат предыдущей суммы и
    количество елементов, тогда зная эти два числа можно вычислить новое среднее значение.
    (используйте nonlocal)

    :return:
    """
def make_averager():
    series = []  # замыкание переменной
    total = 0
    lenght = 0
    def averager(new_value):  # вложенная функция
        series.append(new_value)  # добавить значение в список
        nonlocal total, lenght
        total = sum(series)  # посчитать сумма всех
        lenght = len(series)
        return total/lenght  # вернуть среднее значение
    return averager  # вернуть функцию

# avg = make_averager()
# print(avg(10))
# print(avg(11))
# print(avg(12))

def func8():

    """
    С помощью функции map преобразовать случайного список целых чисел в новый список
    где каждый елеменет будет умножен на 2

    """
    l = random.sample(range(100), 10)
    print(l)
    l = list(map(lambda x:  x*2,l))
    print(l)
#func8()

def func9():
    """
    С помощью функции filter выбрать только положительные целочисленные елементы
    случайного списка

    :return:
    """
    l = random.sample(range(-100,100), 10)
    print(l)
    l = list(filter(lambda x: x >= 0, l))
    print(l)
#func9()

def func10():
    """
    С помощью функции reduce умножить все числа в списке

    :return:
    """
    l = random.sample(range(1,20), 5)
    print(l)
    l = functools.reduce(lambda a,b: a*b, l)
    print(l)
#func10()

def func11():
    """
    С помощью функции map преобразовать список строк в список чисел:
    [‘1’, ‘2’, ‘3’, ‘4’] => [1, 2, 3, 4]

    :return:
    """
    l = ['1', '2', '3', '4']
    print(l)
    l = list(map(lambda x: int(x), l))
    print(l)
#func11()

def func12():
    """
    С помощью функции map преобразовать список с милями в список с километрами, где 1 mile = 1.6 km

    :return:
    """
    mile = 1.609344
    l = [1, 2, 3, 4]
    print(l)
    l = list(map(lambda x: x * mile, l))
    print(l)
#func12()