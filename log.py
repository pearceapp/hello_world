# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 278)
        self.submit = QtWidgets.QPushButton(Form)
        self.submit.setGeometry(QtCore.QRect(130, 160, 81, 23))
        self.submit.setObjectName("submit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.username_lineEdit = QtWidgets.QLineEdit(Form)
        self.username_lineEdit.setGeometry(QtCore.QRect(130, 90, 261, 20))
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.password_lineEdit = QtWidgets.QLineEdit(Form)
        self.password_lineEdit.setGeometry(QtCore.QRect(130, 120, 261, 20))
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.use_key = QtWidgets.QPushButton(Form)
        self.use_key.setGeometry(QtCore.QRect(310, 160, 81, 23))
        self.use_key.setObjectName("use_key")
        self.message_lineEdit = QtWidgets.QLineEdit(Form)
        self.message_lineEdit.setGeometry(QtCore.QRect(20, 220, 261, 20))
        self.message_lineEdit.setObjectName("message_lineEdit")
        self.Save_My_Message = QtWidgets.QPushButton(Form)
        self.Save_My_Message.setGeometry(QtCore.QRect(290, 220, 101, 21))
        self.Save_My_Message.setObjectName("Save_My_Message")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login Form"))
        self.submit.setText(_translate("Form", "Submit"))
        self.label.setText(_translate("Form", "Login Form"))
        self.label_2.setText(_translate("Form", "Username"))
        self.label_3.setText(_translate("Form", "Password"))
        self.use_key.setText(_translate("Form", "Generate Key"))
        self.Save_My_Message.setText(_translate("Form", "Save My Message"))
