# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sign_up.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sign_up(object):
    def setupUi(self, sign_up):
        sign_up.setObjectName("sign_up")
        sign_up.resize(811, 478)
        self.sign_up_widget = QtWidgets.QWidget(sign_up)
        self.sign_up_widget.setGeometry(QtCore.QRect(20, 20, 781, 441))
        self.sign_up_widget.setObjectName("sign_up_widget")
        self.sign_up_label = QtWidgets.QLabel(self.sign_up_widget)
        self.sign_up_label.setGeometry(QtCore.QRect(490, 50, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.sign_up_label.setFont(font)
        self.sign_up_label.setObjectName("sign_up_label")
        self.name_label = QtWidgets.QLabel(self.sign_up_widget)
        self.name_label.setGeometry(QtCore.QRect(400, 190, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.workid_label = QtWidgets.QLabel(self.sign_up_widget)
        self.workid_label.setGeometry(QtCore.QRect(400, 140, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.workid_label.setFont(font)
        self.workid_label.setObjectName("workid_label")
        self.name_lineEdit = QtWidgets.QLineEdit(self.sign_up_widget)
        self.name_lineEdit.setGeometry(QtCore.QRect(490, 190, 181, 21))
        self.name_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.workid_lineEdit = QtWidgets.QLineEdit(self.sign_up_widget)
        self.workid_lineEdit.setGeometry(QtCore.QRect(490, 140, 181, 21))
        self.workid_lineEdit.setObjectName("workid_lineEdit")
        self.sign_up_pushButton = QtWidgets.QPushButton(self.sign_up_widget)
        self.sign_up_pushButton.setGeometry(QtCore.QRect(490, 350, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sign_up_pushButton.setFont(font)
        self.sign_up_pushButton.setObjectName("sign_up_pushButton")
        self.password_label = QtWidgets.QLabel(self.sign_up_widget)
        self.password_label.setGeometry(QtCore.QRect(400, 240, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.password_lineEdit = QtWidgets.QLineEdit(self.sign_up_widget)
        self.password_lineEdit.setGeometry(QtCore.QRect(490, 240, 181, 21))
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.check_password_label = QtWidgets.QLabel(self.sign_up_widget)
        self.check_password_label.setGeometry(QtCore.QRect(400, 290, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.check_password_label.setFont(font)
        self.check_password_label.setObjectName("check_password_label")
        self.check_password_lineEdit = QtWidgets.QLineEdit(self.sign_up_widget)
        self.check_password_lineEdit.setGeometry(QtCore.QRect(490, 290, 181, 21))
        self.check_password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.check_password_lineEdit.setObjectName("check_password_lineEdit")

        self.retranslateUi(sign_up)
        QtCore.QMetaObject.connectSlotsByName(sign_up)

    def retranslateUi(self, sign_up):
        _translate = QtCore.QCoreApplication.translate
        sign_up.setWindowTitle(_translate("sign_up", "Form"))
        self.sign_up_label.setText(_translate("sign_up", "注册"))
        self.name_label.setText(_translate("sign_up", "姓名:"))
        self.workid_label.setText(_translate("sign_up", "工号:"))
        self.sign_up_pushButton.setText(_translate("sign_up", "注册"))
        self.password_label.setText(_translate("sign_up", "密码:"))
        self.check_password_label.setText(_translate("sign_up", "确认密码:"))
