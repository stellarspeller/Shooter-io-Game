from src.constants import *
from src.particle import *
from src.itemdrop import *
import random
from data.enemyData import *
import copy
#from src. import *

class Enemy():
    def __init__(self, pos, enemyType, hpMultiplier=1):
        self.pos = pos
        self.vel = Vect(0,0)
        self.enemyType = enemyType
        self.hp = enemyData[enemyType]["hp"] * hpMultiplier
        self.isAdvanced = enemyType in ["red2", "orange2", "yellow2", "green2", "cyan2", "blue2", "purple2", "pink2", "white2"]
        self.rotation = 0
        self.hitboxCenter = Vect(0,0)
        self.personalShooterList = copy.deepcopy(enemyData[enemyType]["shooters"]) #thank you chatgpt
        for i in self.personalShooterList:
            i.cooldownFrames = random.randint(0, round(FPS * i.cooldown))
        self.rotPerSecond = enemyData[enemyType]["rotationPerSecond"] * random.choice((-1, 1)) * random.uniform(0.9, 1.1)
        self.xpValue = round(enemyData[enemyType]["xpReleased"] * random.triangular(0.7, 1.3))
        self.trackingPattern = random.randint(0, 2)
        self.doesShoot = random.randint(10, 40) < len(enemyList) #enemies have a chance to not shoot based on the amount currently on screen (reduce lag and reduce chaos)
        self.circleDirection = random.choice((-1, 1))
        self.framesToNextTrackingChange = random.randint(5*FPS, 20*FPS)
        self.currentOpacity = 255
        self.specificScaleFactor = 1
        if self.enemyType in ["white", "white2"]:
            self.specificScaleFactor = 2
        self.scaled_image = pygame.transform.scale(enemyData[self.enemyType]["sprite"], (int(15 * enemyScaleFactor * self.specificScaleFactor), int(15 * enemyScaleFactor * self.specificScaleFactor)))
        if self.isAdvanced:
            self.shooterAccuracy = enemyShooterAccuracy
        else: 
            self.shooterAccuracy = advancedEnemyShooterAccuracy

    def kill(self):
        for i in range(particlesPerDeath):
            particleList.append(Particle(self.pos.getX(), self.pos.getY(), 1.1, 10, enemyData[self.enemyType]["particleColor"], 10))
        
        minimumDrops = round((max(1, min(round(self.xpValue * 0.1), round(math.sqrt(self.xpValue))*0.75))))
        maximumDrops = round(math.sqrt(self.xpValue))
        numOfDrops = random.randint(minimumDrops, maximumDrops)
        #print(numOfDrops)
        xpParticleValues = [math.floor(self.xpValue/numOfDrops)] * numOfDrops
        xpParticleValues[0] += (self.xpValue - xpParticleValues[0] * numOfDrops)

        for i in xpParticleValues:
            xpList.append(itemDrop(Vect(self.pos.getX()+random.randint(-24,24), self.pos.getY()+random.randint(-24,24)), i))
        
        #purpose of try except is to prevent the enemy from being removed if it is not in the enemy list
        #not sure why this would ever happen but ive encountered it before
        #if i didnt have this, enemies randomly become unkillable
        #if i do have this, it occasionally crashes a game when it detects an enemy not in the list
        try:
            enemyList.remove(self)
        except:
            pass
        del self

    def shootReady(self):
        for i in self.personalShooterList:
            if i.cooldownFrames <= 0:
                xComp = self.pos.getX()#+cameraPos.getX()+15
                yComp = self.pos.getY()#+cameraPos.getY()+15
                shootAngle = math.atan2(player.pos.getY()-self.pos.getY()+cameraPos.getY()+15, player.pos.getX()-self.pos.getX()+cameraPos.getX()+15)
                variability = random.triangular(-self.shooterAccuracy, self.shooterAccuracy, 0)
                i.shoot(Vect(xComp, yComp), shootAngle+variability, False)
                i.cooldownFrames = FPS * i.cooldown/globalSpeedConst * globalReloadConst

    def generateParticles(self):
        if settings["enemyParticles"]:
            if self.currentOpacity > 3*256/4: #only has particles if the enemy is mostly opaque
                if random.uniform(0,1) <= (10/FPS):
                    xComp = (self.hitboxCenter.getX()+cameraPos.getX())
                    yComp = (self.hitboxCenter.getY()+cameraPos.getY())
                    particleList.append(Particle(xComp, yComp, .24, 5, enemyData[self.enemyType]["particleColor"], 18, Vect(0, 0), round(self.currentOpacity)))
    
    def update(self):
        """Does the functionality of both Render and Update because the hitbox is influenced by the sprite's rotation"""
        farAway = False
        initComponent = Vect(self.vel.getX(),self.vel.getY()).multiply(1-(enemyMoveConst/FPS))
        xComp = player.pos.getX()-self.pos.getX()-(enemyScaleFactor*self.specificScaleFactor*15/4)+cameraPos.getX()+playerWidth/2
        yComp = player.pos.getY()-self.pos.getY()-(enemyScaleFactor*self.specificScaleFactor*15/4)+cameraPos.getY()+playerWidth/2 
        #idk why divided by 4 works, it just does
        modifyComponent = Vect(xComp, yComp)
        if (modifyComponent.getMagnitude() >= (screenSize.x + screenSize.y)*1.5):
            farAway = True
        modifyComponent.multiply(enemyMoveConst/FPS)
        if self.trackingPattern == 1:
            modifyComponent.multiply(self.circleDirection).setPerpindicularCW()
        if self.trackingPattern == 2:
            modifyComponent.multiply(-1)
        self.vel = initComponent.add(modifyComponent)
        self.rotation += self.rotPerSecond * (120/FPS) * globalSpeedConst
        if self.vel.getMagnitude() >= enemyData[self.enemyType]["maxVelocity"] * globalSpeedConst:
            self.vel.unitize(enemyData[self.enemyType]["maxVelocity"] * 1.3 * globalSpeedConst * 120/FPS)
        self.pos.add(Vect(self.vel.getX(), self.vel.getY()).multiply(0.14))


        xComp = self.pos.getRoundX()-cameraPos.getX()
        yComp = self.pos.getRoundY()-cameraPos.getY()

        #this is a mess but so am i :D

        rotated_image = pygame.transform.rotate(self.scaled_image, self.rotation)
        
        #set opacity for rotated image
        rotated_image.set_alpha(self.currentOpacity)
        image_rect = enemyData[self.enemyType]["sprite"].get_rect()
        image_center = image_rect.center
        rotation_point = image_center
        rotated_rect = rotated_image.get_rect(center=rotation_point)
        #scaled_rect = scaled_image.get_rect(center=(self.pos.getX(), self.pos.getY()))
        screen.blit(rotated_image, (xComp + rotated_rect.x, yComp + rotated_rect.y))

        self.hitboxCenter = Vect(xComp - rotated_rect.x/2 -.5, yComp - rotated_rect.y/2 -.5)
        #screen.blit(rotated_image, (xComp, yComp))

        self.generateParticles()

        for i in playerBulletList:
            if i.pos.getManhattanDist(self.pos) <= 90: #check if bullet is close enough to enemy to warrant a collision detection calculation
                xComp = i.pos.getX()-self.hitboxCenter.getX()-(round(i.size/2))-cameraPos.getX()
                yComp = i.pos.getY()-self.hitboxCenter.getY()-(round(i.size/2))-cameraPos.getY()
                if Vect(xComp, yComp).getMagnitudeSq() <= (25.6 * (enemyScaleFactor/2) * self.specificScaleFactor)**2:
                    if self.hp - i.penetration <= 0:
                        i.penetration -= self.hp * globalDamageConst
                        self.kill()
                    else:
                        self.hp -= i.damage * globalDamageConst
                        i.kill()
                        self.doesShoot = True #enemy will shoot if it is damaged
                        if self.isAdvanced:
                            self.currentOpacity = max(
                                self.currentOpacity + 40,
                                40 * 1/player.skillStats["cooldown"][player.skillTree["cooldown"]]
                            )  
                            if self.currentOpacity >= 255:
                                self.currentOpacity = 255

        if self.isAdvanced:
            self.currentOpacity -= 0.6 * 120/FPS
            if self.currentOpacity <= -127:
                self.currentOpacity = 255

        if not farAway: #enemy doesnt shoot if not close enough to the player (4x off screen)
            if self.doesShoot:
                self.shootReady()
            else:
                if len(enemyList) < 11:
                    self.doesShoot = True
        else: #if enemy is far away
            self.trackingPattern = 0 #beeline to player
            self.pos.add(self.vel.getMultiply(80/FPS)) #moves at extremely fast pace towards the player

        self.framesToNextTrackingChange -= 1

        if self.framesToNextTrackingChange == 0:
            #sets self.trackingPattern to a random pattern
            randVar = random.randint(1, 100)
            if randVar < 50:
                self.trackingPattern = 0
                self.doesShoot = True
            elif randVar < 80:
                self.trackingPattern = 1
            else:
                self.trackingPattern = 2 #run away, smaller chance because it makes the game boring like "oh why are there no enemies"
                self.doesShoot = False
            if self.trackingPattern in (0, 1):
                self.framesToNextTrackingChange = random.randint(5*FPS, 10*FPS)
            else:
                self.framesToNextTrackingChange = random.randint(2*FPS, 4*FPS) #less time between tracking swap if in the "run away" pattern
