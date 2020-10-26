from PyQt5.QtWidgets import *


class FuncButtons(QWidget):
    """ 本类包含了所有功能按钮以及功能按钮的槽函数
        __self_upload：把语音文件上传转写后返回语音对应的文本文件
    """
    def __init__(self):
        super(FuncButtons, self).__init__()
        self.__init_control()

    def __init_control(self):
        # 创建功能按键
        self.__btn_upload = QPushButton('语音转写')

        # 创建布局管理器，管理功能按键
        vlayout = QVBoxLayout()

        # 添加控件到布局管理器
        vlayout.addWidget(self.__btn_upload)

        self.setLayout(vlayout)

        # 绑定功能按钮的槽函数
        self.__btn_upload.clicked.connect(self.on_btn_upload_clicked)

    # 语音上传转写功能按钮槽函数
    def on_btn_upload_clicked(self):
        files = QFileDialog.getOpenFileNames(self, '选择文件',
                                             '/Users/wangjunqiang/PycharmProjects/GUI_Project', 'All Files (*);;')
        print(files[0])
