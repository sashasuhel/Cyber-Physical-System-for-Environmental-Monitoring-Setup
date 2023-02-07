
# try:
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

TRIG = 16#change 
ECHO = 18#change 
BUZZER = 13#change 
i=0

GPIO.setwarnings(False)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
# GPIO.setup(ECHO,GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

GPIO.output(TRIG, False)
print ("Calibrating.....")
time.sleep(2)

print ("[EARLY WARNING SYSTEM is ACTIVE]")

try:
    while True:
#         print("started1")
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        
#         print("started2")
        while GPIO.input(ECHO)==0:
#             print("first while")
            pulse_start = time.time()
            
#         print("started2a")
        while GPIO.input(ECHO)==1:
            pulse_end = time.time()
            
#         print("started2b")
        
        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150

        distance = round(distance, 2)
    
#         print("started3")
        if distance<=20 and distance>=5:
            print ("distance:",distance,"cm")
            GPIO.output(13,GPIO.HIGH)

        else:
            print ("distance:",distance,"cm")
            GPIO.output(13,GPIO.LOW)
        
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Keyboard Interrupted!")
    GPIO.cleanup()
# except:
#     print('[info:Service Execution halted, Retry Running]')
