from PyQt5.QtWidgets import *
from PyQt5.QtCore import QStringListModel, pyqtSignal, QPoint, QUrl, QTime, QModelIndex
from PyQt5.QtGui import QIcon, QCursor, QMouseEvent
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtMultimedia import *
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
    back_signal = pyqtSignal()
    forward_signal = pyqtSignal()

    def __init__(self):
        super(PlayerGui, self).__init__()
        self.__player = QMediaPlayer(self)
        self.__play_list = QMediaPlaylist(self)
        self.__player.setPlaylist(self.__play_list)
        self.__play_list.setCurrentIndex(0)
        self.__init_control()

    def __init_control(self):
        # 被选中的列表
        self.files = []

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

        self.__back_btn.setIcon(QIcon(os.path.join(os.path.join(os.getcwd(), 'RES'), 'back.png')))
        self.__play_btn.setIcon(QIcon(os.path.join(os.path.join(os.getcwd(), 'RES'), 'play.png')))
        self.__forward_btn.setIcon(QIcon(os.path.join(os.path.join(os.getcwd(), 'RES'), 'forward.png')))
        self.__stop_btn.setIcon(QIcon(os.path.join(os.path.join(os.getcwd(), 'RES'), 'stop.png')))

        # 播放时间
        self.__time_label1 = QLabel("00:00", self)
        self.__time_label1.setStyle(QStyleFactory.create('Fusion'))
        self.__time_label2 = QLabel("00:00", self)
        self.__time_label2.setStyle(QStyleFactory.create('Fusion'))

        # 播放进度条
        self.__time_slider = QSlider(Qt.Horizontal, self)
        self.__time_slider.setStyle(QStyleFactory.create('Fusion'))
        self.__time_slider.installEventFilter(self)

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

        # 连接打开文件列表按键的槽函数
        self.__btn_open_files.clicked.connect(self.on_btn_open_files_clicked)
        self.__list_files.clicked.connect(self.on_list_files_clicked)
        self.__list_files.doubleClicked.connect(self.on_list_files_doubleclicked)

        # 连接播放按键的槽函数
        self.__back_btn.pressed.connect(self.on_btn_back_pressed)
        self.__play_btn.pressed.connect(self.on_btn_play_pressed)
        self.__forward_btn.pressed.connect(self.on_btn_forward_pressed)
        self.__stop_btn.pressed.connect(self.on_btn_stop_pressed)

        # 连接播放器信号的槽函数
        self.__player.positionChanged.connect(self.on_update_slider)
        self.__player.durationChanged.connect(self.on_media_changed)
        self.__player.stateChanged.connect(self.on_player_state_changed)

        # 设置菜单
        self.__list_files.setContextMenuPolicy(3)
        self.__list_files.customContextMenuRequested[QPoint].connect(self.list_fils_right_key_menu)

    # 打开文件按钮的槽函数
    def on_btn_open_files_clicked(self):
        files_path = QFileDialog.getOpenFileNames(self, '打开文件', os.getcwd(), 'Audio Files (*.wav);;')[0]

        # 把打开的文件都保存到文件列表中
        for str in files_path:
            exist_flag = 0
            for exit_file in self.files:
                if os.path.basename(str) == exit_file.file_name:
                    exist_flag = 1
                    break
            if not exist_flag:
                file = File(str)
                self.files.append(file)
                # 把打开的文件预先存放到播放列表里面
                self.__play_list.addMedia(QMediaContent(QUrl.fromLocalFile(file.file_path)))
                # 打开文件之后给开始转写发送信号，表示已经拿到文件
                self.files_signal.emit(file)

        slm = QStringListModel()
        slm.setStringList([file.file_name for file in self.files])
        self.__list_files.setModel(slm)
        self.__list_files.setCurrentIndex(slm.index(0))

    # 文件列表单击的槽函数
    def on_list_files_clicked(self, index):
        self.select_file.emit(self.files[index.row()].file_name)

    # 文件列表双击的槽函数
    def on_list_files_doubleclicked(self, index):
        self.stop()
        self.__play_list.setCurrentIndex(index.row())
        self.play()

    # 文件列表右键功能，还未完成
    def list_fils_right_key_menu(self, point):
        menu = QMenu()
        menu.addAction('删除')
        menu.exec_(QCursor.pos())

    # 播放按钮被点击
    def on_btn_play_pressed(self):
        if not self.__play_list.isEmpty():
            if self.__player.mediaStatus() == QMediaPlayer.NoMedia:
                self.play()
            elif self.__player.state() == QMediaPlayer.StoppedState:
                self.play()
            elif self.__player.state() == QMediaPlayer.PlayingState:
                self.pause()
            elif self.__player.state() == QMediaPlayer.PausedState:
                self.play()

    # 上一首按钮被点击
    def on_btn_back_pressed(self):
        self.back()

    # 下一首按钮被点击
    def on_btn_forward_pressed(self):
        self.forward()

    # 停止按钮被点击
    def on_btn_stop_pressed(self):
        self.stop()

    # 媒体文件状态改变时，更新进度条和时间标签
    def on_media_changed(self, time):
        duration = QTime(0, time / 60000, int(round((time % 60000) / 1000.0, 0)))
        self.__time_label2.setText(duration.toString('mm:ss'))
        self.__time_slider.setRange(0, time)

    # 当时间变化时更改进度条时间
    def on_update_slider(self, position):
        duration = QTime(0, position / 60000, int(round((position % 60000) / 1000.0, 0)))
        self.__time_label1.setText(duration.toString('mm:ss'))
        self.__time_slider.setValue(position)

    def on_player_state_changed(self, state):
        if state == QMediaPlayer.PlayingState:
            self.__play_btn.setIcon(QIcon(os.path.join(os.path.join(os.getcwd(), 'RES'), 'pause.png')))
        elif state == QMediaPlayer.PausedState:
            self.__play_btn.setIcon(QIcon(os.path.join(os.path.join(os.getcwd(), 'RES'), 'play.png')))
        elif state == QMediaPlayer.StoppedState:
            self.__play_btn.setIcon(QIcon(os.path.join(os.path.join(os.getcwd(), 'RES'), 'play.png')))
            self.__time_slider.setValue(0)
            self.__time_label1.setText('00:00')
        # 重绘播放控件
        self.__play_btn.repaint()
        self.__time_slider.repaint()
        self.__time_label1.repaint()

    def eventFilter(self, obj, event):
        if obj == self.__time_slider and  (self.__player.state() == QMediaPlayer.PlayingState or
        self.__player.state() == QMediaPlayer.PausedState):
            if event.type() == QEvent.MouseButtonPress:
                mouse_event = QMouseEvent(event)
                if mouse_event.buttons() == Qt.LeftButton:
                    range = self.__time_slider.maximum()
                    width = self.__time_slider.width()

                    pos = mouse_event.pos().x() / width * range
                    self.__player.setPosition(pos)
                    if self.__player.state() == QMediaPlayer.PausedState:
                        self.play()

        return QDialog.eventFilter(QDialog(), obj, event)

    ####################### 播放器功能 ####################
    def play(self):
        self.__player.play()

    def stop(self):
        self.__player.stop()

    def pause(self):
        self.__player.pause()

    def back(self):
        # 先停止当前曲目的播放
        self.stop()

        # 计算上一首曲目的偏移量
        count = len(self.files)
        cur_index = self.__play_list.currentIndex()
        cur_index -= 1
        self.__play_list.setCurrentIndex(cur_index % count)

        # 播放下一首曲目
        self.play()

    def forward(self):
        # 先停止当前曲目的播放
        self.stop()

        # 计算下一首曲目的偏移量
        count = len(self.files)
        cur_index = self.__play_list.currentIndex()
        cur_index += 1
        self.__play_list.setCurrentIndex(cur_index % count)

        # 播放下一首曲目
        self.play()
