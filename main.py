# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 460)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.first_num = QtWidgets.QLineEdit(self.centralWidget)
        self.first_num.setGeometry(QtCore.QRect(450, 75, 220, 20))
        self.first_num.setObjectName("first_num")
        self.answer = QtWidgets.QLineEdit(self.centralWidget)
        self.answer.setGeometry(QtCore.QRect(340, 340, 331, 90))
        self.answer.setObjectName("answer")
        self.second_num = QtWidgets.QLineEdit(self.centralWidget)
        self.second_num.setGeometry(QtCore.QRect(450, 205, 220, 20))
        self.second_num.setObjectName("second_num")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(270, 70, 170, 30))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(270, 200, 170, 30))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(270, 330, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 180, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.PLUS = QtWidgets.QPushButton(self.centralWidget)
        self.PLUS.setGeometry(QtCore.QRect(10, 70, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.PLUS.setFont(font)
        self.PLUS.setObjectName("PLUS")
        self.MINUS = QtWidgets.QPushButton(self.centralWidget)
        self.MINUS.setGeometry(QtCore.QRect(140, 70, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.MINUS.setFont(font)
        self.MINUS.setObjectName("MINUS")
        self.MULT = QtWidgets.QPushButton(self.centralWidget)
        self.MULT.setGeometry(QtCore.QRect(10, 200, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.MULT.setFont(font)
        self.MULT.setObjectName("MULT")
        self.DIV = QtWidgets.QPushButton(self.centralWidget)
        self.DIV.setGeometry(QtCore.QRect(140, 200, 100, 100))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.DIV.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.DIV.setFont(font)
        self.DIV.setObjectName("DIV")
        self.INT_DIV = QtWidgets.QPushButton(self.centralWidget)
        self.INT_DIV.setGeometry(QtCore.QRect(10, 330, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.INT_DIV.setFont(font)
        self.INT_DIV.setObjectName("INT_DIV")
        self.MOD = QtWidgets.QPushButton(self.centralWidget)
        self.MOD.setGeometry(QtCore.QRect(140, 330, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.MOD.setFont(font)
        self.MOD.setObjectName("MOD")
        #MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Введите первое число:"))
        self.label_2.setText(_translate("MainWindow", "Введите второе число:"))
        self.label_3.setText(_translate("MainWindow", "Ответ:"))
        self.label_4.setText(_translate("MainWindow", "Выберите действие"))
        self.PLUS.setText(_translate("MainWindow", "+"))
        self.MINUS.setText(_translate("MainWindow", "-"))
        self.MULT.setText(_translate("MainWindow", "*"))
        self.DIV.setText(_translate("MainWindow", "/"))
        self.INT_DIV.setText(_translate("MainWindow", "//"))
        self.MOD.setText(_translate("MainWindow", "%"))
