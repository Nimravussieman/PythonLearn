import datetime as t
import time as t2
def func1():
    """
    Написать декоратор, который будет валидировать входные данные (параметры декорируемой функции,
    например разрешить только числа).
    Применить декоратор к функции, которая принимает несколько чисел.
    Вызвать декорируемую функцию. (И реализовать как класс)
    :return:
    """
    def decor(func):
        def wrapper(*args):
            print(args)
            func(tuple((x for x in args if isinstance(x, (int, float)))))
        return wrapper

    def decor_func(*args):
        print(*args)

    q = decor(decor_func)
    q(1,2,3,"k")

    def decor1(func):
        def wrapper(self,*args):
            print(args)
            func(tuple((x for x in args if isinstance(x, (int, float)))))
        return wrapper

    class a:
        @decor1
        def decor_func(*args):
            print(*args)

    #a().decor_func(1,2,3,"g")

#func1()

def func2():
    """
    Объявить класс Person с переменной класса _secret_data и переменной инстанса is_admin.
    Написать декоратор, который проверяет есть ли у пользователя доступ к данной
    функции(if is_admin). Применить декоратор к методу класса Person.get_secret_data
    (getter для _secret_data). Создать несколько объектов Person с разными is_admin
    значениями и вызвать у каждого метод get_secret_data.
    :return:
    """

    def decor(func):
        def wrapper(self):
            if self.is_admin:
                return func(self)
        return wrapper


    class Person:
        _secret_data = "derParoll"
        def __init__(self,is_admin,secret_data = ""):
            #Person._secret_data = secret_data
            self.is_admin = is_admin
        @decor
        def get_secret_data(self):
            return self._secret_data

    l = [Person(False),Person(False),Person(True)]
    [print(x.get_secret_data()) for x in l]
#func2()

def func3():
    """
    Написать функцию-декоратор и класс таймер и декорировать им несколько функций с вычислениями.
    :return:
    """
    class Timerr:
        def __init__(self,func):
            self._func = func
            self._t = None
        @property
        def runTime(self):
            return self._t
        def __call__(self, _list):
            time = t.datetime.now().time()
            res = self._func(_list)
            newTime = t.datetime.now().time()
            self._t = t.timedelta(hours=newTime.hour - time.hour,
                                 minutes=newTime.minute - time.minute,
                                 seconds=newTime.second - time.second,
                                 microseconds=newTime.microsecond - time.microsecond)
            print(self.runTime)
            return res
    @Timerr
    def fun1(_list):
        for x in _list:
            print(x)
            t2.sleep(1)
    @Timerr
    def fun2(_list):
        t2.sleep(_list[0])
    fun1([1,2,3])
    fun2([5])
#func3()

def func4():
    """
    Написать функцию-декоратор, которая будет выводить на экран с какими аргументами
    вызывается функция
    :return:
    """
    def decor(func):
        def wrapper(*args):
            print(args)
            func(args)
        return wrapper
    @decor
    def fun1(*args):
        print("do something with ",*args)
    fun1(1,2,3)
#func4()
import json
def func5():
    """
    Написать функцию-декоратор которая проверяет что функция возвращает валидные
    JSON данные. Применить декоратор к 2м функциям - одна возвращает валидные JSON
    данные, вторая - нет.
    :return:
    """
    def decor(fun):
        def wrapper(_dict):
            try:
                _dict.update(json.loads(fun()))
                return True
            except Exception as ex:
                return False
        return wrapper
    def fun1():
        return """{    "researcher": {
                "name": "Ford Prefect",
                "species": "Betelgeusian",
                "relatives": [
                    {
                        "name": "Zaphod Beeblebrox",
                        "species": "Betelgeusian"
                    }
                ]
                }
                }
                """
    def fun2():
        return "Upss!"

    l = {}
    if decor(fun1)(l):
        print(l)
    if decor(fun2)(l):
        print(l)
#func5()
from functools import wraps
def func6():
    """
    Объявить глобальную переменную history (пустой список) и реализовать функцию-декоратор,
    которая при вызове функции будет добавлять информацию о ней в history. Задекорировать
    несколько функций и вызвать их. В конце вывести history на экран
    :return:
    """
    history = []

    def decor(func):
        #@wraps(func)
        def wrapper():
            history.append(func.__doc__)
            func()
        return wrapper
    @decor
    def fun1():
        """fun1"""

    @decor
    def fun2():
        """fun2"""

    @decor
    def fun3():
        """fun3"""

    fun3()
    fun1()
    fun2()
    [print(x) for x in history]
#func6()

def func7():
    """
    Написать класс-регистратор для существующих классов.
    В классе должна быть переменная класса _registry, в которую необходимо добавить
    ссылку на класс обернутый декоратором. Реализовать метод get_registry для того чтоб
    посмотреть какие классы были зарегестрированы.
    :return:
    """
    class Reg:
        _registry = []
        @classmethod
        def getReg(self):
            [print(x) for x in self._registry]
        @classmethod
        def setClass(self,obj):
                self._registry.append(obj)

    #class ClassDecorator:

    def decorator(cls):
        return cls

    @decorator
    class DecoratedClass1:
        pass
    @decorator
    class DecoratedClass2:
        pass
    @decorator
    class DecoratedClass3:
        pass
    Reg.setClass(DecoratedClass1())
    Reg.setClass(DecoratedClass2())
    Reg.setClass(DecoratedClass3())

    Reg.getReg()
func7()