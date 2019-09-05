#建立数据集的代码

import cv2
import sys
import math

if __name__ == '__main__':
    
    tracker_type = 'CSRT'
    
    tracker = cv2.TrackerCSRT_create()

    # Read video
    video = cv2.VideoCapture('C:/Users/hp/Desktop/skate.mp4')

    videofps = video.get(cv2.CAP_PROP_FPS)


    # Exit if video not opened.
    if not video.isOpened():
        print("Could not open video")
        sys.exit()


    # Read first frame.
    ok, frame = video.read()

    if not ok:
        print('Cannot read video file')
        sys.exit()


    #这里四个参数分别为 起始坐标xy 和 宽 高
    #skate视频，较好的三个值（731,448,53,60）大正、（718,479,39,116）长、（744,451,42,40）小正
    #bbox = (650, 20,115, 80)
    #bbox=(669,20,112,78)
    
    
    # Define an initial bounding box

    bbox = cv2.selectROI(frame, False)

 
    # Initialize tracker with first frame and bounding box

    ok = tracker.init(frame, bbox)

    num = 0

    x=0

    y=0

    detax = []
    
    detay = []

    locationx = []

    locationy = []

    
    #时刻
    timepoint = [0,41,91,141,191,241,292,342,392,445,494,548,594,651,695,754,798,863,898,956,998,1048,1098,1149,1199,1249,1299,1349,1400,1450,1504,1550,1612,1654,1718,1760,1825,1860,1911,1961,2011,2060,2111,2161,2211,2261,2311,2364,2413,2468,2514,2576,2663,2835,2970,3020,3071,3121,3171,3221,3271,3322,3371,3433,3476,3536,3580,3640,3684,3745,3789,3852,3896,3960,3996,4058,4097,4155,4196,4258,4297,4347,4397,4447,4497,4547,4599,4648,4703,4749,4808,4851,4917,4951,5012,5051,5111,5152,5202,5252,5303,5352,5403,5453,5504,5564,5614,5668,5713,5780,5813,5877,5913,5970,6012,6062,6113,6164,6214,6263,6313,6364,6428,6468,6531,6568,6620,6667,6718,6768,6820,6869,6919,6969,7020,7070,7120,7170,7220,7270,7321,7373,7423,7477,7542,7581,7685,7698,7748,7798,7848,7902,7952,8014,8052,8102,8152,8202,8252,8334,8365,8404,8455,8504,8554,8605,8661,8705,8761,8814,8856,8906,8957,9006,9057,9106,9157,9207,9267,9307,9368,9407,9458,9512,9562,9617,9662,9716,9762,9812,9862,9913,9963,10023,10064,10122,10163,10213,10264,10316,10364,10414,10473,10515,10577,10619,10682,10719,10769,10819,10869,10920,10969,11023,11073,11131,11175,11239,11276,11334,11376,11426,11476,11526,11576,11626,11679,11729,11782,11832,11886,11932,11993,12036,12097,12141,12206,12242,12304,12342,12400,12442,12492,12542,12592,12677,12693,12744,12794,12848,12897,12961,13002,13065,13109,13171,13214,13277,13315,13365,13414,13465,13515,13566,13616,13666,13718,13768,13827,13875,13928,13973,14037,14073,14131,14174,14224,14274,14324,14374,14424,14474,14524,14581,14626,14690,14733,14796,14833,14895,14933,14984,15034,15084,15134,15184,15234,15284,15339,15388,15443,15488,15548,15589,15654,15689,15740,15790,15840,15890,15940,15990,16040,16090,16141,16195,16241,16297,16343,16408,16443,16498,16543,16593,16644,16693,16744,16794,16844,16894,16947,16997,17052,17097,17152,17197,17247,17297,17347,17398,17448,17506,17549,17599,17690,17703,17753,17802,17855,17907,17957,18010,18070,18114,18159,18209,18259,18341,18372,18414,18464,18514,18564,18614,18666,18714,18764,18814,18865,18915,18967,19015,19067,19120,19174,19220,19270,19320,19370,19424,19471,19529,19577,19635,19683,19741,19784,19841,19884,19934,19984,20035,20085,20139,20193,20246,20303,20345,20392,20442,20492,20542,20592,20642,20692,20743,20793,20854,20901,20962,21002,21052,21102,21152,21207,21253,21308,21352,21403,
                 21454,21507,21554,21611,21658,21714,21760,21821,21866,21925,21967,22025,22067,
                 22117,22167,22217,22268,22317,22372,22418,22471,22518,22569,22618,22706,22718,
                 22778,22819,22869,22919,22969,23019,23069,23119,23170,23223,23273,23328,23374,
                 23431,23474,23537,23580,23643,23680,23738,23781,23831,23881,23931,23981,24031,
                 24081,24131,24184,24233,24291,24335,24400,24435,24485,24535,24585,24636,24686,
                 24736,24786,24836,24886,24943,24987,25051,25093,25159,25193,25249,25293,25344,25394,25444,25494,25544,25594,25644,25696,25745,25801,25846,25901,25947,26011,26052,26117,26158,26220,26261,26325,26362,26412,26462,26512,26563,26612,26662,26713,26763,26813,26866,26915,26970,27016,27069,27116,27166,27216,27266,27316,27366,27416,27466,27534,27570,27620,27706,27720,27770,27820,27870,27925,27971,28061,28078,28128,28178,28228,28278,28388,28399,28448,28498,28547,28597,28648,28699,28749,28803,28851,28907,28952,29012,29053,29108,29158,29210,29259,29310,29359,29410,29460,29510,29561,29611,29662,29711,29768,29815,29875,29920,29979,30026,30085,30132,30183,30233,30286,30336,30390,30436,30489,30536,30587,30638,30688,30741,30789,30850,30889,30939,30989,31039,31090]
    
    timepoint1 = [int(i*videofps/1000) for i in timepoint]

    timepoint1[0] = 1
    
    
    while True:

        x0 = x

        y0 = y

        # Read a new frame

        ok, frame = video.read()

        num += 1

        if not ok :
            break
        
        
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

            if num in timepoint1:

                x = (p1[0]+p2[0])/2
                
                y = (p1[1]+p2[1])/2

                locationx.append(x)

                locationy.append(y)

                detax.append(x-x0)

                detay.append(y-y0)
            

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

'''
del detax[0]

del detay[0]

del locationx[0]

del locationx[0]

del locationy[0]

del locationy[0]
'''

locationlists = []

detalists = []

for a,b in zip(locationx,locationy):
    dimension = (a,b)
    locationlists.append(dimension)

for m,n in zip(detax,detay):
    bala = (m,n)
    detalists.append(bala)
    

data=input('>>>:')

if data == '1':

    
    file = open('C:/Users/hp/Desktop/locationskate.txt',mode='w')

    hhhh = open('C:/Users/hp/Desktop/detaskate.txt',mode='w')

    #llll = open('C:/Users/hp/Desktop/detastop.txt',mode='a')

    for i in locationlists:
        file.writelines(str(i))
        file.write(',')

        
    for i in detalists:
        hhhh.writelines(str(i))
        hhhh.write(',')
    '''
    for i in detalists:
        llll.writelines(str(i))
        llll.write(',')
    '''
    
    file.close()
    hhhh.close()
    #llll.close()
    
    print(locationlists[0])

    print('time:',len(timepoint))

    print('location:',len(locationlists))

    print('deta:',len(detalists))

    print(len(timepoint)-len(locationlists))
    

else :
    print('not okay!')


'''
for x,y in zip(row,column):
    juli.append(round(math.hypot(abs(x),abs(y)),3))

for a,b in zip(row,column):
    if a==0:
        if b>0:
            jiaodu.append(1.571)
        if b<0:
            jiaodu.append(-1.571)
            
    elif a<0 and b>0:
        res = 1.571-math.atan(b/a)
        jiaodu.append(round(res,3))
    
    elif a<0 and b<0:
        res1 = 4.712-math.atan(b/a)
        jiaodu.append(round(res1,3))
        
    else:
        jiaodu.append(round(math.atan(b/a),3))
    

print(juli)
print(jiaodu)
'''

