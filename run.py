import pygame
import random
import math
#from os import system
pygame.init()
#Font=pygame.font.SysFont('fontify.ttf', 96)


"""
playerImage = pygame.image.load("res/guy.png")
redSprite = pygame.image.load("res/enemies/RED.png")
orangeSprite = pygame.image.load("res/enemies/ORANGE.png")
yellowSprite = pygame.image.load("res/enemies/YELLOW.png")
greenSprite = pygame.image.load("res/enemies/GREEN.png")
cyanSprite = pygame.image.load("res/enemies/CYAN.png")
blueSprite = pygame.image.load("res/enemies/BLUE.png")
purpleSprite = pygame.image.load("res/enemies/PURPLE.png")
pinkSprite = pygame.image.load("res/enemies/PINK.png")
"""
playerImage = pygame.image.load("res/guy.png")


#dQw4w9WgXcQ

# Define the background colour
# using RGB color coding.
background_color = (27, 21, 33)
white = (255, 255, 255)
  
# Define the dimensions of
# screen object(width,height)
screen = pygame.display.set_mode((1200, 675), pygame.RESIZABLE)

##screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
  
# Set the caption of the screen
pygame.display.set_caption("Redemption Arc")
  
# Fill the background colour to the screen
screen.fill(background_color)

# Update the display using flip
pygame.display.flip()

FPS = 120
  
# Variable to keep our game loop running
running = True

class Vect():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, inputVect):
        self.x += inputVect.x
        self.y += inputVect.y
        # Optionally, return self if you want to chain methods
        return self

    
    def __str__(self):
        return str([self.x, self.y])
    
    def unitize(self, radius=None):
        if radius is None:
            radius = 1
        c = math.sqrt(self.x**2 + self.y**2) * (1/radius)
        if c != 0:
            self.x /= c
            self.y /= c

    def multiply(self, scale):
        self.x *= scale
        self.y *= scale
        # Optionally, return self if you want to chain methods
        return self
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getMagnitude(self):
        return math.sqrt(self.y**2 + self.x**2)
    
    def getRoundX(self):
        return round(self.x)
    
    def getRoundY(self):
        return round(self.y)
    
    def clamp(self, clampRadius):
        if self.y >=  clampRadius: self.y =  clampRadius
        if self.y <= -clampRadius: self.y = -clampRadius
        if self.x >=  clampRadius: self.x =  clampRadius
        if self.x <= -clampRadius: self.x = -clampRadius
    

class Particle(): #thank you chatgpt
    def __init__(self, x, y, speed, size, color, framesPerDownsize):
        self.pos = Vect(x, y)
        angle = random.uniform(0, 2 * math.pi)  # Random angle in radians
        xVel = speed * math.cos(angle)
        yVel = speed * math.sin(angle)
        self.vel = Vect(xVel, yVel)
        self.vel.multiply(120/FPS)
        self.size = size
        self.color = color
        self.framesPerDownsize = framesPerDownsize * FPS/120
        self.ticks = 0

    def render(self):
        pygame.draw.rect(screen, self.color, (self.pos.getX()-(round(self.size/2))-cameraPos.getX(), self.pos.getY()-(round(self.size/2))-cameraPos.getY(), self.size, self.size))

    def tick(self):
        #deltaVelocity = self.vel.multiply(1/FPS)
        #print(self.vel.multi)
        #print(deltaVelocity)
        self.pos.add(self.vel)
        if self.ticks >= self.framesPerDownsize:
            self.ticks = 0
            self.size -= 1
            if self.size <= 0:
                particleList.remove(self)
                del self
        else: 
            self.ticks += 1

    
class Player():
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel
        self.hp = 100
        self.xp = 0

    def render(self):
        #pygame.transform.scale(playerImage, (64,64), screen)
        screen.blit(playerImage, (self.pos.getRoundX(), self.pos.getRoundY()))
        #pygame.draw.ellipse(screen, white, (self.pos.getRoundX(), self.pos.getRoundY(), 10, 10))

    def update(self):
        cameraPos.add(self.vel)


class BaseBullet():
    def __init__(self, speed, size, damage, penetration):
        self.speed = speed
        self.size = size
        self.damage = damage
        self.penetration = penetration


class Bullet():
    def __init__(self, pos, angle, bulletBase):
        self.pos = pos
        self.vel = Vect(bulletBase.speed * math.cos(angle), bulletBase.speed * math.sin(angle)) #thank you chatgpt, i was too lazy to write this myself
        self.size = bulletBase.size
        self.damage = bulletBase.damage
        self.penetration = bulletBase.penetration

    def update(self):
        self.pos.add(Vect(self.vel.getX(), self.vel.getY()).multiply(0.2))
        self.penetration -= 0.25 * 1/FPS
        if self.penetration <= 0:
            bulletList.remove(self)
            del self
    
    def kill(self):
        bulletList.remove(self)
        del self
        
    def render(self):
        x = round(self.pos.getX()-self.size/2 - cameraPos.getX())
        y = round(self.pos.getY()-self.size/2 - cameraPos.getY())
        pygame.draw.rect(screen, white, (x, y, self.size, self.size))

#speed size damage pen.
bulletTypes = {
    "basic":BaseBullet(10, 5, 2, 1),
    "sniper":BaseBullet(20, 4, 6, 3),
    "cannonball":BaseBullet(6, 12, 20, 20)
}

class Shooter():
    def __init__(self, cooldown, bulletCreated, angleVariant):
        """NOTE - Cooldown measured in seconds // angleVariant is the degrees of rotation away from perfect accuracy"""
        self.cooldown = cooldown
        self.bulletCreated = bulletCreated
        self.angleVariant = angleVariant
        self.cooldownFrames = FPS * cooldown

    def shoot(self, position, angle):
        
        bulletList.append(Bullet(position, angle, self.bulletCreated))


enemyData = {
    "red":{
        "hp":10,
        "maxVelocity":2,
        "shooters":[
            Shooter(.7, bulletTypes["basic"], 0)
        ],
        "sprite":pygame.image.load("res/enemies/RED.png"),
        "particleColor":(255,0,0)
    },
    "orange":{
        "hp":18,
        "maxVelocity":3,
        "shooters":[
            Shooter(.8, bulletTypes["basic"], 0), 
            Shooter(1, bulletTypes["basic"], 0)
        ],
        "sprite":pygame.image.load("res/enemies/ORANGE.png"),
        "particleColor":(255,127,0)
    },
    "yellow":{
        "hp":21,
        "maxVelocity":4,
        "shooters":[
            Shooter(.6, bulletTypes["basic"], 0), 
            Shooter(.9, bulletTypes["basic"], -0.2),
            Shooter(.9, bulletTypes["basic"], 0.2)
        ],
        "sprite":pygame.image.load("res/enemies/YELLOW.png"),
        "particleColor":(255,255,0)
    }
}


class itemDrop():
    def __init__(self, pos, value):
        """pos - Vect // value - int"""
        self.pos = pos
        self.value = value

    def render(self):
        pygame.draw.ellipse(screen, xpColor[0], (self.pos.getX(), self.pos.getY(), xpSize[0], xpSize[0]))
        pygame.draw.ellipse(screen, xpColor[1], (self.pos.getX(), self.pos.getY(), xpSize[1], xpSize[1]))

    def update(self):
        xComp = player.pos.getX()-self.pos.getX()-cameraPos.getX()
        yComp = player.pos.getY()-self.pos.getY()-cameraPos.getY()
        if Vect(xComp, yComp).getMagnitude() <= 18:
            self.pickup()


    def pickup(self):

        xpList.remove(self)
        del self


class Enemy():
    def __init__(self, pos, enemyType):
        self.pos = pos
        self.vel = Vect(0,0)
        self.enemyType = enemyType
        self.hp = enemyData[enemyType]["hp"]
        self.rotation = 0
        self.hitboxCenter = Vect(0,0)

    def kill(self):
        for i in range(particlesPerDeath):
            particleList.append(Particle(self.pos.getX(), self.pos.getY(), 1.1, 10, enemyData[self.enemyType]["particleColor"], 10))
        xpList.append(itemDrop(Vect(self.pos.getX()+random.randint(-20,20), self.pos.getY()+random.randint(-20,20), ), 10))
        enemyList.remove(self)
        del self
    
    def update(self):
        """Does the functionality of both Render and Update because the hitbox is influenced by the sprite's rotation"""
        moveConst = 2
        initComponent = Vect(self.vel.getX(),self.vel.getY()).multiply(1-(moveConst/FPS))
        xComp = player.pos.getX()-self.pos.getX()-(enemyScaleFactor*15/4)+cameraPos.getX()+playerWidth/2
        yComp = player.pos.getY()-self.pos.getY()-(enemyScaleFactor*15/4)+cameraPos.getY()+playerWidth/2 
        #idk why divided by 4 works, it just does
        modifyComponent = Vect(xComp, yComp).multiply(moveConst/FPS)
        self.vel = initComponent.add(modifyComponent)
        self.rotation += 0.1 * (120/FPS)
        if self.vel.getMagnitude() >= enemyData[self.enemyType]["maxVelocity"]:
            self.vel.unitize(enemyData[self.enemyType]["maxVelocity"])
        self.pos.add(Vect(self.vel.getX(), self.vel.getY()).multiply(0.14))


        xComp = self.pos.getRoundX()-cameraPos.getX()
        yComp = self.pos.getRoundY()-cameraPos.getY()

        scaled_image = pygame.transform.scale(enemyData[self.enemyType]["sprite"], (int(15 * enemyScaleFactor), int(15 * enemyScaleFactor)))
        rotated_image = pygame.transform.rotate(scaled_image, self.rotation)
        image_rect = enemyData[self.enemyType]["sprite"].get_rect()
        image_center = image_rect.center
        rotation_point = image_center
        #print(rotation_point)
        rotated_rect = rotated_image.get_rect(center=rotation_point)
        #print(rotated_rect)
        #scaled_rect = scaled_image.get_rect(center=(self.pos.getX(), self.pos.getY()))
        screen.blit(rotated_image, (xComp + rotated_rect.x, yComp + rotated_rect.y))

        #pygame.draw.ellipse(screen, white, (xComp - rotated_rect.x/2 -.5, yComp - rotated_rect.y/2 -.5, 5, 5))
        self.hitboxCenter = Vect(xComp - rotated_rect.x/2 -.5, yComp - rotated_rect.y/2 -.5)
        #print(self.hitboxCenter)
        #screen.blit(rotated_image, (xComp, yComp))

        for i in bulletList:
            #(self.pos.getX()-(round(self.size/2))-cameraPos.getX(), self.pos.getY()-(round(self.size/2))
            xComp = i.pos.getX()-self.hitboxCenter.getX()-(round(i.size/2))-cameraPos.getX()
            yComp = i.pos.getY()-self.hitboxCenter.getY()-(round(i.size/2))-cameraPos.getY()
            if Vect(xComp, yComp).getMagnitude() <= 25.6:
                if i.penetration >= self.hp:
                    i.penetration -= self.hp
                    self.kill()
                else:
                    self.hp -= i.damage
                    i.kill()
                #print(Vect(i.pos.getX(), i.pos.getY()).multiply(-1).add(self.hitboxCenter).getMagnitude() <= 50)

        




"""class Particle():
    def __init__(self, pos, vel, size):
        self.pos = Vect(pos)
        self.vel = Vect(vel)
        self.size = size"""
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
logoPixelSize = 10




particleList = []
bulletList = []
enemyShooters = []
playerShooters = []
enemyList = []
xpList = []

enemyList.append(Enemy(Vect(70,70), "red"))

cameraPos = Vect(0,0)
screenSize = Vect(1200, 675)

lineDensity = 60
lineThickness = 1
playerMaxVelocity = 2
decelConst = -0.075
frameCount = 0
playerWidth = 32
enemyScaleFactor = 2
particlesPerDeath = 7
xpColor = ((180, 220, 8), (220, 255, 10))
xpSize = (12, 8)

player = Player(Vect(screenSize.getX()/2 - playerWidth/2,screenSize.getY()/2 - playerWidth/2), Vect(0,0))

#Shooter(cooldown,  )
#Shooter(1, Bullet(Vect(player.pos.getX(), player.pos.getY()), 0, bulletTypes["basic"]), 0)
playerShooters.append(Shooter(.4, bulletTypes["basic"], 0))
playerShooters.append(Shooter(.9, bulletTypes["cannonball"], 0))



clock = pygame.time.Clock()
# game loop
while running:
    clock.tick(FPS)
    frameCount += 1

    for i in playerShooters:
        if i.cooldownFrames > 0:
            i.cooldownFrames -= 1



    pygame.display.update()

    for event in pygame.event.get():
      
        # Check for QUIT event      
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.VIDEORESIZE:
            # If the window is resized, get the new dimensions and update the screen
            #WIDTH, HEIGHT = event.w, event.h
            screenSize.x = event.w
            screenSize.y = event.h
            screen = pygame.display.set_mode((screenSize.getX(), screenSize.getY()), pygame.RESIZABLE)
            player.pos = Vect(screenSize.getX()/2 - playerWidth/2, screenSize.getY()/2 - playerWidth/2)



    screen.fill(background_color)


    """Input Handling"""
    inputRight = pygame.key.get_pressed()[pygame.K_l]+pygame.key.get_pressed()[pygame.K_d]+pygame.key.get_pressed()[pygame.K_RIGHT]
    inputLeft = pygame.key.get_pressed()[pygame.K_j]+pygame.key.get_pressed()[pygame.K_a]+pygame.key.get_pressed()[pygame.K_LEFT]
    inputDown = pygame.key.get_pressed()[pygame.K_k]+pygame.key.get_pressed()[pygame.K_s]+pygame.key.get_pressed()[pygame.K_DOWN]
    inputUp = pygame.key.get_pressed()[pygame.K_i]+pygame.key.get_pressed()[pygame.K_w]+pygame.key.get_pressed()[pygame.K_UP]

    inputVect = Vect(inputRight-inputLeft, inputDown-inputUp)
    
    inputVect.clamp(1)

    inputVect.multiply(.1)

    if inputVect.getMagnitude() == 0:
        inputVect = Vect(player.vel.getX()*(decelConst), player.vel.getY()*(decelConst))

    player.vel.add(inputVect)

    if player.vel.getMagnitude() <= 0.00001:
        player.vel = Vect(0,0)

    if player.vel.getMagnitude() > playerMaxVelocity:
        player.vel.unitize(playerMaxVelocity)



    """Mouse Input"""
    mousePos = Vect(pygame.mouse.get_pos()[0]-player.pos.getX(), pygame.mouse.get_pos()[1]-player.pos.getY())
    mousePos.unitize()


    """Click to Shoot"""
    if(pygame.mouse.get_pressed(3)[0]): 
        for i in playerShooters:
            if i.cooldownFrames <= 0:
                i.shoot(Vect(player.pos.getX()+cameraPos.getX()+playerWidth/2,player.pos.getY()+cameraPos.getY()+playerWidth/2), math.atan2(mousePos.getY(), mousePos.getX()))
                i.cooldownFrames = FPS * i.cooldown


    """Updating and rendering orders"""
    for i in range(round(screenSize.getRoundX()/lineDensity)+2):
        pygame.draw.line(screen, white, ((lineDensity*i)-cameraPos.getRoundX()%lineDensity, -10), ((lineDensity*i)-cameraPos.getRoundX()%lineDensity, screenSize.getY()+10), lineThickness)
    for i in range(round(screenSize.getY()/lineDensity)+2):
        pygame.draw.line(screen, white, (-10, ((lineDensity*i)-cameraPos.getRoundY()%lineDensity)), (screenSize.getX()+10, (lineDensity*i)-cameraPos.getRoundY()%lineDensity), lineThickness)
    
    for i in particleList:
        #print(i.vel)
        i.tick()
        i.render()

    for i in xpList:
        i.render()
        i.update()

    for i in bulletList:
        i.update()
        i.render()

    for i in enemyList:
        i.update()
        #i.render()

    player.update()
    player.render()

    """if frameCount < 240:
        for i in particlePositions:
            pygame.draw.rect(screen, white, (logoPixelSize*i[0]+100, logoPixelSize*i[1]+100, logoPixelSize, logoPixelSize))
    if len(particleList) <= 0 and frameCount >= 240 and frameCount <= 240+logoPixelSize*6:
        for i in particlePositions:
            particleList.append(Particle(logoPixelSize*i[0]+100, logoPixelSize*i[1]+100, 1, logoPixelSize, white, 6))"""

    #for i in particleList:
    #    pygame.draw.rect(screen, white, (i.pos.getX(), i.pos.y, i.size, i.size))

    #pygame.draw.rect(screen, white ,(900,150,100,50))

    particleList.append(Particle(400, 400, 1.1, 10, white, 10))

    #print(cameraPos)

    #system.clear()
    #print("Particles: " + str(len(particleList)))




    #print(inputVect)

    #inputVect.multiply(-3)

    #cameraPos.add(inputVect)


    #draw player
