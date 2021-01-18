# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainGUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(474, 703)
        MainWindow.setMinimumSize(QtCore.QSize(474, 703))
        MainWindow.setMaximumSize(QtCore.QSize(474, 703))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-7, -7, 481, 701))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("resources/background.png"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 240, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Aachen")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(
            "color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 310, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Aachen")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(
            "color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_4.setObjectName("label_4")
        self.height_field = QtWidgets.QLineEdit(self.centralwidget)
        self.height_field.setGeometry(QtCore.QRect(220, 330, 101, 31))
        font = QtGui.QFont()
        font.setFamily("PT Bold Heading")
        font.setPointSize(12)
        self.height_field.setFont(font)
        self.height_field.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.height_field.setObjectName("height_field")
        self.weight_field = QtWidgets.QLineEdit(self.centralwidget)
        self.weight_field.setGeometry(QtCore.QRect(220, 260, 101, 31))
        font = QtGui.QFont()
        font.setFamily("PT Bold Heading")
        font.setPointSize(12)
        self.weight_field.setFont(font)
        self.weight_field.setObjectName("weight_field")
        self.main_logo_pic = QtWidgets.QLabel(self.centralwidget)
        self.main_logo_pic.setGeometry(QtCore.QRect(80, -10, 331, 281))
        self.main_logo_pic.setText("")
        self.main_logo_pic.setPixmap(QtGui.QPixmap("resources/loginLogo.png"))
        self.main_logo_pic.setScaledContents(True)
        self.main_logo_pic.setObjectName("main_logo_pic")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 460, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Aachen")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(
            "color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_5.setObjectName("label_5")
        self.calculate_button = QtWidgets.QPushButton(self.centralwidget)
        self.calculate_button.setGeometry(QtCore.QRect(120, 390, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.calculate_button.setFont(font)
        self.calculate_button.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculate_button.setStyleSheet(
            "    background:linear-gradient(to bottom, #59635c 5%, #5cbf2a 100%);\n"
            "    background-color:#ADD8E6;\n"
            "    border-radius:15px;\n"
            "    border:1px solid #18ab29;\n"
            "    color:purple;\n"
            "    padding:10px 36px;\n"
            "    text-decoration:none;\n"
        )
        self.calculate_button.setObjectName("calculate_button")
        self.bmi_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.bmi_lcd.setGeometry(QtCore.QRect(260, 470, 121, 41))
        self.bmi_lcd.setStyleSheet("color: rgb(53, 236, 230);\n"
                                   "color: rgb(95, 83, 247);")
        self.bmi_lcd.setSmallDecimalPoint(False)
        self.bmi_lcd.setDigitCount(5)
        self.bmi_lcd.setMode(QtWidgets.QLCDNumber.Dec)
        self.bmi_lcd.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.bmi_lcd.setProperty("value", 0.0)
        self.bmi_lcd.setProperty("intValue", 0)
        self.bmi_lcd.setObjectName("bmi_lcd")
        self.healthState_label = QtWidgets.QLabel(self.centralwidget)
        self.healthState_label.setGeometry(QtCore.QRect(90, 530, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Nova")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.healthState_label.setFont(font)
        self.healthState_label.setAutoFillBackground(False)
        self.healthState_label.setStyleSheet("color: rgb(95, 83, 247);\n"
                                             "")
        self.healthState_label.setTextFormat(QtCore.Qt.AutoText)
        self.healthState_label.setAlignment(QtCore.Qt.AlignCenter)
        self.healthState_label.setWordWrap(False)
        self.healthState_label.setObjectName("healthState_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Your Personal BMI assist."))
        MainWindow.setWindowIcon(QtGui.QIcon("resources/yoga-logo.png"))
        self.label_2.setText(_translate("MainWindow", "Your Weight"))
        self.label_4.setText(_translate("MainWindow", "Your Height"))
        self.height_field.setPlaceholderText(_translate("MainWindow", "cm"))
        self.weight_field.setPlaceholderText(_translate("MainWindow", "k.g"))
        self.label_5.setText(_translate("MainWindow", "Your Body Mass Index:"))
        self.calculate_button.setText(
            _translate("MainWindow", "Calculate BMI"))
        self.healthState_label.setText(_translate("MainWindow", " "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
