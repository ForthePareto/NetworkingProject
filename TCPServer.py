import socket
from laneDetector import LaneDetector 

class TCPServer():

    def __init__(self,serverPort,saveTo):
        self.serverSocket = None
        self.serverState = None
        self.connectionSocket = None
        self.clientAddr = None

        self.initServer(serverPort)

        self.initConnection()
        self.recieveFrame(saveTo)

        self.sendDirection('left')
        self.serverSocket.close()


    def initServer(self,serverPort):

        self.serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.serverSocket.bind(('',serverPort))
        print(f'---- Created serverSocket ----')
        self.serverSocket.listen(1)
        print(f'serverSocket Listening...')
        self.serverState = True
        # serverPort = 1200
    
    def initConnection(self):

        # while self.serverState:
        self.connectionSocket , self.clientAddr = self.serverSocket.accept()
        print(f'-- Created connectionSocket --')
        print(f'conncted with: {self.clientAddr}')
            


    def recieveFrame(self,saveTo):
        frameFile = open(saveTo,'wb')
        while True:

            # self.connectionSocket.settimeout()
            recievedPartialFrame = self.connectionSocket.recv(512)
            if not recievedPartialFrame:
                break
            frameFile.write(recievedPartialFrame)
            
            print(f'Recived: {recievedPartialFrame}\n\n')
            print('in loop')
        print('out of loop')
        frameFile.close()
        print(f'Recived complete Frame')


    # def sendDirection(self,direction):   
    #     self.initConnection()
    #     self.connectionSocket.send(direction.encode())
                
    #     print(f'Sent: {direction}')
    #     self.connectionSocket.close()
    #     print(f'-- End connection --')

    
    def processFrame(self):
        pass    

    
    
server = TCPServer(1208,'rcvdFrame.jpeg')

    # def closeServer(self):
        # pass
        # print(f'---- SERVER is CLOSED ----')


