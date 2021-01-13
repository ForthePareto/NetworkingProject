from socket import socket,AF_INET,SOCK_STREAM,SHUT_RDWR ,timeout
import sys

class TCPServer():

    def __init__(self,serverPort):
        self.serverSocket = None
        self.serverState = None
        self.connectionSocket = None
        self.clientAddr = None

        self.initServer(serverPort)
        self.initConnection()

        # self.chatFClient()
        # self.chatTClient('HELLLLOOOO')
        self.chatLoop()

        self.serverSocket.shutdown(SHUT_RDWR)
        self.serverSocket.close()
        sys.exit()


    def initServer(self,serverPort):
        # Create the server Welcoming socket
        self.serverSocket = socket(AF_INET,SOCK_STREAM)
        # Bind the Welcoming socket to {it's interfaces} and {serverPort}
        self.serverSocket.bind(('192.168.1.3',serverPort))
        print(f'---- Created serverSocket ----')
        # server Welcoming socket is waiting for clients to connect to it ... 
        self.serverSocket.listen(1)
        print(f'serverSocket Listening...')

        self.serverState = True
    

    def initConnection(self):

        # while self.serverState:
        self.connectionSocket , self.clientAddr = self.serverSocket.accept()
        # if idle: times out after 10 secs 
        self.connectionSocket.settimeout(10)
        print(f'-- Created new connectionSocket --')
        print(f'conncted with: {self.clientAddr}')
            


    def chatFClient(self):

        recievedMsg = self.connectionSocket.recv(1024).decode()
        
        print(f'{self.clientAddr} says: {recievedMsg}')

        return recievedMsg


    def chatTClient(self,messageTosend:str):   
        self.connectionSocket.send(messageTosend.encode())
                
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

if __name__ == "__main__":
    server = TCPServer(22222)




