from PyQt5.QtWidgets import QWidget, QListView, QAbstractItemView, QFileDialog, QMenu, QGridLayout, QLabel
from PyQt5.QtCore import QStringListModel, pyqtSignal, QPoint
from PyQt5.QtGui import QCursor
import os
import re
from alaw2pcm import alaw2pcm
from file import File


class FileList(QWidget):
    clicked_file = pyqtSignal(int)
    double_clicked_file = pyqtSignal(int)
    open_files = pyqtSignal(File)

    def __init__(self, parent = None):
        super(FileList, self).__init__()
        self.init_file_list()
        self.setParent(parent)

    def init_file_list(self):
        gridlayout = QGridLayout()

        # 定义文件列表
        self.__list_files = QListView(self)
        self.__list_files.setMinimumSize(200, 400)
        self.__list_model = QStringListModel()
        self.__list_files.setModel(self.__list_model)
        self.__list_files.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.__list_files.setContextMenuPolicy(3)
        self.__list_files.customContextMenuRequested[QPoint].connect(self.__list_fils_right_key_menu)

        # 连接打开文件列表按键的槽函数
        self.__list_files.clicked.connect(self.__on_list_files_clicked)
        self.__list_files.doubleClicked.connect(self.__on_list_files_doubleclicked)

        gridlayout.addWidget(QLabel("文件列表："), 0, 0)
        gridlayout.addWidget(self.__list_files, 1, 0)

        self.setLayout(gridlayout)

    # 文件列表单击的槽函数
    def __on_list_files_clicked(self, index):
        self.clicked_file.emit(index.row())

    # 文件列表双击的槽函数
    def __on_list_files_doubleclicked(self, index):
        self.double_clicked_file.emit(index.row())

    # 文件列表右键功能，还未完成
    def __list_fils_right_key_menu(self, point):
        menu = QMenu()
        menu.addAction('删除')
        menu.exec_(QCursor.pos())

    #提供给主窗口点打开文件时的槽函数
    def add_files2list(self):
        files_path, file_type = QFileDialog.getOpenFileNames(self, "打开文件", os.getcwd(),
                                                             "V3文件 (*.V3);;wav文件 (*.wav);;", "V3文件 (*.V3)")

        # 把打开的文件都保存到文件列表中
        for str in files_path:
            exist_flag = 0
            for exit_file in self.__list_model.stringList():
                if os.path.basename(str).split('.')[0] == exit_file.split('.')[0]:
                    exist_flag = 1
                    break
            if not exist_flag:
                if re.match('.*\.V3', file_type):
                    with open(str, 'rb') as f:
                        raw_data = f.read()
                    str = os.path.join(os.path.dirname(str), os.path.basename(str).split('.')[0] + '.wav')
                    wave_write = alaw2pcm(str, 1, 8000, 8)
                    wave_write.write(raw_data)
                    wave_write.close()

                file = File(str)
                # 打开文件之后给开始转写发送信号，表示已经拿到文件
                self.open_files.emit(file)
                # 给列表模型增加一行
                self.__list_model.insertRows(self.__list_model.rowCount(), 1)
                # 获取增加行的下标
                index = self.__list_model.index(self.__list_model.rowCount() - 1)
                # 给增加的行设置数据
                self.__list_model.setData(index, file.file_name)

    def change_file_list_idx(self, index):
       model_index = self.__list_model.index(index)
       self.__list_files.setCurrentIndex(model_index)
       self.clicked_file.emit(index)