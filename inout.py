import RPi.GPIO as GPIO
import time



GPIO.setmode(GPIO.BCM)

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





while True:
        
                if GPIO.input(5):
                        ch1 = not ch1
                        GPIO.output(4,ch1)
                        time.sleep(.5)
                                
                        
                        
            
                if GPIO.input(6):
                        ch2 = not ch2
                        GPIO.output(17,ch2)
                        time.sleep(.5)
                        

                if GPIO.input(13):
                        ch3 = not ch3
                        GPIO.output(27,ch3)
                        time.sleep(.5)
                        

                if GPIO.input(19):
                        ch4 = not ch4
                        GPIO.output(22,ch4)
                        time.sleep(.5)
                    

                if GPIO.input(26):
                        ch5 = not ch5
                        GPIO.output(18,ch5)
                        time.sleep(.5)
                    

                if GPIO.input(12):
                        ch6 = not ch6
                        GPIO.output(23,ch6)
                        time.sleep(.5)
                    

                if GPIO.input(16):
                        ch7 = not ch7
                        GPIO.output(24,ch7)
                        time.sleep(.5)
                    

                if GPIO.input(20):
                        ch8 = not ch8
                        GPIO.output(25,ch8)
                        time.sleep(.5)
                    
              

GPIO.cleanup()

        






