import home2_9, unittest, datetime
from unittest.mock import patch

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = home2_9.Book("1","Lorem.txt")

    def test__init__(self):
        self.assertIsInstance(self.book, home2_9.Book)        # self.assertIn("big size",pizza.Pizza.PIZZA_SIZE)

    def test_str(self):
        self.assertEqual(self.book.__str__(), "1")

    def test_count_of_lines(self):
        self.assertEqual(self.book.count_of_lines, 5)

class TestBookRack(unittest.TestCase):
    def setUp(self):
        self.book1 = home2_9.Book("1","Lorem.txt")
        self.book2 = home2_9.Book("2", "Lorem.txt")
        self.rack1 = home2_9.BookRack(self.book1)
        self.rack2 = home2_9.BookRack(self.book2)
    def test_init_(self):
        self.assertEqual(self.rack1.name,"1")
        self.assertEqual(self.rack2.name,"2")
        self.assertEqual(len(self.rack1._all_books_rack), 1)
    def test_books_count(self):
        self.assertEqual(self.rack2.books_count, 1)
        self.rack2.add_book(self.book1)
        self.assertEqual(self.rack2.books_count, 2)
        #print(self.rack2.books_count)
    def test_get_book(self):
        #print(self.rack2.books_count)
        self.assertIsInstance(self.rack2.get_book, home2_9.Book)
        #print(self.rack2.books_count)
        self.assertEqual(self.rack2.books_count, 0)
        self.rack2.add_book(self.book1)
        self.rack2.add_book(self.book1)
        self.assertEqual(self.rack2.books_count, 2)
    def test_str_(self):
        self.assertEqual(self.rack1.__str__(), "book: 1, count: 1")

date = datetime.datetime.now()
class TestOrder(unittest.TestCase):
    @patch.object(datetime,"now",return_value=date)
    def setUp(self):
        self.book1 = home2_9.Book("1", "Lorem.txt")
        self.order = home2_9.Order(self.book1)
        self.assertEqual(self.order.book, "1")
        self.assertEqual(self.order.when_was_taken, date)

    # def test_expiration_date(self):
    #     print(datetime.datetime.now())
    #     print(datetime.datetime.now() + datetime.timedelta(days=30))
        #self.assertEqual(self.order.expiration_date, date + datetime.timedelta(days=30))

    #def test_str(self):

class TestPerson(unittest.TestCase):

    def test_init_(self):
        person = home2_9.Person("1","2",date)
        self.assertEqual(person.name, '1')
        self.assertEqual(person.surname, "2")
        self.assertEqual(person.date_of_birth, date)

class TestPersonCard(unittest.TestCase):
    def setUp(self):
        self.book = home2_9.Book("1","Lorem.txt")
        self.person = home2_9.Person("name","surname",date)

    #@patch.object(datetime, "now", return_value=date)
    def test_init_(self):
        personcard = home2_9.PersonCard(self.person)
        self.assertEqual(personcard.person, self.person)
        #self.assertEqual(personcard.date_of_registration, date)
        self.assertEqual(personcard.ordered_books, [])

    def test_get_book_back(self):
        book = home2_9.Book("1", "Lorem.txt")
        order = home2_9.Order(book)
        person = home2_9.Person("name", "surname", date)
        personcard = home2_9.PersonCard(person)
        personcard.ordered_books.append(order)
        personcard.ordered_books.append(order)

        self.assertEqual(len(personcard.ordered_books), 2)

        self.assertIsInstance(personcard.get_book_back("1"), home2_9.Book)
        self.assertEqual(len(personcard.ordered_books), 1)

    def test_get_book_back_exception(self):
        with self.assertRaises(Exception):
            book = home2_9.Book("1", "Lorem.txt")
            order = home2_9.Order(book)
            person = home2_9.Person("name", "surname", date)
            personcard = home2_9.PersonCard(person)
            personcard.ordered_books.append(order)
            personcard.get_book_back("2")

class TestBiblioteck(unittest.TestCase):
    def setUp(self):
        self.book1 = home2_9.Book("1", "Lorem.txt")
        self.book11 = home2_9.Book("11", "Lorem.txt")
        self.book2 = home2_9.Book("2", "Lorem.txt")

        self.order1 = home2_9.Order(self.book1)
        self.order2 = home2_9.Order(self.book2)

        self.person1 = home2_9.Person("name1", "surname1", date)
        self.person2 = home2_9.Person("name2", "surname2", date)

        self.personcard = home2_9.PersonCard(self.person1)

        self.bibliotec = home2_9.Biblioteck()

    def test_addBook(self):
        self.assertEqual(self.bibliotec.addBook(self.book1), True)
        self.assertEqual(len(self.bibliotec.availabile_books_rack), 1)
        self.assertEqual(self.bibliotec.addBook(self.book1), True)
        self.assertEqual(len(self.bibliotec.availabile_books_rack), 1)
        self.assertEqual(self.bibliotec.availabile_books_rack[0].books_count, 2)

        self.assertEqual(self.bibliotec.addBook(self.book2), True)
        self.assertEqual(len(self.bibliotec.availabile_books_rack), 2)
        self.assertEqual(self.bibliotec.availabile_books_rack[1].books_count, 1)

        self.assertEqual(self.bibliotec.addBook(self.person1), False)
        self.assertEqual(self.bibliotec.availabile_books_rack[0].books_count, 2)
        self.assertEqual(len(self.bibliotec.availabile_books_rack), 2)
        self.assertEqual(self.bibliotec.availabile_books_rack[1].books_count, 1)

    def test_register_person(self):
        self.assertIsInstance(self.bibliotec.register_person(self.person1),home2_9.PersonCard)
        self.assertEqual(len(self.bibliotec.person_cards), 1)
        with self.assertRaises(Exception):
             self.assertEqual(self.bibliotec.register_person(self.personcard), home2_9.PersonCard)

    def test_is_person_registered_and_get_person_card(self):
        self.assertEqual(self.bibliotec.is_person_registered(self.person1), False)
        self.assertIsInstance(self.bibliotec.register_person(self.person1),home2_9.PersonCard)
        self.assertEqual(self.bibliotec.is_person_registered(self.person1), True)
        self.assertEqual(self.bibliotec.is_person_registered(self.person2), False)
        self.assertIsInstance(self.bibliotec.get_person_card(self.person1), home2_9.PersonCard)
        with self.assertRaises(Exception):
             self.bibliotec.get_person_card(self.person2)

    def test_book_count(self):
        self.assertEqual(self.bibliotec.addBook(self.book1), True)
        self.assertEqual(self.bibliotec.book_count(), 1)

    def test_get_book(self):
        self.bibliotec.addBook(self.book1)
        self.bibliotec.addBook(self.book2)
        self.bibliotec.get_book(self.person1,self.book1.name)
        self.bibliotec.get_book(self.person1, self.book2.name)
        self.bibliotec.show_all_books_info(self.person1)
        pers = self.bibliotec.get_person_card(self.person1)
        self.assertEqual(len(pers.ordered_books), 2)
        pers.get_book_back(self.book2.name)
        self.assertEqual(len(self.bibliotec.get_person_card(self.person1).ordered_books), 1)

    def test_get_book_back(self):
        self.bibliotec.addBook(self.book1)
        self.bibliotec.addBook(self.book2)
        self.bibliotec.get_book(self.person1, self.book1.name)
        self.bibliotec.get_book(self.person1, self.book2.name)
        self.bibliotec.show_all_books_info(self.person1)
        pers = self.bibliotec.get_person_card(self.person1)
        self.assertEqual(len(pers.ordered_books), 2)
        self.bibliotec.get_book_back(self.person1,self.book1.name)
        self.assertEqual(len(self.bibliotec.get_person_card(self.person1).ordered_books), 1)
        self.bibliotec.show_all_books_info(self.person1)

unittest.main()