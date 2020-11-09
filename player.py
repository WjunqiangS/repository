from PyQt5.QtCore import *

class PlayerThread(QThread):
    end_signal = pyqtSignal()

    def __init__(self, file = None):
        super(PlayerThread, self).__init__()
        self.file = file

    # 开始播放
    def run(self):
        return

    # 播放下一首
    def next(self, file):
        return

    # 播放前一首
    def previous(self, file ):
        return

    # 停止播放