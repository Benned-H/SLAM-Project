"""
All functions for plotting the LiDAR data.
Author: Benned Hedegaard
Last revised 2/16/2020
"""

import pygame
import numpy as np
import PyLidar3
import time # Time module

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)

SIZE = [1200,800]
CENTER = [SIZE[0]/2,SIZE[1]/2]

def initScreen(title, size):
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(title)
    return screen

def drawRangeBearing(screen, start, range, bearing):
	x_ = start[0] + range * np.cos(bearing)
	y_ = start[1] + range * np.sin(bearing)
	pygame.draw.line(screen, BLUE, start, [x_,y_], 3)

def get_data():
	samples = np.linspace(0,2*np.pi,100)

def main():
	screen = initScreen("Lidar GUI",SIZE)

	done = False
	clock = pygame.time.Clock()

	#Serial port to which lidar connected, Get it from device manager windows
	#In linux type in terminal -- ls /dev/tty* 
	port = input("Enter port name which lidar is connected:") #windows
	#port = "/dev/ttyUSB0" #linux
	lidar = PyLidar3.YdLidarX4(port) #PyLidar3.your_version_of_lidar(port,chunk_size) 
	if lidar.Connect():
		#PyGame chunk
		while not done:
			screen.fill(WHITE) # Always clear the screen.
			clock.tick(60) # Limits loop to this many times per second.


			for event in pygame.event.get(): # User did something!
				if event.type == pygame.QUIT: # If user clicked close...
					done = True # Flag done so we exit this loop

			data = get_data()

			for d in data:
				drawRangeBearing(screen,CENTER,d[0],d[1])

			pygame.display.flip() # Update screen to display all changes made.


    	print(lidar.GetDeviceInfo())
    	gen = lidar.StartScanning()
    	t = time.time() # start time

    	data = next(gen)
    	print(type(data))
   		
   		lidar.StopScanning()
    	lidar.Disconnect()
	else:
    	print("Error connecting to device")

    pygame.quit() # Be IDLE friendly

if __name__ == "__main__":
	main()