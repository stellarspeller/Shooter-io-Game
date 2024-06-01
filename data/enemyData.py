from data.bullets import *
from src.shooter import *

enemyData = {
    "red":{
        "hp":10,
        "maxVelocity":1.6,
        "shooters":[
            Shooter(1.1, bulletTypes["basic"], 0)
        ],
        "sprite":pygame.image.load("res/enemies/RED.png"),
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
        "sprite":pygame.image.load("res/enemies/ORANGE.png"),
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
        "sprite":pygame.image.load("res/enemies/YELLOW.png"),
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
        "sprite":pygame.image.load("res/enemies/GREEN.png"),
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
        "sprite":pygame.image.load("res/enemies/GREEN.png"),
        "particleColor":(0,255,255),
        "rotationPerSecond":0.3,
        "xpReleased":44
    }
}
