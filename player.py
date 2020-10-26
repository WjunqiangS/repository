from PyQt5.QtWidgets import QApplication
import sys
import pygame

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pygame.init()
    print("播放音乐1")
    track = pygame.mixer.music.load('/Users/wangjunqiang/Downloads/Oh_Father.mp3')

    pygame.mixer.music.play()

    sys.exit(app.exec())
