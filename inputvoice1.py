# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 17:19:32 2019

@author: dell
"""
import pyaudio
import wave
input_filename = "input.wav"               # 麦克风采集的语音输入
input_filepath = "D:/"              # 输入文件的path
in_path = input_filepath + input_filename

def get_audio(filepath):
    CHUNK = 256
    FORMAT = pyaudio.paInt16
    CHANNELS = 1                # 声道数
    RATE = 11025                # 采样率
    RECORD_SECONDS = 15          # 录音时间
    WAVE_OUTPUT_FILENAME = filepath
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("*"*10, "开始录音：请在15秒内输入语音")
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("*"*10, "录音结束\n")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

get_audio(in_path)
