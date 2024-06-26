import pygame
from src.vect import *
from src.util import *

background_color = (27, 21, 33)
#line color should be lighter bg color
lineColor = (27*2.8, 21*2, 33*2.4)

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

scene = "play"

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
cannonUpgradeUI = False

#fonts
font = pygame.font.SysFont(None, 48, False, False)
fontSmall1 = pygame.font.SysFont(None, 36, False, False)
fontSmall2 = pygame.font.SysFont(None, 24, False, False)
fontSmall3 = pygame.font.SysFont(None, 18, False, False)
fontLarge1 = pygame.font.SysFont(None, 72, False, False)

#gameplay
globalDamageConst = 0.9
globalReloadConst = 0.9
#the above should always be equal

globalSpeedConst = 1.3
playerMaxVelocity = 2 * globalSpeedConst
enemyMoveConst = 0.03 * globalSpeedConst
bulletMoveConst = 1 * globalSpeedConst
xpMoveConst = 35000 * globalSpeedConst
decelConst = -0.075
frameCount = 0
enemyShooterAccuracy = 0.07
advancedEnemyShooterAccuracy = 0.035
playerShooterAccuracy = 0.05

settings = {
    "musicVolume": 0,
    "soundVolume": 0,
    "enemyParticles": True
}

particleList = []
#bulletList = []
playerBulletList = [] #separated for player and enemy to reduce useless collision detection
enemyBulletList = []
enemyList = []
xpList = []
textList = []
skillTreeUIList = [] # list of ui text objects

def generateXpCurve(maxLevel):
    xpCurve = []
    baseXp = 35
    xpMultiplier = 1.055
    for i in range(maxLevel+1):
        xpCurve.append(round(int(baseXp * (xpMultiplier ** i))/5)*5)
    return xpCurve

xpToLevelUp = generateXpCurve(98)
print(xpToLevelUp)
#print sum of xpToLevelUp
print(sum(xpToLevelUp))
print(f'xp to get to level 79: {sum(xpToLevelUp[0:79])}')
xpToLevelUp.append(-1) #placeholder to make sure that nothing crashes if you reach max level and try to display the xp curve

pressedSkillTree = False

spawningThresholds = [
    [6, 1],
    [16, 2],
    [30, 3],
    #[45, 5],
    [99999999, 99999999] #placeholder
]

bosc = 10 #bullet off screen constant, basically the amount of pixels the bullet can go off screen before not being rendered
#dont want this to be 0 because that would mean the bullet would not be rendered at the very edge of the screen

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

enemyHitSounds = [
    pygame.mixer.Sound("res/sound/sfx/enemyHit1.wav"),
    pygame.mixer.Sound("res/sound/sfx/enemyHit2.wav")
]
enemyDeathSounds = [
    pygame.mixer.Sound("res/sound/sfx/enemyDeath1.wav"),
    pygame.mixer.Sound("res/sound/sfx/enemyDeath2.wav")
]
playerShootSounds = [
    pygame.mixer.Sound("res/sound/sfx/playerShoot1.wav"),
    pygame.mixer.Sound("res/sound/sfx/playerShoot2.wav"),
    pygame.mixer.Sound("res/sound/sfx/playerShoot3.wav")
]
xpPickupSounds = [
    pygame.mixer.Sound("res/sound/sfx/xp1.wav"),
    pygame.mixer.Sound("res/sound/sfx/xp2.wav"),
    pygame.mixer.Sound("res/sound/sfx/xp3.wav")
]
levelUpSound = pygame.mixer.Sound("res/sound/sfx/levelUp.wav")

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