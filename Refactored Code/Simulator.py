"""
Simulator Class
Author: Benned Hedegaard
Last revised: 3/12/2020
"""

import pygame

class Pose:
    def __init__(self):
        self.position = [0,0]
        self.heading = 0

class Simulator:
    def __init__(self):
        self.pose = Pose()

    # Simulate moving a certain amount forward in time.
    def step(self):
        self.pose.position[0] = self.pose.position[0] + 0.01

        return self.pose

def main():
    pass

if __name__ == "__main__":
    main()
