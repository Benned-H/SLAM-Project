import pygame
import numpy as np

from environment import *

deg_increment = 360/500

gridScale = 10 # Pixels for dimension of each grid box

#maxLen = sqrt(roomW*roomW+roomH*roomH) # Longest possible ray length in the room.
maxLen = 200 # Range the rays can 'see'

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)

def main():
    screen = initScreen()
 
    done = False
    clock = pygame.time.Clock()

    walls = getWalls()
    grid = getGrid(gridScale)
    
    deg = 0
    while not done: # Loop until user closes window.
        screen.fill(BLACK) # Always clear the screen.
        plotGrid(grid,gridScale,screen)

        clock.tick(60) # Limits loop to this many times per second.
        
        for event in pygame.event.get(): # User did something!
            if event.type == pygame.QUIT: # If user clicked close...
                done = True # Flag done so we exit this loop

        for wall in walls:
            pygame.draw.line(screen, WHITE, wall[0], wall[1], 3)

        mousePos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, RED, mousePos, 8)

        roomGrid = mouseToGrid(mousePos,grid,gridScale)

        castRays(mousePos,maxLen,walls,screen)
        #castRay(mousePos,maxLen,deg,lines,screen) # For LiDAR simulation.
     
        pygame.display.flip() # Update screen to display all changes made.

        # Update LiDAR laser.
        deg += deg_increment
        if deg >= 360:
            deg -= 360
 
    pygame.quit() # Be IDLE friendly

def test():
    pass

TEST = False
if __name__ == "__main__":
    if TEST:
        test()
    else:
        main()