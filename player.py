from PyQt5.QtWidgets import QWidget
from PyQt5.QtMultimedia import QMediaPlayer

class Player(QWidget):
    def __init__(self):
        super(Player, self).__init__()
        self.player == QMediaPlayer(self)
