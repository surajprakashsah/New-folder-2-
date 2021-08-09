import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Motor():
        def __init__(self,Ena,In1,In2):
            self.Ena= Ena
            self.In1= In1
            self.In2= In2

            GPIO.setup(self.Ena,GPIO.OUT)
            GPIO.setup(self.In1,GPIO.OUT)
            GPIO.setup(self.In2,GPIO.OUT)

            self.pwmA= GPIO.PWM(self.Ena,100);
            self.pwmA.start(0);

def moveF(self,speed=50,direction= 1):
    if direction == 1:
    GPIO.output(self.In1,GPIO.HIGH)
    GPIO.output(self.In2,GPIO.LOW)
else:
    GPIO.output(self.In1,GPIO.LOW)
    GPIO.output(self.In2,GPIO.HIGH)
    self.pwmA.ChangeDutyCycle(speed);
#sleep(t)
def stop(self):

    self.pwmA.ChangeDutyCycle(0);
#sleep(t)

def main():
    motorL.moveF(100)
    motorR.moveF(100)
    sleep(3)
    motorL.stop()
    motorR.stop()
    sleep(3)
    motorL.moveF(0)
    motorR.moveF(100)
    sleep(3)
    motorL.stop()
    motorR.stop()
    #GPIO.cleanup()
 if __name__== &#39;__main__&#39;:
    motorL= Motor(2,3,4)
    motorR= Motor(17,22,27)
    main()