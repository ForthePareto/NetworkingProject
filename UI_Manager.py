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
        serverIp = get_local_IP()
        serverPort = 22222
        self.client = TCPClient(serverIp, serverPort)
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
        state_label ={"new":"New User","success":"Successful Login","fail":"Wrong Password"}
        state = self.client.check_authority( f'{user},{password}')
        self.login_window.password_state_label.setText(state_label[state])
        accepatble_states = ["success","new"]
        if state in accepatble_states:
            self.clear_fields()
            self.MainWindow.show()
        else:
            print(state)
              
        #now the user filled the entries an clicked on calculate
        print(user,password)
    def clear_fields(self):
        self.main_window.weight_field.setText("")
        self.main_window.height_field.setText("")
        self.main_window.bmi_lcd.display(float(000))
        self.main_window.healthState_label.setText("")
    def get_user_entries(self):
        self.weight= str(self.main_window.weight_field.text())
        self.height= str(self.main_window.height_field.text())
        self.dataToSend = self.weight +"," + self.height
        self.received_data =  self.client.get_bmi(self.dataToSend)
        bmi = self.received_data.split(",")[1]
        self.main_window.bmi_lcd.display(float(bmi))
        self.main_window.healthState_label.setText(self.received_data.split(",")[2])
    def __del__(self):
        print("Close Client GUI Window")
        self.client.close_connection()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = UiManager()
    MainWindow.show()
    sys.exit(app.exec_())

