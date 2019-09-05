#用于演示代码

import cv2
import sys
from keras.models import load_model
import time
import socket
import numpy as np

SERVER_IP = "192.168.137.39"
SERVER_PORT = 1188
model = load_model('F:/my_model2.h5')
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
        print("Can't connect to server,try it later!")
        time.sleep(1)
        continue
print("~wai~")
V=np.zeros([2000,2],dtype = 'float32')
Vc=np.zeros([2,2],dtype = 'float32')
i=0
tag=0
if re_mes == "Welcome to server!":
    
 if __name__ == '__main__':
    
    tracker_type = 'CSRT'
    
    tracker = cv2.TrackerCSRT_create()

    # Read video
    video = cv2.VideoCapture(0)

    # Exit if video not opened.
    if not video.isOpened():
        print("Could not open video")
        sys.exit()


    # Read first frame.
    ok, frame = video.read()

    if not ok:
        print('Cannot read video file')
        sys.exit()

 
    # Define an initial bounding box
    
    #bbox = (600, 400, 200, 200)#这里四个参数分别为 起始坐标xy 和 宽 高

    
    # Uncomment the line below to select a different bounding box

    bbox = cv2.selectROI(frame, False)

 
    # Initialize tracker with first frame and bounding box

    ok = tracker.init(frame, bbox)

    num = 0

    while True:


        # Read a new frame

        ok, frame = video.read()

        if not ok :
            break

        num += 1
        
        # Start timer. cv2.getTickCount()记录电脑启动以来的时钟周期数

        timer = cv2.getTickCount()


        # Update tracker

        ok, bbox = tracker.update(frame)


        # Calculate Frames per second (FPS)
        #cv2.getTickFrequency()得到电脑主频
        #前后相减再除以主频就是代码的运行时间

        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);


        # Draw bounding box

        if ok:

            # Tracking success

            p1 = (int(bbox[0]), int(bbox[1]))

            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))

            cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
            
            x = (p1[0]+p2[0])/2
                
            y = (p1[1]+p2[1])/2
            
            V[i]=(x,y)
            if(i>=3)   :

              #判断是否传输坐标
                 #传送x,y
              print(i)

              Vc=V[i-2:i]-V[i-3:i-1]
              
              Vc.resize(1,4)
              predicted=model.predict(Vc)
              throttle1=str(predicted[0][0]+3)+"d"
              angle1=str(predicted[0][1])+"d"
              print("x: "+str(x)+"   y: "+str(y))
              sock.send((throttle1).encode("utf-8"))
              print("throttle: "+throttle1)
              sock.send((angle1).encode("utf-8"))
              print("angle: "+angle1)
            i=i+1                        
            '''if tag == 1:
    
                predicted=model.predict(V[i-1:i+1])
                throttle1=str(predicted[0][0])+"d"
                angle1=str(predicted[0][0])+"d"
                sock.send((throttle1).encode("utf-8"))
                sock.send((angle1).encode("utf-8"))
                time.sleep(0.03)
                throttle2=str(predicted[1][0])+"d"
                angle2=str(predicted[1][0])+"d"     
                sock.send((throttle2).encode("utf-8"))
                sock.send((angle2).encode("utf-8"))      
                tag=0'''
            '''if tag == 1:
           
                predicted=model.predict(V[i-1:i])
                throttle1=str(predicted[0][0]+3)+"d"
                angle1=str(predicted[0][1])+"d"
                #predicted=model.predict(V)
                #throttle1="1d"
                #angle1="2d"
                sock.send((throttle1).encode("utf-8"))
                print("throttle: "+throttle1)
                sock.send((angle1).encode("utf-8"))
                print("angle: "+angle1)
                tag=0
            else: 
                tag = 1'''
                      

        else:

            # Tracking failure

            cv2.putText(frame, "Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

 

        # Display tracker type on frame

        cv2.putText(frame, tracker_type + " Tracker", (100, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2);

 

        # Display FPS on frame

        cv2.putText(frame, "FPS : " + str(int(fps)), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2);

 

        # Display result

        cv2.imshow("Tracking", frame)

 

        # Exit if ESC pressed

        k = cv2.waitKey(1) & 0xff

        if k == 27: break
        
 cv2.destroyAllWindows()

 video.release()
 sock.close()

