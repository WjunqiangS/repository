from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel, QSlider, QStyleFactory, QDialog
from PyQt5.QtGui import QIcon, QMouseEvent
from PyQt5.QtCore import Qt, QTime, QEvent, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist, QMediaContent
import os

# 测试
from PyQt5.QtWidgets import QApplication, QFileDialog
import sys
import re
from alaw2pcm import alaw2pcm
from file import File


class Player(QWidget):
    def __init__(self):
        super(Player, self).__init__()
        self.__init_player()
        self.__control_layouy()

    def __init_player(self):
        self.__player = QMediaPlayer(self)
        self.__play_list = QMediaPlaylist(self)
        self.__player.setPlaylist(self.__play_list)
        self.__play_list.setCurrentIndex(0)

        self.__player.positionChanged.connect(self.__on_update_slider)
        self.__player.durationChanged.connect(self.__on_media_changed)
        self.__player.stateChanged.connect(self.__on_player_state_changed)

    def __control_layouy(self):
        glayout = QGridLayout()
        # 播放控制按钮初始化
        self.__back_btn = QPushButton(self)
        self.__back_btn.setIcon(QIcon(os.path.join(os.path.join(os.getcwd(), 'RES'), 'back.png')))
        self.__back_btn.pressed.connect(self.__on_btn_back_pressed)

        self.__play_btn = QPushButton(self)
        self.__play_btn.setIcon(QIcon(os.path.join(os.path.join(os.getcwd(), 'RES'), 'play.png')))
        self.__play_btn.pressed.connect(self.__on_btn_play_pressed)

        self.__forward_btn = QPushButton(self)
        self.__forward_btn.setIcon(QIcon(os.path.join(os.path.join(os.getcwd(), 'RES'), 'forward.png')))
        self.__forward_btn.pressed.connect(self.__on_btn_forward_pressed)


        self.__stop_btn = QPushButton(self)
        self.__stop_btn.setIcon(QIcon(os.path.join(os.path.join(os.getcwd(), 'RES'), 'stop.png')))
        self.__stop_btn.pressed.connect(self.__on_btn_stop_pressed)

        # 播放时间
        self.__time_label1 = QLabel("00:00", self)
        self.__time_label1.setStyle(QStyleFactory.create('Fusion'))
        self.__time_label2 = QLabel("00:00", self)
        self.__time_label2.setStyle(QStyleFactory.create('Fusion'))

        # 播放进度条
        self.__time_slider = QSlider(Qt.Horizontal, self)
        self.__time_slider.setStyle(QStyleFactory.create('Fusion'))
        self.__time_slider.setTracking(False)
        self.__time_slider.installEventFilter(self)
        self.__time_slider.sliderMoved.connect(self.__on_slider_moved)

        # 设置播放按钮的布局
        glayout.addWidget(self.__time_label1, 0, 0, 1, 1)
        glayout.addWidget(self.__time_slider, 0, 1, 1, 12)
        glayout.addWidget(self.__time_label2, 0, 13)
        glayout.addWidget(self.__back_btn, 1, 1, 1, 3)
        glayout.addWidget(self.__play_btn, 1, 4, 1, 3)
        glayout.addWidget(self.__forward_btn, 1, 7, 1, 3)
        glayout.addWidget(self.__stop_btn, 1, 10, 1, 3)

        self.setLayout(glayout)


    # 播放按钮被点击
    def __on_btn_play_pressed(self):
        if not self.__play_list.isEmpty():
            if self.__player.mediaStatus() == QMediaPlayer.NoMedia:
                self.__play()
            elif self.__player.state() == QMediaPlayer.StoppedState:
                self.__play()
            elif self.__player.state() == QMediaPlayer.PlayingState:
                self.__pause()
            elif self.__player.state() == QMediaPlayer.PausedState:
                self.__play()

    # 上一首按钮被点击
    def __on_btn_back_pressed(self):
        self.__back()

    # 下一首按钮被点击
    def __on_btn_forward_pressed(self):
        self.__forward()

    # 停止按钮被点击
    def __on_btn_stop_pressed(self):
        self.__stop()

    # 媒体文件状态改变时，更新进度条和时间标签
    def __on_media_changed(self, time):
        duration = QTime(0, time / 60000, int(round((time % 60000) / 1000.0, 0)))
        self.__time_label2.setText(duration.toString('mm:ss'))
        self.__time_slider.setRange(0, time)

    # 当时间变化时更改进度条时间
    def __on_update_slider(self, position):
        duration = QTime(0, position / 60000, int(round((position % 60000) / 1000.0, 0)))
        self.__time_label1.setText(duration.toString('mm:ss'))
        self.__time_slider.setValue(position)

    def __on_player_state_changed(self, state):
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

    # 进度条滑动
    def __on_slider_moved(self, value):
        self.__player.setPosition(value)

    # 过滤获取进度条的点击事件
    def eventFilter(self, obj, event):
        if obj == self.__time_slider and (self.__player.state() == QMediaPlayer.PlayingState or
                                          self.__player.state() == QMediaPlayer.PausedState):
            if event.type() == QEvent.MouseButtonPress:
                mouse_event = QMouseEvent(event)
                if mouse_event.buttons() == Qt.LeftButton:
                    range = self.__time_slider.maximum()
                    width = self.__time_slider.width()

                    pos = mouse_event.pos().x() / width * range
                    self.__player.setPosition(pos)
                    if self.__player.state() == QMediaPlayer.PausedState:
                        self.__play()
        elif obj == self.__time_slider:
            self.__time_slider.setValue(0)

        return QDialog.eventFilter(QDialog(), obj, event)


    def __play(self):
        self.__player.play()

    def __stop(self):
        self.__player.stop()

    def __pause(self):
        self.__player.pause()

    def __back(self):
        if self.__play_list.isEmpty():
            return
        # 先停止当前曲目的播放
        self.__stop()

        # 计算上一首曲目的偏移量
        count = self.__play_list.mediaCount()
        cur_index = self.__play_list.currentIndex()
        cur_index -= 1
        self.__play_list.setCurrentIndex(cur_index % count)

        # 播放下一首曲目
        self.__play()


    def __forward(self):
        if self.__play_list.isEmpty():
            return
        # 先停止当前曲目的播放
        self.__stop()

        # 计算下一首曲目的偏移量
        count = self.__play_list.mediaCount()
        cur_index = self.__play_list.currentIndex()
        cur_index += 1
        self.__play_list.setCurrentIndex(cur_index % count)

        # 播放下一首曲目
        self.__play()

    def set_play_list(self, file_path):
        self.__play_list.addMedia(QMediaContent(QUrl.fromLocalFile(file_path)))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_gui = Player()

    files_path, file_type = QFileDialog.getOpenFileNames(main_gui, "打开文件", os.getcwd(),
                                                         "V3文件 (*.V3);;wav文件 (*.wav);;", "V3文件 (*.V3)")

    # 把打开的文件都保存到文件列表中
    for str in files_path:
        exist_flag = 0
        if re.match('.*\.V3', file_type):
            with open(str, 'rb') as f:
                raw_data = f.read()
            str = os.path.join(os.path.dirname(str), os.path.basename(str).split('.')[0] + '.wav')
            wave_write = alaw2pcm(str, 1, 8000, 8)
            wave_write.write(raw_data)
            wave_write.close()

            file = File(str)
            # 把打开的文件预先存放到播放列表里面
            main_gui.set_play_list(file.file_path)

    main_gui.show()
    sys.exit(app.exec())
