"""
All functions for plotting the LiDAR data.
Author: Benned "Robert Moon" Hedegaard
Last revised 2/21/2020
"""

import pygame
import numpy as np
import PyLidar3
import time # Time module

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)

SIZE = [400,400]
CENTER = [SIZE[0]/2,SIZE[1]/2]

def initScreen(title, size):
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(title)
    return screen

def drawRangeBearing(screen, start, r, bearing):
    # This function draws a single measurement to the screen
    # r is the range (distance of measurement)
    # bearing is the angle of the measurement
    x_ = start[0] + r * np.cos(bearing)
    y_ = start[1] + r * np.sin(bearing)
    pygame.draw.line(screen, BLUE, start, [x_,y_], 3)

def main():
    screen = initScreen("Lidar GUI",SIZE)

    done = False
    clock = pygame.time.Clock()

    #Serial port to which lidar connected, Get it from device manager windows
    #In linux type in terminal -- ls /dev/tty* 
    
    lidar = PyLidar3.YdLidarX4("/dev/ttyUSB0")
    
    if(lidar.Connect()):
        print(lidar.GetDeviceInfo())
        gen = lidar.StartScanning()
        t = time.time() # start time
        
        # Run for given time and make sure window is not closed.
        while (time.time() - t) < 5 and not done:
            data = next(gen)
            print(type(data))
            print(data)
          
            screen.fill(WHITE) # Always clear the screen.
            #clock.tick(60) # Limits loop to this many times per second.

            for event in pygame.event.get(): # User did something!
                if event.type == pygame.QUIT: # If user clicked close...
                    done = True # Flag done so we exit this loop

            for angle in range(360):
                r = data[angle]
                drawRangeBearing(screen,CENTER,r,angle)

            pygame.display.flip() # Update screen to display all changes made.
            time.sleep(0.5) 
        
        lidar.StopScanning()
        
        lidar.Disconnect()
        print("Device disconnected")
    else:
        print("Error connecting to device")

    pygame.quit() # Be IDLE friendly

if __name__ == "__main__":
    main()