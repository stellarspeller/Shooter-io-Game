import pygame
#import random
import math
#from os import system
pygame.init()
#Font=pygame.font.SysFont('fontify.ttf', 96)
from src.constants import *
from data.bullets import *
from src.enemy import *
from data import *

running = True

enemyList.append(Enemy(Vect(70,70), "red"))

playerShooters.append(Shooter(.4, bulletTypes["basic"], 0))
playerShooters.append(Shooter(.9, bulletTypes["cannonball"], 0))


clock = pygame.time.Clock()
# game loop
while running:
    clock.tick(FPS)
    frameCount += 1

    for i in playerShooters:
        if i.cooldownFrames > 0:
            i.cooldownFrames -= 1

    for i in enemyList:
        for j in i.personalShooterList:
            if j.cooldownFrames > 0:
                j.cooldownFrames -= 1



    pygame.display.update()

    for event in pygame.event.get():
      
        # Check for QUIT event      
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.VIDEORESIZE:
            # If the window is resized, get the new dimensions and update the screen
            #WIDTH, HEIGHT = event.w, event.h
            screenSize.x = event.w
            screenSize.y = event.h
            screen = pygame.display.set_mode((screenSize.getX(), screenSize.getY()), pygame.RESIZABLE)
            player.pos = Vect(screenSize.getX()/2 - playerWidth/2, screenSize.getY()/2 - playerWidth/2)



    screen.fill(background_color)


    """Input Handling"""
    inputRight = pygame.key.get_pressed()[pygame.K_l]+pygame.key.get_pressed()[pygame.K_d]+pygame.key.get_pressed()[pygame.K_RIGHT]
    inputLeft = pygame.key.get_pressed()[pygame.K_j]+pygame.key.get_pressed()[pygame.K_a]+pygame.key.get_pressed()[pygame.K_LEFT]
    inputDown = pygame.key.get_pressed()[pygame.K_k]+pygame.key.get_pressed()[pygame.K_s]+pygame.key.get_pressed()[pygame.K_DOWN]
    inputUp = pygame.key.get_pressed()[pygame.K_i]+pygame.key.get_pressed()[pygame.K_w]+pygame.key.get_pressed()[pygame.K_UP]

    inputVect = Vect(inputRight-inputLeft, inputDown-inputUp)
    
    inputVect.clamp(1)

    inputVect.multiply(.1)

    if inputVect.getMagnitude() == 0:
        inputVect = Vect(player.vel.getX()*(decelConst), player.vel.getY()*(decelConst))

    player.vel.add(inputVect)

    if player.vel.getMagnitude() <= 0.0001:
        player.vel = Vect(0,0)

    if player.vel.getMagnitude() > playerMaxVelocity:
        player.vel.unitize(playerMaxVelocity)



    """Mouse Input"""
    mousePos = Vect(pygame.mouse.get_pos()[0]-player.pos.getX(), pygame.mouse.get_pos()[1]-player.pos.getY())
    mousePos.unitize()


    """Click to Shoot"""
    if(pygame.mouse.get_pressed(3)[0]): 
        for i in playerShooters:
            if i.cooldownFrames <= 0:
                i.shoot(Vect(player.pos.getX()+cameraPos.getX()+playerWidth/2,player.pos.getY()+cameraPos.getY()+playerWidth/2), math.atan2(mousePos.getY(), mousePos.getX()), True)
                i.cooldownFrames = FPS * i.cooldown


    """Updating and rendering orders"""
    for i in range(round(screenSize.getRoundX()/lineDensity)+2):
        pygame.draw.line(screen, white, ((lineDensity*i)-cameraPos.getRoundX()%lineDensity, -10), ((lineDensity*i)-cameraPos.getRoundX()%lineDensity, screenSize.getY()+10), lineThickness)
    for i in range(round(screenSize.getY()/lineDensity)+2):
        pygame.draw.line(screen, white, (-10, ((lineDensity*i)-cameraPos.getRoundY()%lineDensity)), (screenSize.getX()+10, (lineDensity*i)-cameraPos.getRoundY()%lineDensity), lineThickness)
    
    for i in particleList:
        #print(i.vel)
        i.update()
        i.render()

    for i in xpList:
        i.update()
        i.render()

    for i in bulletList:
        i.update()
        i.render()

    for i in enemyList:
        i.update()

    player.update()
    player.render()

    """if frameCount < 240:
        for i in particlePositions:
            pygame.draw.rect(screen, white, (logoPixelSize*i[0]+100, logoPixelSize*i[1]+100, logoPixelSize, logoPixelSize))
    if len(particleList) <= 0 and frameCount >= 240 and frameCount <= 240+logoPixelSize*6:
        for i in particlePositions:
            particleList.append(Particle(logoPixelSize*i[0]+100, logoPixelSize*i[1]+100, 1, logoPixelSize, white, 6))"""

    #for i in particleList:
    #    pygame.draw.rect(screen, white, (i.pos.getX(), i.pos.y, i.size, i.size))

    #pygame.draw.rect(screen, white ,(900,150,100,50))

    particleList.append(Particle(400, 400, 1.1, 10, white, 10))

    #print(cameraPos)

    #system.clear()
    print("Particles: " + str(len(particleList)))




    #print(inputVect)

    #inputVect.multiply(-3)

    #cameraPos.add(inputVect)


    #draw player
