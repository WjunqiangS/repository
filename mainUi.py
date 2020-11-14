from PyQt5.QtWidgets import QPushButton, QGridLayout, QWidget, QAction, QMainWindow, QStatusBar
from player import Player
from filelist import FileList
from transform import VoiceTans


class MainGui(QMainWindow):
    """ 窗口主界面

    """
    def __init__(self):
        super().__init__()
        self.__init_control()

    # 初始化控件的位置
    def __init_control(self):

        # 创建语音播放控件、播放列表和语音转写控件
        # 语音转写控件
        self.voice_trans = VoiceTans()
        self.voice_trans.resize(600, 400)
        self.voice_trans.transform_status.connect(self.set_statusbar)

        # 语音播放控件
        self.player = Player()
        self.player.resize(600, 200)
        self.player.position_change.connect(self.voice_trans.on_playing_show)
        self.player.media_changed.connect(self.voice_trans.change_playing_idx)

        # 文件列表控件
        self.file_list = FileList()
        self.file_list.resize(200, 400)
        self.file_list.open_files.connect(self.voice_trans.get_open_files)
        self.file_list.open_files.connect(self.player.set_play_list)
        self.file_list.double_clicked_file.connect(self.player.play_clicked_file)
        self.file_list.double_clicked_file.connect(self.voice_trans.on_btn_voice_trans_clicked)
        self.file_list.clicked_file.connect(self.voice_trans.show_file_txt)

        # 创建语音转写按钮
        self.trans_btn = QPushButton("文件转写")
        self.trans_btn.resize(200, 50)
        self.trans_btn.clicked.connect(self.voice_trans.on_btn_voice_trans_clicked)

        # 创建菜单栏
        self.init_menubar()

        # 创建状态栏
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)

#        # 获取当前显示器的大小，并设置窗口的大小
#        desktop = QApplication.desktop()
#        rect_size = desktop.screenGeometry()
#        width = rect_size.width()
#        self.setMinimumWidth(width * 0.5)

        # 网格布局管理器
        glayout = QGridLayout()
        glayout.setColumnStretch(0, 1)
        glayout.setColumnStretch(1, 3)

        #把控件添加到网格布局管理器中
        glayout.addWidget(self.file_list, 1, 0)
        glayout.addWidget(self.voice_trans, 1, 1)
        glayout.addWidget(self.trans_btn, 2, 0)
        glayout.addWidget(self.player, 2, 1)

        #设置中央控件
        central_widget = QWidget()
        central_widget.setLayout(glayout)
        self.setCentralWidget(central_widget)

    def init_menubar(self):
        # 创建总菜单栏
        menubar = self.menuBar()

        # 创建文件菜单栏
        file_menu = menubar.addMenu('文件')
        # 添加文件菜单栏的选项
        open_file = QAction('打开文件', self)
        open_file.triggered.connect(self.file_list.add_files2list)
        file_menu.addAction(open_file)

        # 创建功能菜单栏
        function_menu = menubar.addMenu('功能')
        # 添加文件菜单栏的选项
        file_trans = QAction('文件转写', self)
        file_trans.triggered.connect(self.voice_trans.on_btn_voice_trans_clicked)
        file_export = QAction('导出转写内容', self)
        file_export.triggered.connect(self.voice_trans.on_btn_export_clicked)
        function_menu.addAction(file_trans)
        function_menu.addAction(file_export)


    def set_statusbar(self, str):
        self.statusbar.showMessage(str)
        self.statusbar.repaint()


