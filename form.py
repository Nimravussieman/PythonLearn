from logging import Formatter

class MyFormat(Formatter):
    def __init__(self):
        super(MyFormat, self).__init__()
    def format(self, record):
        # record.message = record.getMessage()
        # if record.message[-1:] != '\n':
        #     pass
        # return Formatter.format(self, record)+"!!!"
        # return record.message + "!!!"
        return f"{record.__dict__['levelname']}:{record.__dict__['name']}:{record.message}!!!"
