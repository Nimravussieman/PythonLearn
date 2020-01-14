import socket,sys,errno,timeit,threading

HOST = "localhost"
PORT = 10000



def server():
    client_list = set()
    exit = True
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(10)
        while exit:
            conn, addr = s.accept()
            client_list.add(conn)
            conn.settimeout(False)
            # with conn:
            print('Connected by', addr)
            data = bytearray()
            while True:
                try:
                    data+=bytearray(conn.recv(1024))
                except socket.error as e:
                    err = e.args[0]
                    if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
                        if data == b'<EOF>':    sys.exit(0)
                        newset = []

                        for c in client_list:
                            try:
                                c.sendall(data)
                            except Exception as ex:
                                newset.append(c)
                                print(ex)
                                #client_list.remove(c)
                                # if len(client_list) == 0:   exit=False
                                # print(ex)
                        for x in newset:
                            print(newset.pop())

                        print(len(client_list))
                        break
        else:
            for conn in client_list:
                try:
                    conn.close()
                except:
                    pass
if __name__ == "__main__":
    server()