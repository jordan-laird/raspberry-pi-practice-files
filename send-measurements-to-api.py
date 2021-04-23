import requests
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

temp_c = sense.get_temperature()
humidity = sense.get_humidity()

payload = {'temp_c': temp_c, 'humidity': humidity}
r = requests.post("https://httpbin.org/post", data=payload)
print(r.text)