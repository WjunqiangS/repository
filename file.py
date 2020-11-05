import os

class File():
    def __init__(self, file_name = None, file_path = None):
        self.file_name = file_name
        self.file_path = file_path
        self.finish_transform = False
        self.file_txt = ''
        self.full_path = os.path.join(file_path, file_name)

    def set_file_txt(self, string):
        self.file_txt = string

    def set_file_name(self, name):
        self.file_name = name

    def set_file_path(self, path):
        self.file_path = path

    def get_file_txt(self):
        return self.file_txt
