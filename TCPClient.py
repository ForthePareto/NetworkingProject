import socket


class TCPClient():
    def __init__(self,frameToSend,serverIp,serverPort):
        self.direction = None
        # create a tcp socket
        self.clientSocket = None
        print(f'--- Created socket ---')

        self.initConnection(serverIp,serverPort)
        self.sendFrame(frameToSend)
        self.recivedDirection()


    def initConnection(self,serverIp,serverPort):
        self.clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # initiate three-way tcp handshake with the server 
        self.clientSocket.connect((serverIp,serverPort))
        print(f'Connected to server: {(serverIp,serverPort)}')


    def sendFrame(self,FrameToSend):
                
        frame = open(FrameToSend,'rb')  
        while True:
            partialData = frame.read(512)
            if not partialData:
                break
            self.clientSocket.send(partialData)
            print(f'Sent: {partialData}\n\n')
        print('Sent Complete Frame')
        self.clientSocket.close()
        
        # self.clientSocket.send('SentAll'.encode())

        frame.close()
            

        # recivedMessage = self.clientSocket.recv(1024).decode()

        # print(f'Recived: {recivedMessage}')


    def recivedDirection(self):
        print('waiting for direction...\n')
        self.initConnection(serverIp,serverPort)

        self.direction = self.clientSocket.recv(1024).decode()
        print(f'turn: {self.direction}')
        self.clientSocket.close()
        print('--- BYE ---')


# serverIp = '192.168.1.3' # home lan ip
serverIp = '172.28.132.215' # sbme lan ip
serverPort = 1208

client = TCPClient('lane3.jpg',serverIp,serverPort)