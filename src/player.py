from src.constants import *
from src.particle import *
from src.textHandler import *
from src.util import *

class Player():
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel
        self.hp = 60
        self.maxHp = 60
        self.hpRegen = 5
        self.xp = 0
        self.level = 1

    def render(self):
        #layered behind the player sprite, place a "circular health bar"
        #this should range from a 0 degree arc at 0 hp to a 360 degree arc at hp=maxhp
        hpArc = ((self.hp/self.maxHp)*2*math.pi)

        pygame.draw.arc(screen, (red[0]/2, red[1]/2, red[2]/2, 127), (self.pos.getRoundX()-3.5, self.pos.getRoundY()-3.5, playerWidth+7, playerWidth+7), 0, hpArc, 5)
        pygame.draw.arc(screen, red, (self.pos.getRoundX()-2.5, self.pos.getRoundY()-2.5, playerWidth+5, playerWidth+5), 0, hpArc, 5)

        #pygame.draw.arc(screen, white, (1, 1, 1, 1),  )
        screen.blit(playerImage, (self.pos.getRoundX(), self.pos.getRoundY()))
        

    def update(self):
        cameraPos.add(self.vel.getMultiply(120/FPS))
        self.hpCheck()

    def kill(self):
        pass
        print("u lose lmao")

    def hpCheck(self, cycles=1):
        if self.hp < self.maxHp:
            self.hp += self.hpRegen * 120/FPS * 0.002 * cycles
        if self.hp > self.maxHp:
            self.hp = self.maxHp

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
            #regenerate some hp
            self.hpCheck(120*6*120/FPS) # equivalent to 6 seconds of hp regen

            #increment level, mess with stats etc
            self.xp -= xpToLevelUp[self.level-1]
            self.level += 1
            
            #spawn particle effect
            for i in range(particlesPerLevelup):
                particleList.append(Particle(player.pos.getX()+cameraPos.getX()+playerWidth/2, player.pos.getY()+cameraPos.getY()+playerWidth/2, random.uniform(0.3, 0.4), random.randint(6, 8), random.choice(xpColor), random.randint(32, 44), Vect(player.vel.getX(), player.vel.getY())))

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