import unittest
import pizza
import datetime
import home2_2
import home2_6
import home2_7
class TestPizza(unittest.TestCase):
    """
        написать тесты на классы, их методы и взаимодействия между собой из pizza.py
    """
    def setUp(self):
        self.pizza = pizza.Pizza(pizza.PIZZA_SMALL_SIZE)

    def test_pizza_init(self):
        self.assertIsInstance(self.pizza,pizza.Pizza)
        #self.assertIn("big size",pizza.Pizza.PIZZA_SIZE)

        self.assertEqual(self.pizza.pizza_size,pizza.Pizza.PIZZA_SIZE.get(pizza.PIZZA_SMALL_SIZE))
    def test_pizza_anit_Except(self):
        with self.assertRaises(TypeError):
            pizza.Pizza(2)
    def test_pizza_size(self):
        self.assertEqual(self.pizza.pizza_size, pizza.Pizza.PIZZA_SIZE[pizza.PIZZA_SMALL_SIZE])

class TestOrder(unittest.TestCase):

    def test_select_pizza(self):
        order = pizza.Order()
        order.select_pizza(pizza.PIZZA_SMALL_SIZE)
        order.select_payment(pizza.PAYMENT_BY_CARD)
        order.confirm_order(True)
        self.assertEqual(order.payment,order.PAYMENT_METHOD.get(pizza.PAYMENT_BY_CARD))
        self.assertIsInstance(order.pizza, pizza.Pizza)
        self.assertEqual(order.confirmed,True)

class TestUser(unittest.TestCase):
    def test_init(self):
        user = pizza.User(1)
        self.assertEqual(user.__str__(),"1")
    def test_get_last_order(self):
        order = pizza.Order()
        order.select_pizza(pizza.PIZZA_SMALL_SIZE)
        order.select_payment(pizza.PAYMENT_BY_CARD)
        order.confirm_order(True)
        user = pizza.User(1)
        self.assertEqual(user.get_last_order(), None)
        user.orders.append(order)
        self.assertEqual(user.get_last_order(),order)
    def test_can_create_order(self):
        order = pizza.Order()
        order.select_pizza(pizza.PIZZA_SMALL_SIZE)
        order.select_payment(pizza.PAYMENT_BY_CARD)
        order.confirm_order(True)
        user = pizza.User(1)
        self.assertEqual(user.can_create_order(),True)

        user.orders.append(order)
        self.assertEqual(user.can_create_order(),True)
        order.confirm_order(None)
        self.assertEqual(user.can_create_order(), False)


##########################  home2_2  tests  ##################################


class TestPerson(unittest.TestCase):
    def test_init(self):
        pers = home2_2.Person(datetime.date(1999,12,23),"first","Last")
        self.assertIsInstance(pers.get_age(),int)
    def test_is_teenager(self):
        pers = home2_2.Person(datetime.date(1999,12,23),"first","Last")
        #print(pers.get_age())
        self.assertEqual(home2_2.Person.is_teenager(pers),False)
class TestStudent(unittest.TestCase):
    def test__init(self):
        student = home2_2.Student(home2_2.Person())
        self.assertIsInstance(student,home2_2.Student)
class TestClassRoom(unittest.TestCase):
    def test_init(self):
        student = home2_2.Student(home2_2.Person())
        classroom = home2_2.ClassRoom(student)
        self.assertEqual(len(classroom.studentList),0)
        classroom = home2_2.ClassRoom([student])
        self.assertEqual(len(classroom.studentList), 1)
    def test_addStudent(self):
        classroom = home2_2.ClassRoom()
        self.assertEqual(len(classroom.studentList),0)
        classroom.addStudent(home2_2.Student(home2_2.Person()))
        self.assertEqual(len(classroom.studentList),1)
class TestSchool(unittest.TestCase):
    def test_add(self):
        student = home2_2.Student(home2_2.Person())
        teacher = home2_2.Teacher(home2_2.Person())
        classroom = home2_2.ClassRoom([student,student])
        school = home2_2.School()
        self.assertEqual(school.add_techer(teacher),True)
        self.assertEqual(len(school.teachers),1)
        self.assertEqual(school.add_class(classroom),True)
        self.assertEqual(len(school.classrooms),1)
        self.assertEqual(school.add_class(teacher),False)
    def test_get_teachers(self):
        teacher = home2_2.Teacher(home2_2.Person())
        school = home2_2.School()
        school.add_techer(teacher,"math")
        school.add_techer(teacher, "math")
        self.assertEqual(len(home2_2.School.get_teachers(school,"math")),2)
class TestSchedules(unittest.TestCase):
    def test_get_lesons_count(self):
        schedule = home2_2.Schedule(home2_2.Leson("axqwcc",home2_2.Teacher(home2_2.Person()),"math"),datetime.date.today(),105)
        student = home2_2.Student(home2_2.Person())
        schedule.set_absent(student)
        schedules = home2_2.Schedules()
        schedules.add_schedule(schedule)
        self.assertEqual(schedules.get_lesons_count(datetime.date.today()),1)
        self.assertEqual(len(schedules.get_absents(datetime.date.today(),"math")),1)


##################################
class TestHome2_6_1(unittest.TestCase):
    def test_init(self):
        distance = home2_6.Distance(1)
        self.assertEqual(distance.getdistance(),1)
        distance.distance = 2
        self.assertEqual(distance.getdistance(),2)
        self.assertEqual(distance.inFeet,2/0.67)
class TestHome2_6_2(unittest.TestCase):
    def test_init(self):
        walet = home2_6.Wallet(1,1002)
        self.assertEqual(walet.dollars_int,11)
        #print(walet.money)
class TestHome2_6_3(unittest.TestCase):
    def test_init(self):
        celsius = home2_6.Celcius(10)
        self.assertEqual(celsius.toF,10 * 1.8 + 32)
class TestHome2_6_4(unittest.TestCase):
    def test_init(self):
        d = 10
        converter = home2_6.USDCurrencyConverter(d)
        self.assertEqual(converter.in_UAH,d*25)
        self.assertEqual(converter.in_EUR,d*0.89)
class TestHome2_6_5(unittest.TestCase):
    def test_init(self):
        card1 = home2_6.Card("10","tref",False)
        card2 = home2_6.Card("val","tref",False)
        self.assertEqual(card1 == card2, False)
        self.assertEqual(card1 > card2, False)
        self.assertEqual(card1 < card2, True)
class TestHome2_6_6(unittest.TestCase):
    def test_init(self):
        place = home2_6.Place("here")
        self.assertEqual(place.place,"here")
        city = home2_6.City("here","zap")
        self.assertEqual(city.city,"zap")
        region = home2_6.Region("here","zap")
        self.assertEqual(region.region,["zap"])
        metropolis = home2_6.Metropolis("here","metr")
        self.assertEqual(metropolis.metropolis,"metr")
class TestHome2_6_7(unittest.TestCase):
    def test_init(self):
        self.assertEqual(home2_6.Superman(10,False,"man",30).save_world(20),False)

###############################################
class TestHome2_7_1(unittest.TestCase):
    def test_init(self):
        koloda = [home2_7.Kard("Chirva", "10"), home2_7.Kard("Trefa", "tuz"), home2_7.Kard("Pika", "8")]
        koloda = home2_7.Koloda(koloda)
        koloda.__next__()
        self.assertEqual(koloda.__next__().value,"tuz")
class TestHome2_7_2(unittest.TestCase):
    def test_init(self):
        soldats = [home2_7.Soldat("Chirva", "10"), home2_7.Soldat("Trefa", "tuz"), home2_7.Soldat("Pika", "8")]
        army = home2_7.Army(soldats)
        army.__next__()
        army.__next__()
        self.assertEqual(army.__next__().ranc, "8")
class TestHome2_7_4(unittest.TestCase):
    def test_func3(self):
        res = home2_7.func3()
        self.assertEqual(next(res).name, "1")
class TestHome2_7_3(unittest.TestCase):
    def test_fib(self):
        n=10
        res = home2_7.fib(n)
        self.assertEqual(next(res), 2)

class TestHome2_7_5(unittest.TestCase):
    def test_sim(self):
        s = home2_7.Simp(10)
        self.assertEqual(s.__next__(), 2)
        self.assertEqual(s.__next__(), 3)
        self.assertEqual(s.__next__(), 5)

class TestHome2_7_6(unittest.TestCase):
    def test_func_sim(self):
        g = home2_7.simp()
        self.assertEqual(next(g), 2)
        self.assertEqual(next(g), 3)
        self.assertEqual(next(g), 5)
class TestHome2_7_7(unittest.TestCase):
    def test_finner(self):
        lines = home2_7.fInner()
        next(lines)
        next(lines)
        next(lines)
        next(lines)
        next(lines)
        with self.assertRaises(StopIteration):
            next(lines)


unittest.main()