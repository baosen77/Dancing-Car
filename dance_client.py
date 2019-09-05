###两个参数需要传输，一个是tempo(音乐节奏),代码里的a；一个是res，音量值。###

import _thread
import librosa
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pyaudio
import wave
import os
import time
import socket

input_filename = "input.wav"               # 麦克风采集的语音输入
input_filepath = "D:/"              # 输入文件的path
in_path = input_filepath + input_filename

#RPi's IP
SERVER_IP = "192.168.137.39"
SERVER_PORT = 88

print("Starting socket: TCP...")
server_addr = (SERVER_IP, SERVER_PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    try:
        #print("Connecting to server @ %s:%d..." %(SERVER_IP, SERVER_PORT))
        print("Connecting to server @ %s:%d..." %(SERVER_IP, SERVER_PORT))
        sock.connect(server_addr)
        sock.send(b'request')
        re_mes = sock.recv(512).decode()
        print(re_mes)
        break
    except Exception:
        print("Can't connect to server,try it latter!")
        time.sleep(1)
        continue
print("~wai~")

def get_audio(filepath):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1                # 声道数
    RATE = 44100                # 采样率
    RECORD_SECONDS = 10         # 录音时间
    WAVE_OUTPUT_FILENAME = filepath
    
    while(True):
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
        
        print("*"*10, "开始录音：请在10秒内输入语音")
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
    
        y,sr=librosa.load(filepath,sr=None)
        onset_env=librosa.onset.onset_strength(y,sr=sr,hop_length=512,aggregate=np.median)
        tempo,_=librosa.beat.beat_track(onset_envelope=onset_env,sr=sr)
        #a为将传送给小车的参数
        if(tempo<110):
            a="16"
        elif(tempo<120):
            a="17"
        elif(tempo<135):
            a="18"
        else:
            a="19"
        print("send:"+a)
        sock.send((a).encode("utf-8"))
            
        
       

class SubplotAnimation(animation.TimedAnimation):
    def __init__(self, static=False, path=None):
        """
        音频波形动态显示，实时显示波形
        :param static: 是否为静态模式
        :param path:   wav 文件路径
        """
        self.static = static
        if static and os.path.isfile(path):
            self.stream = wave.open(path)
            self.rate = self.stream.getparams()[2]
            self.chunk = self.rate / 2
            self.read = self.stream.readframes
        else:
            self.rate = 2 ** 16
            self.chunk = 2 ** 12
            p = pyaudio.PyAudio()
            self.stream = p.open(format=pyaudio.paInt16, channels=1, rate=self.rate,
                            input=True, frames_per_buffer=self.chunk)
            self.read = self.stream.read

        fig = plt.figure()
        ax1 = fig.add_subplot(2, 1, 1)
        ax2 = fig.add_subplot(2, 1, 2)

        self.t = np.linspace(0, self.chunk - 1, self.chunk)

        ax1.set_xlabel('t')
        ax1.set_ylabel('x')
        self.line1, = ax1.plot([], [], lw=2)
        ax1.set_xlim(0, self.chunk)
        ax1.set_ylim(-15000, 15000)

        ax2.set_xlabel('hz')
        ax2.set_ylabel('y')
        self.line2, = ax2.plot([], [], lw=2)
        ax2.set_xlim(0, self.chunk)
        ax2.set_ylim(-50, 100)

        # 更新间隔/ms
        interval = int(1000*self.chunk/self.rate)
        animation.TimedAnimation.__init__(self, fig, interval=interval, blit=True)

    def _draw_frame(self, framedata):
        i = framedata
        x = np.linspace(0, self.chunk - 1, self.chunk)
        if self.static:
            # 读取静态wav文件波形
            y = np.fromstring(self.read(self.chunk/2 +1), dtype=np.int16)[:-1]
        else: 
            # 实时读取声频,y值为音量
            y = np.fromstring(self.read(self.chunk), dtype=np.int16)
            a=abs(max(y))
            b=abs(min(y))
            res=max(a,b)
            #之后传输res，即音量值
            #。。。。
        return res         
    
    def new_frame_seq(self):
        return iter(range(self.t.size))

    def _init_draw(self):
        lines = [self.line1, self.line2]
        for l in lines:
            l.set_data([], [])



ani = SubplotAnimation()
_thread.start_new_thread(get_audio,(in_path,))

if re_mes == "Welcome to server!":
  ani = SubplotAnimation()

  while (True):
    t2=t1=time.time()
    while (t2-t1)<1:
        t2=time.time()  
    res=abs(ani._draw_frame(44100))
    if (res<500):
        a="1"
 
    elif (res<800):
        a="2"
    
    elif (res<1200):
        a="3"
       
    elif (res<1500):
        a="4"
       
    elif (res<1800):
        a="5"
     
    elif (res<2100):
        a="6"
          
    elif (res<2500):
        a="7"
           
    elif (res<2900):
        a="8"
       
    elif (res<3400):
        a="9"
       
    elif (res<3900):
        a="10"
        
    elif (res<4500):
        a="11"
    
    elif (res<5000):
        a="12"
       
    elif (res<10000):
        a="13"
   
    elif (res<20000):
        a="14"
      
    elif (res>=20000):
        a="15"
                    
    print("send:"+a)
    sock.send((a).encode("utf-8"))
  sock.close()     