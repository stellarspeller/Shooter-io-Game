import pygame
import math
pygame.init()
from src.constants import *
from data.bullets import *
from src.enemy import *
from data import *
from src.waveHandler import *
from src.textHandler import *

running = True

enemyList.append(Enemy(Vect(70,70), "red"))

playerShooters.append(Shooter(.4, bulletTypes["basic"], 0))
#playerShooters.append(Shooter(.9, bulletTypes["cannonball"], 0))
#bgMusic = pygame.mixer.Sound("res/sound/music/tis.wav")
#pygame.mixer.music.load("res/sound/music/tis.wav")
#pygame.mixer.music.play(-1)

#skillTreeUIList.append(TextHandler("9 - Xp Multiplier", fontSmall1, Vect(10, screenSize.y - 10), white))



"""if frameCount < 240:
        for i in particlePositions:
            pygame.draw.rect(screen, white, (logoPixelSize*i[0]+100, logoPixelSize*i[1]+100, logoPixelSize, logoPixelSize))
    if len(particleList) <= 0 and frameCount >= 240 and frameCount <= 240+logoPixelSize*6:
        for i in particlePositions:
            particleList.append(Particle(logoPixelSize*i[0]+100, logoPixelSize*i[1]+100, 1, logoPixelSize, white, 6))"""

pygame.mouse.set_visible(False)

clock = pygame.time.Clock()
# game loop
while running:
    #Stuff with frame counting
    clock.tick(FPS)
    frameCount += 1

    for i in playerShooters:
        if i.cooldownFrames > 0:
            i.cooldownFrames -= 1

    for i in enemyList:
        for j in i.personalShooterList:
            if j.cooldownFrames > 0:
                j.cooldownFrames -= 1


    """Spawning New Enemies"""
    waveHandler.update()


    """Rendering:"""

    #background and grid
    screen.fill(background_color)
    for i in range(round(screenSize.getRoundX()/lineDensity)+2):
        pygame.draw.line(screen, white, ((lineDensity*i)-cameraPos.getRoundX()%lineDensity, -10), ((lineDensity*i)-cameraPos.getRoundX()%lineDensity, screenSize.getY()+10), lineThickness)
    for i in range(round(screenSize.getY()/lineDensity)+2):
        pygame.draw.line(screen, white, (-10, ((lineDensity*i)-cameraPos.getRoundY()%lineDensity)), (screenSize.getX()+10, (lineDensity*i)-cameraPos.getRoundY()%lineDensity), lineThickness)
    
    #particles
    for i in particleList:
        i.update()
        i.render()

    #xp particles
    for i in xpList:
        i.update()
        i.render()

    #bullets
    for i in bulletList:
        i.update()
        i.render()

    #enemies
    for i in enemyList:
        i.update()

    #the player

    """Player Input"""
    player.handleInputs()
    player.handleClickShoot()

    """Playout Output"""
    player.update()
    player.render()
    player.checkBulletCollision()
    player.checkLevelUp()
    #print(player.hp)

    """UI"""
    #crosshare
    mousePos = Vect(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    pygame.draw.rect(screen, black, (mousePos.getX()-9, mousePos.getY()-1, 20, 4))
    pygame.draw.rect(screen, black, (mousePos.getX()-1, mousePos.getY()-9, 4, 20))

    pygame.draw.rect(screen, white, (mousePos.getX()-8, mousePos.getY(), 18, 2))
    pygame.draw.rect(screen, white, (mousePos.getX(), mousePos.getY()-8, 2, 18))

    #text = font.render(str(player.xp) + "/" + str(xpToLevelUp[player.level-1]) + " xp\nlevel " + str(player.level), True, white)
    levelText = font.render("Level " + str(player.level), True, white)
    levelTextRect = levelText.get_rect()
    levelTextRect.topleft = (20, 20)
    screen.blit(levelText, levelTextRect)

    xpText = fontSmall1.render(str(math.floor(player.xp)) + "/" + str(xpToLevelUp[player.level-1]) + " xp", True, white)
    xpTextRect = xpText.get_rect()
    xpTextRect.topleft = levelTextRect.bottomleft
    screen.blit(xpText, xpTextRect)

    skillText = fontSmall1.render("Skill Points: " + str(player.skillPoints), True, white)
    skillTextRect = skillText.get_rect()
    skillTextRect.topleft = xpTextRect.bottomleft
    screen.blit(skillText, skillTextRect)

    #skill tree spending ui
    #detect shift pressed, make this a toggle
    if (pygame.key.get_pressed()[pygame.K_LSHIFT] or pygame.key.get_pressed()[pygame.K_RSHIFT]) and not skillTreeUICooldown:
        skillTreeUI = not skillTreeUI
        skillTreeUICooldown = True
    elif not (pygame.key.get_pressed()[pygame.K_LSHIFT] or pygame.key.get_pressed()[pygame.K_RSHIFT]):
        skillTreeUICooldown = False
        
    
    #skill tree:
    """
    "healthRegen": 0,
            "maxHealth": 0,
            "speed": 0,
            "spread": 0,
            "cooldown": 0,
            "bulletSpeed": 0,
            "bulletDamage": 0,
            "bulletPenetration": 0,
            "xpGain": 0
    """

    if skillTreeUI:
        skillTreeUIList = [
            TextHandler(f"{player.skillTree['xpGain']}/5 - Xp Multiplier - 9", fontSmall2, (10, screenSize.y - 30), white),
            TextHandler(f"{player.skillTree['bulletPenetration']}/5 - Bullet Penetration - 8", fontSmall2, (10, screenSize.y - 50), white),
            TextHandler(f"{player.skillTree['bulletDamage']}/5 - Bullet Damage - 7", fontSmall2, (10, screenSize.y - 70), white),
            TextHandler(f"{player.skillTree['bulletSpeed']}/5 - Bullet Speed - 6", fontSmall2, (10, screenSize.y - 90), white),
            TextHandler(f"{player.skillTree['cooldown']}/5 - Cooldown - 5", fontSmall2, (10, screenSize.y - 110), white),
            TextHandler(f"{player.skillTree['spread']}/5 - Bullet Spread - 4", fontSmall2, (10, screenSize.y - 130), white),
            TextHandler(f"{player.skillTree['maxHealth']}/5 - Max Health - 3", fontSmall2, (10, screenSize.y - 150), white),
            TextHandler(f"{player.skillTree['speed']}/5 - Speed - 2", fontSmall2, (10, screenSize.y - 170), white),
            TextHandler(f"{player.skillTree['healthRegen']}/5 - Health Regen - 1", fontSmall2, (10, screenSize.y - 190), white),
        ]
        for i in skillTreeUIList:
            i.update()
            i.render()

        #check for inputs to upgrade
        keys = [
            pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5,
            pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9
        ]
        stats = [
            "healthRegen", "speed", "maxHealth", "spread", "cooldown",
            "bulletSpeed", "bulletDamage", "bulletPenetration", "xpGain"
        ]

        for i, key in enumerate(keys):
            if pygame.key.get_pressed()[key] and ((not pressedSkillTree) and player.skillPoints >= 1):
                pressedSkillTree = True
                player.skillPoints -= 1
                #print(((not pressedSkillTree) and player.skillPoints >= 1))
                #print(player.skillPoints)
                player.skillTree[stats[i]] += 1
                break
        allKeysNotPressed = all(not pygame.key.get_pressed()[key] for key in keys)
        if allKeysNotPressed:
            pressedSkillTree = False



    #wave UI
    waveText = font.render("Wave " + str(waveHandler.waveNum), True, white)
    waveTextRect = waveText.get_rect()
    waveTextRect.topright = (screenSize.x - 20, 20)
    screen.blit(waveText, waveTextRect)

    for i in textList:
        i.update()
        i.render()


    #additional testing
    particleList.append(Particle(400, 400, 1.1, 10, white, 10))

    #draw all to screen
    pygame.display.update()

    for event in pygame.event.get():
      
        # Check for QUIT event      
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.VIDEORESIZE:
            # If the window is resized, get the new dimensions and update the screen
            #WIDTH, HEIGHT = event.w, event.h
            screenSizeTempX = screenSize.x
            screenSizeTempY = screenSize.y
            screenSize.x = event.w
            screenSize.y = event.h
            screen = pygame.display.set_mode((screenSize.getX(), screenSize.getY()), pygame.RESIZABLE)
            #cameraPos = Vect(cameraPos.getX() - round(-(screenSize.x-screenSizeTempX)/2), cameraPos.getY() - round(-(screenSize.y-screenSizeTempY)/2))
            cameraPos.x -= (screenSize.x-screenSizeTempX)/2
            cameraPos.y -= (screenSize.y-screenSizeTempY)/2
            player.pos = Vect(screenSize.getX()/2 - playerWidth/2, screenSize.getY()/2 - playerWidth/2)
    #print(spawningThresholds)
    #print(waveHandler.waveNum)