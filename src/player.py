from src.constants import *

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
        cameraPos.add(self.vel)

    def kill(self):
        pass
        print("u lose lmao")

    def checkBulletCollision(self):
        for i in bulletList:
            if not i.isFromPlayer:
                xComp = i.pos.getX()-self.pos.getX()-cameraPos.getX()-playerWidth/2
                yComp = i.pos.getY()-self.pos.getY()-cameraPos.getY()-playerWidth/2
                #print("a")
                if Vect(xComp, yComp).getMagnitude() <= 16:
                    print(self.hp)
                    #print("YOUR MOM")
                    if i.penetration >= self.hp:
                        i.penetration -= self.hp
                        self.kill()
                    else:
                        self.hp -= i.damage
                        i.kill()

    def checkLevelUp(self):
        if self.xp >= xpToLevelUp[self.level-1]:
            self.xp -= xpToLevelUp[self.level-1]
            self.level += 1
            #levelup sequence

player = Player(Vect(screenSize.getX()/2 - playerWidth/2,screenSize.getY()/2 - playerWidth/2), Vect(0,0))