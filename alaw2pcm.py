#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/8 下午2:19
# @Author  : lovemefan
# @File    : alaw2pcm.py

import struct


class WavRead:
    def __init__(self, f):
        self._file = open(f, "rb")
        self._numchannels = 0
        self._samplerate = 0
        self._byterate = 0
        self._bytespersample = 0
        self._bitspersample = 0
        self._samplelength = 0
        self._data = None
        self._audioformat = 0
        self._extraparams = -1
        self.__read()
        self._file.close()

    def getnumofchannels(self):
        return self._numchannels

    def getsamplerate(self):
        return self._samplerate

    def getbyterate(self):
        return self._byterate

    def getbytespersample(self):
        return self._bytespersample

    def getbitspersample(self):
        return self._bitspersample

    def getsamplelength(self):
        return self._samplelength

    def getdata(self):
        return self._data

    def getaudioformat(self):
        return self._audioformat

    def getparams(self):
        params = {}
        params['numchannels'] = self._numchannels
        params['samplerate'] = self._samplerate
        params['byterate'] = self._byterate
        params['bytespersample'] = self._bytespersample
        params['bitspersample'] = self._bitspersample
        params['samplelength'] = self._samplelength
        params['audioformat'] = self._audioformat

        return params

    def __read(self):
        # RIFF header
        riff_chunk_id = self._file.read(4)
        if riff_chunk_id != b'RIFF':
            raise Exception("No RIFF header found")
        riff_chunk_size = struct.unpack('<I', self._file.read(4))[0]

        wave_format = self._file.read(4)
        if wave_format != b"WAVE":
            raise Exception("Not a WAVE file")

        # read fmt chunk
        fmt_chunk_id = self._file.read(4)
        if fmt_chunk_id != b'fmt ':
            raise Exception("fmt chunk missing")

        fmt_chunk_size = struct.unpack('<I', self._file.read(4))[0]
        self._audioformat = struct.unpack('<H', self._file.read(2))[0]
        self._numchannels = struct.unpack('<H', self._file.read(2))[0]
        self._samplerate = struct.unpack('<I', self._file.read(4))[0]
        self._byterate = struct.unpack('<I', self._file.read(4))[0]
        self._bytespersample = struct.unpack('<H', self._file.read(2))[0]
        self._bitspersample = struct.unpack('<H', self._file.read(2))[0]
        if fmt_chunk_size == 18:
            self._extraparams = struct.unpack('<H', self._file.read(2))[0]
            fact_chunk_id = self._file.read(4)
            if fact_chunk_id != b'fact':
                raise Exception("fact chunk missing")

            fact_chunk_size = struct.unpack('<I', self._file.read(4))[0]
            self._samplelength = struct.unpack('<I', self._file.read(4))[0]
        data_chunk_id = self._file.read(4)
        if data_chunk_id != b'data':
            raise Exception("data chunk missing")
        data_chunk_size = struct.unpack('<I', self._file.read(4))[0]
        if self._samplelength == 0:  # no fact chunk
            self._samplelength = data_chunk_size
        self._data = self._file.read(data_chunk_size)

class alaw2pcm:
    def __init__(self, f, channels, samplerate, bitspersample):
        self._file = open(f, "wb")
        self._numofchannels = channels
        self._samplerate = samplerate
        self._bitspersample = bitspersample


    def write(self, rawdata):
        self._file.write(b'RIFF')
        datalength = len(rawdata)

        self._file.write(struct.pack('<L4s4sLHHLLHH4s',
                                     36 + datalength, b'WAVE', b'fmt ', 16,
                                     6, self._numofchannels, self._samplerate,
                                     int(self._numofchannels * self._samplerate * (self._bitspersample / 8)),
                                     int(self._numofchannels * (self._bitspersample / 8)), self._bitspersample,
                                     b'data'))
        self._file.write(struct.pack('<L', datalength))
        self._file.write(rawdata)

    def close(self):
        self._file.close()



if __name__ == '__main__':

    with open('/Users/wangjunqiang/PycharmProjects/GUI_Project/RES/1726026.V3', 'rb') as f:
        raw_data = f.read()
    wave_write = alaw2pcm("/Users/wangjunqiang/PycharmProjects/GUI_Project/RES/1726026.wav", 1, 8000, 8)
    wave_write.write(raw_data)
    # close the file stream and save the file
    wave_write.close()



    # wave_read = WavRead("/home/lovemefan/disk1/lovemefan/语音数据集/录音测试/1726026.V3")
    # wave_read2 = WavRead("/home/lovemefan/disk1/lovemefan/语音数据集/录音测试/1726026.wav")
    # # print parameters like number of channels, sample rate, bits per sample, audio format etc
    # # Audio format 1 = PCM (without compression)
    # # Audio format 6 = PCMA (with A-law compression)
    # # Audio format 7 = PCMU (with mu-law compression)
    # print(wave_read.getparams())
    # print(wave_read2.getparams())
