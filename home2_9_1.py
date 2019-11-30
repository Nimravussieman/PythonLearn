from datetime import datetime
class Book:
    count = 0
    def __init__(self,name,file_path):
        self.name = name
        self.file_path = file_path
        Book.count += 1
        self.id = Book.count
        self._count_of_lines = 0

    # def get_text(self):
    #     with open(self.file_path) as f:
    #         return f.read()


    @property
    def count_of_lines(self):
        if self._count_of_lines:
            with open(self.file_path) as f:
                self._count_of_lines = len(f.readlines())
        return self._count_of_lines

# class BookIndex:
#     def __init__(self,book,index):
#         self.book = book
#         self._index = index
#     @property
#     def get_index(self):
#         return self._index
    # def __iter__(self):
    #     return self.name
class Order:
    def __init__(self,book,person_id):
        self.book_id = book.id
        self.book_name + book.name
        self.person_id = person_id
        self.when_was_taken = datetime.now()
        #self.expiration_date = datetime.now() + datetime.timedelta(days=30)
    @property
    def date_in(self):
        return self.when_was_taken + datetime.timedelta(days=30)

# class BookRack:
#     def __init__(self,book):
#         self.books_count = 0
#         self.all_books_rack = []
#         self.name = self.add_book(book)
#     def add_book(self,book):
#         if isinstance(book,Book):
#             self.books_count +=1
#             self.book_rack.append(BookIndex(book,self.books_count))
#             return book.name

class PersonCard:
    count = 0
    def __init__(self,name,surname,date_of_birth):
        PersonCard.count+=1
        self.id = PersonCard.count
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth

class Biblioteck:
    def __init__(self):
        self.book_index = 0
        self.person_index = 0
        self.all_books = set()
        self.person_cards = set()
        self.orders = set()
    def addBook(self,book):
        if isinstance(book,Book):
            self.book_index +=1
            self.all_books.add(book)
    def is_person_registered(self,person):
        return True if person in self.person_cards else False
    def register_person(self,person):
        if isinstance(person,Person):
            self.person_cards.append(person)
        return self.is_person_registered(person)
    def get_person_card(self, person):
        # вернуть карточку пользователя
        index = self.person_cards..index(person)
        return self.person_cards[index]
    def get_book(self, person, book_name):
        # выдать книгу определенному пользователю если она свободна
        # если пользователь зарегестрирован в библиотеке

        # проверить зарегестрирован ли пользователь в библиотеке
        # если нет - зарегестрировать
        if not is_person_registered(person, biblioteck):
            person_card = register_person(person, biblioteck)
        else:
            person_card = get_person_card(biblioteck, person)

        available_books = all_available_books(biblioteck)
        for book in available_books:
            if book == book_name:
                order = {
                    "book_name": book,
                    "when_was_taken": datetime.now(),
                    "expiration_date": datetime.now() + timedelta(days=30)
                }
                person_card["taken_books"].append(order)
        else:
            print("Book is not available")
