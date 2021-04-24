from picamera import PiCamera 
from time import sleep

camera = PiCamera()
camera.rotation = 180
camera.capture('home/pi/Documents/rasberry-pi-practice-files/python-test-image.jpg')
