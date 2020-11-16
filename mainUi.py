from PyQt5.QtWidgets import QPushButton, QGridLayout, QWidget, QAction, QMainWindow, QStatusBar, QDialog
from PyQt5.QtCore import QEvent
from player import Player
from filelist import FileList
from transform import VoiceTans
from login import Login


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
        self.voice_trans = VoiceTans(self)
        self.voice_trans.resize(600, 400)

        # 语音播放控件
        self.player = Player(self)
        self.player.resize(600, 200)

        # 播放器安装安装事件过滤器
        self.player.installEventFilter(self)

        # 文件列表控件
        self.file_list = FileList(self)
        self.file_list.resize(200, 400)

        # 绑定语音转写状态信号的槽函数
        self.voice_trans.transform_status.connect(self.set_statusbar)
        self.voice_trans.transform_status.connect(self.file_list.set_file_status)

        # 绑定播放器信号对应的槽函数
        self.player.position_change.connect(self.voice_trans.on_playing_show)
        self.player.media_changed.connect(self.voice_trans.change_playing_idx)
        self.player.media_changed.connect(self.file_list.change_file_list_idx)
        self.player.media_changed.connect(self.voice_trans.show_file_txt)
        self.player.stop_status.connect(self.voice_trans.stop2show_playing_file)

        # 绑定文件列表中信号的槽函数
        self.file_list.open_files.connect(self.voice_trans.get_open_files)
        self.file_list.open_files.connect(self.player.set_play_list)
        self.file_list.double_clicked_file.connect(self.player.play_clicked_file)
        self.file_list.double_clicked_file.connect(self.voice_trans.on_btn_voice_trans_clicked)
        self.file_list.double_clicked_file.connect(self.voice_trans.show_file_txt)
        self.file_list.clicked_file.connect(self.voice_trans.show_file_txt)

        # 创建语音转写按钮
        self.trans_btn = QPushButton("文件转写")
        self.trans_btn.clicked.connect(self.voice_trans.on_btn_voice_trans_clicked)

        # 创建转存文件按钮
        self.save_trans_btn = QPushButton("转写存储")
        self.save_trans_btn.clicked.connect(self.voice_trans.on_btn_export_clicked)

        # 创建菜单栏
        self.init_menubar()

        # 创建状态栏
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)

        # 网格布局管理器
        glayout = QGridLayout()
        glayout.setColumnStretch(0, 1)
        glayout.setColumnStretch(1, 6)

        #把控件添加到网格布局管理器中
        glayout.addWidget(self.file_list, 1, 0)
        glayout.addWidget(self.voice_trans, 1, 1)
        glayout.addWidget(self.trans_btn, 2, 0)
        glayout.addWidget(self.save_trans_btn, 3, 0)
        glayout.addWidget(self.player, 2, 1, 2, -1)

        #设置中央控件
        central_widget = QWidget()
        central_widget.setLayout(glayout)
        self.setCentralWidget(central_widget)


    def init_menubar(self):
        # 创建总菜单栏
        menubar = self.menuBar()

        # 创建用户登陆
        login_menu = menubar.addMenu('登陆')
        usr_login = QAction('用户登陆', self)
        usr_manager_login = QAction('管理员登陆', self)
        usr_login.triggered.connect(self.login_process)
        usr_manager_login.triggered.connect(self.login_process)
        login_menu.addAction(usr_login)
        login_menu.addAction(usr_manager_login)


        # 创建文件菜单栏
        file_menu = menubar.addMenu('文件')
        # 添加文件菜单栏的选项
        open_file = QAction('打开文件', self)
        open_file.triggered.connect(self.file_list.add_files2list)
        file_export = QAction('导出转写内容', self)
        file_export.triggered.connect(self.voice_trans.on_btn_export_clicked)
        file_menu.addAction(open_file)
        file_menu.addAction(file_export)

        # 创建功能菜单栏
        function_menu = menubar.addMenu('功能')
        # 添加文件菜单栏的选项
        file_trans = QAction('文件转写', self)
        file_trans.triggered.connect(self.voice_trans.on_btn_voice_trans_clicked)
        function_menu.addAction(file_trans)


    def set_statusbar(self, files):
        for file in files:
            if file.file_status != 'Success':
                self.statusbar.showMessage('文件正在转写中...')
                return

        self.statusbar.showMessage('文件转写完成...')
        self.statusbar.repaint()

    def login_process(self):
        dlg = Login()
        if dlg.exec() == QDialog.Accepted:
            print('用户名：' + dlg.get_usr_name())
            print('密码：' + dlg.get_passwd())

    # 当点击除了控件的其他位置的时候，设置播放器为焦点
    def mouseReleaseEvent(self, mouse_event):
        self.player.setFocus()

    # 当播放器被点击时，设置为当前焦点
    def eventFilter(self, obj, event):
        if obj == self.player and event.type() == QEvent.MouseButtonPress:
            self.player.setFocus()

        return QDialog.eventFilter(QDialog(), obj, event)
