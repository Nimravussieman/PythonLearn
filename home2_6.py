#def func1():
    # """
    # Написать класс Distance с приватным атрибутом _distance (в метрах). Объявить для этого
    # атрибута setter, getter, deleter, который будет показывать дистанцию в метрах. Создать
    # вычисляемый атрибут для перевода дистанции в шаги (in_feet, 1м = 0.67 шагов)
    # :return:
    # """

class Distance:
    def __init__(self,newdistance):
        self._distance = newdistance
        self.in_feet = None

    def setdistance(self,distance):
        self._distance = distance

    def getdistance(self):
        return self._distance

    def deldistance(self):
        del self._distance

    @property
    def inFeet(self):
        return self.getdistance() / 0.67

    distance = property(getdistance,setdistance,deldistance)

    # d = Distance(1)
    # print(d.inFeet)
#func1()


# def func2():
#     """
#     Написать класс Wallet с приватными атрибутами класса: dollars, cents. Написать
#     setter, deleter, getter для cents и вычисляемый атрибут для общего количества денег.
#
#     :return:
#     """
class Wallet:
    def __init__(self, dollars=0, cents=0):
        try:
            self._dollars = int(dollars)
            self._cents = int(cents)
        except Exception as ex:
            self._dollars = 0 if self._dollars == None else self._dollars
            self._cents = 0 if self._cents == None else self._cents
            print(ex)

    def setcents(self,cents):
        self._cents = cents

    def deleter(self):
        del self._cents

    def getcents(self):
        return self._cents

    Cents = property(getcents,setcents,deleter)
    def dol(self):
        c = self._cents % 10
        return ((self._cents - c) // 100)+self._dollars

    @property
    def money(self):
        c = self._cents % 10
        return "{} dolars {} cents".format(self.dol(),c)
    @property
    def dollars(self):
        return "{} dolars".format(self.dol())
    @property
    def dollars_int(self):
        return self.dol()

    # w = Wallet(0,102)
    # print(w.dollars)
    # w.Cents += 100
    # print(w.dollars)
    # print(w.money)

#func2()

# def func3():
#     """
#     Создать класс Celcius с приватным атрибутом _temperature. Объявить для этого
#     атрибута setter, getter, deleter. Создать вычисляемый атрибут для перевода по фаренгейту.
#     :return:
#     """
class Celcius:
    def __init__(self,temperature):
        self._temperature = temperature

    def settemperature(self,temperature):
        self._temperature = temperature

    def deltemperature(self):
        del self._temperature

    def gettemperature(self):
        return self._temperature

    temperature = property(gettemperature,settemperature,deltemperature)

    @property
    def toF(self):
        return self.temperature * 1.8 + 32

    # temp = Celcius(10)
    # print(temp.toF)
#func3()

# def func4():
#     """
#     Создать класс USDCurrencyConverter, с приватным атрибутом current_value (в USD) и
#     вычисляемыми атрибутами для перевода из USD в другие валюты, например EUR, UAH.
#     :return:
#     """
class USDCurrencyConverter:
    def __init__(self,current_value):
        self._current_value = current_value

    def set_current_value(self,current_value):
        self._current_value = current_value
    def del_current_value(self):
        del self._current_value
    def get_current_value(self):
        return self._current_value
    value = property(get_current_value,set_current_value,del_current_value)

    @property
    def in_UAH(self):
        curs = 25
        return self.value * curs
    @property
    def in_EUR(self):
        curs = 0.89
        return self.value * curs

# def func5():
#     """
#     Создать класс Карта с атрибутами значение и масть, перегрузить методы __lt__, __gt__,
#     __eq__ для сравнения карт
#
#     :return:
#     """
class Card:
    card_banc = {"6":6,"7":7,"8":8,"9":9,"10":10,"val":11,"dam":12,"kor":13,"tuz":14}
    def __init__(self,value,type,koz):
        self._value = Card.card_banc.get(value)
        self._type = type
        self._koz = koz
    @property
    def value(self):
        return self._value
    @property
    def type(self):
        return self._type
    @property
    def koz(self):
        return self._koz

    def __lt__(self,other):
        if self.type == other.type:
            return True if self.value < other.value else False
        else:
            if other.koz:
                return True
            return False
    def __gt__(self,other):
        if self.type == other.type:
            return False if self.value < other.value else True
        else:
            if self.koz:
                return True
            return False
    def __eq__(self, other):
        return True if self.type == other.type and self.value == other.value else False

# def func6():
#     """
#     Создать иерархию наследования классов: место (локация), город, область, мегаполис
#     :return:
#     """
class Place:
    def __init__(self,name):
        self._place = name
    @property
    def place(self):
        return self._place
class City(Place):
    def __init__(self,place,name):
        super(City, self).__init__(place)
        self._city = name
    @property
    def city(self):
        return self._city
    def __str__(self):
        return self.city
class Region(Place):
    def __init__(self,place,*cities):
        super(Region,self).__init__(place)
        self._cities = [City(place,x) for x in cities]
    @property
    def region(self):
        return [city.city for city in self._cities]
class Metropolis(Place):
    def __init__(self,place,name):
        super(Metropolis, self).__init__(place)
        self._metropolis = name
    @property
    def metropolis(self):
        return self._metropolis
#     r=Region("ux","zapor","maric","melitop")
#     print(r.region)
# func6()
# def func7():
#     """
#     Создать иерархию наследования классов: Человек, Мужчина, Женщина,
#     Супермен (с приватным атрибутом force и методом save_world)
#     :return:
#     """
class Human:
    def __init__(self,name,age):
        self._name = name
        self._age = age
class Man(Human):
    def __init__(self,true,name,age):
        super(Man, self).__init__(name,age)
        self._man = true
class Superman(Man):
    def __init__(self,force,true,name,age):
        super(Superman, self).__init__(true,name,age)
        self._force = force

    def save_world(self,evil_force):
        if self._force > evil_force:
            return True
        # elif self._force == evil_force:
        #     return "борьба продолжается"

        return False
