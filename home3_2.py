import os,logging
from form import MyFormat

# log = logging.getLogger("l")
# handler = logging.FileHandler("home3_2.log")
# handler.setLevel(logging.DEBUG)
# handler.setFormatter(MyFormat())
# log.addHandler(handler)
# log.info('kuku')
# log.warning("kotostrofa")

logging.basicConfig()#.basicConfig()#filename="home3_2.log",filemode='w',level=logging.INFO
handler = logging.FileHandler("home3_2.log")

# handler.setLevel(logging.DEBUG)
# handler.level = logging.DEBUG
logging.root.setLevel(logging.DEBUG)
handler.setFormatter(MyFormat())
# handler.formatter = MyFormat()
logging.root.addHandler(handler)
# logging.getLogger('').addHandler(handler)
def main(arg):
    try:
        import platform
        num = int("".join(platform.python_version_tuple()))
        cpu_num(num)
        version = num < 370
        if len(arg)>2:
            path = os.path(arg[1],arg[2])
            logging.info('if len(arg)>2')
            if version:
                os.mkdir(path)
                logging.debug('os.mkdir(path)')
            else:
                os.remove(path)
                logging.debug('os.remove(path)')
        else:
            logging.info('if len(arg)>2:else')
            if version:
                os.mkdir(arg[1])
                logging.debug('os.mkdir(arg[1])')
            else:
                os.remove(arg[1])
                logging.debug('os.remove(arg[1])')
    except Exception as ex:
        logging.exception(f"{ex}")


def cpu_num(num):
    if num < 340:
        import multiprocessing
        count = multiprocessing.cpu_count()
    else:
        count = os.cpu_count()
    if count < 4:
        raise SystemExit()






if __name__ == '__main__':
    import sys
    try:
        main(sys.argv)
    except:
        pass

