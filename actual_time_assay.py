# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 08:42:15 2019

@author: dell
"""

import pyaudio
#import tkinter as tk
import wave
import time
import threading
import queue
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
def atual_time_input():
    CHUNK = 1024   #定义数据流块
    FORMAT = pyaudio.paInt16    #16位整型数据？？？？
    CHANNELS = 1  #声道
    RATE = 44100  #采样率
    WAVE_OUTPUT_FILENAME = "D:/output.wav"#文件路径
    Recording=True  #记录音频
    frames=[]       #frames帧数组
    counter=1       #counter标志????
    
    #GUI图形用户界面  GUI接口 
#    class Application(tk.Frame):
#        def __init__(self,master=None):
#            tk.Frame.__init__(self,master)
#            self.grid()
#            self.creatWidgets()
#    
#        def creatWidgets(self):
#            self.quitButton=tk.Button(self,text='quit',command=root.destroy)
#            self.quitButton.grid(column=1,row=3)
#    
#    
    # pyaudio使用这个可以进行录音，播放，生成wav文件等等
    p = pyaudio.PyAudio()
    q = queue.Queue()
    #Queue是构造方法
    
    #调用函数读取数据由调用函数读取改为callback读取, 
    #把数据放在了一个queue里面, 这样子写好之后就不用管他了. 需要数据的之后直接读取这个queue就好
    #另外还包括一个event, ad_rdy_ev也就是数据OK时, 通知处理部分程序用的Event
    def audio_callback(in_data, frame_count, time_info, status):
        global ad_rdy_ev
    
        q.put(in_data)
        ad_rdy_ev.set()
        if counter <= 0:
            return (None,pyaudio.paComplete)
        else:
            return (None,pyaudio.paContinue)
    
    #打开数据流
    stream = p.open(format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            output=False,
            frames_per_buffer=CHUNK,
            stream_callback=audio_callback)
    
    
    if Recording:#####并没有被执行！！！！！！！！！
        #只读方式打开wav文件
        print("recording:")
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
    
    
    print("Start Recording")
    stream.start_stream()
    
    #processing block
    count=0
    window = signal.hamming(CHUNK)
    sign=0
    #数据处理
    def read_audio_thead(q,stream,frames,ad_rdy_ev):
        global rt_data
        
        while stream.is_active():#????????????
            #print("Stream is active.")
            
            ad_rdy_ev.wait(timeout=1000)
            if not q.empty():
                #process audio data here
                data=q.get()
             #   print("data:",data)
                while not q.empty():
                    q.get()
               
                rt_data = np.frombuffer(data,np.dtype('<i2'))  #i2——int16
                rt_data = rt_data * window
                t1=time.time()
                t2=t1=time.time()
                
                while((t2-t1)<0.5):
                    t2=time.time()
                global count
                global sign
    #            music.append(abs(rt_data[512]))
                
                if(abs(rt_data[512])<=1000):
                    sign=1
                elif((abs(rt_data[512])<=4000)&(abs(rt_data[512])>1000)):
                    sign=2
                else:
                    sign=3
                if Recording :
                    frames.append(data)
    #            print("data:",data)
            ad_rdy_ev.clear()
    ad_rdy_ev=threading.Event()
    
    t=threading.Thread(target=read_audio_thead,args=(q,stream,frames,ad_rdy_ev))
    
    t.daemon=True
    t.start()
    
    #可删除
    plt.show()
    root=tk.Tk()
    app=Application(master=root)
    app.master.title("Test")
    app.mainloop()
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    print("* done recording")
    if Recording:
        wf.writeframes(b''.join(frames))
        wf.close()
    return sign


    