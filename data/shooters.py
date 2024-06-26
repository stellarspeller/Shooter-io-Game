from src.constants import *
from src.shooter import *
from data.bullets import *
shooterUpgrades = {
    "primary": [
        [
            Shooter(.4, bulletTypes["basic"], 0)
        ], #initial primary weapon
        [
            Shooter(.4, bulletTypes["basic"], 0), 
            Shooter(.7, bulletTypes["basic"], 0)
        ],
        [
            Shooter(.4, bulletTypes["basic"], 0), 
            Shooter(.55, bulletTypes["basic"], 0)
        ],
        [
            Shooter(.4, bulletTypes["basic"], 0), 
            Shooter(1.9, bulletTypes["cannonball"], 0)
        ],
        [
            Shooter(.35, bulletTypes["basic"], 0), 
            Shooter(1.7, bulletTypes["cannonball"], 0), 
            Shooter(1.4, bulletTypes["sniper"], 0)
        ],
        [
            Shooter(.3, bulletTypes["basic"], 0), 
            Shooter(1.4, bulletTypes["cannonball"], 0), 
            Shooter(1.2, bulletTypes["sniper"], 0)
        ],
        [
            Shooter(.3, bulletTypes["basic"], 0), 
            Shooter(.45, bulletTypes["basic"], 0), 
            Shooter(1.5, bulletTypes["cannonball"], 0), 
            Shooter(1.1, bulletTypes["sniper"], 0)
        ],
        [
            Shooter(.25, bulletTypes["basic"], 0), 
            Shooter(.4, bulletTypes["basic"], 0), 
            Shooter(1.4, bulletTypes["cannonball"], 0), 
            Shooter(1.1, bulletTypes["cannonball"], 0), 
            Shooter(1, bulletTypes["sniper"], 0)]
    ],
    "secondary": [
        [], #player has no initial secondary weapons
        [
            Shooter(0.65, bulletTypes["machineFire"], -0.15), 
            Shooter(0.65, bulletTypes["machineFire"], 0.15)
        ],
        [
            Shooter(0.65, bulletTypes["machineFire"], -0.15), 
            Shooter(0.65, bulletTypes["machineFire"], 0.15), 
            Shooter(0.95, bulletTypes["machineFire"], -0.25), 
            Shooter(0.95, bulletTypes["machineFire"], 0.25)
        ],
        [
            Shooter(0.35, bulletTypes["machineFire"], -0.15), 
            Shooter(0.35, bulletTypes["machineFire"], 0.15), 
            Shooter(0.45, bulletTypes["machineFire"], -0.25), 
            Shooter(0.45, bulletTypes["machineFire"], 0.25)
        ],
        [
            Shooter(0.35, bulletTypes["machineFire"], -0.15), 
            Shooter(0.35, bulletTypes["machineFire"], 0.15), 
            Shooter(0.45, bulletTypes["machineFire"], -0.25), 
            Shooter(0.45, bulletTypes["machineFire"], 0.25), 
            Shooter(0.35, bulletTypes["machineFire"], -0.1), 
            Shooter(0.35, bulletTypes["machineFire"], 0.1)
        ],
        [
            Shooter(0.3, bulletTypes["machineFire"], -0.15), 
            Shooter(0.3, bulletTypes["machineFire"], 0.15), 
            Shooter(0.4, bulletTypes["machineFire"], -0.25), 
            Shooter(0.4, bulletTypes["machineFire"], 0.25), 
            Shooter(0.3, bulletTypes["machineFire"], -0.1), 
            Shooter(0.3, bulletTypes["machineFire"], 0.1), 
            Shooter(0.3, bulletTypes["machineFire"], -0.05), 
            Shooter(0.3, bulletTypes["machineFire"], 0.05)
        ],
    ],
    "tertiary": [
        [], #player has no initial tertiary weapons
        [
            Shooter(1.6, bulletTypes["machineFire"], 0), 
            Shooter(1.6, bulletTypes["machineFire"], math.pi)
        ],
        [
            Shooter(1.4, bulletTypes["machineFire"], 0), 
            Shooter(1.4, bulletTypes["machineFire"], math.pi), 
            Shooter(1.4, bulletTypes["machineFire"], math.pi/2), 
            Shooter(1.4, bulletTypes["machineFire"], -math.pi/2)
        ],
        [
            Shooter(1.1, bulletTypes["machineFire"], 0), 
            Shooter(1.1, bulletTypes["machineFire"], math.pi), 
            Shooter(1.1, bulletTypes["machineFire"], math.pi/2), 
            Shooter(1.1, bulletTypes["machineFire"], -math.pi/2)
        ],
        [
            Shooter(0.95, bulletTypes["basic"], 0), 
            Shooter(0.95, bulletTypes["basic"], math.pi), 
            Shooter(0.95, bulletTypes["basic"], math.pi/2), 
            Shooter(0.95, bulletTypes["basic"], -math.pi/2)
        ],
        [
            Shooter(0.95, bulletTypes["basic"], 0), 
            Shooter(0.95, bulletTypes["basic"], math.pi), 
            Shooter(0.95, bulletTypes["basic"], math.pi/2), 
            Shooter(0.95, bulletTypes["basic"], -math.pi/2), 
            Shooter(0.95, bulletTypes["basic"], -math.pi/4), 
            Shooter(0.95, bulletTypes["basic"], math.pi/4), 
            Shooter(0.95, bulletTypes["basic"], -math.pi*3/4), 
            Shooter(0.95, bulletTypes["basic"], math.pi*3/4)
        ],
        [
            Shooter(0.7, bulletTypes["basic"], 0), 
            Shooter(0.7, bulletTypes["basic"], math.pi), 
            Shooter(0.7, bulletTypes["basic"], math.pi/2), 
            Shooter(0.7, bulletTypes["basic"], -math.pi/2), 
            Shooter(0.7, bulletTypes["basic"], -math.pi/4), 
            Shooter(0.7, bulletTypes["basic"], math.pi/4), 
            Shooter(0.7, bulletTypes["basic"], -math.pi*3/4), 
            Shooter(0.7, bulletTypes["basic"], math.pi*3/4)
        ],
        [
            Shooter(0.7, bulletTypes["sniper"], 0), 
            Shooter(0.7, bulletTypes["sniper"], math.pi), 
            Shooter(0.7, bulletTypes["sniper"], math.pi/2), 
            Shooter(0.7, bulletTypes["sniper"], -math.pi/2), 
            Shooter(0.7, bulletTypes["sniper"], -math.pi/4), 
            Shooter(0.7, bulletTypes["sniper"], math.pi/4), 
            Shooter(0.7, bulletTypes["sniper"], -math.pi*3/4), 
            Shooter(0.7, bulletTypes["sniper"], math.pi*3/4)
        ],
        [
            Shooter(0.7, bulletTypes["sniper"], 0), 
            Shooter(0.7, bulletTypes["sniper"], math.pi), 
            Shooter(0.7, bulletTypes["sniper"], math.pi/2), 
            Shooter(0.7, bulletTypes["sniper"], -math.pi/2), 
            Shooter(0.7, bulletTypes["sniper"], -math.pi/4), 
            Shooter(0.7, bulletTypes["sniper"], math.pi/4), 
            Shooter(0.7, bulletTypes["sniper"], -math.pi*3/4), 
            Shooter(0.7, bulletTypes["sniper"], math.pi*3/4), 
            Shooter(0.7, bulletTypes["sniper"], math.pi/8), 
            Shooter(0.7, bulletTypes["sniper"], -math.pi/8), 
            Shooter(0.7, bulletTypes["sniper"], -math.pi*3/8), 
            Shooter(0.7, bulletTypes["sniper"], math.pi*3/8), 
            Shooter(0.7, bulletTypes["sniper"], math.pi*5/8), 
            Shooter(0.7, bulletTypes["sniper"], -math.pi*5/8), 
            Shooter(0.7, bulletTypes["sniper"], -math.pi*7/8), 
            Shooter(0.7, bulletTypes["sniper"], math.pi*7/8)
        ],
    ]
}