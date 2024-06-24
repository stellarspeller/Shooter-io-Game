from src.constants import *
import random
from src.enemy import *
from data.waves import *

class WaveHandler():
    def __init__(self):
        self.waveNum = 79
        self.enemyThreshold = 0
        self.rangeFromPlayer = (100,220)
        self.queue = [] #NUM of enemies, frames, type
        self.queueFrames = 0
        self.recentSpawnFlag = False
        self.xpToGrab = 0
        if self.waveNum > 0:
            #write a function to go through enemydata, pick out all the enemies and their xp stats, then give that much xp to the player
            for i in range(self.waveNum):
                for j in waveData[i]:
                    self.xpToGrab += enemyData[j["enemyType"]]["xpReleased"] * j["count"] * 1.65

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

        if self.waveNum <= 80:
            enemyList.append(Enemy(Vect(xComp, yComp), enemyType))
        else:
            enemyList.append(Enemy(Vect(xComp, yComp), enemyType, self.waveNum/80))
            #1/80 factor is to give the enemies more hp as the wave increases past 80

    def addToQueue(self, numOfEnemies, secondsPerSpawn, enemyType):
        self.queue.append([numOfEnemies, round(secondsPerSpawn*FPS), enemyType])

    def checkThresholdIncrease(self):
        if self.waveNum >= spawningThresholds[0][0]:
            self.enemyThreshold = spawningThresholds[0][1]
            del spawningThresholds[0]

    def update(self):
        if ((len(enemyList) <= self.enemyThreshold) and (not self.recentSpawnFlag)):
            if self.waveNum < len(waveData): #check if there are still waves
                for i in waveData[self.waveNum]:
                    self.addToQueue(i["count"], i["spawnDelay"], i["enemyType"])
                    self.recentSpawnFlag = True
            else: #end of waves, continue with procedurally generated waves
                """
                Wrote a description for how i wanted this to work several weeks ago:
                for extended, add a enemyHealthMultiplier to enemy init, then:
                for each wave, take a base wave. assume wave 99 or something powerful
                then, randomly pick N other waves (random from 0-100), where N is determined by how far into the extension you are
                then, take (waveNum/100) and set that to enemyhealthmultipler, maybe add some scaling
                """
                #use random.choice to choose from base extended waves
                """Spawns base wave for extended"""
                for i in random.choice(extendedWaveData):
                    self.addToQueue(i["count"], i["spawnDelay"], i["enemyType"])
                    self.recentSpawnFlag = True #i have genuinely no idea why this is here but it probably has a purpose

                """In the case that youre early into the extension, spawn a wave proportional to your progress - Otherwise, pick a random wave with no account for progression"""
                if self.waveNum <= 100:
                    #"easy" mode
                    selectedWaveNum = random.triangular(4*(self.waveNum-80)-40, 4*(self.waveNum-80)+40)
                    #when between waves 80 and 100 this returns a value between 0 and 80
                    j = round(min(79, max(0, selectedWaveNum))) #clamps to a value corresponding to a wave that actually exists
                    for i in waveData[j]:
                        self.addToQueue(i["count"], i["spawnDelay"], i["enemyType"])
                        self.recentSpawnFlag = True
                    #self.addToQueue(waveData[j]["count"], waveData[j]["spawnDelay"], waveData[j]["enemyType"])

                else:
                    for i in range(
                        round(
                            1 +
                            (self.waveNum-80)/24 +
                            ((self.waveNum-80)**2) / 300
                        ) #slowly ramps up the amount of waves selected
                    ):
                        #should be a random wave in the predefined set of 80 (0-79)
                        randomSelectedWave = random.randint(0, 79)
                        for i in waveData[randomSelectedWave]:
                            self.addToQueue(i["count"], i["spawnDelay"], i["enemyType"])
                            self.recentSpawnFlag = True
                    
            self.waveNum += 1
            self.checkThresholdIncrease()

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