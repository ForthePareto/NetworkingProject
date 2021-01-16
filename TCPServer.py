from socket import socket, AF_INET, SOCK_STREAM, SHUT_RDWR, timeout, SOCK_DGRAM ,error,gethostname,gethostbyname
import sys



class TCPServer():

    def __init__(self, serverPort):
        self.serverSocket = None
        self.serverState = None
        self.connectionSocket = None
        self.clientAddr = None

        self.initServer(serverPort)
        self.initConnection()

        self.chatLoop()

        self.serverSocket.shutdown(SHUT_RDWR)
        self.serverSocket.close()
        sys.exit()

    def initServer(self, serverPort):
        localIP = get_local_IP()
        # Create the server Welcoming socket
        self.serverSocket = socket(AF_INET, SOCK_STREAM)
        # Bind the Welcoming socket to {it's interface} and {serverPort}
        try:
            self.serverSocket.bind((localIP, serverPort))
        except error:
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
        # if idle: times out after 30 secs
        self.connectionSocket.settimeout(30)
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
            inputMsg = str(input('Send: '))
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

# ----------------------------- helper functions ----------------------------- #

def get_local_IP() -> str:
    hostName = gethostname()
    local_ip = gethostbyname(hostName)
    return local_ip
# ---------------------------------------------------------------------------- #


if __name__ == "__main__":

    # ------------------------- single connection server ------------------------- #
    server = TCPServer(22226)
    # ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
