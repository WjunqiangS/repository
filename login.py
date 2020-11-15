from PyQt5.QtWidgets import QDialog, QPushButton, QLineEdit, QLabel

from PyQt5.QtWidgets import QWidget, QApplication
import sys


class Login(QDialog):
    def __init__(self, parent = None):
        super(Login, self).__init__()
        self.__init_layout()
        self.setParent(parent)

    def __init_layout(self):
        self.__login_btn = QPushButton("登陆", self)
        self.__cancle_btn = QPushButton("取消", self)
        self.__usr_name = QLineEdit(self)
        self.__passwd = QLineEdit(self)
        self.__usr_label = QLabel('用户名：', self)
        self.__passwd_label = QLabel('密码：', self)

        self.__usr_label.move(20, 30)
        self.__usr_label.resize(60, 25)

        self.__usr_name.move(85, 30)
        self.__usr_name.resize(180, 25)

        self.__passwd_label.move(20, 65)
        self.__passwd_label.resize(60, 25)

        self.__passwd.move(85, 65)
        self.__passwd.resize(180, 25)
        self.__passwd.setEchoMode(QLineEdit.Password)

        self.__cancle_btn.move(85,100)
        self.__cancle_btn.resize(85,30)

        self.__login_btn.move(180,100)
        self.__login_btn.resize(85,30)

        self.setWindowTitle('登陆')
        self.setFixedSize(285, 130)

        self.__login_btn.clicked.connect(self.__on_login_btn_clicked)
        self.__cancle_btn.clicked.connect(self.__on_cancle_btn_clicked)

    def __on_login_btn_clicked(self):
        self.done(QDialog.Accepted)
        return

    def __on_cancle_btn_clicked(self):
        self.done(QDialog.Rejected)
        return

    def get_usr_name(self):
        return self.__usr_name.text()

    def get_passwd(self):
        return self.__passwd.text()

