from src.constants import *
from src.particle import *
from src.itemdrop import *
import random
from data.enemyData import *
#from src. import *

class Enemy():
    def __init__(self, pos, enemyType):
        self.pos = pos
        self.vel = Vect(0,0)
        self.enemyType = enemyType
        self.hp = enemyData[enemyType]["hp"]
        self.rotation = 0
        self.hitboxCenter = Vect(0,0)
        self.personalShooterList = enemyData[enemyType]["shooters"].copy() #thank you chatgpt

    def kill(self):
        for i in range(particlesPerDeath):
            particleList.append(Particle(self.pos.getX(), self.pos.getY(), 1.1, 10, enemyData[self.enemyType]["particleColor"], 10))
        xpList.append(itemDrop(Vect(self.pos.getX()+random.randint(-20,20), self.pos.getY()+random.randint(-20,20), ), 10))
        enemyList.remove(self)
        del self

    def shootReady(self):
        for i in self.personalShooterList:
            if i.cooldownFrames <= 0:
                xComp = self.pos.getX()+cameraPos.getX()+15
                yComp = self.pos.getY()+cameraPos.getY()+15
                shootAngle = math.atan2(player.pos.getY()-self.pos.getY()-cameraPos.getY()+15, player.pos.getX()-self.pos.getX()-cameraPos.getX()+15)
                variability = random.triangular(-enemyShooterAccuracy, enemyShooterAccuracy, 0)
                i.shoot(Vect(xComp, yComp), shootAngle+variability, False)
                i.cooldownFrames = FPS * i.cooldown
    
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

        #this is a mess but so am i :D

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

        if random.uniform(0,1) <= (10/FPS):
            xComp = (self.hitboxCenter.getX()+cameraPos.getX())
            yComp = (self.hitboxCenter.getY()+cameraPos.getY())
            particleList.append(Particle(xComp, yComp, .14, 5, enemyData[self.enemyType]["particleColor"], 18))
        

        for i in bulletList:
            if i.isFromPlayer:
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
        self.shootReady()
