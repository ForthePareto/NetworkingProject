import socket
from socket import socket, AF_INET, SOCK_STREAM, SHUT_RDWR, timeout, SOCK_DGRAM


import sys
import selectors
import types

LOCAL_IP = '8.8.8.8'


class TCPServer():

    def __init__(self, serverPort):
        self.serverSocket = None
        self.serverState = None
        self.connectionSocket = None
        self.clientAddr = None
        self.ip = " "

        self.initServer(serverPort)
        self.initConnection()

        # self.chatFClient()
        # self.chatTClient('HELLLLOOOO')
        self.chatLoop()

        self.serverSocket.shutdown(SHUT_RDWR)
        self.serverSocket.close()
        sys.exit()

    def initServer(self, serverPort):
        localIP = get_local_IP()
        # Create the server Welcoming socket
        self.serverSocket = socket(AF_INET, SOCK_STREAM)
        # Bind the Welcoming socket to {it's interfaces} and {serverPort}
        try:
            self.serverSocket.bind((localIP, serverPort))
        except socket.error:
            print("Failed to bind")
            sys.exit()
        print(f'---- Created serverSocket ----')
        # server Welcoming socket is waiting for clients to connect to it ...
        self.serverSocket.listen(1)
        print(f'serverSocket Listening...')

        self.serverState = True

    def initConnection(self):

        # while self.serverState:
        self.connectionSocket, self.clientAddr = self.serverSocket.accept()
        # if idle: times out after 10 secs
        self.connectionSocket.settimeout(10)
        print(f'-- Created new connectionSocket --')
        print(f'conncted with: {self.clientAddr}')

    def chatFClient(self):

        recievedMsg = self.connectionSocket.recv(1024).decode()

        print(f'{self.clientAddr} says: {recievedMsg}')

        return recievedMsg

    def chatTClient(self, messageTosend: str):
        self.connectionSocket.sendall(messageTosend.encode())

        # print(f'Sent: {messageTosend}')

    def chatLoop(self):
        inputMsg = ' '
        rcvdMsg = ' '
        while rcvdMsg.upper().strip() != 'BYE':
            inputMsg = str(input())
            if (inputMsg.upper().strip() == 'BYE'):
                self.chatTClient(inputMsg)
                break
            self.chatTClient(inputMsg)
            try:
                rcvdMsg = self.chatFClient()
            except timeout:
                print('TIMEOUT')
                self.chatTClient('BYE')
                break

        self.connectionSocket.shutdown(SHUT_RDWR)
        self.connectionSocket.close()
        print(f'-- End connection from Server side--')


class MultiConnectionServer:

    def __init__(self, host, port):
        # initiate a default selector to handle multiple connections
        self.host = host
        self.port = port
        self.sel = selectors.DefaultSelector()
        self.chatLoop()

    def accept_wrapper(self, sock):
        conn, addr = sock.accept()  # Should be ready to read
        print("accepted connection from", addr)
        conn.setblocking(False)
        data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        self.sel.register(conn, events, data=data)

    def service_connection(self, key, mask):
        sock = key.fileobj
        data = key.data
        if mask & selectors.EVENT_READ:
            recv_data = sock.recv(1024)  # Should be ready to read
            if recv_data:
                data.outb += recv_data
            else:
                print("closing connection to", data.addr)
                self.sel.unregister(sock)
                sock.close()
        if mask & selectors.EVENT_WRITE:
            if data.outb:
                print("echoing", repr(data.outb), "to", data.addr)
                sent = sock.send(data.outb)  # Should be ready to write
                data.outb = data.outb[sent:]

    def chatLoop(self, host=None, port=None):
        if host == None:
            host = self.host
        if port == None:
            port = self.port

        lsock = socket(AF_INET, SOCK_STREAM)
        lsock.bind((host, port))
        lsock.listen()
        print("listening on", (host, port))
        lsock.setblocking(False)
        self.sel.register(lsock, selectors.EVENT_READ, data=None)

        try:
            while True:
                events = self.sel.select(timeout=None)
                for key, mask in events:
                    if key.data is None:
                        self.accept_wrapper(key.fileobj)
                    else:
                        self.service_connection(key, mask)
        except KeyboardInterrupt:
            print("caught keyboard interrupt, exiting")
        finally:
            self.sel.close()


# ----------------------------- helper functions ----------------------------- #

def get_local_IP() -> str:
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    local_ip = s.getsockname()[0]
    s.close()
    return local_ip
# ---------------------------------------------------------------------------- #


if __name__ == "__main__":

    # ------------------------- single connection server ------------------------- #

    # server = TCPServer(22222)
    # ---------------------------------------------------------------------------- #

    # ------------------------ multiple connection server ------------------------ #
    host, port = (get_local_IP(), 22222)
    MultiServer = MultiConnectionServer(host, port)
# ---------------------------------------------------------------------------- #
