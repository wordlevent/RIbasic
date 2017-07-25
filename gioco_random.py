import RPi.GPIO as GPIO
import time
import random
import sys
from contextlib import ExitStack, contextmanager
from timeit import default_timer
import urllib.request as urllib2


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
END = 30
start = time.time()
seconds = 0


ch1 = False
ch2 = False
ch3 = False
ch4 = False
ch5 = False
ch6 = False
ch7 = False
ch8 = False

GPIO.setup(4,GPIO.OUT)

GPIO.setup(5,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(6,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(19,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(26,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(20,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)



GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.output(4, GPIO.HIGH)
GPIO.output(17, GPIO.HIGH)
GPIO.output(27, GPIO.HIGH)
GPIO.output(22, GPIO.HIGH)
GPIO.output(18, GPIO.HIGH)
GPIO.output(23, GPIO.HIGH)
GPIO.output(24, GPIO.HIGH)
GPIO.output(25, GPIO.HIGH)



def end_time():
    end = time.time()
    temp = end -start
    hours = temp//3600
    temp = temp - 3600*hours
    minutes = temp//60
    seconds = temp - 60*minutes
    if int(seconds) == END:
        print("END ",seconds)
        sys.exit()


def pressed(num, punti):
    
    if num == 1:
        if GPIO.input(5):
            print("Spengo il display1")
            GPIO.output(4,False)
            punti += 1
            print("PUNTI +1", punti)
            return punti
        else:
            time.sleep(2)
            print("Spengo il display 1")
            GPIO.output(4,False)
            return punti


            
    if num == 2:
       if GPIO.input(6):
           print("Spengo il display 2")
           GPIO.output(17,False)
           punti += 1
           return punti
       else:
           time.sleep(2)
           print("Spengo il display 2")
           GPIO.output(17,False)
           return punti

    if num == 3:
       if GPIO.input(13):
           print("Spengo il display 3")
           GPIO.output(27,False)
           punti += 1
           return punti
       else:
           time.sleep(2)
           print("Spengo il display 3")
           GPIO.output(27,False)
           return punti



    if num == 4:
        if GPIO.input(19):
           print("Spengo il display 4")
           GPIO.output(22,False)
           punti += 1
           return punti
        else:
           time.sleep(2)
           print("Spengo il display 4")
           GPIO.output(22,False)
           return punti


    if num == 5:
       if GPIO.input(26):
           print("Spengo il display 5")
           GPIO.output(18,False)
           punti += 1
           return punti
       else:
           time.sleep(2)
           print("Spengo il display 5")
           GPIO.output(18,False)
           return punti

        
        
    if num == 6:
        if GPIO.input(12):
           print("Spengo il display 6")
           GPIO.output(23,False)
           punti += 1
           return punti
        else:
           time.sleep(2)
           print("Spengo il display 6")
           GPIO.output(23,False)
           return punti


    if num == 7:
        if GPIO.input(16):
            print("Spengo il display 7")
            GPIO.output(24,False)
            punti += 1
            return punti
        else:
            time.sleep(2)
            print("Spengo il display 7")
            GPIO.output(24,False)
            return punti


    if num == 8:
        if GPIO.input(20):
            print("Spengo il display 8")
            GPIO.output(25,False)
            punti += 1
            return punti
            
        else:
            time.sleep(2)
            print("Spengo il display 8")
            GPIO.output(25,False)
            return punti



punti = 0
while True:

        numeroRandom = random.randint(1,8)
        
        if numeroRandom == 1:
            GPIO.output(4,True)
            print("Accendo il display1")
            punti = pressed(1,punti)
            print("<<",punti )
            
            

        if numeroRandom == 2:
            GPIO.output(17,True)
            print("Accendo il display2")
            punti =pressed(2,punti)
            print("<<",punti )
          

        if numeroRandom == 3:
            GPIO.output(27,True)
            print("Accendo il display3")
            punti = pressed(3,punti)
            print("<<",punti)
          
            
        if numeroRandom == 4:
            GPIO.output(22,True)
            print("Accendo il display4")
            punti = pressed(4,punti)
            print("<<",punti)
          

        if numeroRandom == 5:
            GPIO.output(18,True)
            print("Accendo il display5")
            punti = pressed(5,punti)
            print("<<",punti)
          

        if numeroRandom == 6:
            GPIO.output(23,True)
            print("Accendo il display6")
            punti = pressed(6,punti)
            print("<<",punti)
          

        if numeroRandom == 7:
            GPIO.output(24,True)
            print("Accendo il display7")
            punti = pressed(7,punti)
            print("<<",punti)
          

        if numeroRandom == 8:
            GPIO.output(25,True)
            print("Accendo il display8")
            punti = pressed(8,punti)
            print("<<",punti)
          
        
        end_time()


#test send url
url = 'http://ciaotrading.com/gioco/?punti='+punti
response = urllib2.urlopen(url).read()
print(response)


















#with elapsed_timer() as elapsed:
#    time.sleep(1)
#    print(elapsed())
#    time.sleep(2)
#    print(elapsed())
#    time.sleep(3)

#ciclo START da 30sec
#for i in range(1,START):
#    print("test",i)
#    time.sleep(1)





