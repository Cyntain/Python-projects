import pygame, sys, random
from pygame.locals import *

# Constants representing colours
BLACK = (0, 0, 0 )
BROWN = (153, 76, 0 )
GREEN = (0, 255, 0 )
BLUE = (0, 0, 255 )
RED = (255, 0 , 0 )
GRAY = (160, 160, 160 )

# Constants representing the different resources
DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
STONE = 4
LAVA = 5

# Dictionary linking the resources to the tiles
textures = {
                    DIRT : pygame.image.load('dirt.png'),
                    GRASS : pygame.image.load('grass.png'),
                    WATER : pygame.image.load('water.png'),
                    COAL : pygame.image.load('coal.png'),
                    STONE : pygame.image.load('stone.png'),
                    LAVA : pygame.image.load('lava.png')
                }

## Game Dimensions
TILESIZE = 40
MAPWIDTH = 40
MAPHEIGHT = 20

## Dealing with map creation
resources = [DIRT,GRASS,WATER,COAL,LAVA,STONE]
# list comprehension to create tilemap
tilemap = [ [DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT) ]

# Set up the display
pygame.init()
DISPLAY = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))

## Player
PLAYER = pygame.image.load('player.png').convert_alpha()
# player coords
playerPos = [0, 0]

for rw in range(MAPHEIGHT):
    for cl in range(MAPWIDTH):
        randomNumber = random.randint(0,15)

        if randomNumber == 0:
            tile = COAL
        elif randomNumber == 1 or randomNumber == 2:
            tile = WATER
        elif randomNumber == 3:
            tile = LAVA
        elif randomNumber >= 4 and randomNumber <= 8:
            tile = GRASS
        elif randomNumber >=9 and randomNumber <= 12:
            tile = STONE
        else:
            tile = DIRT

        tilemap[rw][cl] = tile


# LOOP
while True:

    # get all the user events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT and playerPos[0] < MAPWIDTH - 1:
                playerPos[0] += 1
            if event.key == K_LEFT and playerPos[0] > 0:
                playerPos[0] -= 1
            if event.key == K_UP and playerPos[1] > 0:
                playerPos[1] -= 1
            if event.key == K_DOWN and playerPos[1] < MAPHEIGHT -1:
                playerPos[1] += 1

    # Loop through the tile maps rows
    for row in range(MAPHEIGHT):
        # loop through each column in the row
        for column in range(MAPWIDTH):
            DISPLAY.blit(textures[tilemap[row][column]], (column*TILESIZE, row*TILESIZE))

    DISPLAY.blit(PLAYER, (playerPos[0]*TILESIZE, playerPos[1]*TILESIZE))
       
    # Update the display
    pygame.display.update()
