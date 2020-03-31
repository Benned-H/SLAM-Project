"""
All functions for calculation and display of the environment.
Author: Benned Hedegaard
Last revised: 11/20/2019
"""
import pygame
import numpy as np
from math import sin,cos,radians,degrees,sqrt

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)

size = [1200,800]
border = 100
roomW = size[0] - 2*border
roomH = size[1] - 2*border

roomTop = border
roomBottom = size[1] - border
roomLeft = border
roomRight = size[0] - border

def initScreen():
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Testing out PyGame")
    return screen

def getWalls():
    # These are just lists of points showing the path the walls should take.
    leftWall = [(100,100),(100,395),(310,395),(310,405),(100,405),(100,700)]
    bottomWall = [(300,700),(300,505),(310,505),(310,700),(860,700),(860,450),
        (1000,450),(1000,460),(870,460),(870,700),(1100,700)]
    rightWall = [(1100,100)]
    topWall = [(420,100),(420,340),(990,340),(990,200),(1000,200),(1000,350),
        (760,350),(760,600),(520,600),(520,590),(750,590),(750,350),(420,350),
        (420,600),(410,600),(410,100),(100,100)]
    points = leftWall + bottomWall + rightWall + topWall

    walls = []
    for i in range(len(points)-1):
        walls.append([points[i],points[i+1]])

    return walls

def getGrid(scale):
    if (roomH % scale != 0 or roomW % scale != 0):
        print("Error: Grid scale",scale,"doesn't divide evenly into",roomH,"or",roomW)
        return
    grid = np.zeros((int(roomH/scale), int(roomW/scale)))
    return grid

def getSegment(pos,a,radius):
    # Returns line segment from <pos> to point <radius> away at angle <a> (degrees).
    x2 = radius*cos(radians(a)) + pos[0]
    y2 = radius*sin(radians(a)) + pos[1]
    segment = [pos,(x2,y2)]
    return segment

def intersect(line1,line2):
    # Checks if given lines intersect. If so, returns that point.
    #       else returns None
    # Ensure that the first line is the wall, not the ray.
    x1 = line1[0][0]
    y1 = line1[0][1]
    x2 = line1[1][0]
    y2 = line1[1][1]
    x3 = line2[0][0]
    y3 = line2[0][1]
    x4 = line2[1][0]
    y4 = line2[1][1]

    t_num = (x1-x3)*(y3-y4)-(y1-y3)*(x3-x4)
    denom = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
    if denom == 0: # Parallel or coincident
        return None

    t = t_num / denom

    u_num = -((x1-x2)*(y1-y3)-(y1-y2)*(x1-x3))
    u = u_num / denom

    # Check that the intersection is actually in one of the lines...
    if (t <= 0 or 1 <= t or u <= 0 or 1 <= u):
        return None

    point = (x1+t*(x2-x1),y1+t*(y2-y1))
    #print("Point",point)
    return point

def distance(p1,p2):
    # Returns Euclidean distances between two points.
    return sqrt((p1[0]-p2[0])*(p1[0]-p2[0])+(p1[1]-p2[1])*(p1[1]-p2[1]))

def castRays(pos,maxLen,walls,screen):
    # Finds and draws rays to all closest <walls> from point <pos>.

    # First illustrate the rays' range.
    rect = ((pos[0]-maxLen,pos[1]-maxLen),(maxLen*2,maxLen*2))
    pygame.draw.arc(screen, RED, rect, 0, 4*np.pi, width=1)

    # Now calculate and plot the rays.
    for deg in np.linspace(0,360,500): # 360º of rays.
        ray = getSegment(pos,deg,maxLen)

        # Track which wall was the closest.
        minDist = maxLen
        closest = None
        thick = 1

        for wall in walls:
            point = intersect(wall,ray)
            if point != None:
                d = distance(pos,point)
                if d < minDist:
                    minDist = d
                    closest = point

        # Having found the closest wall, show the ray.
        if closest != None:
            pygame.draw.line(screen, BLUE, pos, closest, 1)

def castRay(pos,deg,walls,screen):
    # Finds and draws ray to all closest <walls> from point <pos>.
    ray = getSegment(pos,deg,maxLen)

    # Track which wall was the closest.
    minDist = maxLen
    closest = None
    thick = 1

    for wall in walls:
        point = intersect(wall,ray)
        if point != None:
            d = distance(pos,point)
            if d < minDist:
                minDist = d
                closest = point

    # Having found the closest wall, show the ray.
    if closest != None:
        pygame.draw.line(screen, BLUE, pos, closest, 1)

def plotGrid(grid,gridScale,screen):
    # Plots given grid, assuming it was created using gridScale/roomW/roomH.
    # Grid should be an np array.
    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r,c] != 0:
                left = border + c*gridScale
                top = border + r*gridScale
                pygame.draw.rect(screen,RED,(left,top,gridScale,gridScale))

def mouseToGrid(mousePos,grid,gridScale):
    if (roomLeft < mousePos[0] and mousePos[0] < roomRight and roomTop < mousePos[1] and mousePos[1] < roomBottom):
        col = (mousePos[0] - border)//gridScale
        row = (mousePos[1] - border)//gridScale
        grid[row,col] = 1
    return grid
