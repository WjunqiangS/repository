from PyQt5.QtWidgets import *
from PyQt5.QtCore import QStringListModel, pyqtSignal, QPoint
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtCore import Qt
from file import File
import os

class PlayerGui(QWidget):
    """ 本类包含了打开文件、文件列表、还有声音播放的功能以及控制按钮
        __btn_open_files: 打开文件按钮
        __list_files: 文件列表
        files_path: 选择打开的文件路径
    """
    files_signal = pyqtSignal(File)
    select_file = pyqtSignal(str)

    def __init__(self):
        super(PlayerGui, self).__init__()
        self.files = []
        self.__init_control()

    def __init_control(self):
        # 创建布局管理器，管理功能按键
        glayout = QGridLayout()
        vlayout = QVBoxLayout()

        # 打开文件按钮
        self.__btn_open_files = QPushButton('打开文件')
        self.__list_files = QListView()
        self.__list_files.setEditTriggers(QAbstractItemView.NoEditTriggers)


        # 播放控制按钮
        self.__back_btn = QPushButton(self)
        self.__play_btn = QPushButton(self)
        self.__forward_btn = QPushButton(self)
        self.__stop_btn = QPushButton(self)

        self.__back_btn.setIcon(QIcon('./RES/back.png'))
        self.__play_btn.setIcon(QIcon('./RES/play.png'))
        self.__forward_btn.setIcon(QIcon('./RES/forward.png'))
        self.__stop_btn.setIcon(QIcon('./RES/stop.png'))

        # 播放时间
        self.__time_label1 = QLabel("00:00", self)
        self.__time_label1.setStyle(QStyleFactory.create('Fusion'))
        self.__time_label2 = QLabel("00:00", self)
        self.__time_label2.setStyle(QStyleFactory.create('Fusion'))

        # 播放进度条
        self.__time_slider = QSlider(Qt.Horizontal, self)
        self.__time_slider.setStyle(QStyleFactory.create('Fusion'))

        # 设置播放按钮的布局
        glayout.addWidget(self.__time_label1, 0, 0, 1, 1)
        glayout.addWidget(self.__time_slider, 0, 1, 1, 12)
        glayout.addWidget(self.__time_label2, 0, 13)
        glayout.addWidget(self.__back_btn, 1, 1, 1, 3)
        glayout.addWidget(self.__play_btn, 1, 4, 1, 3)
        glayout.addWidget(self.__forward_btn, 1, 7, 1, 3)
        glayout.addWidget(self.__stop_btn, 1, 10, 1, 3)
        vlayout.addWidget(QLabel('语音播放区：'))
        vlayout.addWidget(self.__btn_open_files)
        vlayout.addWidget(self.__list_files)
        vlayout.addLayout(glayout)

        self.setLayout(vlayout)

        # 绑定按键和槽函数
        self.__btn_open_files.clicked.connect(self.on_btn_open_files_clicked)
        self.__list_files.clicked.connect(self.on_list_files_cliked)
        #设置菜单
        self.__list_files.setContextMenuPolicy(3)
        self.__list_files.customContextMenuRequested[QPoint].connect(self.list_fils_right_key_menu)

    # 打开文件按钮的槽函数
    def on_btn_open_files_clicked(self):
        files_path = QFileDialog.getOpenFileNames(self, '打开文件', os.getcwd(), 'Audio Files (*.[V|v]3);;Audio Files (*.wav);;')[0]

        # 把打开的文件都保存到文件列表中
        for str in files_path:
            exist_flag = 0
            for exit_file in self.files:
                if os.path.basename(str) == exit_file.file_name:
                    exist_flag = 1
                    break
            if not exist_flag:
                file = File(os.path.basename(str), os.path.dirname(str))
                self.files.append(file)
                # 打开文件之后给开始转写发送信号，表示已经拿到文件
                self.files_signal.emit(file)

        slm = QStringListModel()
        slm.setStringList([file.file_name for file in self.files])
        self.__list_files.setModel(slm)

    # 文件列表点击的槽函数
    def on_list_files_cliked(self, index):
        self.select_file.emit(self.files[index.row()].file_name)

    def list_fils_right_key_menu(self, point):
        menu = QMenu()
        menu.addAction('删除')
        menu.exec_(QCursor.pos())
