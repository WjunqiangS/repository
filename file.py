import os


class File():
    def __init__(self, file_path = None):
        self.file_name = os.path.basename(file_path)
        self.file_path = file_path
        self.file_status = ''
        self.file_txt = ''
        self.voice_msg = []

    def set_file_txt(self, string):
        self.file_txt = string

    def get_file_txt(self):
        return self.file_txt

    def get_slice_time(self):
        for dict in self.voice_msg:
            yield

