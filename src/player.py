from src.constants import *

class Player():
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel
        self.hp = 100
        self.xp = 0

    def render(self):
        #pygame.transform.scale(playerImage, (64,64), screen)
        screen.blit(playerImage, (self.pos.getRoundX(), self.pos.getRoundY()))
        #pygame.draw.ellipse(screen, white, (self.pos.getRoundX(), self.pos.getRoundY(), 10, 10))

    def update(self):
        cameraPos.add(self.vel)

player = Player(Vect(screenSize.getX()/2 - playerWidth/2,screenSize.getY()/2 - playerWidth/2), Vect(0,0))