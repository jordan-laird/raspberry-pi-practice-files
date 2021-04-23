from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

#sense.show_message("Eat Ass. Suck a dick. Sell drugs.")

# r, g, b = 255,255, 255
# sense.clear((r,g,b))

sense.clear()
#temp_c = sense.get_temperature()
#temp_f = temp_c * 2 + 30

humidity = sense.get_humidity()
print(humidity)

#Set pixels
# blue = (0, 0, 255)
# red = (255, 0, 0)
# 
# sense.set_pixel(0, 2, blue)
# sense.set_pixel(7, 4, red)

# Draw face on LED
# sense.set_pixel(2, 2, (0, 0, 255))
# sense.set_pixel(4, 2, (0, 0, 255))
# sense.set_pixel(3, 4, (100, 0, 0))
# sense.set_pixel(1, 5, (255, 0, 0))
# sense.set_pixel(2, 6, (255, 0, 0))
# sense.set_pixel(3, 6, (255, 0, 0))
# sense.set_pixel(4, 6, (255, 0, 0))
# sense.set_pixel(5, 5, (255, 0, 0))
# 
# sense.set_pixel(2, 2, (0, 0, 255))
# sense.set_pixel(4, 2, (0, 0, 255))
# sense.set_pixel(3, 4, (100, 0, 0))
# sense.set_pixel(1, 5, (255, 0, 0))
# sense.set_pixel(2, 6, (255, 0, 0))
# sense.set_pixel(3, 6, (255, 0, 0))
# sense.set_pixel(4, 6, (255, 0, 0))
# sense.set_pixel(5, 5, (255, 0, 0))

# w = (150, 150, 150)
# b = (0, 0, 255)
# e = (0, 0, 0)
# 
# image = [
# e,e,e,e,e,e,e,e,
# e,e,e,e,e,e,e,e,
# w,w,w,e,e,w,w,w,
# w,w,b,e,e,w,w,b,
# w,w,w,e,e,w,w,w,
# e,e,e,e,e,e,e,e,
# e,e,e,e,e,e,e,e,
# e,e,e,e,e,e,e,e
# ]
# 
# sense.set_pixels(image)
# 
# while True:
#     sleep(1)
#     sense.flip_h()


while True:
	acceleration = sense.get_accelerometer_raw()
	x = acceleration['x']
	y = acceleration['y']
	z = acceleration['z']

	x=round(x, 0)
	y=round(y, 0)
	z=round(z, 0)

	print("x={0}, y={1}, z={2}".format(x, y, z))
