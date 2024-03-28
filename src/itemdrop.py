from src.constants import *
from src.player import *

class itemDrop():
    def __init__(self, pos, value):
        """pos - Vect // value - int"""
        self.pos = pos
        self.value = value

    def render(self):
        xComp = self.pos.getX()-cameraPos.getX()
        yComp = self.pos.getY()-cameraPos.getY()
        pygame.draw.ellipse(screen, xpColor[0], (xComp, yComp, xpSize[0], xpSize[0]))
        xComp = self.pos.getX()-cameraPos.getX()+(xpSize[0]-xpSize[1])/2
        yComp = self.pos.getY()-cameraPos.getY()+(xpSize[0]-xpSize[1])/2
        pygame.draw.ellipse(screen, xpColor[1], (xComp, yComp, xpSize[1], xpSize[1]))

    def update(self):
        xComp = player.pos.getX()+playerWidth/2-self.pos.getX()+cameraPos.getX()
        yComp = player.pos.getY()+playerWidth/2-self.pos.getY()+cameraPos.getY()
        if Vect(xComp, yComp).getMagnitude() <= 22:
            self.pickup()

    def pickup(self):
        player.xp += self.value
        xpList.remove(self)
        del self
