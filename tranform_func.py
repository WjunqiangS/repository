from PyQt5.QtWidgets import *
from client import  send_file
import requests
import time
import json


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
            for file in self.__files:
                self.__text.appendPlainText(file.full_path)
                self.__text.repaint()

    # 让转写语音的控件获取打开的文件
    def get_files(self, files):
        self.__files = files

    def get_txt_data(self, file_path):
        ip = "speech.yuntrans.cn"
        port = 5002
        taskid = send_file(file_path, ip, port).decode('utf-8')
        print(taskid)
        # taskid = '45972493eab64466861d9db77b4311b6'
        header = {'Content-Type': 'application/json'}
        while True:

            url = f"http://speech.yuntrans.cn:5003/process?taskid={taskid}"
            print(url)
            try:
                # if you not sleep you will gat 500 error
                time.sleep(1)
                res = requests.get(url, headers=header)

                # res 为 json 格式， 例子如下：
                # {'task_status': 'Success', 'task_result': {'result': ['那就行了啊，这个样子，你说你说你说那个那个把把把人家拿一个什么什么的话，你就不知道你不知道这个人是不是还想想想想想。不是不是不是不是不是我的，人家说你想想想想想想想想想想点点点点点起来就想起来一个小时候就是不是不是不是不是不是十分钟多多多多多多多点点，你要不要把要不要讲哎？你给我打电话给你自己可以来给你打电话。走走走走走走了。这样的话就是这样一个这个这个叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫想起来了，下一个下一个来来来来来来来来来来。好吧，那个是哪个人？'], 'detailed_result': [{'res': ['那就行了啊，这个样子，你说你说你说那个那个把把把人家拿一个什么什么的话，你就不知道你不知道这个人是不是还想想想想想。'], 'end_time': 8780, 'begin_time': 140, 'words_info': [], 'sn': '862681538521604562375', 'corpus_no': '6891542926155788442'}, {'res': ['不是不是不是不是不是我的，人家说你想想想想想想想想想想点点点点点起来就想起来一个小时候就是不是不是不是不是不是十分钟多多多多多多多点点，你要不要把要不要讲哎？你给我打电话给你自己可以来给你打电话。'], 'end_time': 20180, 'begin_time': 9380, 'words_info': [], 'sn': '672523470511604562375', 'corpus_no': '6891542926200247485'}, {'res': ['走走走走走走了。'], 'end_time': 26375, 'begin_time': 24400, 'words_info': [], 'sn': '244242383971604562375', 'corpus_no': '6891542925736041325'}, {'res': ['这样的话就是这样一个这个这个叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫叫想起来了，下一个下一个来来来来来来来来来来。'], 'end_time': 33840, 'begin_time': 26600, 'words_info': [], 'sn': '395234329791604562375', 'corpus_no': '6891542926489307643'}, {'res': ['好吧，那个是哪个人？'], 'end_time': 42290, 'begin_time': 40100, 'words_info': [], 'sn': '893333468411604562375', 'corpus_no': '6891542926354232239'}], 'corpus_no': '6891542926155788442'}, 'task_id': '5fa3adbe1282a44cad3b91d8'}
                # task_status 有三种结果 Success（上传成功）,Running(正在上传), Failure（上传失败）
                if json.loads(res.text)['task_status'] == "Success":
                    # 得到结果
                    print(json.loads(res.text))
                    break
                elif json.loads(res.text)['task_status'] == "Running":
                    print(f"{file_path}正在上传中...")
                elif json.loads(res.text)['task_status'] == "Failure":
                    print(f"{file_path}上传失败")
                    break
            except Exception as e:
                print(e.__cause__)
            time.sleep(1)
