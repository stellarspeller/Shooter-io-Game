from data.bullets import *
from src.shooter import *

enemyData = {
    "red":{
        "hp":10,
        "maxVelocity":1.6,
        "shooters":[
            Shooter(1.1, bulletTypes["basic"], 0)
        ],
        "sprite":pygame.image.load("res/enemies/RED.png").convert_alpha(),
        "particleColor":(255,0,0),
        "rotationPerSecond":0.1,
        "xpReleased":10
    },
    "orange":{
        "hp":18,
        "maxVelocity":2.2,
        "shooters":[
            Shooter(1.2, bulletTypes["basic"], 0), 
            Shooter(1.6, bulletTypes["basic"], 0)
        ],
        "sprite":pygame.image.load("res/enemies/ORANGE.png").convert_alpha(),
        "particleColor":(255,127,0),
        "rotationPerSecond":0.15,
        "xpReleased":14
    },
    "yellow":{
        "hp":21,
        "maxVelocity":3,
        "shooters":[
            Shooter(.9, bulletTypes["basic"], 0), 
            Shooter(1.3, bulletTypes["basic"], -0.4),
            Shooter(1.3, bulletTypes["basic"], 0.4)
        ],
        "sprite":pygame.image.load("res/enemies/YELLOW.png").convert_alpha(),
        "particleColor":(255,255,0),
        "rotationPerSecond":0.2,
        "xpReleased":20
    },
    "green":{
        "hp":18,
        "maxVelocity":3.5,
        "shooters":[
            Shooter(1.2, bulletTypes["basic"], 0), 
            Shooter(1.4, bulletTypes["machineFire"], -0.15),
            Shooter(1.4, bulletTypes["machineFire"], 0.15),
            Shooter(1.7, bulletTypes["machineFire"], -0.3),
            Shooter(1.7, bulletTypes["machineFire"], 0.3)
        ],
        "sprite":pygame.image.load("res/enemies/GREEN.png").convert_alpha(),
        "particleColor":(0,255,0),
        "rotationPerSecond":0.25,
        "xpReleased":22
    },
    "cyan":{
        "hp":38,
        "maxVelocity":1.9,
        "shooters":[
            Shooter(2.3, bulletTypes["basic"], 0), 
            Shooter(2.5, bulletTypes["basic"], 0), 
            Shooter(2, bulletTypes["cannonball"], 0), 
        ],
        "sprite":pygame.image.load("res/enemies/CYAN.png").convert_alpha(),
        "particleColor":(0,255,255),
        "rotationPerSecond":0.3,
        "xpReleased":44
    },
    "blue":{
        "hp":40,
        "maxVelocity":2.4,
        "shooters":[
            Shooter(1.4, bulletTypes["sniper"], 0), 
            Shooter(1.4, bulletTypes["basic"], -0.2), 
            Shooter(1.4, bulletTypes["basic"], 0.2), 
            Shooter(1.4, bulletTypes["basic"], -0.1),
            Shooter(1.4, bulletTypes["basic"], 0.1)
        ],
        "sprite":pygame.image.load("res/enemies/BLUE.png").convert_alpha(),
        "particleColor":(0,0,255),
        "rotationPerSecond":0.35,
        "xpReleased":42
    },
    "purple":{
        "hp":62,
        "maxVelocity":2.6,
        "shooters":[
            Shooter(0.4, bulletTypes["machineFire"], 0), 
            Shooter(1.1, bulletTypes["basic"], -0.1),
            Shooter(1.1, bulletTypes["basic"], 0.1)
        ],
        "sprite":pygame.image.load("res/enemies/PURPLE.png").convert_alpha(),
        "particleColor":(127,0,255),
        "rotationPerSecond":0.4,
        "xpReleased":52
    },
    "pink":{
        "hp":75,
        "maxVelocity":2.6,
        "shooters":[
            Shooter(0.8, bulletTypes["cannonball"], 0), 
            Shooter(1.1, bulletTypes["sniper"], -0.08),
            Shooter(1.1, bulletTypes["sniper"], 0.08)
        ],
        "sprite":pygame.image.load("res/enemies/PINK.png").convert_alpha(),
        "particleColor":(255,0,255),
        "rotationPerSecond":0.45,
        "xpReleased":60
    },

    "red2":{
        "hp":20,
        "maxVelocity":1.4,
        "shooters":[
            Shooter(0.9, bulletTypes["basic"], 0)
        ],
        "sprite":pygame.image.load("res/enemies/RED.png").convert_alpha(),
        "particleColor":(255,0,0),
        "rotationPerSecond":0.1,
        "xpReleased":20
    },
    "orange2":{
        "hp":36,
        "maxVelocity":1.9,
        "shooters":[
            Shooter(1.2, bulletTypes["basic"], 0), 
            Shooter(1.6, bulletTypes["basic"], 0),
            Shooter(2.0, bulletTypes["basic"], 0),
            Shooter(2.4, bulletTypes["basic"], 0)
        ],
        "sprite":pygame.image.load("res/enemies/ORANGE.png").convert_alpha(),
        "particleColor":(255,127,0),
        "rotationPerSecond":0.15,
        "xpReleased":28
    },
    "yellow2":{
        "hp":42,
        "maxVelocity":2.6,
        "shooters":[
            Shooter(1.1, bulletTypes["sniper"], 0), 
            Shooter(1.3, bulletTypes["basic"], -0.4),
            Shooter(1.3, bulletTypes["basic"], 0.4),
            Shooter(1.4, bulletTypes["basic"], -0.7),
            Shooter(1.4, bulletTypes["basic"], 0.7),
        ],
        "sprite":pygame.image.load("res/enemies/YELLOW.png").convert_alpha(),
        "particleColor":(255,255,0),
        "rotationPerSecond":0.2,
        "xpReleased":40
    },
    "green2":{
        "hp":36,
        "maxVelocity":4.4,
        "shooters":[
            Shooter(1.2, bulletTypes["sniper"], 0), 
            Shooter(1.4, bulletTypes["basic"], -0.15),
            Shooter(1.4, bulletTypes["basic"], 0.15),
            Shooter(1.7, bulletTypes["basic"], -0.3),
            Shooter(1.7, bulletTypes["basic"], 0.3)
        ],
        "sprite":pygame.image.load("res/enemies/GREEN.png").convert_alpha(),
        "particleColor":(0,255,0),
        "rotationPerSecond":0.25,
        "xpReleased":44
    },
    "cyan2":{
        "hp":76,
        "maxVelocity":1.4,
        "shooters":[
            Shooter(1.3, bulletTypes["basic"], 0), 
            Shooter(1.5, bulletTypes["basic"], 0), 
            Shooter(1.4, bulletTypes["cannonball"], 0), 
            Shooter(5, bulletTypes["cannonball"], 0), 
        ],
        "sprite":pygame.image.load("res/enemies/CYAN.png").convert_alpha(),
        "particleColor":(0,255,255),
        "rotationPerSecond":0.3,
        "xpReleased":44
    },
    "blue2":{
        "hp":80,
        "maxVelocity":1.7,
        "shooters":[
            Shooter(1.1, bulletTypes["sniper"], 0), 
            Shooter(1.8, bulletTypes["basic"], -0.4), 
            Shooter(1.8, bulletTypes["basic"], 0.4), 
            Shooter(1.6, bulletTypes["basic"], -0.3), 
            Shooter(1.6, bulletTypes["basic"], 0.3), 
            Shooter(1.4, bulletTypes["basic"], -0.2), 
            Shooter(1.4, bulletTypes["basic"], 0.2), 
            Shooter(1.2, bulletTypes["basic"], -0.1),
            Shooter(1.2, bulletTypes["basic"], 0.1)
        ],
        "sprite":pygame.image.load("res/enemies/BLUE.png").convert_alpha(),
        "particleColor":(0,0,255),
        "rotationPerSecond":0.35,
        "xpReleased":84
    },
    "purple2":{
        "hp":124,
        "maxVelocity":2.1,
        "shooters":[
            Shooter(0.25, bulletTypes["machineFire"], 0), 
            Shooter(0.25, bulletTypes["machineFire"], -0.05), 
            Shooter(0.25, bulletTypes["machineFire"], 0.05), 
            Shooter(1.1, bulletTypes["sniper"], -0.1),
            Shooter(1.1, bulletTypes["sniper"], 0.1)
        ],
        "sprite":pygame.image.load("res/enemies/PURPLE.png").convert_alpha(),
        "particleColor":(127,0,255),
        "rotationPerSecond":0.4,
        "xpReleased":104
    },
    "pink2":{
        "hp":150,
        "maxVelocity":1.7,
        "shooters":[
            Shooter(0.7, bulletTypes["cannonball"], 0), 
            Shooter(1.3, bulletTypes["cannonball"], -0.25), 
            Shooter(1.3, bulletTypes["cannonball"], 0.25), 
            Shooter(0.4, bulletTypes["sniper"], -0.08),
            Shooter(0.4, bulletTypes["sniper"], 0.08)
        ],
        "sprite":pygame.image.load("res/enemies/PINK.png").convert_alpha(),
        "particleColor":(255,0,255),
        "rotationPerSecond":0.45,
        "xpReleased":120
    },
}
