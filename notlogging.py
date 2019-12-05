from enum import Enum

class Level(Enum):
    UNSET = 0
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50

# print(getattr(Level,"UNSET"))
# print(Level.DEBUG.value)
# level = 100
# print(level if isinstance(level,Level) else Level[level] if isinstance(level,str) else Level(level) if isinstance(level,int) else Level.DEBUG)


def getlogger(name):
    if str(name)==name:
        class Format:
            def __init__(self):
                pass
        class Loger:
            def __init__(self,name = "root",level = Level.DEBUG,formater = None):
                self.name = name if str(name) == name else "root"
                try:
                    # nonlocal level
                    self.level = level if isinstance(level,Level) else Level[level] if isinstance(level,str) else Level(level) if isinstance(level,int) else Level.DEBUG
                except ValueError:
                    self.level = Level.DEBUG

    else:
        raise TypeError
    return Loger(name)

loger = getlogger("name")
print(loger.level)