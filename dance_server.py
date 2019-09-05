#!/usr/bin/python
 
import time
import math
import smbus
import socket

class PCA9685:
 
  # Registers/etc.
  __SUBADR1            = 0x02
  __SUBADR2            = 0x03
  __SUBADR3            = 0x04
  __MODE1              = 0x00
  __PRESCALE           = 0xFE
  __LED0_ON_L          = 0x06
  __LED0_ON_H          = 0x07
  __LED0_OFF_L         = 0x08
  __LED0_OFF_H         = 0x09
  __ALLLED_ON_L        = 0xFA
  __ALLLED_ON_H        = 0xFB
  __ALLLED_OFF_L       = 0xFC
  __ALLLED_OFF_H       = 0xFD
 
  def __init__(self, address=0x40, debug=False):
    self.bus = smbus.SMBus(1)
    self.address = address
    self.debug = debug
    if (self.debug):
      print("Reseting PCA9685")
    self.write(self.__MODE1, 0x00)
 
  def write(self, reg, value):
    "Writes an 8-bit value to the specified register/address"
    self.bus.write_byte_data(self.address, reg, value)
    if (self.debug):
      print("I2C: Write 0x%02X to register 0x%02X" % (value, reg))
 
  def read(self, reg):
    "Read an unsigned byte from the I2C device"
    result = self.bus.read_byte_data(self.address, reg)
    if (self.debug):
      print("I2C: Device 0x%02X returned 0x%02X from reg 0x%02X" % (self.address, result & 0xFF, reg))
    return result
 
  def setPWMFreq(self, freq):
    "Sets the PWM frequency"
    prescaleval = 25000000.0    # 25MHz
    prescaleval /= 4096.0       # 12-bit
    prescaleval /= float(freq)
    prescaleval -= 1.0
    if (self.debug):
      print("Setting PWM frequency to %d Hz" % freq)
      print("Estimated pre-scale: %d" % prescaleval)
    prescale = math.floor(prescaleval + 0.5)
    if (self.debug):
      print("Final pre-scale: %d" % prescale)
 
    oldmode = self.read(self.__MODE1);
    newmode = (oldmode & 0x7F) | 0x10        # sleep
    self.write(self.__MODE1, newmode)        # go to sleep
    self.write(self.__PRESCALE, int(math.floor(prescale)))
    self.write(self.__MODE1, oldmode)
    time.sleep(0.005)
    self.write(self.__MODE1, oldmode | 0x80)
 
  def setPWM(self, channel, on, off):
    "Sets a single PWM channel"
    self.write(self.__LED0_ON_L+4*channel, on & 0xFF)
    self.write(self.__LED0_ON_H+4*channel, on >> 8)
    self.write(self.__LED0_OFF_L+4*channel, off & 0xFF)
    self.write(self.__LED0_OFF_H+4*channel, off >> 8)
    if (self.debug):
      print("channel: %d  LED_ON: %d LED_OFF: %d" % (channel,on,off))
 
  def setServoPulse(self, channel, pulse):
    "Sets the Servo Pulse,The PWM frequency must be 50HZ"
    pulse = pulse*4096/20000        #PWM frequency is 50HZ,the period is 20000us
    self.setPWM(channel, 0, pulse)


#RPi's IP
#define host ip: Rpi's IP
HOST_IP = "192.168.137.39"
HOST_PORT = 88
print("Starting socket: TCP...")
#1.create socket object:socket=socket.socket(family,type)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("TCP server listen @ %s:%d!" %(HOST_IP, HOST_PORT) )
host_addr = (HOST_IP, HOST_PORT)
#2.bind socket to addr:socket.bind(address)
sock.bind(host_addr)
#3.listen connection request:socket.listen(backlog)
sock.listen(1)
#4.waite for client:connection,address=socket.accept()

# ============================================================================
# Raspi PCA9685 16-Channel PWM Servo Driver
# ============================================================================
pwm = PCA9685(0x40, debug=True)
pwm.setPWMFreq(50)
d=1575
z=1686
   
while True:
     
     connection,address = sock.accept()
     Building_connection = connection.recv(1024)
     print(Building_connection)
     if Building_connection == b"request":
          print("connection is ok!")
          connection.send(b'Welcome to server!')   
     
     while Building_connection==b"request":
            a=connection.recv(1024)
            if a == b"exit":
               connection.send(b"close")
               break
            if a !=b"request"and a:
                if a=='1':                    
                  print((a).decode())
                  d = 1757
                  z = 1686
                  
                
                elif  a=='2':
                  print((a).decode())
                  d = 1840
                  z = 1786
                  
                 
                elif  a=='3':
                  print((a).decode())
                  d = 1840
                  z = 1586
               
                                   
                elif  a=='4':
                  pwm.setServoPulse(0,1757)
                  time.sleep(0.06)                      
                  print((a).decode())
                  d = 1570
                  z = 1786
                                  
                elif  a=='5':
                  pwm.setServoPulse(0,1757)
                  time.sleep(0.06)                      
                  print((a).decode())
                  d = 1575
                  z = 1586
                                 
                elif  a=='6':
                  print((a).decode())
                  d = 1842
                  z = 1986
                
                                   
                elif  a=='7':
                  print((a).decode())
                  d = 1842
                  z = 1386
              
                
                elif  a=='8':
                  pwm.setServoPulse(0,1757)
                  time.sleep(0.06)                      
                  print((a).decode())
                  d = 1565
                  z = 1986
                                   
                elif  a=='9':
                  pwm.setServoPulse(0,1757)
                  time.sleep(0.06)                      
                  print((a).decode())
                  d = 1565
                  z = 1386
                         
                elif  a=='10':
                  print((a).decode())
                  d = 1845
                  z = 2186
                 
                  dj = 880                 
                elif  a=='11':
                  print((a).decode())
                  d = 1845
                  z = 1186
                
                  dj = 880               
                elif  a=='12':
                  pwm.setServoPulse(0,1757)
                  time.sleep(0.06)                      
                  print((a).decode())
                  d = 1565
                  z = 2186
                              
                elif  a=='13':
                  pwm.setServoPulse(0,1757)
                  time.sleep(0.06)                      
                  print((a).decode())
                  d = 1560
                  z = 1186    
                                 
                elif  a=='14':
                  pwm.setServoPulse(0,1757)
                  time.sleep(0.06)                 
                  print((a).decode())
                  d = 1560
                  z = 1686
                 
                  dj = 1470                  
                elif  a=='15':
                  print((a).decode())
                  d = 1848
                  z = 1686                     
                             
                elif a=='16':
                       print((a).decode())
                       print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")                       
                       pwm.setServoPulse(12,2200) 
                       pwm.setServoPulse(13,660)     
                       pwm.setServoPulse(14,1860)
                       pwm.setServoPulse(15,1560)
                       for i in range(930,1830,10):  
                         pwm.setServoPulse(12,i) 
                         pwm.setServoPulse(13,2860-i)
                         time.sleep(0.02)         
                       for i in range(1830,930,10):  
                         pwm.setServoPulse(12,i) 
                         pwm.setServoPulse(13,2860-i)
                         time.sleep(0.02)     
                       pwm.setServoPulse(12,2200) 
                       pwm.setServoPulse(13,660)     
                       pwm.setServoPulse(14,1500)
                       pwm.setServoPulse(15,1530)                        
                elif a=='17':   
                   print((a).decode())  
                   print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")                   
                   for i in range(1630,2230,10):  
                       pwm.setServoPulse(12,i) 
                       pwm.setServoPulse(13,2860-i)
                       time.sleep(0.02)         
                   for i in range(2230,1630,10):  
                       pwm.setServoPulse(12,i) 
                       pwm.setServoPulse(13,2860-i)
                       time.sleep(0.02)
                   for i in range(1630,2230,10):  
                       pwm.setServoPulse(12,i) 
                       pwm.setServoPulse(13,2860-i)
                       time.sleep(0.02)         
                   for i in range(2230,1630,10):  
                       pwm.setServoPulse(12,i) 
                       pwm.setServoPulse(13,2860-i)
                       time.sleep(0.02) 
                   for i in range(1630,2230,10):  
                       pwm.setServoPulse(12,i) 
                       pwm.setServoPulse(13,2860-i)
                       time.sleep(0.02)         
                   for i in range(2230,1630,10):  
                       pwm.setServoPulse(12,i) 
                       pwm.setServoPulse(13,2860-i)
                       time.sleep(0.02)        
                   pwm.setServoPulse(12,2200) 
                   pwm.setServoPulse(13,660)     
                   pwm.setServoPulse(14,1500)
                   pwm.setServoPulse(15,1530)
                elif a=='18':   
                  print((a).decode())
                  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                  for i in range(1300,1700,15):  
                       pwm.setServoPulse(12,i)
                       pwm.setServoPulse(13,2860-i)
                       pwm.setServoPulse(14,i)
                       pwm.setServoPulse(15,2*i-1750)
                       time.sleep(0.02)         
                  for i in range(1700,1300,-15):  
                       pwm.setServoPulse(14,i)
                       pwm.setServoPulse(15,2*i-1750)
                       time.sleep(0.02)     
                  for i in range(1300,1700,15):  
                       pwm.setServoPulse(12,i)
                       pwm.setServoPulse(13,2860-i)
                       pwm.setServoPulse(14,i)
                       pwm.setServoPulse(15,2*i-1750)
                       time.sleep(0.02)         
                  for i in range(1700,1300,-15):  
                       pwm.setServoPulse(14,i)
                       pwm.setServoPulse(15,2*i-1750)
                       time.sleep(0.02) 
                  for i in range(1300,1700,15):  
                       pwm.setServoPulse(12,i)
                       pwm.setServoPulse(13,2860-i)
                       pwm.setServoPulse(14,i)
                       pwm.setServoPulse(15,2*i-1750)
                       time.sleep(0.02)         
                  for i in range(1700,1300,-15):  
                       pwm.setServoPulse(14,i)
                       pwm.setServoPulse(15,2*i-1750)
                       time.sleep(0.02) 
                  pwm.setServoPulse(12,2200) 
                  pwm.setServoPulse(13,660)     
                  pwm.setServoPulse(14,1500)
                  pwm.setServoPulse(15,1530)                       
                elif a=='19':   
                  print((a).decode())
                  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                  for i in range(2130,730,-20):  
                       pwm.setServoPulse(12,i)
                       pwm.setServoPulse(13,i)
                       pwm.setServoPulse(14,1500)     
                       pwm.setServoPulse(15,i)                       
                       time.sleep(0.02)                    
                  for i in range(730,2130,20):  
                       pwm.setServoPulse(12,i)
                       pwm.setServoPulse(13,i)
                       pwm.setServoPulse(14,1500)
                       pwm.setServoPulse(15,i) 
                       time.sleep(0.02)                         
                  for i in range(2130,730,-20):  
                       pwm.setServoPulse(12,i)
                       pwm.setServoPulse(13,i)
                       pwm.setServoPulse(14,1500)     
                       pwm.setServoPulse(15,i)                       
                       time.sleep(0.02)                    
                  for i in range(730,2130,20):  
                       pwm.setServoPulse(12,i)
                       pwm.setServoPulse(13,i)
                       pwm.setServoPulse(14,1500)
                       pwm.setServoPulse(15,i) 
                       time.sleep(0.02) 
                  for i in range(2130,730,-20):  
                       pwm.setServoPulse(12,i)
                       pwm.setServoPulse(13,i)
                       pwm.setServoPulse(14,1500)     
                       pwm.setServoPulse(15,i)                       
                       time.sleep(0.02)                    
                  for i in range(730,2130,20):  
                       pwm.setServoPulse(12,i)
                       pwm.setServoPulse(13,i)
                       pwm.setServoPulse(14,1500)
                       pwm.setServoPulse(15,i) 
                       time.sleep(0.02)  
                  pwm.setServoPulse(12,2200) 
                  pwm.setServoPulse(13,660)     
                  pwm.setServoPulse(14,1500)
                  pwm.setServoPulse(15,1530)                        
                print("throttle:")
                print(d)
                pwm.setServoPulse(0,d)            
                print("angle:")
                print(z)
                pwm.setServoPulse(1,z)
                
        
        
     break

connection.close()
print("close")

 
