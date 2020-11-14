from PyQt5.QtWidgets import QWidget, QPlainTextEdit, QLineEdit, QPushButton, QGridLayout, QMessageBox, QFileDialog, QLabel
from PyQt5.QtGui import QTextCursor
from voice_transform import VoiceTransThread
from docx import Document
from docx.oxml.ns import qn
from pandas import DataFrame
import os
import re


class VoiceTans(QWidget):
    def __init__(self, parent = None):
        super(VoiceTans, self).__init__()
        self.__files = []
        self.cur_idx = 0
        self.__init_layout()
        self.voice_trans_thread = None
        self.setParent(parent)

    def __init_layout(self):
        # 创建文本区
        self.__text = QPlainTextEdit(self)
        self.__text.setMinimumSize(600, 300)

        # 创建语音对应修改的文本框
        self.__line_text = QLineEdit(self)
        self.__line_text.setMinimumSize(500,30)
        self.__line_text.textChanged.connect(self.on_text_changed)

        #创建保存修改按键
        self.__btn_save = QPushButton('保存修改内容', self)
        self.__btn_save.setEnabled(False)
        self.__btn_save.setMaximumSize(50, 30)
        self.__btn_save.clicked.connect(self.on_btn_save_clicked)

        # 创建布局管理器管理控件
        gridlayout = QGridLayout(self)
        gridlayout.addWidget(QLabel("语音转写区:"), 0 , 0, 1, 2)
        gridlayout.addWidget(self.__text, 1, 0, 1, 2)
        gridlayout.addWidget(self.__line_text, 2, 0)
        gridlayout.addWidget(self.__btn_save, 2, 1)

        self.setLayout(gridlayout)

    def on_btn_save_clicked(self):
        ret = QMessageBox.information(self, '警告', '是否保存文件', QMessageBox.No|QMessageBox.Yes)
        if ret == QMessageBox.Yes:
            return

    # 语音上传转写功能按钮槽函数
    def on_btn_voice_trans_clicked(self):
        if not self.__files:
            QMessageBox(QMessageBox.Warning, '警告', '请打开要转写的语音文件').exec()
        else:
            self.__text.clear()
            self.__text.appendPlainText('正在转写中...')
            self.__text.setEnabled(False)
            self.__btn_save.setEnabled(False)
            self.voice_trans_thread = VoiceTransThread(self.__files)
            self.voice_trans_thread.trans_end.connect(self.voice_trans_end)
            for file in self.__files:
                file.transforming = True
            self.voice_trans_thread.start()

    # 语音转写完成之后退出线程
    def voice_trans_end(self, files):
        # 转写完成之后更新文件的信息
        self.__files = files

        # 设置各个控件的状态
        self.__text.clear()
        self.__text.appendPlainText('语音转写完成')
        self.__text.setEnabled(True)
        self.__btn_save.setEnabled(False)

        # 退出线程
        self.voice_trans_thread.quit()
        self.voice_trans_thread = None

    # 转写内容被修改之后打开保存修改内容按钮
    def on_text_changed(self):
        self.__btn_save.setEnabled(True)

    def on_playing_show(self, position):
        def do_hilght_search(target):
            text = self.__text.toPlainText()
            index = text.find(target[:5])
            if index > 0:
                cursor = self.__text.textCursor()
                cursor.setPosition(index)
                cursor.setPosition(index + len(target), QTextCursor.KeepAnchor)
                self.__text.setTextCursor(cursor)
                self.__text.repaint()

        if not self.__files:
            return
        if self.__files[self.cur_idx]:
            slice_text = self.__files[self.cur_idx].voice_msg
            if slice_text:
                for dict in slice_text:
                    if position >= dict['text_begin'] and position <= dict['text_end']:
                        if self.__line_text.text() != dict['text']:
                            self.__line_text.clear()
                            self.__line_text.setText(dict['text'])
                            self.__line_text.repaint()
                            self.__btn_save.setEnabled(True)
                            do_hilght_search(dict['text'])




    def get_open_files(self, file):
        # 如果发现语音转写线程被开启，则把后面加上文件状态改为正在转写状态
        if self.voice_trans_thread :
            file.transforming = True
        self.__files.append(file)

    # 点击文件列表的时候，显示选中文件的内容
    def show_file_txt(self, index):
        self.cur_idx = index
        # 获取被选中的文件
        self.__files[index]
        self.__text.clear()
        # 如果文件完成转写，则显示转写的内容，如果还在转写，则显示正在转写中
        if self.__files[index].finish_transform:
            self.__text.appendPlainText(self.__files[index].get_file_txt())
        elif self.__files[index].transforming:
            self.__text.appendPlainText('正在转写中...')
        self.__btn_save.setEnabled(False)

    # 转存语音文件按键点击槽函数
    def on_btn_export_clicked(self):
        flag = 0
        for file in self.__files:
            if file.finish_transform:
                flag = 1
                break
        if (not self.__files) or (not flag):
            QMessageBox(QMessageBox.Warning, '警告', '请先转写语音文件').exec()
            return
        file_path, file_type = QFileDialog.getSaveFileName(self,
                                                           "文件保存",
                                                           os.getcwd(), "文档格式 (*.docx);;表格格式 (*.xlsx)")
        if not file_path:
            return
        if re.match('.*\.docx', file_type):
            self.write2doc(file_path)
        else:
            self.write2excel(file_path)

    # 把内容写为docx
    def write2doc(self, path):
        doc = Document()
        doc.styles['Normal'].font.name = u'宋体'
        doc.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')

        for file in self.__files:
            if file.finish_transform:
                doc.add_paragraph(file.file_name)
                doc.add_paragraph(file.get_file_txt())
                doc.add_paragraph('\n')

        doc.save(path)

    # 把内容写为xlsx
    def write2excel(self, path):
        file_name =[]
        trans_content = []
        for file in self.__files:
            if file.finish_transform:
                file_name.append(file.file_name)
                trans_content.append(file.get_file_txt())

        struct = {
            '文件名': file_name,
            '转写内容':trans_content
        }
        pd = DataFrame(struct)
        pd.to_excel(path)
