from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QFileDialog, QListView, QAbstractItemView
from PyQt5.QtCore import QStringListModel


class FuncButtons(QWidget):
    def __init__(self):
        super(FuncButtons, self).__init__()
        self.__init_control()

    def __init_control(self):
        vlayout = QVBoxLayout()
        self.__btn_upload = QPushButton('上传文件')
        self.__btn_open_files = QPushButton('打开文件')
        self.__list_files = QListView()
        self.__list_files.setEditTriggers(QAbstractItemView.NoEditTriggers)

        vlayout.addWidget(self.__btn_upload)
        vlayout.addWidget(self.__btn_open_files)
        vlayout.addWidget(self.__list_files)

        self.btn_count = vlayout.count()
        self.setLayout(vlayout)

        self.__btn_open_files.clicked.connect(self.on_btn_open_files_clicked)
        self.__btn_upload.clicked.connect(self.on_btn_upload_clicked)
        self.__list_files.clicked.connect(self.on_list_files_cliked)

    def on_btn_upload_clicked(self):
        files = QFileDialog.getOpenFileNames(self, '选择文件',
                                             '/Users/wangjunqiang/PycharmProjects/GUI_Project', 'All Files (*);;')


    def on_btn_open_files_clicked(self):
        files = QFileDialog.getOpenFileNames(self, '打开文件',
                                             '/Users/wangjunqiang/PycharmProjects/GUI_Project', 'All Files (*);;')

        self.files = list(files)[:-1][0]

        slm = QStringListModel()
        slm.setStringList(self.files)

        self.__list_files.setModel(slm)

    def on_list_files_cliked(self, index):
        print(self.files[index.row()])
