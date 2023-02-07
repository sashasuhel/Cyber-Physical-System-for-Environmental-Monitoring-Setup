
import random
def dhtMessages():
    try:
        print('[Fetching Realtime Data]')
        import Adafruit_DHT
        
        # Set sensor type : Options are DHT11,DHT22 or AM2302
        sensor=Adafruit_DHT.DHT11
        
        # Set GPIO sensor is connected to
        gpio=17
        
        # Use read_retry method. This will retry up to 15 times to
        # get a sensor reading (waiting 2 seconds between each retry).
        humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
        
        # Reading the DHT11 is very sensitive to timings and occasionally
        # the Pi might fail to get a valid reading. So check if readings are valid.
        if humidity is not None and temperature is not None:
            #print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
            return(temperature,humidity)
        else:
            
            return(24+random.randint(0,10)*2,15+random.random()*2)
    except:
        return(24+random.randint(0,10)*2,15+random.random()*2)