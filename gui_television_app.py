# Form implementation generated from reading ui file 'gui_television_app.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(400, 600))
        MainWindow.setMaximumSize(QtCore.QSize(400, 600))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_1.setGeometry(QtCore.QRect(100, 330, 61, 41))
        self.button_1.setObjectName("button_1")
        self.group_buttons = QtWidgets.QButtonGroup(MainWindow)
        self.group_buttons.setObjectName("group_buttons")
        self.group_buttons.addButton(self.button_1)
        self.button_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_2.setGeometry(QtCore.QRect(170, 330, 61, 41))
        self.button_2.setObjectName("button_2")
        self.group_buttons.addButton(self.button_2)
        self.button_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_3.setGeometry(QtCore.QRect(240, 330, 61, 41))
        self.button_3.setObjectName("button_3")
        self.group_buttons.addButton(self.button_3)
        self.button_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_5.setGeometry(QtCore.QRect(170, 370, 61, 41))
        self.button_5.setObjectName("button_5")
        self.group_buttons.addButton(self.button_5)
        self.button_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_4.setGeometry(QtCore.QRect(100, 370, 61, 41))
        self.button_4.setObjectName("button_4")
        self.group_buttons.addButton(self.button_4)
        self.button_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_6.setGeometry(QtCore.QRect(240, 370, 61, 41))
        self.button_6.setObjectName("button_6")
        self.group_buttons.addButton(self.button_6)
        self.button_8 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_8.setGeometry(QtCore.QRect(170, 410, 61, 41))
        self.button_8.setObjectName("button_8")
        self.group_buttons.addButton(self.button_8)
        self.button_7 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_7.setGeometry(QtCore.QRect(100, 410, 61, 41))
        self.button_7.setObjectName("button_7")
        self.group_buttons.addButton(self.button_7)
        self.button_9 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_9.setGeometry(QtCore.QRect(240, 410, 61, 41))
        self.button_9.setObjectName("button_9")
        self.group_buttons.addButton(self.button_9)
        self.button_0 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_0.setGeometry(QtCore.QRect(170, 450, 61, 41))
        self.button_0.setObjectName("button_0")
        self.group_buttons.addButton(self.button_0)
        self.button_power = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_power.setGeometry(QtCore.QRect(232, 290, 71, 32))
        self.button_power.setObjectName("button_power")
        self.button_plus = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_plus.setGeometry(QtCore.QRect(100, 500, 61, 32))
        self.button_plus.setObjectName("button_plus")
        self.button_minus = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_minus.setGeometry(QtCore.QRect(100, 540, 61, 32))
        self.button_minus.setObjectName("button_minus")
        self.button_down = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_down.setGeometry(QtCore.QRect(240, 540, 61, 32))
        self.button_down.setObjectName("button_down")
        self.button_up = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_up.setGeometry(QtCore.QRect(240, 500, 61, 32))
        self.button_up.setObjectName("button_up")
        self.button_mute = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_mute.setGeometry(QtCore.QRect(100, 290, 71, 32))
        self.button_mute.setObjectName("button_mute")
        self.slider_volume = QtWidgets.QSlider(parent=self.centralwidget)
        self.slider_volume.setGeometry(QtCore.QRect(70, 250, 221, 21))
        self.slider_volume.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.slider_volume.setObjectName("slider_volume")
        self.label_channel = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_channel.setGeometry(QtCore.QRect(170, 220, 61, 16))
        self.label_channel.setObjectName("label_channel")
        self.label_volume = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_volume.setGeometry(QtCore.QRect(310, 250, 21, 16))
        self.label_volume.setObjectName("label_volume")
        self.label_screen = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_screen.setGeometry(QtCore.QRect(70, 40, 260, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_screen.sizePolicy().hasHeightForWidth())
        self.label_screen.setSizePolicy(sizePolicy)
        self.label_screen.setMinimumSize(QtCore.QSize(260, 150))
        self.label_screen.setMaximumSize(QtCore.QSize(260, 150))
        self.label_screen.setText("")
        self.label_screen.setPixmap(QtGui.QPixmap("black.jpg"))
        self.label_screen.setScaledContents(True)
        self.label_screen.setObjectName("label_screen")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Television App"))
        self.button_1.setText(_translate("MainWindow", "1"))
        self.button_2.setText(_translate("MainWindow", "2"))
        self.button_3.setText(_translate("MainWindow", "3"))
        self.button_5.setText(_translate("MainWindow", "5"))
        self.button_4.setText(_translate("MainWindow", "4"))
        self.button_6.setText(_translate("MainWindow", "6"))
        self.button_8.setText(_translate("MainWindow", "8"))
        self.button_7.setText(_translate("MainWindow", "7"))
        self.button_9.setText(_translate("MainWindow", "9"))
        self.button_0.setText(_translate("MainWindow", "0"))
        self.button_power.setText(_translate("MainWindow", "Power"))
        self.button_plus.setText(_translate("MainWindow", "+"))
        self.button_minus.setText(_translate("MainWindow", "-"))
        self.button_down.setText(_translate("MainWindow", "▼"))
        self.button_up.setText(_translate("MainWindow", "▲"))
        self.button_mute.setText(_translate("MainWindow", "Mute"))
        self.label_channel.setText(_translate("MainWindow", "Power Off"))
        self.label_volume.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
