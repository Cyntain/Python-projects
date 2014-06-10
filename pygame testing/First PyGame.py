## Learning how to use pygame
# Import pygame and system
import pygame, sys
# From pygame import all
from pygame.locals import *

# Start pygame
pygame.init()

# Set a screen up and give the screen a title
DISPLAYSURF =pygame.display.set_mode((300, 300))
pygame.display.set_caption("My First PyGame!")

# Start the loop
while True:
    
    # Get all of the users events (mouse clicks ect)
    for event in pygame.event.get():

        # If the event is to quit
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Draw a square: display, (colour), (where to draw and size)
    pygame.draw.rect(DISPLAYSURF, (0, 255, 0), (100, 50, 20, 20))
    
    # Update pygame's display
    pygame.display.update()
