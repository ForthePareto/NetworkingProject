from socket import socket, AF_INET, SOCK_STREAM, SHUT_RDWR, SOCK_DGRAM
from TCPServer import get_local_IP
import sys
import hashlib


class TCPClient():
    def __init__(self, serverIp, serverPort):
        # create a tcp socket
        self.clientSocket = None
        print(f'--- Created socket ---')
        self.dataToSend = " "
        self.dataReceived = " "
        self.initConnection(serverIp, serverPort)
        # self.chatTServer(messageToSend)
        # self.chatFServer()
        # self.chatLoop()

    def initConnection(self, serverIp, serverPort):
        self.clientSocket = socket(AF_INET, SOCK_STREAM)
        # initiate three-way tcp handshake with the server
        self.clientSocket.connect((serverIp, serverPort))
        print(f'Connected to server: {(serverIp,serverPort)}')

    def chatTServer(self, messageToSend: str):

        self.clientSocket.sendall(messageToSend.encode())
        # print(f'Sent: {messageToSend}\n')

    def chatFServer(self):

        message = self.clientSocket.recv(1024).decode()
        print(f'server says: {message}\n')

        return message

    def chatLoop(self):
        inputMsg = ' '
        rcvdMsg = ' '
        stillOn = True

        # rcvdMsg = self.chatFServer()  # greetings from server and request credentials
        while stillOn:
            # if rcvdMsg.upper().strip() == 'BYE':
            #     break
            inputMsg = str(input('username,password: '))
            # TODO : hash the password then send it
            if (inputMsg.upper().strip() == 'EXIT'):
                # send bye msg to notify the server to close it's side of the connection
                self.chatTServer(inputMsg)
                stillOn = False
                break
            username, password = inputMsg.strip().split(',')
            self.username = username
            hashedPassword = hashlib.sha256()
            hashedPassword.update(password.encode())
            # send credentials
            self.chatTServer(f'{username},{hashedPassword.hexdigest()}')

            statFlag, oldBmi = self.chatFServer().strip().split(
                ':')  # check credentials from server
            if (statFlag.lower().strip() == 'success') or (statFlag.lower().strip() == 'new'):
                # self.chatFServer() # requesting weight and height
                self.chatTServer(str(input("Weight,Height: ")))  # send them
                self.dataReceived = self.chatFServer()  # get back the BMI
                stillOn = False
            else:
                #TODO: repeat
                # ::DONE::
                print('TRY AGAIN...\n')

        self.clientSocket.shutdown(SHUT_RDWR)
        self.clientSocket.close()
        print(f'-- End connection from client Side --')

    def check_authority(self, name_pass_pair):
        rcvdMsg = ' '
            
        username, password = name_pass_pair.strip().split(',')
        self.username= username 
        hashedPassword = hashlib.sha256()
        hashedPassword.update(password.encode())
        # send credentials
        self.chatTServer(f'user_password,{username},{hashedPassword.hexdigest()}')

        _, statFlag = self.chatFServer().strip().split(',')  # check credentials from server
        
        return statFlag.lower().strip()

    def get_bmi(self, weight_height):
        self.chatTServer("body_info,"+weight_height+","+self.username)  # send them
        return self.chatFServer()  # get back the BMI

    def CommunicationLoop(self, name_pass_pair):
        inputMsg = ' '
        rcvdMsg = ' '
        stillOn = True

        rcvdMsg = self.chatFServer()  # greetings from server and request credentials
        while stillOn:
            # if rcvdMsg.upper().strip() == 'BYE':
            #     break
            inputMsg = name_pass_pair
            print(inputMsg)
            # TODO : hash the password then send it
            if (inputMsg.upper().strip() == 'EXIT'):
                # send bye msg to notify the server to close it's side of the connection
                self.chatTServer(inputMsg)
                stillOn = False
                break
            username, password = inputMsg.strip().split(',')[:2]
            hashedPassword = hashlib.sha256()
            hashedPassword.update(password.encode())
            # send credentials
            self.chatTServer(f'{username},{hashedPassword.hexdigest()}')

            statFlag, oldBmi = self.chatFServer().strip().split(
                ':')  # check credentials from server
            if (statFlag.lower().strip() == 'success') or (statFlag.lower().strip() == 'new'):
                # self.chatFServer() # requesting weight and height

                weight_height_lst = inputMsg.strip().split(',')[2:]
                weight_height = weight_height_lst[0] + \
                    "," + weight_height_lst[1]
                self.chatTServer(weight_height)  # send them
                self.dataReceived = self.chatFServer()  # get back the BMI
                stillOn = False
            else:
                #TODO: repeat
                # ::DONE::
                print('TRY AGAIN...\n')

    def close_connection(self):
        self.clientSocket.shutdown(SHUT_RDWR)
        self.clientSocket.close()
        print(f'-- End connection from client Side --')
        # sys.exit()


if __name__ == "__main__":

    # assuming server is on same machine of client ,this function gets the default local  IPv4 Address for any machine.
    serverIp = get_local_IP()
    serverPort = 22222

    client = TCPClient(serverIp, serverPort)
    # client.CommunicationLoop("esl,8388")
