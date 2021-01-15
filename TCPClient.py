from socket import socket, AF_INET, SOCK_STREAM, SHUT_RDWR, SOCK_DGRAM
from TCPServer import get_local_IP
import sys


class TCPClient():
    def __init__(self, serverIp, serverPort):
        # create a tcp socket
        self.clientSocket = None
        print(f'--- Created socket ---')

        self.initConnection(serverIp, serverPort)
        # self.chatTServer(messageToSend)
        # self.chatFServer()
        self.chatLoop()
        sys.exit()

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
        print(f'server says: {message}')

        return message

    def chatLoop(self):
        inputMsg = ' '
        rcvdMsg = ' '
        while True:
            # rcvdMsg = self.chatFServer()
            inputMsg = input("message to send:  ")
            self.chatTServer(inputMsg)
            # if rcvdMsg.upper().strip() == 'BYE':
            #     break
            # inputMsg = str(input())
            # if (inputMsg.upper().strip() == 'BYE'):
            #     self.chatTServer(inputMsg)
            #     break
            self.chatTServer(inputMsg)
            rcvdMsg = self.chatFServer()
        self.clientSocket.shutdown(SHUT_RDWR)
        self.clientSocket.close()
        print(f'-- End connection from client Side --')


if __name__ == "__main__":

    # assuming server is on same machine of client ,this function gets the default local  IPv4 Address for any machine.
    serverIp = get_local_IP()
    serverPort = 22222

    client = TCPClient(serverIp, serverPort)
