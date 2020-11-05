from PyQt5.QtWidgets import *
import os


class TransformFunc(QWidget):
    """ 本类包含了所有功能按钮以及功能按钮的槽函数
        __self_upload：把语音文件上传转写后返回语音对应的文本文件
    """
    def __init__(self):
        super(TransformFunc, self).__init__()
        self.__files = []
        self.__init_control()

    def __init_control(self):
        # 创建功能按键
        self.__btn_upload = QPushButton('语音转写')

        # 创建文本区
        self.__text = QPlainTextEdit()

        # 创建布局管理器，管理功能按键
        vlayout = QVBoxLayout()

        # 添加控件到布局管理器
        vlayout.addWidget(QLabel('语音转写区:'))
        vlayout.addWidget(self.__text)
        vlayout.addWidget(self.__btn_upload)

        self.setLayout(vlayout)

        # 绑定功能按钮的槽函数
        self.__btn_upload.clicked.connect(self.on_btn_upload_clicked)

    # 语音上传转写功能按钮槽函数
    def on_btn_upload_clicked(self):
        if not self.__files:
            QMessageBox(QMessageBox.Warning, '警告', '请打开要转写的语音文件').exec()
        else:
            for file in self.__files:
                print(file.full_path)

    def get_files(self, files):
        self.__files = files