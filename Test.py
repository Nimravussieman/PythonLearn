import datetime
import home2_9
class Book:
    count = 0
    def __init__(self,name,file_path):
        self.name = name
        self.file_path = file_path
        self.__count_of_lines = 0
        self.id_method = Book.id()
        Book.count+=1
        self.id = Book.count
        #lambda id = None: lambda new_id = None: id if not id else id = new_id
    # def get_text(self):
    #     with open(self.file_path) as f:
    #         return f.read()

    @property
    def count_of_lines(self):
        if not self.__count_of_lines:
            with open(self.file_path) as f:
                self.__count_of_lines = len(f.readlines())
        return self.__count_of_lines

    @classmethod
    def set_id(cls, id):
        if cls.id:
            cls.id = id
            return cls

    @staticmethod
    def id():
        _id = None
        def new_id(_new_id = None):
            nonlocal _id
            # if _id:
            #     return _id
            if not _id and _new_id:
                _id = _new_id
            return _id
        return new_id

    def set_id1(self, id):
        if self.id:
            self.id = id
            return self



    # def __str__(self):
    #     return None if not self.id else str(self.id)

class BookIndex(Book):
    def __init__(self,name,file_path,index):
        super().__init__(name,file_path)
        self._index = index

    @property
    def get_index(self):
        return self._index
    def __iter__(self):
        return self.name
# book = Book("name","Lorem.txt")
# print(book.id_method())
# #book.id = 1
# print(book.id_method(1))
# print(book.id_method(2))
# print("numbers of lines: "+str(book.count_of_lines))
# l = [Book("name1","path"),Book("name2","path")]
# i=l.index(book)
# print(l[i])
#print("person info: {}\n {}".format("person",[(str(x)+"\n") for x in [1,2,3]]),)

# print(datetime.datetime.now())
# print(datetime.datetime.now() + datetime.timedelta(days=30))

# date = datetime.datetime.now()
# book = home2_9.Book("1", "Lorem.txt")
# order = home2_9.Order(book)
# person = home2_9.Person("name", "surname", date)
# personcard = home2_9.PersonCard(person)
# personcard.ordered_books.append(order)
# personcard.ordered_books.append(order)
#
# print(personcard)
#
# print(personcard.get_book_back("1"))
# print(len(personcard.ordered_books))
# print(personcard.get_book_back("1"))
# print(len(personcard.ordered_books))

class MyClass:
    def __init__(self):
        self.a=10
    @classmethod
    def method(cls,obj):
        #print('%s classmethod. %d' % (cls.__name__, arg))
        print(obj.a)
m = MyClass()
MyClass.method(m)
