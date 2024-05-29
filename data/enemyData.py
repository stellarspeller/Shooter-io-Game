from data.bullets import *
from src.shooter import *

enemyData = {
    "red":{
        "hp":10,
        "maxVelocity":1.6,
        "shooters":[
            Shooter(.7, bulletTypes["basic"], 0)
        ],
        "sprite":pygame.image.load("res/enemies/RED.png"),
        "particleColor":(255,0,0),
        "rotationPerSecond":0.1,
        "xpValue":10
    },
    "orange":{
        "hp":18,
        "maxVelocity":2.2,
        "shooters":[
            Shooter(.8, bulletTypes["basic"], 0), 
            Shooter(1, bulletTypes["basic"], 0)
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
            Shooter(.6, bulletTypes["basic"], 0), 
            Shooter(.9, bulletTypes["basic"], -0.2),
            Shooter(.9, bulletTypes["basic"], 0.2)
        ],
        "sprite":pygame.image.load("res/enemies/YELLOW.png"),
        "particleColor":(255,255,0),
        "rotationPerSecond":0.2,
        "xpReleased":20
    }
}
