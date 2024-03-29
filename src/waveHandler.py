from src.constants import *
import random
from src.enemy import *

class WaveHandler():
    def __init__(self):
        self.waveNum = 0
        self.enemyThreshold = 0
        self.rangeFromPlayer = (80,150)

    def update(self):
        if len(enemyList) <= self.enemyThreshold:
            for i in range(30):
                sideChosen = random.randint(0,3)
                if sideChosen == 0:
                    xComp = cameraPos.getX()-random.randint(self.rangeFromPlayer[0], self.rangeFromPlayer[1])
                    yComp = random.randint(cameraPos.getRoundY()-random.randint(self.rangeFromPlayer[0], self.rangeFromPlayer[1]), cameraPos.getRoundY()+screenSize.getRoundY()+random.randint(self.rangeFromPlayer[0], self.rangeFromPlayer[1]))
                elif sideChosen == 1:
                    xComp = cameraPos.getX()+screenSize.getRoundX()+random.randint(self.rangeFromPlayer[0], self.rangeFromPlayer[1])
                    yComp = random.randint(cameraPos.getRoundY()-random.randint(self.rangeFromPlayer[0], self.rangeFromPlayer[1]), cameraPos.getRoundY()+screenSize.getRoundY()+random.randint(self.rangeFromPlayer[0], self.rangeFromPlayer[1]))
                elif sideChosen == 2:
                    xComp = random.randint(cameraPos.getRoundX()-random.randint(self.rangeFromPlayer[0], self.rangeFromPlayer[1]), cameraPos.getRoundX()+screenSize.getRoundX()+random.randint(self.rangeFromPlayer[0], self.rangeFromPlayer[1]))
                    yComp = cameraPos.getY()-random.randint(self.rangeFromPlayer[0], self.rangeFromPlayer[1])
                else:
                    xComp = random.randint(cameraPos.getRoundX()-random.randint(self.rangeFromPlayer[0], self.rangeFromPlayer[1]), cameraPos.getRoundX()+screenSize.getRoundX()+random.randint(self.rangeFromPlayer[0], self.rangeFromPlayer[1]))
                    yComp = cameraPos.getY()+screenSize.getRoundY()+random.randint(self.rangeFromPlayer[0], self.rangeFromPlayer[1])
                enemyList.append(Enemy(Vect(xComp, yComp), "red"))

waveHandler = WaveHandler()