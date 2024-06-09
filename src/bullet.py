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
        self.pos.add(Vect(self.vel.getX(), self.vel.getY()).multiply(0.2*120/FPS))
        self.penetration -= 0.25 * 1/FPS
        if self.penetration <= 0:
            bulletList.remove(self)
            del self
    
    def kill(self):
        bulletList.remove(self)
        del self
        
    def render(self):
        x = round(self.pos.getX()-self.size/2 - cameraPos.getX())
        y = round(self.pos.getY()-self.size/2 - cameraPos.getY())
        if self.isFromPlayer:
            color = cyan
        else:
            color = red
        pygame.draw.rect(screen, color, (x, y, self.size, self.size))
