
# def func1():
class Kard:
    def __init__(self,mast,value):
        self.mast = mast
        self.value = value
    def __str__(self):
        return "{}: {}".format(self.mast,self.value)
class Koloda:
    _koloda = None
    def __init__(self,koloda = []):
        self.index = -1
        self._koloda = koloda
    def __iter__(self):
        return self
    def __next__(self):
        self.index +=1
        if self.index < len(self._koloda):
            return self._koloda[self.index]
        raise StopIteration

    # koloda = [Kard("Chirva","10"),Kard("Trefa","tuz"),Kard("Pika","8")]
    # koloda = Koloda(koloda)
    # for kard in koloda:
    #     print(kard)
#func1()

# def func2():
class Soldat:
    def __init__(self,name = '',ranc = "soldier"):
        self.ranc = ranc
        self.name = name
    def __str__(self):
        return "name: {}, ranc: {}".format(self.name,self.ranc)
class Army:
    _army = None
    def __init__(self,army = []):
        self.index = -1
        self._army = army
    def __iter__(self):
        return self
    def __next__(self):
        self.index += 1
        if self.index < len(self._army):
            return self._army[self.index]
        raise StopIteration

def func3():
    soldiers = [Soldat("1"),Soldat("2"),Soldat("3")]
    army = Army(soldiers)
    def gen(l):
        for x in l:
            yield x
    return gen(army)
# res = func3()
# try:
#     while True:
#         print(next(res))
# except StopIteration:
#     pass

#func2()

# def func4():
def fib(n):
    fib1 = fib2 = 1

    #n = int(input("Номер элемента ряда Фибоначчи: ")) - 2

    while n > 0:
        fib1, fib2 = fib2, fib1 + fib2
        n -= 1
        yield fib2
# n=10
# res = fib(n)
# for x in res:
#     print(x)
#func4()

# def func5():
class Simp:
    def __init__(self,n):
        self._n = n
        self._first = 2
    def __iter__(self):
        return self
    def __next__(self):

        while self._first < self._n:
            i = self._first - 1

            while i > 1:
                if not self._first % i:
                    self._first += 1
                    break
                i -= 1
            else:
                res = self._first
                self._first += 1
                return res
        else:
            raise StopIteration

    # s = Simp(100)
    # for x in s:
    #     print(x)
#func5()

# def func6():
def simp():
        _first = 2

        while True:
            i = _first - 1

            while i > 1:
                if not _first % i:
                    _first += 1
                    break
                i -= 1
            else:
                res = _first
                _first += 1
                yield res

    # g = simp()
    # for x in g:
    #     print(x)
#func6()

# def func7():
def fInner():
    with open("Lorem.txt","r") as f:
        for s in f:
            yield s
# lines = fInner()
# for x in lines:
#     print(x)
#func7()