from MainWindowUI import Ui_MainWindow
from  login_ui import LoginWindow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from TCPClient import TCPClient
from TCPServer import get_local_IP
# from QtCore import QProcess ,QTimer

class  UiManager(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiManager, self).__init__()
        self.login_window = LoginWindow()
        self.MainWindow = QtWidgets.QMainWindow()
        self.main_window = Ui_MainWindow()
        self.main_window.setupUi(self.MainWindow)
        self.login_window.setupUi(self)
        self.main_window.calculate_button.clicked.connect(lambda : self.get_user_entries())

        self.is_info_sent = False
        self.login_window.login_Button.clicked.connect(lambda : self.validate_login())
        
    def validate_login(self):
        user = self.login_window.login_userName_field.text()
        password = self.login_window.login_password_field.text()
        self.dataToSendList = [user,password]
        self.dataToSend = f"{self.dataToSendList[0]} , {self.dataToSendList[1]}"

        self.MainWindow.show()      
        #now the user filled the entries an clicked on calculate
        print(user,password)

    def get_user_entries(self):
        self.weight= str(self.main_window.weight_field.text())
        self.height= str(self.main_window.height_field.text())
        self.dataToSend += ", "+ self.weight +", " + self.height
        serverIp = get_local_IP()
        serverPort = 22222
        client = TCPClient(serverIp, serverPort)
        client.CommunicationLoop(self.dataToSend)
        self.received_data = client.dataReceived
        bmi = self.received_data.split(",")[0]
        self.main_window.bmi_lcd.display(float(bmi))
        self.main_window.healthState_label.setText(self.received_data.split(",")[1])
    def start_tracking(self):
        if self.is_info_sent ==True :
            self.timer.stop()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = UiManager()
    MainWindow.show()
    sys.exit(app.exec_())

