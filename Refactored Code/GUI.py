"""
GUI Class
Author: Benned Hedegaard
Last revised: 3/12/2020
"""

import pygame
from Simulator import Simulator

BLACK = (0,0,0)
GREY = (128,128,128)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)

SIZE = [800,800] # Width by height
CENTER = [int(SIZE[0]/2),int(SIZE[1]/2)]

SCALE = 50 # This many pixels in the pygame screen represent one unit in the robot's world.

class GUI:
    def __init__(self):
        pygame.init()
        s = pygame.display.set_mode(SIZE)
        pygame.display.set_caption("GUI")
        self.screen = s
        self.clock = pygame.time.Clock()

        # Store most recent values for the following:
        self.x = 0
        self.y = 0
        self.heading = 0

    # # Given a point (x,y) in the robot's frame, scale it to plot on the GUI screen.
    # def scaleGUI(self,point):
    #     point[0] = point[0]*SCALE + CENTER[0]
    #     point[1] = point[1]*SCALE + CENTER[1]
    #     return point

    # x,y is all messed up unless I fix for the flip in PyGame. Switch to C++ and OpenGL perhaps?

    def draw(self, pose):
        self.screen.fill(WHITE)
        self.drawGrid()
        self.drawMouse()
        self.drawPose(pose)
        pygame.display.flip() # Update screen to display all changes made.

    # Draws a grid with the defined scale (# pixels per unit).
    def drawGrid(self):
        for x in range(int(SIZE[0]/SCALE)):
            pygame.draw.line(self.screen, GREY, [x*SCALE,0], [x*SCALE,SIZE[1]], 1)
        for y in range(int(SIZE[1]/SCALE)):
            pygame.draw.line(self.screen, GREY, [0,y*SCALE], [SIZE[0],y*SCALE], 1)

    # Draws the mouse location on the screen.
    def drawMouse(self):
        pygame.draw.circle(self.screen, RED, pygame.mouse.get_pos(), 3)

    def drawPose(self, pose):
        pygame.draw.circle(self.screen, BLACK, self.scaleGUI(pose.position), 7)

def main():
    gui = GUI()
    sim = Simulator()

    done = False
    while not done: # Loop until user closes window.        
        for event in pygame.event.get(): # User did something!
            if event.type == pygame.QUIT: # If user clicked close...
                done = True # Flag done so we exit this loop

        pose = sim.step()
        gui.draw(pose)
 
    pygame.quit() # Be IDLE friendly

if __name__ == "__main__":
    main()
