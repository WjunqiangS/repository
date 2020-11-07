from PyQt5.QtWidgets import *
from voice_transform import VoiceTransThread


class TransformFunc(QWidget):
    """ 本类包含了所有功能按钮以及功能按钮的槽函数
        __self_upload：把语音文件上传转写后返回语音对应的文本文件
    """
    def __init__(self):
        super(TransformFunc, self).__init__()
        self.__files = []
        self.__init_control()

    def __init_control(self):
        # 创建功能按键
        self.__btn_upload = QPushButton('语音转写')

        # 创建文本区
        self.__text = QPlainTextEdit()

        # 创建布局管理器，管理功能按键
        vlayout = QVBoxLayout()

        # 添加控件到布局管理器
        vlayout.addWidget(QLabel('语音转写区:'))
        vlayout.addWidget(self.__text)
        vlayout.addWidget(self.__btn_upload)

        self.setLayout(vlayout)

        # 绑定功能按钮的槽函数
        self.__btn_upload.clicked.connect(self.on_btn_upload_clicked)

    # 语音上传转写功能按钮槽函数
    def on_btn_upload_clicked(self):
        if not self.__files:
            QMessageBox(QMessageBox.Warning, '警告', '请打开要转写的语音文件').exec()
        else:
            self.__text.clear()
            self.__text.appendPlainText('正在转写中...')
            self.__btn_upload.setEnabled(False)
            self.__text.setEnabled(False)
            self.voice_trans_thread = VoiceTransThread(self.__files)
            self.voice_trans_thread.trans_end.connect(self.voice_trans_end)
            for file in self.__files:
                file.transforming = True
            self.voice_trans_thread.start()

    # 获取打开的文件
    def get_files(self, file):
        self.__files.append(file)

    # 语音转写完成之后退出线程
    def voice_trans_end(self, files):
        self.__files = files
        self.__text.clear()
        self.__text.appendPlainText(self.__files[0].get_file_txt())
        self.__text.repaint()
        self.voice_trans_thread.quit()
        self.__text.setEnabled(True)
        self.__btn_upload.setEnabled(True)

    #点击文件列表的时候，显示选中文件的内容
    def show_file_txt(self, file_name):
        for file in self.__files:
            if file_name == file.file_name:
                break;
        self.__text.clear()
        # 如果文件完成转写，则显示转写的内容，如果还在转写，则显示正在转写中
        if file.finish_transform:
            self.__text.appendPlainText(file.get_file_txt())
        elif file.transforming:
            self.__text.appendPlainText('正在转写中...')
