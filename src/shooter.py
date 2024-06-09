from src.constants import *
from src.bullet import *

class Shooter():
    def __init__(self, cooldown, bulletCreated, angleVariant):
        """NOTE - Cooldown measured in seconds // angleVariant is the RADIANS of rotation away from perfect accuracy"""
        self.cooldown = cooldown
        self.bulletCreated = bulletCreated
        self.angleVariant = angleVariant
        self.cooldownFrames = FPS * cooldown

    """MODIFIER LIST:
    0 - spread
    1 - bulletSpeed
    2 - bulletDamage
    3 - bulletPenetration
    """
    def shoot(self, position, angle, isFromPlayer, modifiers=[1, 1, 1, 1]):
        bulletList.append(Bullet(
            position, 
            angle + self.angleVariant + random.uniform(-playerShooterAccuracy, playerShooterAccuracy) * modifiers[0], 
            self.bulletCreated, 
            isFromPlayer, 
            modifiers[1],
            modifiers[2],
            modifiers[3]
        ))