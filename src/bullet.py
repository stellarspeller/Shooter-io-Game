from src.constants import *

class Bullet():
    def __init__(self, pos, angle, bulletBase, isFromPlayer):
        self.pos = pos
        self.vel = Vect(bulletBase.speed * math.cos(angle), bulletBase.speed * math.sin(angle)) #thank you chatgpt, i was too lazy to write this myself
        self.size = bulletBase.size
        self.damage = bulletBase.damage
        self.penetration = bulletBase.penetration
        self.isFromPlayer = isFromPlayer

    def update(self):
        self.pos.add(Vect(self.vel.getX(), self.vel.getY()).multiply(0.2))
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
        pygame.draw.rect(screen, white, (x, y, self.size, self.size))
