import threading,time,multiprocessing,urllib.request

def foo(*text):
    s = 0
    old = time.time()
    for n in range(1,1001):
        s+=n
    time.sleep(1)
    print(f"sum = {s}",f'{text[0]} time + 1sec. = {time.time()-old}')

def foo2(path,filename,text=''):
    try:
        old = time.time()
        with urllib.request.urlopen(path) as pathopen:
            with open(filename, 'ab') as fileopen:
                while pathopen:
                    data = pathopen.read(1024)
                    fileopen.write(data)
                    if not data:
                        break
        print(text,f': time = {time.time()-old}')
    except:
        pass
if __name__ == '__main__':

    workers = []
    for index in range(1,6):
        proc = multiprocessing.Process(target=foo,args=(f'process {index}',))
        workers.append(proc)
        proc.start()
    for index in range(1,6):
        thread = threading.Thread(target=foo,args=(f'thread {index}',))
        workers.append(thread)
        thread.start()

    proc = multiprocessing.Process(target=foo2, kwargs={
    'path':'https://www.guru99.com/reading-and-writing-files-in-python.html', 'filename':'Process_1_file.txt', 'text':'process1'})
    thread = threading.Thread(target=foo2, kwargs={
    'path':'https://www.guru99.com/reading-and-writing-files-in-python.html', 'filename':'Thread_1_file.txt', 'text':'thread1'})
    proc.start()
    thread.start()
    workers.append(proc)
    workers.append(thread)

    proc = multiprocessing.Process(target=foo2, kwargs={
    'path':'https://docs.python.org/3.7/library/urllib.request.html#module-urllib.request', 'filename':'Process_2_file.txt', 'text':'process2'})
    thread = threading.Thread(target=foo2, kwargs={
    'path':'https://docs.python.org/3.7/library/urllib.request.html#module-urllib.request', 'filename':'Thread_2_file.txt', 'text':'thread2'})
    proc.start()
    thread.start()
    workers.append(proc)
    workers.append(thread)

    proc = multiprocessing.Process(target=foo2, kwargs={
    'path':'https://requests.readthedocs.io/en/master/', 'filename':'Process_3_file.txt', 'text':'process3'})
    thread = threading.Thread(target=foo2, kwargs={
    'path':'https://requests.readthedocs.io/en/master/', 'filename':'Thread_3_file.txt', 'text':'thread3'})
    proc.start()
    thread.start()
    workers.append(proc)
    workers.append(thread)



    for each in workers:
        each.join()

