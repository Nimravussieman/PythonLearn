import datetime
class Book:
    def __init__(self,name,file_path):
        self.name = name
        self.file_path = file_path
        self._count_of_lines = 0
    # def get_text(self):
    #     with open(self.file_path) as f:
    #         return f.read()
    @property
    def count_of_lines(self):
        if not self._count_of_lines:
            with open(self.file_path) as f:
                self._count_of_lines = len(f.readlines())
        return self._count_of_lines
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.__str__()

# class BookIndex:
#     def __init__(self,book,index):
#         self.book = book
#         self._index = index
#     @property
#     def get_index(self):
#         return self._index
    # def __iter__(self):
    #     return self.name

# class RentedBook:
#     def __init__(self,index,person):
#         self.book_index = index
#         self.

class BookRack:
    def __init__(self,book):
        self._all_books_rack = []
        self.name = self.add_book(book)

    @property
    def books_count(self):
        return len(self._all_books_rack)

    def add_book(self,book):
        if isinstance(book,Book):
            self._all_books_rack.append(book)
            return book.name

    @property
    def get_book(self):
        return self._all_books_rack.pop(0)

    def __str__(self):
        return "book: {}, count: {}".format(self.name,len(self._all_books_rack))
    def __repr__(self):
        return self.__str__()


class Order:
    def __init__(self,book):
        self.book = book
        self.when_was_taken = datetime.datetime.now()
        #self._expiration_date = datetime.datetime.now() + datetime.timedelta(days=30)
    @property
    def expiration_date(self):
        return self.when_was_taken + datetime.timedelta(days=30)
    def __str__(self):
        return "book: {}, when was taken: {}, expiration_date: {}".format(self.book, self.when_was_taken.strftime("%d/%m/%Y"), self.expiration_date.strftime("%d/%m/%Y"))
    def __repr__(self):
        return self.__str__()

class Person:
    def __init__(self,name,surname,date_of_birth):
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
    def __eq__(self, obj):
        return isinstance(obj, self.__class__) and obj.name == self.name and obj.surname == self.surname
    def __str__(self):
        return "name: {}, surname: {}, date of birth: {}".format(self.name,self.surname,self.date_of_birth.strftime("%d/%m/%Y"))
    def __repr__(self):
        return self.__str__()

class PersonCard:
    def __init__(self,person):
        self.date_of_registration = datetime.datetime.now()
        self.person = person
        self.ordered_books = []

    def __str__(self):
        return "person info: {}\n {}".format(self.person,[x for x in self.ordered_books])
    def __repr__(self):
        return self.__str__()

    def get_book_back(self,book_name):
        #l = [order for order in self.ordered_books if order.book.name == book_name]
        for i,order in enumerate(self.ordered_books):
            if order.book.name == book_name:
                return self.ordered_books.pop(i).book
        else:
            raise Exception


class Biblioteck:
    def __init__(self):
        self.availabile_books_rack = []
        self.donts = []
        self.person_cards = set()

    def addBook(self,book):
        if isinstance(book,Book):
            for rack in self.availabile_books_rack:
                if rack.name == book.name:
                    rack._all_books_rack.append(book)
                    return True
            self.availabile_books_rack.append(BookRack(book))
            return True
        return False

    def is_person_registered(self,person):
        for card in self.person_cards:
            if card.person == person:
                return True
        return False

    def register_person(self,person):
        if isinstance(person,Person):
            pers_c = PersonCard(person)
            self.person_cards.add(pers_c)
            return pers_c
        else:
            raise Exception("isinstance error")

    def get_person_card(self, person):
        # вернуть карточку пользователя
        for card in self.person_cards:
            if person == card.person:
                return card
        else:
            raise Exception("Not exists")

    def book_count(self):
        res = sum([len(rack._all_books_rack) for rack in self.availabile_books_rack])
        res += sum([len(card.ordered_books) for card in self.person_cards])
        # вернуть количество всех книг
        return res

    def show_all_books_info(self,person):
        # вывести на экран информацию о пользователе и книгах которые у него на руках
        try:
            card = self.get_person_card(person)
            print(card)
        except Exception:
            print("Not exists")

    def get_book_back(self, person, book_name):
        # вернуть книгу обратно в библиотеку
        card = self.get_person_card(person)
        self.addBook(card.get_book_back(book_name))

    # def all_available_books(self):
    #     # Сделать с помощью списковых включений
    #     return [book for rack in self.availabile_books_rack for book in rack._all_books_rack]

    def get_book(self, person, book_name):
        # выдать книгу определенному пользователю если она свободна
        # если пользователь зарегестрирован в библиотеке
        # проверить зарегестрирован ли пользователь в библиотеке
        # если нет - зарегестрировать
        if not self.is_person_registered(person):
            person_card = self.register_person(person)
        else:
            person_card = self.get_person_card(person)

        for rack in self.availabile_books_rack: #available_books:
            if rack.name == book_name:
                if len(rack._all_books_rack):
                    order = Order(rack._all_books_rack.pop())
                    person_card.ordered_books.append(order)
                    break
        else:
            print("Book is not available")


def main():
    print('library closed for construction \\(*_*)/')
if __name__ == '__main__':
    main()
