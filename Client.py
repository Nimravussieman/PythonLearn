import socket,json,threading,errno,time


HOST = "localhost"
PORT = 10000
#Server
#s=socket.gethostname()
class Client:
    def __init__(self,name):
        self.name = name
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(2)
        # self.socket.settimeout(0)
        self.trhread = threading.Thread(target=self.recv)
        self.loop = True
        self.connect = False
        self.data=None
        self.gotdata=False
    def __del__(self):
        self.close()
    def close(self):
        try:            self.socket.close()
        except:            pass
    def conn(self,host, port):
        try:
            self.socket.connect((host, port))
            self._setconn(True)
            return True
        except Exception as ex:
            return False
    def sendall(self,message):
        try:
            j = json.dumps({self.name: message}).encode('utf-8')
            self.socket.sendall(j)
            return True
        except:
            return False
    def _setconn(self,state):
        self.connect = state
    def run(self):
        if self.connect:
            try:
                self.loop = True
                self.trhread.start()
                return True
            except Exception as ex:
                print(ex)
                return False
        return False
    def stop(self):
        self.loop = False
    def recv(self):
        while self.loop:
            # data = set()
            data = bytearray()
            while True:
                try:
                    data+=self.socket.recv(1024)
                except socket.timeout as e:
                    err = e.args[0]
                    if err == 'timed out':
                        if data:
                            break
                        else:
                            time.sleep(1)
                            self.gotdata = False
                            continue
                    # else:
                    #     self._setconn(False)
                    #     self.gotdata = self.data = False
                    #     return False
                # except socket.error as e:
                #     err = e.args[0]
                #     if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
                #         if data:
                #             break
                #         else:
                #             time.sleep(5)
                #             self.gotdata=False
                #             continue
                #     else:
                #         self._setconn(False)
                #         self.gotdata=self.data = False
                #         return False

                # except Exception as ex:
                #     self._setconn(False)
                #     self.data = False
                #     return False


            self.data = data
            self.gotdata = True
            print(self.data)
            time.sleep(5)




# def client(host,port,name='',message = ''):
#     if not name: name = input('your name: ')
#     if not message: message = input('your message: ')
#     j = json.dumps({name:message}).encode('utf-8')
#     #j='<EOF>'.encode('utf-8')
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.connect((host, port))
#         s.sendall(j)
#         data = s.recv(1024)
#     print('Received', repr(data.decode()))
#
#
# thread_list = []
# for x in range(1,100):
#     t = threading.Thread(target=client,args=(HOST,PORT,f"client {x}",f'message {x}'))
#     thread_list.append(t)
#     t.start()
# [t.join() for t in thread_list]

clientList = []
for x in range(1,10):
    c = Client(f'name {x}')
    if not c.conn(HOST,PORT):
        continue
    if not c.run():
        continue
    clientList.append(c)

while True:

    for i,c in enumerate(clientList):
        c.sendall(f'message {i}')

        # time.sleep(10)
    time.sleep(10)

#     time.sleep(30)
#
#     for c in clientList:
#         print('print data: ',c.data)
#
#
# print('ok')
# for c in clientList:
#     c.close()
# for c in clientList:
#     clientList.pop()