import socket,sys,errno,timeit,threading,time

HOST = "localhost"
PORT = 10000

class ServerClient:
    def __init__(self,conn,addr,dell_method,send_method):
        self.conn = conn
        self.conn.settimeout(2)
        self.addr = addr
        self.dell_method = dell_method
        self.send_method = send_method
        self.thread_receive = threading.Thread(target=self.receive)
        self.thread_receive.start()
    def __del__(self):
        self.close()
    def close(self):
        try:
            self.conn.close()
        except: pass
    def send(self,data):
        try:
            self.trhrear_send = threading.Thread(target=self._send,kwargs={'data':data})
            self.trhrear_send.start()
        except:
            pass
    def _send(self,data):
        try:
            self.conn.sendall(data)
        except socket.error as exc:
            self.dell_method(self)
    def receive(self):
        while True:
            data = bytearray()
            while True:
                try:
                    data += bytearray(self.conn.recv(1024))
                except socket.timeout as e:
                    err = e.args[0]
                    if err == 'timed out':
                        if data:
                            if data == b'<EOF>':
                                self.dell_method(self)
                                return
                            self.send_method(self,data)
                            break
                        else:
                            time.sleep(1)
                            continue


class Server:
    def __init__(self):
        self.client_list = set()
        self.clien_out = []
        self.exit = True

    def client_out_append(self,client):
        self.clien_out.append(client)
    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen(10)
            while self.exit:
                conn, addr = s.accept()
                #self.client_list.add(conn)
                self.client_list.add(ServerClient(conn,addr,self.client_out_append,self.sendall))

    def sendall(self,client_owner,data):
        for client in self.client_list:
            try:
                if client.__hash__() != client_owner.__hash__():
                    client.send(data)
            except: pass
        for bad_client in self.clien_out:
            bad_client.pop()

if __name__ == "__main__":
    Server().run()