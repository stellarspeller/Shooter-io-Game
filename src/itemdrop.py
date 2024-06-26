from src.constants import *
from src.player import *
#import random

class itemDrop():
    def __init__(self, pos, value, vel=Vect(0,0)):
        """pos - Vect // value - int"""
        self.pos = pos
        self.value = value
        self.vel = Vect(0,0)

    def render(self):
        xComp = self.pos.getX()-cameraPos.getX()
        yComp = self.pos.getY()-cameraPos.getY()
        pygame.draw.ellipse(screen, xpColor[0], (xComp, yComp, xpSize[0], xpSize[0]))
        xComp = self.pos.getX()-cameraPos.getX()+(xpSize[0]-xpSize[1])/2
        yComp = self.pos.getY()-cameraPos.getY()+(xpSize[0]-xpSize[1])/2
        pygame.draw.ellipse(screen, xpColor[1], (xComp, yComp, xpSize[1], xpSize[1]))

    def update(self):

        #movement towards player

        xComp = player.pos.getX()+playerWidth/2-self.pos.getX()+cameraPos.getX()
        yComp = player.pos.getY()+playerWidth/2-self.pos.getY()+cameraPos.getY()
        if Vect(xComp, yComp).getMagnitude() <= 22:
            self.pickup()

        self.vel.x += (84/(Vect(xComp, yComp).getMagnitude()*FPS))*xComp
        self.vel.y += (84/(Vect(xComp, yComp).getMagnitude()*FPS))*yComp


        self.vel.circularClamp(player.skillStats["xpBoost"][player.skillTree["xpBoost"]] * xpMoveConst/(8000+0.75*Vect(xComp, yComp).getMagnitude()*FPS))

        self.vel.multiply(120/FPS)
        self.pos.x += self.vel.getX()
        self.pos.y += self.vel.getY()

    def pickup(self):
        pygame.mixer.Sound.play(random.choice(xpPickupSounds), 0, 0, 100)
        if player.level <= 99:
            player.xp += self.value * player.skillStats["xpBoost"][player.skillTree["xpBoost"]]
            player.checkLevelUp()
        else:
            player.hp += self.value * player.skillStats["xpBoost"][player.skillTree["xpBoost"]] * 0.2
        xpList.remove(self)
        del self
