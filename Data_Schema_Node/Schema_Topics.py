import csv
import random

def recordDATA(location):
    count=0
    while (count<=100):
        count+=1
        try:
            print('[Fetching Realtime Data]')
            import Adafruit_DHT
            sensor=Adafruit_DHT.DHT11
            gpio=17
            humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)  
            if humidity is not None and temperature is not None:            
                message=(temperature,humidity)
            else:
                message=(24+random.randint(0,10)*2,15+random.random()*2)
        except:
            message=(24+random.randint(0,10)*2,15+random.random()*2)
        with open(location, 'a', newline='') as file:
                print("[recorded Message]")
                writer = csv.writer(file)
                writer.writerow(message)


