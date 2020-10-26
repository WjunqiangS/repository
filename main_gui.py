from PyQt5.QtWidgets import *
from func_buttons import FuncButtons
from func_play import Player


class MainGui(QMainWindow):
    """ 窗口主界面

    """
    def __init__(self):
        super().__init__()
        self.__init_control()

    # 初始化控件的位置
    def __init_control(self):
        glayout = QGridLayout()

        text_edit = QPlainTextEdit()

        func_buttons = FuncButtons()
        play = Player()

        glayout.addWidget(play, 0, 0)
        glayout.addWidget(text_edit, 0, 1)
        glayout.addWidget(QLabel('功能区:'))
        glayout.addWidget(func_buttons)

        widget_layout = QWidget()
        widget_layout.setLayout(glayout)
        self.setCentralWidget(widget_layout)
