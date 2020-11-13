from PyQt5.QtWidgets import *
from tranformUi import TransformGui
from playerUi import PlayerGui


class MainGui(QMainWindow):
    """ 窗口主界面

    """
    def __init__(self):
        super().__init__()
        self.__init_control()

    # 初始化控件的位置
    def __init_control(self):
        glayout = QGridLayout()

        # 创建语音播放控件和语音转写控件
        self.__transform_gui = TransformGui()
        self.__player_gui = PlayerGui()

        # 创建菜单栏
        self.init_menubar()


        # 把控件添加到相应的位置
        glayout.addWidget(self.__player_gui)
        glayout.addWidget(self.__transform_gui)
        widget_layout = QWidget()
        widget_layout.setLayout(glayout)
        self.setCentralWidget(widget_layout)

        # 获取当前显示器的大小，并设置窗口的大小
        desktop = QApplication.desktop()
        rect_size = desktop.screenGeometry()
        width = rect_size.width()
        self.setMinimumWidth(width * 0.5)

        # 把player的信号与transform的函数绑定
        self.__player_gui.files_signal.connect(self.__transform_gui.get_files)
        self.__player_gui.select_file.connect(self.__transform_gui.show_file_txt)

    def init_menubar(self):
        # 创建总菜单栏
        menubar = self.menuBar()

        # 创建文件菜单栏
        file_menu = menubar.addMenu('文件')
        # 添加文件菜单栏的选项
        open_file = QAction('打开文件', self)
        open_file.triggered.connect(self.__player_gui.on_btn_open_files_clicked)
        file_menu.addAction(open_file)

        # 创建功能菜单栏
        function_menu = menubar.addMenu('功能')
        # 添加文件菜单栏的选项
        file_trans = QAction('文件转写', self)
        file_trans.triggered.connect(self.__transform_gui.on_btn_upload_clicked)
        file_export = QAction('导出转写内容', self)
        file_export.triggered.connect(self.__transform_gui.on_btn_export_clicked)
        function_menu.addAction(file_trans)
        function_menu.addAction(file_export)
