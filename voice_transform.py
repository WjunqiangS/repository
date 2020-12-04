import struct

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
            if file.file_status == 'Success':
                continue
            else:
                file.file_status = 'Running'
                ret = self.get_txt_data(file)
                if file.file_status == 'Failure':
                   continue
                time.sleep(2)

            if isinstance(ret, str):
                self.trans_end.emit(list(ret))
                return

        # 转写完成之后发出停止信号，并且把转写好的文件发送
        self.trans_end.emit(self.files)

    def get_txt_data(self, file):
        ip = "speech.yuntrans.cn"
        port = 5002
        taskid = self.send_file(file.file_path, ip, port)
        header = {'Content-Type': 'application/json'}
        while True:
            url = f"http://speech.yuntrans.cn:5003/process?taskid={taskid}"
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
                    file.file_status = json.loads(res.text)['task_status']
                    return 0
                elif json.loads(res.text)['task_status'] == "Running":
                    file.file_status = json.loads(res.text)['task_status']
                elif json.loads(res.text)['task_status'] == "Failure":
                    file.file_status = json.loads(res.text)['task_status']
                    return '文件转写失败'
            except Exception as e:
                print(e)
                return '语音转写传输失败'
            time.sleep(1)

    def send_file(self, file_path, ip, port):
        # 获取文件
        # 如果文件不存在
        if not os.path.exists(file_path):
            print('文件不存在')
            return '文件不存在'

        """发送文件到服务器"""
        # 循环读入文件大小
        file_read_size = 10 * 1024 * 1024

        # 客户端连接服务端用到的 Socket 服务
        client = socket(AF_INET, SOCK_STREAM)
        try:
            # 连接 Socket 服务端
            client.connect((ip, port))
        except Exception as e:
            print(e)
            client.close()
            return '连接服务器失败'
        # 获取文件名
        file_name = os.path.basename(file_path)

        # 获取文件大小
        size = os.path.getsize(file_path)

        # 文件信息
        hander = {
            'file_name': file_name,
            'length': size,
            'file_read_size': file_read_size,
        }

        # 报头序列化
        hander_json = json.dumps(hander)

        # 报头bytes转换
        hander_bytes = hander_json.encode('utf-8')

        # 报头长度固定
        s_hander = struct.pack('i', len(hander_bytes))
        try:
            # 传输报头长度
            client.send(s_hander)

            # 传输报头数据
            client.send(hander_bytes)
        except Exception as e:
            print(e)
            client.close()
            return '发送文件头数据失败'

        # 以二进制 binary 读取文件
        with open(file_path, 'rb') as f:
            # 读入文件
            times = 0  # 正在发送的进度
            while (True):
                temp_date = bytes()
                temp_date += f.read(file_read_size)
                if (len(temp_date) > 0):
                    # 传输文件数据
                    client.send(temp_date)
                    times += 1
                else:
                    break

            # 接收返回信息
            taskid = client.recv(1024).decode('utf-8')

            client.close()

            return taskid

