from PyQt5.QtWidgets import *
from tranformUi import TransformGui
from playerUi import PlayerGui


class MainGui(QMainWindow):
    """ 窗口主界面

    """
    def __init__(self):
        super().__init__()
        self.__init_control()

    # 初始化控件的位置
    def __init_control(self):
        glayout = QGridLayout()

        # 创建语音播放控件和语音转写控件
        self.__transform_func = TransformGui()
        self.__player = PlayerGui()

        # 把控件添加到相应的位置
        glayout.addWidget(self.__player)
        glayout.addWidget(self.__transform_func)
        widget_layout = QWidget()
        widget_layout.setLayout(glayout)
        self.setCentralWidget(widget_layout)

        # 获取当前显示器的大小，并设置窗口的大小
        desktop = QApplication.desktop()
        rect_size = desktop.screenGeometry()
        width = rect_size.width()
        self.setMinimumWidth(width * 0.5)

        # 把player的信号与transform的函数绑定
        self.__player.files_signal.connect(self.__transform_func.get_files)
        self.__player.select_file.connect(self.__transform_func.show_file_txt)
