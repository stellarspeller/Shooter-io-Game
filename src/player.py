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
        self.skillPoints = 0
        """
        skillTree - dict
        Purpose: store player skill point investments
        """
        self.skillTree = {
            "healthRegen": 0,
            "maxHealth": 0,
            "speed": 0,
            "spread": 0,
            "cooldown": 0,
            "bulletSpeed": 0,
            "bulletDamage": 0,
            "bulletPenetration": 0,
            "xpGain": 0
        }
        """
        skillStats - dict
        Purpose: store player skill stats
        Note: stats are in the form of multipliers
        Ie: 1.2 = 120% of base stat (given in constants usually)
        """
        self.skillStats = {
            "healthRegen": [1, 1.2, 1.4, 1.8, 2.2, 2.6],
            "maxHealth": [1, 1.25, 1.5, 1.75, 2.25, 3.25],
            "speed": [1, 1.1, 1.25, 1.4, 1.55, 1.7],
            "spread": [1, 0.8, 0.6, 0.4, 0.2, 0.1],
            "cooldown": [1, 0.95, 0.9, 0.8, 0.7, 0.6],
            "bulletSpeed": [1, 1.1, 1.2, 1.3, 1.4, 1.5],
            "bulletDamage": [1, 1.15, 1.3, 1.45, 1.65, 1.9],
            "bulletPenetration": [1, 1.1, 1.2, 1.35, 1.5, 1.65],
            "xpGain": [1, 1.05, 1.1, 1.15, 1.2, 1.3]
        }

    def render(self):
        #layered behind the player sprite, place a "circular health bar"
        #this should range from a 0 degree arc at 0 hp to a 360 degree arc at hp=maxhp
        hpArc = ((self.hp/(self.maxHp*self.skillStats["maxHealth"][self.skillTree["maxHealth"]]))*2*math.pi)

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
        if self.hp < self.maxHp * self.skillStats["maxHealth"][self.skillTree["maxHealth"]]:
            self.hp += self.hpRegen * 120/FPS * 0.002 * cycles * self.skillStats["healthRegen"][self.skillTree["healthRegen"]]
        if self.hp > self.maxHp * self.skillStats["maxHealth"][self.skillTree["maxHealth"]]:
            self.hp = self.maxHp * self.skillStats["maxHealth"][self.skillTree["maxHealth"]]

    def skillTreeUpdate(self):
        pass
        #detect player input to spend on skilltree
        #update skill tree

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

            #increment skill points
            self.skillPoints += 1
            
            #spawn particle effect
            for i in range(particlesPerLevelup):
                particleList.append(Particle(player.pos.getX()+cameraPos.getX()+playerWidth/2, player.pos.getY()+cameraPos.getY()+playerWidth/2, random.uniform(0.3, 0.4), random.randint(6, 8), random.choice(xpColor), random.randint(32, 44), Vect(player.vel.getX(), player.vel.getY())))

            #create level up text
            levelUpText = TextHandler("Level up!", font, (0, 20), (255, 255, 255), True, 3, 6)
            distFromLeftSideOfScreen = (screenSize.x - levelUpText.get_width())/2
            levelUpText.pos = (distFromLeftSideOfScreen, 20)
            textList.append(levelUpText)

            #create level up text rect for particles
            levelUpTextRect = pygame.rect.Rect(levelUpText.pos[0], levelUpText.pos[1], levelUpText.get_width(), levelUpText.get_height())
            for i in range (particlesPerLevelupText):
                particlePos = randomPoint(levelUpTextRect)

                particleList.append(Particle(particlePos[0]+cameraPos.getX(), particlePos[1]+cameraPos.getY(), random.uniform(0.3, 0.4), random.randint(6, 8), random.choice(xpColor), random.randint(20, 32)))

    """Player Input - Directional (Keyboard) Input"""
    def handleInputs(self):
        inputRight = pygame.key.get_pressed()[pygame.K_l]+pygame.key.get_pressed()[pygame.K_d]+pygame.key.get_pressed()[pygame.K_RIGHT]
        inputLeft = pygame.key.get_pressed()[pygame.K_j]+pygame.key.get_pressed()[pygame.K_a]+pygame.key.get_pressed()[pygame.K_LEFT]
        inputDown = pygame.key.get_pressed()[pygame.K_k]+pygame.key.get_pressed()[pygame.K_s]+pygame.key.get_pressed()[pygame.K_DOWN]
        inputUp = pygame.key.get_pressed()[pygame.K_i]+pygame.key.get_pressed()[pygame.K_w]+pygame.key.get_pressed()[pygame.K_UP]

        inputVect = Vect(inputRight-inputLeft, inputDown-inputUp)
        
        inputVect.squareClamp(1)

        inputVect.multiply(.1).multiply(120/FPS)

        if inputVect.getMagnitude() == 0:
            inputVect = Vect(self.vel.getX()*(decelConst), self.vel.getY()*(decelConst)).multiply(120/FPS)

        self.vel.add(inputVect)

        if self.vel.getMagnitude() <= 0.0001*120/FPS:
            self.vel = Vect(0,0)

        if self.vel.getMagnitude() > playerMaxVelocity * self.skillStats["speed"][self.skillTree["speed"]]:
            self.vel.unitize(playerMaxVelocity * self.skillStats["speed"][self.skillTree["speed"]])#*120/FPS)

    """Player Input - Mouse Input"""
    def handleClickShoot(self):
        """Mouse Input"""
        mousePos = Vect(pygame.mouse.get_pos()[0]-self.pos.getX(), pygame.mouse.get_pos()[1]-self.pos.getY())
        mousePos.unitize()

        """Click to Shoot"""
        if(pygame.mouse.get_pressed(3)[0]): 
            for i in playerShooters:
                if i.cooldownFrames <= 0:
                    i.shoot(
                        Vect(self.pos.getX()+cameraPos.getX()+playerWidth/2,self.pos.getY()+cameraPos.getY()+playerWidth/2), 
                        math.atan2(mousePos.getY(), mousePos.getX()), 
                        True,
                        [
                            self.skillStats["spread"][self.skillTree["spread"]],
                            self.skillStats["bulletSpeed"][self.skillTree["bulletSpeed"]],
                            self.skillStats["bulletDamage"][self.skillTree["bulletDamage"]],
                            self.skillStats["bulletPenetration"][self.skillTree["bulletPenetration"]]
                        ]
                    )
                    i.cooldownFrames = FPS * i.cooldown * self.skillStats["cooldown"][self.skillTree["cooldown"]]

player = Player(Vect(screenSize.getX()/2 - playerWidth/2,screenSize.getY()/2 - playerWidth/2), Vect(0,0))