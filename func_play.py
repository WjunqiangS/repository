from PyQt5.QtWidgets import *
from PyQt5.QtCore import QStringListModel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class Player(QWidget):
    """ 本类包含了打开文件、文件列表、还有声音播放的功能以及控制按钮
        __btn_open_files: 打开文件按钮
        __list_files: 文件列表
        files: 选择打开的文件路径
    """
    def __init__(self):
        super(Player, self).__init__()
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
        self.__volume_btn = QPushButton(self)

        self.__back_btn.setIcon(QIcon('./RES/back.png'))
        self.__play_btn.setIcon(QIcon('./RES/play.png'))
        self.__forward_btn.setIcon(QIcon('./RES/forward.png'))
        self.__volume_btn.setIcon(QIcon('./RES/volume.png'))

        # 播放时间
        self.__time_label1 = QLabel("00:00", self)
        self.__time_label1.setStyle(QStyleFactory.create('Fusion'))
        self.__time_label2 = QLabel("00:00", self)
        self.__time_label2.setStyle(QStyleFactory.create('Fusion'))

        # 播放进度条
        self.__time_slider = QSlider(Qt.Horizontal, self)
        self.__time_slider.setStyle(QStyleFactory.create('Fusion'))

        # 设置播放按钮的布局
        glayout.addWidget(self.__time_label1, 0, 0)
        glayout.addWidget(self.__time_slider, 0, 1, 1, 6)
        glayout.addWidget(self.__time_label2, 0, 7)
        glayout.addWidget(self.__back_btn, 1, 0, 1, 2)
        glayout.addWidget(self.__play_btn, 1, 2, 1, 2)
        glayout.addWidget(self.__forward_btn, 1, 4, 1, 2)
        glayout.addWidget(self.__volume_btn, 1, 6, 1, 2)
        vlayout.addWidget(self.__btn_open_files)
        vlayout.addWidget(self.__list_files)
        vlayout.addLayout(glayout)

        self.setLayout(vlayout)

        # 绑定按键和槽函数
        self.__btn_open_files.clicked.connect(self.on_btn_open_files_clicked)
        self.__list_files.clicked.connect(self.on_list_files_cliked)

    # 打开文件按钮的槽函数
    def on_btn_open_files_clicked(self):
        files = QFileDialog.getOpenFileNames(self, '打开文件',
                                             '/Users/wangjunqiang/PycharmProjects/GUI_Project', 'All Files (*);;')

        self.files = files[0]

        slm = QStringListModel()
        slm.setStringList(self.files)

        self.__list_files.setModel(slm)

    # 文件列表点击的槽函数
    def on_list_files_cliked(self, index):
        print(self.files[index.row()])
