from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget, QStackedLayout, QPlainTextEdit, QLabel
from func_buttons import FuncButtons
from control_btn import CtrBottoms


class MainGui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__init_control()

    def __init_control(self):
        glayout = QGridLayout()
        slayout = QStackedLayout()
        text_edit = QPlainTextEdit()
        label = QLabel("test1")

        slayout.addWidget(text_edit)
        slayout.addWidget(label)

        func_buttons = FuncButtons()
        ctr_buttons = CtrBottoms()

        glayout.addWidget(func_buttons, 0, 0, func_buttons.btn_count, 1)
        glayout.addLayout(slayout, 0, 1)
        glayout.addWidget(ctr_buttons, 1, 1)

        widget_layout = QWidget()
        widget_layout.setLayout(glayout)
        self.setCentralWidget(widget_layout)
