# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/samet/PycharmProjects/pythonProject/skorTabelasiNew.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(273, 402)
        font = QtGui.QFont()
        font.setFamily("Poppins ExtraBold")
        font.setPointSize(14)
        Form.setFont(font)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(-10, -10, 291, 421))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.score_1 = QtWidgets.QLineEdit(self.groupBox)
        self.score_1.setGeometry(QtCore.QRect(240, 10, 40, 40))
        self.score_1.setMinimumSize(QtCore.QSize(40, 40))
        self.score_1.setMaximumSize(QtCore.QSize(40, 40))
        self.score_1.setBaseSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.score_1.setFont(font)
        self.score_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.score_1.setObjectName("score_1")
        self.equal_1 = QtWidgets.QLineEdit(self.groupBox)
        self.equal_1.setGeometry(QtCore.QRect(210, 10, 30, 40))
        self.equal_1.setMinimumSize(QtCore.QSize(30, 40))
        self.equal_1.setMaximumSize(QtCore.QSize(30, 40))
        self.equal_1.setBaseSize(QtCore.QSize(30, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.equal_1.setFont(font)
        self.equal_1.setAlignment(QtCore.Qt.AlignCenter)
        self.equal_1.setObjectName("equal_1")
        self.name_1 = QtWidgets.QLineEdit(self.groupBox)
        self.name_1.setGeometry(QtCore.QRect(10, 10, 200, 40))
        self.name_1.setMinimumSize(QtCore.QSize(200, 40))
        self.name_1.setMaximumSize(QtCore.QSize(200, 40))
        self.name_1.setBaseSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.name_1.setFont(font)
        self.name_1.setText("")
        self.name_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name_1.setObjectName("name_1")
        self.equal_2 = QtWidgets.QLineEdit(self.groupBox)
        self.equal_2.setGeometry(QtCore.QRect(210, 50, 30, 40))
        self.equal_2.setMinimumSize(QtCore.QSize(30, 40))
        self.equal_2.setMaximumSize(QtCore.QSize(30, 40))
        self.equal_2.setBaseSize(QtCore.QSize(30, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.equal_2.setFont(font)
        self.equal_2.setAlignment(QtCore.Qt.AlignCenter)
        self.equal_2.setObjectName("equal_2")
        self.name_2 = QtWidgets.QLineEdit(self.groupBox)
        self.name_2.setGeometry(QtCore.QRect(10, 50, 200, 40))
        self.name_2.setMinimumSize(QtCore.QSize(200, 40))
        self.name_2.setMaximumSize(QtCore.QSize(200, 40))
        self.name_2.setBaseSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.name_2.setFont(font)
        self.name_2.setText("")
        self.name_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name_2.setObjectName("name_2")
        self.score_2 = QtWidgets.QLineEdit(self.groupBox)
        self.score_2.setGeometry(QtCore.QRect(240, 50, 40, 40))
        self.score_2.setMinimumSize(QtCore.QSize(40, 40))
        self.score_2.setMaximumSize(QtCore.QSize(40, 40))
        self.score_2.setBaseSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.score_2.setFont(font)
        self.score_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.score_2.setObjectName("score_2")
        self.equal_3 = QtWidgets.QLineEdit(self.groupBox)
        self.equal_3.setGeometry(QtCore.QRect(210, 90, 30, 40))
        self.equal_3.setMinimumSize(QtCore.QSize(30, 40))
        self.equal_3.setMaximumSize(QtCore.QSize(30, 40))
        self.equal_3.setBaseSize(QtCore.QSize(30, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.equal_3.setFont(font)
        self.equal_3.setAlignment(QtCore.Qt.AlignCenter)
        self.equal_3.setObjectName("equal_3")
        self.name_3 = QtWidgets.QLineEdit(self.groupBox)
        self.name_3.setGeometry(QtCore.QRect(10, 90, 200, 40))
        self.name_3.setMinimumSize(QtCore.QSize(200, 40))
        self.name_3.setMaximumSize(QtCore.QSize(200, 40))
        self.name_3.setBaseSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.name_3.setFont(font)
        self.name_3.setText("")
        self.name_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name_3.setObjectName("name_3")
        self.score_3 = QtWidgets.QLineEdit(self.groupBox)
        self.score_3.setGeometry(QtCore.QRect(240, 90, 40, 40))
        self.score_3.setMinimumSize(QtCore.QSize(40, 40))
        self.score_3.setMaximumSize(QtCore.QSize(40, 40))
        self.score_3.setBaseSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.score_3.setFont(font)
        self.score_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.score_3.setObjectName("score_3")
        self.equal_4 = QtWidgets.QLineEdit(self.groupBox)
        self.equal_4.setGeometry(QtCore.QRect(210, 130, 30, 40))
        self.equal_4.setMinimumSize(QtCore.QSize(30, 40))
        self.equal_4.setMaximumSize(QtCore.QSize(30, 40))
        self.equal_4.setBaseSize(QtCore.QSize(30, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.equal_4.setFont(font)
        self.equal_4.setAlignment(QtCore.Qt.AlignCenter)
        self.equal_4.setObjectName("equal_4")
        self.name_4 = QtWidgets.QLineEdit(self.groupBox)
        self.name_4.setGeometry(QtCore.QRect(10, 130, 200, 40))
        self.name_4.setMinimumSize(QtCore.QSize(200, 40))
        self.name_4.setMaximumSize(QtCore.QSize(200, 40))
        self.name_4.setBaseSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.name_4.setFont(font)
        self.name_4.setText("")
        self.name_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name_4.setObjectName("name_4")
        self.score_4 = QtWidgets.QLineEdit(self.groupBox)
        self.score_4.setGeometry(QtCore.QRect(240, 130, 40, 40))
        self.score_4.setMinimumSize(QtCore.QSize(40, 40))
        self.score_4.setMaximumSize(QtCore.QSize(40, 40))
        self.score_4.setBaseSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.score_4.setFont(font)
        self.score_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.score_4.setObjectName("score_4")
        self.equal_5 = QtWidgets.QLineEdit(self.groupBox)
        self.equal_5.setGeometry(QtCore.QRect(210, 170, 30, 40))
        self.equal_5.setMinimumSize(QtCore.QSize(30, 40))
        self.equal_5.setMaximumSize(QtCore.QSize(30, 40))
        self.equal_5.setBaseSize(QtCore.QSize(30, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.equal_5.setFont(font)
        self.equal_5.setAlignment(QtCore.Qt.AlignCenter)
        self.equal_5.setObjectName("equal_5")
        self.name_5 = QtWidgets.QLineEdit(self.groupBox)
        self.name_5.setGeometry(QtCore.QRect(10, 170, 200, 40))
        self.name_5.setMinimumSize(QtCore.QSize(200, 40))
        self.name_5.setMaximumSize(QtCore.QSize(200, 40))
        self.name_5.setBaseSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.name_5.setFont(font)
        self.name_5.setText("")
        self.name_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name_5.setObjectName("name_5")
        self.score_5 = QtWidgets.QLineEdit(self.groupBox)
        self.score_5.setGeometry(QtCore.QRect(240, 170, 40, 40))
        self.score_5.setMinimumSize(QtCore.QSize(40, 40))
        self.score_5.setMaximumSize(QtCore.QSize(40, 40))
        self.score_5.setBaseSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.score_5.setFont(font)
        self.score_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.score_5.setObjectName("score_5")
        self.equal_6 = QtWidgets.QLineEdit(self.groupBox)
        self.equal_6.setGeometry(QtCore.QRect(210, 210, 30, 40))
        self.equal_6.setMinimumSize(QtCore.QSize(30, 40))
        self.equal_6.setMaximumSize(QtCore.QSize(30, 40))
        self.equal_6.setBaseSize(QtCore.QSize(30, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.equal_6.setFont(font)
        self.equal_6.setAlignment(QtCore.Qt.AlignCenter)
        self.equal_6.setObjectName("equal_6")
        self.name_6 = QtWidgets.QLineEdit(self.groupBox)
        self.name_6.setGeometry(QtCore.QRect(10, 210, 200, 40))
        self.name_6.setMinimumSize(QtCore.QSize(200, 40))
        self.name_6.setMaximumSize(QtCore.QSize(200, 40))
        self.name_6.setBaseSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.name_6.setFont(font)
        self.name_6.setText("")
        self.name_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name_6.setObjectName("name_6")
        self.score_6 = QtWidgets.QLineEdit(self.groupBox)
        self.score_6.setGeometry(QtCore.QRect(240, 210, 40, 40))
        self.score_6.setMinimumSize(QtCore.QSize(40, 40))
        self.score_6.setMaximumSize(QtCore.QSize(40, 40))
        self.score_6.setBaseSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.score_6.setFont(font)
        self.score_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.score_6.setObjectName("score_6")
        self.equal_7 = QtWidgets.QLineEdit(self.groupBox)
        self.equal_7.setGeometry(QtCore.QRect(210, 250, 30, 40))
        self.equal_7.setMinimumSize(QtCore.QSize(30, 40))
        self.equal_7.setMaximumSize(QtCore.QSize(30, 40))
        self.equal_7.setBaseSize(QtCore.QSize(30, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.equal_7.setFont(font)
        self.equal_7.setAlignment(QtCore.Qt.AlignCenter)
        self.equal_7.setObjectName("equal_7")
        self.name_7 = QtWidgets.QLineEdit(self.groupBox)
        self.name_7.setGeometry(QtCore.QRect(10, 250, 200, 40))
        self.name_7.setMinimumSize(QtCore.QSize(200, 40))
        self.name_7.setMaximumSize(QtCore.QSize(200, 40))
        self.name_7.setBaseSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.name_7.setFont(font)
        self.name_7.setText("")
        self.name_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name_7.setObjectName("name_7")
        self.score_7 = QtWidgets.QLineEdit(self.groupBox)
        self.score_7.setGeometry(QtCore.QRect(240, 250, 40, 40))
        self.score_7.setMinimumSize(QtCore.QSize(40, 40))
        self.score_7.setMaximumSize(QtCore.QSize(40, 40))
        self.score_7.setBaseSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.score_7.setFont(font)
        self.score_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.score_7.setObjectName("score_7")
        self.equal_8 = QtWidgets.QLineEdit(self.groupBox)
        self.equal_8.setGeometry(QtCore.QRect(210, 290, 30, 40))
        self.equal_8.setMinimumSize(QtCore.QSize(30, 40))
        self.equal_8.setMaximumSize(QtCore.QSize(30, 40))
        self.equal_8.setBaseSize(QtCore.QSize(30, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.equal_8.setFont(font)
        self.equal_8.setAlignment(QtCore.Qt.AlignCenter)
        self.equal_8.setObjectName("equal_8")
        self.name_8 = QtWidgets.QLineEdit(self.groupBox)
        self.name_8.setGeometry(QtCore.QRect(10, 290, 200, 40))
        self.name_8.setMinimumSize(QtCore.QSize(200, 40))
        self.name_8.setMaximumSize(QtCore.QSize(200, 40))
        self.name_8.setBaseSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.name_8.setFont(font)
        self.name_8.setText("")
        self.name_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name_8.setObjectName("name_8")
        self.score_8 = QtWidgets.QLineEdit(self.groupBox)
        self.score_8.setGeometry(QtCore.QRect(240, 290, 40, 40))
        self.score_8.setMinimumSize(QtCore.QSize(40, 40))
        self.score_8.setMaximumSize(QtCore.QSize(40, 40))
        self.score_8.setBaseSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.score_8.setFont(font)
        self.score_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.score_8.setObjectName("score_8")
        self.equal_9 = QtWidgets.QLineEdit(self.groupBox)
        self.equal_9.setGeometry(QtCore.QRect(210, 330, 30, 40))
        self.equal_9.setMinimumSize(QtCore.QSize(30, 40))
        self.equal_9.setMaximumSize(QtCore.QSize(30, 40))
        self.equal_9.setBaseSize(QtCore.QSize(30, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.equal_9.setFont(font)
        self.equal_9.setAlignment(QtCore.Qt.AlignCenter)
        self.equal_9.setObjectName("equal_9")
        self.name_9 = QtWidgets.QLineEdit(self.groupBox)
        self.name_9.setGeometry(QtCore.QRect(10, 330, 200, 40))
        self.name_9.setMinimumSize(QtCore.QSize(200, 40))
        self.name_9.setMaximumSize(QtCore.QSize(200, 40))
        self.name_9.setBaseSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.name_9.setFont(font)
        self.name_9.setText("")
        self.name_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name_9.setObjectName("name_9")
        self.score_9 = QtWidgets.QLineEdit(self.groupBox)
        self.score_9.setGeometry(QtCore.QRect(240, 330, 40, 40))
        self.score_9.setMinimumSize(QtCore.QSize(40, 40))
        self.score_9.setMaximumSize(QtCore.QSize(40, 40))
        self.score_9.setBaseSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.score_9.setFont(font)
        self.score_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.score_9.setObjectName("score_9")
        self.equal_10 = QtWidgets.QLineEdit(self.groupBox)
        self.equal_10.setGeometry(QtCore.QRect(210, 370, 30, 40))
        self.equal_10.setMinimumSize(QtCore.QSize(30, 40))
        self.equal_10.setMaximumSize(QtCore.QSize(30, 40))
        self.equal_10.setBaseSize(QtCore.QSize(30, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.equal_10.setFont(font)
        self.equal_10.setAlignment(QtCore.Qt.AlignCenter)
        self.equal_10.setObjectName("equal_10")
        self.name_10 = QtWidgets.QLineEdit(self.groupBox)
        self.name_10.setGeometry(QtCore.QRect(10, 370, 200, 40))
        self.name_10.setMinimumSize(QtCore.QSize(200, 40))
        self.name_10.setMaximumSize(QtCore.QSize(200, 40))
        self.name_10.setBaseSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.name_10.setFont(font)
        self.name_10.setText("")
        self.name_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name_10.setObjectName("name_10")
        self.score_10 = QtWidgets.QLineEdit(self.groupBox)
        self.score_10.setGeometry(QtCore.QRect(240, 370, 40, 40))
        self.score_10.setMinimumSize(QtCore.QSize(40, 40))
        self.score_10.setMaximumSize(QtCore.QSize(40, 40))
        self.score_10.setBaseSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.score_10.setFont(font)
        self.score_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.score_10.setObjectName("score_10")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.score_1.setText(_translate("Form", "0"))
        self.equal_1.setText(_translate("Form", "="))
        self.name_1.setPlaceholderText(_translate("Form", "-"))
        self.equal_2.setText(_translate("Form", "="))
        self.name_2.setPlaceholderText(_translate("Form", "-"))
        self.score_2.setText(_translate("Form", "0"))
        self.equal_3.setText(_translate("Form", "="))
        self.name_3.setPlaceholderText(_translate("Form", "-"))
        self.score_3.setText(_translate("Form", "0"))
        self.equal_4.setText(_translate("Form", "="))
        self.name_4.setPlaceholderText(_translate("Form", "-"))
        self.score_4.setText(_translate("Form", "0"))
        self.equal_5.setText(_translate("Form", "="))
        self.name_5.setPlaceholderText(_translate("Form", "-"))
        self.score_5.setText(_translate("Form", "0"))
        self.equal_6.setText(_translate("Form", "="))
        self.name_6.setPlaceholderText(_translate("Form", "-"))
        self.score_6.setText(_translate("Form", "0"))
        self.equal_7.setText(_translate("Form", "="))
        self.name_7.setPlaceholderText(_translate("Form", "-"))
        self.score_7.setText(_translate("Form", "0"))
        self.equal_8.setText(_translate("Form", "="))
        self.name_8.setPlaceholderText(_translate("Form", "-"))
        self.score_8.setText(_translate("Form", "0"))
        self.equal_9.setText(_translate("Form", "="))
        self.name_9.setPlaceholderText(_translate("Form", "-"))
        self.score_9.setText(_translate("Form", "0"))
        self.equal_10.setText(_translate("Form", "="))
        self.name_10.setPlaceholderText(_translate("Form", "-"))
        self.score_10.setText(_translate("Form", "0"))

