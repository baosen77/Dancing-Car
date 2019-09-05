# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 16:25:16 2019

@author: dell
"""


import wave
import pyaudio
import numpy
import pylab

input_filename = "input.wav"               # 麦克风采集的语音输入
input_filepath = "D:/"              # 输入文件的path
in_path = input_filepath + input_filename

def get_audio(filepath):
    CHUNK = 256
    FORMAT = pyaudio.paInt16
    CHANNELS = 1                # 声道数
    RATE = 11025                # 采样率
    RECORD_SECONDS = 20          # 录音时间
    WAVE_OUTPUT_FILENAME = filepath
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("*"*10, "开始录音：请在20秒内输入语音")
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
#打开WAV文档，文件路径根据需要做修改
wf = wave.open(in_path, "rb")

#创建PyAudio对象
p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
channels=wf.getnchannels(),
rate=wf.getframerate(),
output=True)
#（采样大小 2B，声道数：1单声道、2立体声，帧率44100，输出）
nframes = wf.getnframes()  #总帧数
framerate = wf.getframerate()   #帧率
channels=wf.getnchannels()
#读取完整的帧数据到str_data中，这是一个string类型的数据
str_data = wf.readframes(nframes)   #nframes
wf.close()


#将波形数据转换为数组
# A new 1-D array initialized from raw binary or text data in a string.
wave_data = numpy.fromstring(str_data, dtype=numpy.short)


#将wave_data数组改为2列，行数自动匹配。在修改shape的属性时，需使得数组的总长度不变。
#wave_data.shape = -1,2

#将数组转置
#wave_data = wave_data.T


#time 也是一个数组，与wave_data[0]或wave_data[1]配对形成系列点坐标

time = numpy.arange(0,nframes)*(1.0/framerate)
sign=[]
i=0
while i<=19:
    floatnum=framerate*i
    intnum=int(floatnum)
    res=(abs(wave_data[intnum]))
    i+=0.5
    if(res>2000):
        sign.append(1)
    elif(res>500):
        sign.append(2)
    else:
        sign.append(3)
        

#绘制波形图

#pylab.plot(time, wave_data)

pylab.subplot(212)

pylab.plot(time, wave_data, c="g")

pylab.xlabel("time (seconds)")

pylab.show()

