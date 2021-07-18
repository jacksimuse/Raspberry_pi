import Adafruit_DHT as dht
import time

sensor = dht.DHT11
pin = 18

try:
    while True:
        h, t = dht.read_retry(11, pin)
        
        # if h is not None and t is not None:
        #     print('Temp = {0}C / Humidity = {1}%'.format(t, h))
        # else:
        #     print('Sensing error')

        time.sleep(1)
except Exception as e:
    print('Error occured : {0}'.format(e))
finally:
    print('End of program')