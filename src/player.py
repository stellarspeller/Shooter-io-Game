from src.constants import *
from src.particle import *
from src.textHandler import *
from src.util import *

class Player():
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel
        self.hp = 100
        self.xp = 0
        self.level = 1

    def render(self):
        #pygame.transform.scale(playerImage, (64,64), screen)
        screen.blit(playerImage, (self.pos.getRoundX(), self.pos.getRoundY()))
        #pygame.draw.ellipse(screen, white, (self.pos.getRoundX(), self.pos.getRoundY(), 10, 10))

    def update(self):
        cameraPos.add(self.vel.getMultiply(120/FPS))

    def kill(self):
        pass
        print("u lose lmao")

    def checkBulletCollision(self):
        for i in bulletList:
            if not i.isFromPlayer:
                xComp = i.pos.getX()-self.pos.getX()-cameraPos.getX()-playerWidth/2
                yComp = i.pos.getY()-self.pos.getY()-cameraPos.getY()-playerWidth/2
                if Vect(xComp, yComp).getMagnitude() <= 16:
                    if i.penetration >= self.hp:
                        i.penetration -= self.hp
                        self.kill()
                    else:
                        self.hp -= i.damage
                        i.kill()

    def checkLevelUp(self):
        if self.xp >= xpToLevelUp[self.level-1]:
            #increment level, mess with stats etc
            self.xp -= xpToLevelUp[self.level-1]
            self.level += 1
            
            #spawn particle effect
            for i in range(particlesPerLevelup):
                particleList.append(Particle(player.pos.getX()+cameraPos.getX()+playerWidth/2, player.pos.getY()+cameraPos.getY()+playerWidth/2, random.uniform(0.3, 0.4), random.randint(6, 8), random.choice(xpColor), random.randint(32, 44)))

            #create level up text
            levelUpText = textHandler("Level up!", font, (0, 20), (255, 255, 255), True, 3, 6)
            distFromLeftSideOfScreen = (screenSize.x - levelUpText.get_width())/2
            levelUpText.pos = (distFromLeftSideOfScreen, 20)
            textList.append(levelUpText)

            #create level up text rect for particles
            levelUpTextRect = pygame.rect.Rect(levelUpText.pos[0], levelUpText.pos[1], levelUpText.get_width(), levelUpText.get_height())
            for i in range (particlesPerLevelupText):
                particlePos = randomPoint(levelUpTextRect)

                particleList.append(Particle(particlePos[0]+cameraPos.getX(), particlePos[1]+cameraPos.getY(), random.uniform(0.3, 0.4), random.randint(6, 8), random.choice(xpColor), random.randint(20, 32)))

player = Player(Vect(screenSize.getX()/2 - playerWidth/2,screenSize.getY()/2 - playerWidth/2), Vect(0,0))