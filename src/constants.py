import pygame
from src.vect import *
from src.util import *

background_color = (27, 21, 33)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
magenta = (255, 0, 255)
cyan = (0, 255, 255)
purple = (127, 0, 255)
black = (0, 0, 0)

FPS = 120

#visual
particlesPerDeath = 7
particlesPerLevelup = 16
particlesPerLevelupText = 20
logoPixelSize = 10
lineDensity = 60
lineThickness = 1
playerWidth = 33
enemyScaleFactor = 2
xpColor = ((180, 220, 8), (220, 255, 10))
xpSize = (12, 8)
skillTreeUI = False

#fonts
font = pygame.font.SysFont(None, 48, False, False)
fontSmall1 = pygame.font.SysFont(None, 36, False, False)
fontSmall2 = pygame.font.SysFont(None, 24, False, False)
fontSmall3 = pygame.font.SysFont(None, 18, False, False)
fontLarge1 = pygame.font.SysFont(None, 72, False, False)

#gameplay
playerMaxVelocity = 2
decelConst = -0.075
frameCount = 0
enemyShooterAccuracy = 0.07

particleList = []
bulletList = []
playerShooters = []
enemyList = []
xpList = []
textList = []
skillTreeUIList = [] # list of ui text objects

xpToLevelUp = [1, 2, 30, 35, 40, 50, 70, 90, 120, 150, 180, 210, 250, 300, 350, 400, 450, 500, 570, 640, 720, 800, 890, 990, 1100, 1250, 1400, 1550, 1700, 1900, 2100, 2350, 2500, 3000]

pressedSkillTree = False

spawningThresholds = [
    [3, 1],
    [24, 2],
    [30, 5],
    [45, 7]
]

particlePositions = [
    [6,0],
    [7,0],
    [8,0],
    [9,0],
    [4,1],
    [5,1],
    [6,1],
    [7,1],
    [8,1],
    [2,2],
    [3,2],
    [4,2],
    [5,2],
    [6,2],
    [1,3],
    [2,3],
    [1,4],
    [2,4],
    [4,4],
    [5,4],
    [8,4],
    [1,5],
    [4,5],
    [5,5],
    [7,5],
    [8,5],
    [7,6],
    [8,6],
    [3,7],
    [4,7],
    [5,7],
    [6,7],
    [7,7],
    [1,8],
    [2,8],
    [3,8],
    [4,8],
    [5,8],
    [0,9],
    [1,9],
    [2,9],
    [3,9],
]

playerImage = pygame.image.load("res/guy2.png")



#dQw4w9WgXcQ

# Define the background colour
# using RGB color coding.

  
# Define the dimensions of
# screen object(width,height)
screen = pygame.display.set_mode((1200, 675), pygame.RESIZABLE)

##screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
  
# Set the caption of the screen
pygame.display.set_caption("Redemption Arc")
  
# Fill the background colour to the screen
screen.fill(background_color)

# Update the display using flip
#pygame.display.flip()

cameraPos = Vect(0,0)
screenSize = Vect(1200, 675)