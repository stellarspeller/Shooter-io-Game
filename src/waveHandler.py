from src.constants import *
import random
from src.enemy import *
from data.waves import *

class WaveHandler():
    def __init__(self):
        self.waveNum = 0
        self.enemyThreshold = 0
        self.rangeFromPlayer = (100,220)
        self.queue = [] #NUM of enemies, frames, type
        self.queueFrames = 0
        self.recentSpawnFlag = False

    def spawn(self, enemyType):

        self.recentSpawnFlag = False

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

        enemyList.append(Enemy(Vect(xComp, yComp), enemyType))

    def addToQueue(self, numOfEnemies, secondsPerSpawn, enemyType):
        self.queue.append([numOfEnemies, round(secondsPerSpawn*FPS), enemyType])

    def update(self):
        if ((len(enemyList) <= self.enemyThreshold) and (not self.recentSpawnFlag)):
            for i in waveData[self.waveNum]:
                self.addToQueue(i["count"], i["spawnDelay"], i["enemyType"])
                self.recentSpawnFlag = True
            self.waveNum += 1

        if len(self.queue) > 0:
            #self.queueFrames = self.queue[0][1] #basically, get the number of frames between each spawn for the #1 in queue

            #check queueframe value
            #if 0, do the spawn procedure
            #if above 0, subtract one

            if self.queueFrames == 0:
                self.spawn(self.queue[0][2])
                self.queue[0][0] -= 1
                self.queueFrames = self.queue[0][1]

                if self.queue[0][0] <= 0:
                    del self.queue[0]

            elif self.queueFrames > 0:
                self.queueFrames -= 1


waveHandler = WaveHandler()