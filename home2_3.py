import datetime,abc
############################# 1.1 #################################
class Person:
    def __init__(self,firstName,lastName,date):
        self.firstName = firstName
        self.lastName = lastName
        self.date = date
    def get_age(self):
        return datetime.date.today().year - self.date.year
    def __str__(self):
        return "First name: "+self.firstName +"\nLast name: "+ self.lastName+"\nAge: "+ str(self.get_age())
    def __repr__(self):
        return self.__str__()
class Student(Person):
    def __init__(self,person):
        if isinstance(person,Person):
            self.firstName = person.firstName
            self.lastName = person.lastName
            self.date = person.date
        else:
            pass
    def __str__(self):
        return "Student " + super().__str__()
    def __repr__(self):
        return self.__str__()
class Teacher(Person):
    def __init__(self,person):
        if isinstance(person, Person):
            if isinstance(person, Person):
                self.firstName = person.firstName
                self.lastName = person.lastName
                self.date = person.date
            else:
                pass
    def __str__(self):
        return "Teacher" + super().__str__()
    def __repr__(self):
        return self.__str__()
######################################### 1.2 ##############################
class Vehicle:
    def __init__(self,rane):
        self.range = range
    def move(self):
        self.range -= 1
        return self.range
class Motorcycle(Vehicle):
    def __init__(self,range):
        self.wheels = 2
        super().__init__(range)
    def move(self):
        return super().move()
class Car(Vehicle):
    def __init__(self, range):
        self.wheels = 4
        super().__init__(range)
    def move(self):
        return super().move()
class Train(Vehicle):
    def __init__(self, range):
        self.wheels = 8
        super().__init__(range)
    def move(self):
        return super().move()
############################################### 1.3 #########################
class Terrain:
    def __init__(self,coordinates,area):
        self.coordinates = coordinates
        self.area = area
    def __repr__(self):
        return "{} {}".format(self.coordinates , self.area)
class Kingdom(Terrain):
    def __init__(self,coordinates,area,king):
        super().__init__(coordinates,area)
        self.king = king
    def __repr__(self):
        return "{} {}".format(super().__repr__() , self.king)
class Monarchy(Kingdom):
    def __init__(self,coordinates,area,capital,monarch):
        super().__init__(coordinates,area,capital)
        self.monarch = monarch
    def __repr__(self):
        return "{} {}".format(super().__repr__() , self.monarch)

class Reublic(Monarchy):
    def __init__(self,coordinates,area,capital,leader):
        super().__init__(coordinates,area,capital,leader)
        self.leader = leader
    def __repr__(self):
        return "{} {}".format(super().__repr__() , self.leader)

class State(Reublic):
    def __init__(self,coordinates,area,capital,presides):
        super().__init__(coordinates,area,capital,presides)
        self.presides = presides
    def __repr__(self):
        return "{} {}".format(super().__repr__() , self.presides)
################################################### 1.4 #######################
class Item:
    def __init__(self,weight,dimension,purpose):
        self.weight = weight
        self.dimension = dimension
        self.purpose = purpose
    def __repr__(self):
        return "Item"
class Mechanism(Item):
    def __init__(self,weight,dimension,purpose):
        super().__init__(weight,dimension,purpose)
    def __repr__(self):
        return "Mechanism"
class Product(Mechanism):
    def __init__(self,weight,dimension,purpose):
        super().__init__(weight,dimension,purpose)
    def __repr__(self):
        return "Product"
##################################### 1.5 ###############################
class Edition:
    def __init__(self,format,pages):
        self.format = format
        self.pages = pages
    def __repr__(self):
        return "{} {}".format(self.format , self.pages)
class Magazine(Edition):
    def __init__(self,format,pages,theme):
        super(Magazine, self).__init__(format,pages)
        self.theme = theme
    def __repr__(self):
        return "{} {}".format(super().__repr__() , self.theme)
class Book(Edition):
    def __init__(self,format,pages,theme):
        super(Book, self).__init__(format,pages)
        self.theme = theme
    def __repr__(self):
        return "{} {}".format(super().__repr__() , self.theme)
class TextBook(Edition):
    def __init__(self,format,pages,theme):
        super(TextBook, self).__init__(format,pages)
        self.theme = theme
    def __repr__(self):
        return "{} {}".format(super().__repr__() , self.theme)
################################# 1.6 ##################################
class Answer:
    def __init__(self,answer,trueness,score):
        self.answer = answer
        self.trueness = trueness
        self.score = score
class Test:
    def __init__(self,question,answers):
        self.question = question
        self.answers = answers
        self.choice = None
    def set_choices(self,*args):
        self.choice = args
    def get_score(self):
        return sum([ self.answers[x].score for x in self.choice])
class Testing:
    def __init__(self,tests):
        self.tests = tests
    def get_test(self):
        for t in self.tests:
            yield t
class Exam:
    def __init__(self,some_practice):
        self.some_practice = some_practice
class FinalExam:
    def __init__(self,exam,testing):
        self.exam = exam
        self.testing = testing
    def do_something(self):
        pass
########################################### 1.7 ############################
class Person:
    def __init__(self,firstName,lastName,date):
        self.firstName = firstName
        self.lastName = lastName
        self.date = date
    def get_age(self):
        return datetime.date.today().year - self.date.year
    def __str__(self):
        return "First name: "+self.firstName +"\nLast name: "+ self.lastName+"\nAge: "+ str(self.get_age())
    def __repr__(self):
        return self.__str__()
class Employee(Person):
    def __init__(self,person,salary):
        if isinstance(person,Person):
            self.firstName = person.firstName
            self.lastName = person.lastName
            self.date = person.date
            self.salary = salary

        else:
            pass
    def __str__(self):
        return "Employee " + super().__str__()
    def __repr__(self):
        return self.__str__()
class Worker(Employee):
    def __init__(self,person,salary,position):
        if isinstance(person, Person):
            if isinstance(person, Person):
                self.firstName = person.firstName
                self.lastName = person.lastName
                self.date = person.date
                self.salary = salary
                self.position = position
            else:
                pass
    def __str__(self):
        return "Worker" + super().__str__()
    def __repr__(self):
        return self.__str__()
class Engineer(Employee):
    def __init__(self,person,salary,position):
        if isinstance(person, Person):
            if isinstance(person, Person):
                self.firstName = person.firstName
                self.lastName = person.lastName
                self.date = person.date
                self.salary = salary
                self.position = position
            else:
                pass
    def __str__(self):
        return "Engineer" + super().__str__()
    def __repr__(self):
        return self.__str__()
############################################ 1.8 ############################
class Gods:
    def __init__(self,price):
        self.price = price
    def __repr__(self):
        return str(self.price)
class Toy(Gods):
    def __init__(self, weight, dimension, purpose,price):
        super().__init__(price)
        self.weight = weight
        self.dimension = dimension
        self.purpose = purpose
    def __repr__(self):
        return "Toy: {} {} {} {}".format(self.weight,self.dimension,self.purpose,super().__repr__())
class FoodProduct:
    def __init__(self,expiration_date):
        self.expiration_date = expiration_date
    def __repr__(self):
        return str(self.expiration_date)
class MilkProduct(FoodProduct,Gods):
    def __init__(self,expiration_date,price,name):
        FoodProduct.__init__(self,expiration_date)
        Gods.__init__(self,price)
        self.name = name
    def __repr__(self):
        return "MilkProduct"
########################################### 2.1 #######################
class Boat(abc.ABC):
    def __repr__(self):
        return  "Bout"
    @abc.abstractmethod
    def swim(self):
        pass
class Ship(Boat):
    def __init__(self,leng,weiht,bearing_capacity,name):
        self.leng = leng
        self.weiht = weiht
        self.bearing_capacity = bearing_capacity
        self.name = name
    def swim(self):
        return "Brrr...rr..r"
class Steamboat(Boat):
    def __init__(self,leng,weiht,bearing_capacity,name):
        self.leng = leng
        self.weiht = weiht
        self.bearing_capacity = bearing_capacity
        self.name = name
    def swim(self):
        return "BRRR...RR..R"
class Sailboat(Boat):
    def __init__(self,leng,weiht,bearing_capacity,name):
        self.leng = leng
        self.weiht = weiht
        self.bearing_capacity = bearing_capacity
        self.name = name
    def swim(self):
        return "Pshhh...sh..h"
############################################## 3 ########################
class Device(abc.ABC):
    @abc.abstractclassmethod
    def consume_electricity(self,volt):
        raise NotImplementedError
class Scanner(Device):
    def __init__(self,name):
        self._A = 1
        self.name = name
    def consume_electricity(self,volt):
        return self._A * volt
    def do_coppy(self):
        pass
class Scanner(Device):
    def __init__(self,name):
        self._A = 1
        self.name = name
    def consume_electricity(self,volt):
        return self._A * volt
    def do_scan(self):
        pass
class Printer(Device):
    def __init__(self,name):
        self._A = 2
        self.name = name
    def consume_electricity(self,volt):
        return self._A * volt
    def do_print(self):
        pass
class Copier(Printer,Scanner):
    def __init__(self,name):
        Printer.__init__(self,name)
        Scanner.__init__(self, name)
    def __repr__(self):
        return "Do everything"
