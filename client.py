#!/usr/bin/python3
# @Time    : 2020/10/26 上午10:50
# @Author  : lovemefan
# @File    : client.py
import time
import os
from socket import socket, AF_INET, SOCK_STREAM
from PyQt5.QtWidgets import *


def send_file(file_name, ip, port):
    """发送文件到服务器"""
    start_time = time.time()

    print(f"[*]正在连接{ip}:{port}")
    clinet = socket(AF_INET, SOCK_STREAM)

    if clinet.connect((ip, port)) == 61:
        QMessageBox(QMessageBox.Warning, '警告', '连接不上服务器').exec()

    file = open(file_name, 'rb')
    while True:
        # 接受套接字的大小
        data = file.read(10*1024*1024)
        clinet.sendall(os.path.basename(file_name).encode('utf-8'))
        time.sleep(0.5)
        if str(data) != "b''":
            clinet.send(data)
            # print(data)  # 此处打印注意被刷屏,仅测试用
        else:
            break
    file.close()
    # 发送成功指令
    clinet.send('upload_finished'.encode())
    # 发送 process 指令 查询进度
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
    return taskid

