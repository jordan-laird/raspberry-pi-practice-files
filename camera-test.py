from picamera import PiCamera 
from time import sleep

camera = PiCamera()

camera.capture('home/pi/Desktop/python-test-image.jpg')
