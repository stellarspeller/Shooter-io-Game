from src.constants import *

class Bullet():
    def __init__(self, pos, angle, bulletBase, isFromPlayer, bulletSpeedExtra = 1, bulletDamageExtra = 1, bulletPenetrationExtra = 1):
        self.pos = pos
        self.vel = Vect(bulletBase.speed * math.cos(angle), bulletBase.speed * math.sin(angle)).multiply(bulletSpeedExtra) #thank you chatgpt, i was too lazy to write this myself
        self.size = bulletBase.size
        self.damage = bulletBase.damage * bulletDamageExtra
        self.penetration = bulletBase.penetration * bulletPenetrationExtra
        self.isFromPlayer = isFromPlayer
        #extras are optional modifiers to the base bullet stats

    def update(self):
        self.pos.add(Vect(self.vel.getX(), self.vel.getY()).multiply(bulletMoveConst*0.2*120/FPS))
        self.penetration -= bulletMoveConst * 0.25 * 1/FPS# * len(enemyBulletList)/6000
        #components of the above equation
        #bulletMoveConst: universal bullet movement speed
        #0.25: base penetration to be removed per frame
        #1/FPS: deltatime basically
        #len(enemyBulletList)/6000: bullets are destroyed faster the more of them there are (lag reduction)
        if self.penetration <= 0:
            self.kill()

        if not self.isFromPlayer:
            #remove bullet if it goes too far off screen, like 3x screen width (do not use bosc constant)
            if (   self.pos.getX()-cameraPos.getX() >  screenSize.x*3 
                or self.pos.getX()-cameraPos.getX() < -screenSize.x*3 
                or self.pos.getY()-cameraPos.getY() >  screenSize.y*3 
                or self.pos.getY()-cameraPos.getY() < -screenSize.y*3
                ):
                self.kill()

    
    def kill(self):
        #try except exists because when you iterate through the list and delete one it doesnt lower the index
        try:
            if self.isFromPlayer:
                playerBulletList.remove(self)
            else: 
                enemyBulletList.remove(self)
        except:
            pass
        del self
        
    def render(self):
        #check to make sure bullet is on screen before rendering
        
        x = round(self.pos.getX()-self.size/2 - cameraPos.getX())
        y = round(self.pos.getY()-self.size/2 - cameraPos.getY())

        #if x is between 0 and the camera x size and y is between 0 and the camera y size
        if x >= -bosc and x <= screenSize.x+bosc and y >= -bosc and y <= screenSize.y+bosc:
            if self.isFromPlayer:
                color = cyan
            else:
                color = red
            pygame.draw.rect(screen, color, (x, y, self.size, self.size))

