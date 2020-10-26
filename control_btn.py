from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QLabel, QSlider, QStyleFactory
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class CtrBottoms(QWidget):
    def __init__(self):
        super(CtrBottoms, self).__init__()
        self.__init_control()

    def __init_control(self):

        glayout = QGridLayout()
        # 播放控制按钮
        self.__back_btn = QPushButton(self)
        self.__play_btn = QPushButton(self)
        self.__forward_btn = QPushButton(self)
        self.__volume_btn = QPushButton(self)

        # 播放时间
        self.__time_label1 = QLabel("00:00", self)
        self.__time_label1.setStyle(QStyleFactory.create('Fusion'))
        self.__time_label2 = QLabel("00:00", self)
        self.__time_label2.setStyle(QStyleFactory.create('Fusion'))

        # 播放进度条
        self.__time_slider = QSlider(Qt.Horizontal, self)
        self.__time_slider.setStyle(QStyleFactory.create('Fusion'))

        self.__back_btn.setIcon(QIcon('./RES/back.png'))
        self.__play_btn.setIcon(QIcon('./RES/play.png'))
        self.__forward_btn.setIcon(QIcon('./RES/forward.png'))
        self.__volume_btn.setIcon(QIcon('./RES/volume.png'))

        glayout.addWidget(self.__time_label1, 0, 0)
        glayout.addWidget(self.__time_slider, 0, 1, 1, 6)
        glayout.addWidget(self.__time_label2, 0, 7)
        glayout.addWidget(self.__back_btn, 1, 0, 1, 2)
        glayout.addWidget(self.__play_btn, 1, 2, 1, 2)
        glayout.addWidget(self.__forward_btn, 1, 4, 1, 2)
        glayout.addWidget(self.__volume_btn, 1, 6, 1, 2)

        self.setLayout(glayout)
