import pygame
import math
pygame.init()
from src.constants import *
from data.bullets import *
from src.enemy import *
from data import *
from src.waveHandler import *
from src.textHandler import *
from data.shooters import *

running = True
print(f"Waves: {len(waveData)}")
print(f"Levels: {len(xpToLevelUp)}")
#enemyList.append(Enemy(Vect(70,70), "red"))

#playerShooters[0].append(Shooter(.4, bulletTypes["basic"], 0))
#playerShooters[0] = shooterUpgrades["primary"][0]
#playerShooters[1] = shooterUpgrades["secondary"][0]
#playerShooters[2] = shooterUpgrades["tertiary"][0]
#playerShooters[0].append(Shooter(.9, bulletTypes["cannonball"], 0))
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

    for i in player.playerShooters:
        for j in i:
            for k in j:
                if k.cooldownFrames > 0:
                    k.cooldownFrames -= 1

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
        if i.hp <= 0:
            i.kill()

    """Player Input"""
    player.handleInputs()
    player.handleClickShoot()

    """Playout Output"""
    player.update()
    player.render()
    player.checkBulletCollision()
    #player.checkLevelUp() not used since player level is checked upon xp particle pickup

    """UI"""
    #crosshare
    mousePos = Vect(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    pygame.draw.rect(screen, black, (mousePos.getX()-9, mousePos.getY()-1, 20, 4))
    pygame.draw.rect(screen, black, (mousePos.getX()-1, mousePos.getY()-9, 4, 20))

    pygame.draw.rect(screen, white, (mousePos.getX()-8, mousePos.getY(), 18, 2))
    pygame.draw.rect(screen, white, (mousePos.getX(), mousePos.getY()-8, 2, 18))

    #text = font.render(str(player.xp) + "/" + str(xpToLevelUp[player.level-1]) + " xp\nlevel " + str(player.level), True, white)
    levelTextObj = TextHandler("Level " + str(player.level), font, (20, 20), white)
    levelTextObj.render()
    levelTextObj.update()

    if player.level <= 99:
        xpTextObj = TextHandler(str(math.floor(player.xp)) + "/" + str(xpToLevelUp[player.level-1]) + " xp", fontSmall1, (20, levelTextObj.get_height()+20), white)
    else:
        xpTextObj = TextHandler("Max Level", fontSmall1, (20, levelTextObj.get_height()+20), white)
    xpTextObj.render()
    xpTextObj.update()

    skillTextObj = TextHandler("Skill Points: " + str(player.skillPoints), fontSmall1, (20, levelTextObj.get_height()+xpTextObj.get_height()+20), white)
    skillTextObj.render()
    skillTextObj.update()

    #skill tree spending ui
    #detect shift pressed, make this a toggle
    if (pygame.key.get_pressed()[pygame.K_LSHIFT] or pygame.key.get_pressed()[pygame.K_RSHIFT]) and not skillTreeUICooldown:
        skillTreeUI = not skillTreeUI
        skillTreeUICooldown = True
    elif not (pygame.key.get_pressed()[pygame.K_LSHIFT] or pygame.key.get_pressed()[pygame.K_RSHIFT]):
        skillTreeUICooldown = False
        
    if (pygame.key.get_pressed()[pygame.K_TAB]) and not cannonUpgradeUICooldown:
        cannonUpgradeUI = not cannonUpgradeUI
        cannonUpgradeUICooldown = True
    elif not (pygame.key.get_pressed()[pygame.K_TAB]):
        cannonUpgradeUICooldown = False
    
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
            "xpBoost": 0
    """

    if skillTreeUI:
        skillTreeUIList = [
            TextHandler(f"{player.skillTree['xpBoost']}/5 - Xp Multiplier - 9", fontSmall2, (10, screenSize.y - 30), white),
            TextHandler(f"{player.skillTree['bulletPenetration']}/5 - Bullet Penetration - 8", fontSmall2, (10, screenSize.y - 50), white),
            TextHandler(f"{player.skillTree['bulletDamage']}/5 - Bullet Damage - 7", fontSmall2, (10, screenSize.y - 70), white),
            TextHandler(f"{player.skillTree['bulletSpeed']}/5 - Bullet Speed - 6", fontSmall2, (10, screenSize.y - 90), white),
            TextHandler(f"{player.skillTree['cooldown']}/5 - Cooldown - 5", fontSmall2, (10, screenSize.y - 110), white),
            TextHandler(f"{player.skillTree['spread']}/5 - Bullet Spread - 4", fontSmall2, (10, screenSize.y - 130), white),
            TextHandler(f"{player.skillTree['maxHealth']}/5 - Max Health - 3", fontSmall2, (10, screenSize.y - 150), white),
            TextHandler(f"{player.skillTree['speed']}/5 - Player Speed - 2", fontSmall2, (10, screenSize.y - 170), white),
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
            "bulletSpeed", "bulletDamage", "bulletPenetration", "xpBoost"
        ]

        for i, key in enumerate(keys):
            if pygame.key.get_pressed()[key] and ((not pressedSkillTree) and player.skillPoints >= 1 and player.skillTree[stats[i]] < 5):
                pressedSkillTree = True
                player.skillPoints -= 1
                player.skillTree[stats[i]] += 1
                break
        allKeysNotPressed = all(not pygame.key.get_pressed()[key] for key in keys)
        if allKeysNotPressed:
            pressedSkillTree = False

    if cannonUpgradeUI:
        cannonUpgradeUIList = [
            TextHandler(
                f"{player.shooterTree['primary']+1}/{len(shooterUpgrades['primary'])} - Primary [b]",
                fontSmall2, (screenSize.x - 190, screenSize.y - 30), white
            ),
            TextHandler(
                f"{player.shooterTree['secondary']+1}/{len(shooterUpgrades['secondary'])} - Spread [n]",
                fontSmall2, (screenSize.x - 190, screenSize.y - 50), white
            ),
            TextHandler(
                f"{player.shooterTree['tertiary']+1}/{len(shooterUpgrades['tertiary'])} - Surround [m]",
                fontSmall2, (screenSize.x - 190, screenSize.y - 70), white
            )
        ]
        for i in cannonUpgradeUIList:
            i.update()
            i.render()
        #check for inputs to upgrade
        keys = [
            pygame.K_b, pygame.K_n, pygame.K_m
        ]
        stats = [
            "primary", "secondary", "tertiary"
        ]

        for i, key in enumerate(keys):
            if pygame.key.get_pressed()[key] and ((not pressedCannonUpgrade) and player.pendingShooterUpgrades >= 1 and player.shooterTree[stats[i]] < len(shooterUpgrades[stats[i]])-1):
                pressedCannonUpgrade = True
                player.pendingShooterUpgrades -= 1
                player.shooterTree[stats[i]] += 1
                player.updateShooterStats()
                break
        allKeysNotPressed = all(not pygame.key.get_pressed()[key] for key in keys)
        if allKeysNotPressed:
            pressedCannonUpgrade = False

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
            screenSizeTempX = screenSize.x
            screenSizeTempY = screenSize.y
            screenSize.x = event.w
            screenSize.y = event.h
            screen = pygame.display.set_mode((screenSize.getX(), screenSize.getY()), pygame.RESIZABLE)
            cameraPos.x -= (screenSize.x-screenSizeTempX)/2
            cameraPos.y -= (screenSize.y-screenSizeTempY)/2
            player.pos = Vect(screenSize.getX()/2 - playerWidth/2, screenSize.getY()/2 - playerWidth/2)