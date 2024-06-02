from src.constants import *
import random

class Particle(): #thank you chatgpt
    def __init__(self, x, y, speed, size, color, framesPerDownsize):
        self.pos = Vect(x, y)
        angle = random.uniform(0, 2 * math.pi)  # Random angle in radians
        xVel = speed * math.cos(angle)
        yVel = speed * math.sin(angle)
        self.vel = Vect(xVel, yVel)
        self.vel.multiply(120/FPS)
        self.size = size
        self.color = color
        self.framesPerDownsize = framesPerDownsize * FPS/120
        self.ticks = 0

    def render(self):
        pygame.draw.rect(screen, self.color, (self.pos.getX()-(round(self.size/2))-cameraPos.getX(), self.pos.getY()-(round(self.size/2))-cameraPos.getY(), round(self.size), round(self.size)))

    def update(self):
        #deltaVelocity = self.vel.multiply(1/FPS)
        #print(self.vel.multi)
        #print(deltaVelocity)
        self.pos.add(self.vel)
        if self.ticks >= self.framesPerDownsize:
            self.ticks = 0
            self.size -= 1
            if self.size <= 0:
                particleList.remove(self)
                del self
        else: 
            self.ticks += 1
