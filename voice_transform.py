from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import pyqtSignal, QThread
import time
import json
import requests
from socket import socket, AF_INET, SOCK_STREAM
import os


class VoiceTransThread(QThread):
    trans_end = pyqtSignal(list)

    def __init__(self, files = None):
        super(VoiceTransThread, self).__init__()
        self.files = files

    def run(self):
        for file in self.files:
            if not file.finish_transform:
                self.get_txt_data(file)

        # 转写完成之后发出停止信号，并且把转写好的文件发送
        self.trans_end.emit(self.files)

    def get_txt_data(self, file):
        ip = "speech.yuntrans.cn"
        port = 5002
        taskid = self.send_file(file.file_path, ip, port).decode('utf-8')
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
                    file.set_file_txt(json.loads(res.text)['result']['tasks_info'][0]['task_result']['result'][0])
                    for i in json.loads(res.text)['result']['tasks_info'][0]['task_result']['detailed_result']:
                        text = i['res'][0]
                        text_begin = i['begin_time']
                        text_end = i['end_time']
                        file.voice_msg.append({'text':text, 'text_begin': text_begin, 'text_end': text_end})
                    file.finish_transform = True
                    break
                elif json.loads(res.text)['task_status'] == "Running":
                    print(f"{file.file_path}正在上传中...")
                elif json.loads(res.text)['task_status'] == "Failure":
                    QMessageBox(QMessageBox.Warning, '警告', '上传失败').exec()
                    self.trans_end.emit([])
                    file.transforming = False
                    break
            except Exception as e:
                QMessageBox(QMessageBox.Warning, '警告', '上传失败').exec()
                self.trans_end.emit([])
                file.transforming = False
            time.sleep(1)
        file.transforming = False

    def send_file(self, file_name, ip, port):
        """发送文件到服务器"""
        start_time = time.time()

        print(f"[*]正在连接{ip}:{port}")
        clinet = socket(AF_INET, SOCK_STREAM)

        try:
            clinet.connect((ip, port))
        except ConnectionRefusedError:
            QMessageBox(QMessageBox.Warning, '警告', '连接不上服务器').exec()
            self.trans_end.emit([])
        except ConnectionRefusedError:
            QMessageBox(QMessageBox.Warning, '警告', '连接不上服务器').exec()
            self.trans_end.emit([])


        file = open(file_name, 'rb')
        while True:
            # 接受套接字的大小
            data = file.read(10*1024*1024)
            clinet.sendall(os.path.basename(file_name).encode('utf-8'))
            time.sleep(2)
            if str(data) != "b''":
                clinet.send(data)
                # print(data)  # 此处打印注意被刷屏,仅测试用
            else:
                break
        file.close()
        # 发送成功指令
        clinet.send('upload_finished'.encode())
        # 发送 process 指令 查询进度
        try:
            commd = clinet.recv(1024)
            print(commd.decode('utf-8'))
            if commd == b"down_load_finished":
                print("正在上传中...")
                taskid = clinet.recv(1024)
                print()
                print(taskid.decode('utf-8'))
            clinet.close()
            print("[*]连接已关闭,等待重新连接")
            end_time = time.time()
            AlL_time = end_time - start_time
            print(f"已经运行{round(AlL_time, 1)}s")
        except Exception:
            QMessageBox(QMessageBox.Warning, '警告', '接受数据出错').exec()
            self.trans_end.emit([])
        return taskid

