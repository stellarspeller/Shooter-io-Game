from src.constants import *
from src.bullet import *

class Shooter():
    def __init__(self, cooldown, bulletCreated, angleVariant):
        """NOTE - Cooldown measured in seconds // angleVariant is the degrees of rotation away from perfect accuracy"""
        self.cooldown = cooldown
        self.bulletCreated = bulletCreated
        self.angleVariant = angleVariant
        self.cooldownFrames = FPS * cooldown

    def shoot(self, position, angle, isFromPlayer):
        bulletList.append(Bullet(position, angle + self.angleVariant, self.bulletCreated, isFromPlayer))