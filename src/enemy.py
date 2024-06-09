from src.constants import *
from src.particle import *
from src.itemdrop import *
import random
from data.enemyData import *
import copy
#from src. import *

class Enemy():
    def __init__(self, pos, enemyType):
        self.pos = pos
        self.vel = Vect(0,0)
        self.enemyType = enemyType
        self.hp = enemyData[enemyType]["hp"]
        self.rotation = 0
        self.hitboxCenter = Vect(0,0)
        self.personalShooterList = copy.deepcopy(enemyData[enemyType]["shooters"]) #thank you chatgpt
        for i in self.personalShooterList:
            i.cooldownFrames = random.randint(0, round(FPS * i.cooldown))
        self.rotPerSecond = enemyData[enemyType]["rotationPerSecond"] * random.choice((-1, 1)) * random.uniform(0.9, 1.1)
        self.xpValue = round(enemyData[enemyType]["xpReleased"] * random.triangular(0.7, 1.3))
        self.trackingPattern = 1
        self.circleDirection = random.choice((-1, 1))
        self.framesToNextTrackingChange = random.randint(5*FPS, 20*FPS)

    def kill(self):
        for i in range(particlesPerDeath):
            particleList.append(Particle(self.pos.getX(), self.pos.getY(), 1.1, 10, enemyData[self.enemyType]["particleColor"], 10))
        
        numOfDrops = random.randint(max(1, round(self.xpValue * 0.1)), round(math.sqrt(self.xpValue)))
        #print(numOfDrops)
        xpParticleValues = [math.floor(self.xpValue/numOfDrops)] * numOfDrops
        xpParticleValues[0] += (self.xpValue - xpParticleValues[0] * numOfDrops)

        for i in xpParticleValues:
            xpList.append(itemDrop(Vect(self.pos.getX()+random.randint(-24,24), self.pos.getY()+random.randint(-24,24)), i))
        
        enemyList.remove(self)
        del self

    def shootReady(self):
        for i in self.personalShooterList:
            if i.cooldownFrames <= 0:
                xComp = self.pos.getX()#+cameraPos.getX()+15
                yComp = self.pos.getY()#+cameraPos.getY()+15
                shootAngle = math.atan2(player.pos.getY()-self.pos.getY()+cameraPos.getY()+15, player.pos.getX()-self.pos.getX()+cameraPos.getX()+15)
                variability = random.triangular(-enemyShooterAccuracy, enemyShooterAccuracy, 0)
                i.shoot(Vect(xComp, yComp), shootAngle+variability, False)
                i.cooldownFrames = FPS * i.cooldown
    
    def update(self):
        """Does the functionality of both Render and Update because the hitbox is influenced by the sprite's rotation"""
        
        moveConst = 0.02
        initComponent = Vect(self.vel.getX(),self.vel.getY()).multiply(1-(moveConst/FPS))
        xComp = player.pos.getX()-self.pos.getX()-(enemyScaleFactor*15/4)+cameraPos.getX()+playerWidth/2
        yComp = player.pos.getY()-self.pos.getY()-(enemyScaleFactor*15/4)+cameraPos.getY()+playerWidth/2 
        #idk why divided by 4 works, it just does
        modifyComponent = Vect(xComp, yComp).multiply(moveConst/FPS)
        if self.trackingPattern == 1:
            modifyComponent.multiply(self.circleDirection).setPerpindicularCW()
        self.vel = initComponent.add(modifyComponent)
        self.rotation += self.rotPerSecond * (120/FPS)
        if self.vel.getMagnitude() >= enemyData[self.enemyType]["maxVelocity"]:
            self.vel.unitize(enemyData[self.enemyType]["maxVelocity"] * 120/FPS)
        self.pos.add(Vect(self.vel.getX(), self.vel.getY()).multiply(0.14))


        xComp = self.pos.getRoundX()-cameraPos.getX()
        yComp = self.pos.getRoundY()-cameraPos.getY()

        #this is a mess but so am i :D

        scaled_image = pygame.transform.scale(enemyData[self.enemyType]["sprite"], (int(15 * enemyScaleFactor), int(15 * enemyScaleFactor)))
        rotated_image = pygame.transform.rotate(scaled_image, self.rotation)
        image_rect = enemyData[self.enemyType]["sprite"].get_rect()
        image_center = image_rect.center
        rotation_point = image_center
        rotated_rect = rotated_image.get_rect(center=rotation_point)
        #scaled_rect = scaled_image.get_rect(center=(self.pos.getX(), self.pos.getY()))
        screen.blit(rotated_image, (xComp + rotated_rect.x, yComp + rotated_rect.y))

        self.hitboxCenter = Vect(xComp - rotated_rect.x/2 -.5, yComp - rotated_rect.y/2 -.5)
        #screen.blit(rotated_image, (xComp, yComp))

        if random.uniform(0,1) <= (10/FPS):
            xComp = (self.hitboxCenter.getX()+cameraPos.getX())
            yComp = (self.hitboxCenter.getY()+cameraPos.getY())
            particleList.append(Particle(xComp, yComp, .24, 5, enemyData[self.enemyType]["particleColor"], 18))

        for i in bulletList:
            if i.isFromPlayer:
                xComp = i.pos.getX()-self.hitboxCenter.getX()-(round(i.size/2))-cameraPos.getX()
                yComp = i.pos.getY()-self.hitboxCenter.getY()-(round(i.size/2))-cameraPos.getY()
                if Vect(xComp, yComp).getMagnitude() <= 25.6:
                    if i.penetration >= self.hp:
                        i.penetration -= self.hp
                        #self.kill()
                    else:
                        self.hp -= i.damage
                        i.kill()
        
        self.shootReady()

        self.framesToNextTrackingChange -= 1

        if self.framesToNextTrackingChange == 0:
            if self.trackingPattern == 0: self.trackingPattern = 1
            else: self.trackingPattern = 0
            self.framesToNextTrackingChange = random.randint(5*FPS, 20*FPS)

