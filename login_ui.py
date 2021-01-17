# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login_Window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class LoginWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(498, 672)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -60, 651, 781))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("resources/background.png"))
        self.label.setObjectName("label")
        self.login_Button = QtWidgets.QPushButton(Dialog)
        self.login_Button.setGeometry(QtCore.QRect(154, 440, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.login_Button.setFont(font)
        self.login_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_Button.setStyleSheet("box-shadow: 3px 5px 0px 0px #3dc21b;\n"
"    background:linear-gradient(to bottom, #59635c 5%, #5cbf2a 100%);\n"
"    background-color:#ADD8E6;\n"
"    border-radius:15px;\n"
"    border:1px solid #18ab29;\n"
"    display:inline-block;\n"
"    cursor:pointer;\n"
"    color:purple;\n"
"    \n"
"    padding:10px 36px;\n"
"    text-decoration:none;\n"
"    text-shadow:0px 4px 0px #2f6627;")
        self.login_Button.setObjectName("login_Button")
        self.login_userName_field = QtWidgets.QLineEdit(Dialog)
        self.login_userName_field.setGeometry(QtCore.QRect(222, 309, 211, 31))
        font = QtGui.QFont()
        font.setFamily("PT Bold Heading")
        font.setPointSize(12)
        self.login_userName_field.setFont(font)
        self.login_userName_field.setObjectName("login_userName_field")
        self.login_password_field = QtWidgets.QLineEdit(Dialog)
        self.login_password_field.setGeometry(QtCore.QRect(220, 380, 211, 31))
        font = QtGui.QFont()
        font.setFamily("PT Bold Heading")
        font.setPointSize(12)
        self.login_password_field.setFont(font)
        self.login_password_field.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.login_password_field.setObjectName("login_password_field")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 360, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Aachen")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_3.setObjectName("label_3")
        self.login_logo_pic = QtWidgets.QLabel(Dialog)
        self.login_logo_pic.setGeometry(QtCore.QRect(30, 10, 441, 291))
        self.login_logo_pic.setText("")
        self.login_logo_pic.setPixmap(QtGui.QPixmap("resources/yoga-logo.png"))
        self.login_logo_pic.setScaledContents(True)
        self.login_logo_pic.setObjectName("login_logo_pic")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 290, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Aachen")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.login_Button.setText(_translate("Dialog", "Login"))
        self.label_3.setText(_translate("Dialog", "Password"))
        self.label_2.setText(_translate("Dialog", "User Name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = LoginWindow()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
