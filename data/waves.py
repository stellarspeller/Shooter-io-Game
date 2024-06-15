from data.enemyData import *
from src.waveHandler import *
#number of each type, delay between spawns, enemy type
waveData = [
    #[ {"count":1, "spawnDelay":1, "enemyType":"red"} ],
    #[ {"count":1, "spawnDelay":1, "enemyType":"orange"} ],
    #[ {"count":1, "spawnDelay":1, "enemyType":"yellow"} ],
    #[ {"count":1, "spawnDelay":1, "enemyType":"green"} ],
    #[ {"count":1, "spawnDelay":1, "enemyType":"cyan"} ],
    #[ {"count":1, "spawnDelay":1, "enemyType":"blue"} ],
    #[ {"count":1, "spawnDelay":1, "enemyType":"purple"} ],
    #[ {"count":1, "spawnDelay":1, "enemyType":"pink2"} ],
    [
        {"count":4, "spawnDelay":5, "enemyType":"red"}
    ], [
        {"count":5, "spawnDelay":4, "enemyType":"red"}
    ], [
        {"count":7, "spawnDelay":5, "enemyType":"red"}
    ], [
        {"count":3, "spawnDelay":5, "enemyType":"red"},
        {"count":3, "spawnDelay":5, "enemyType":"orange"}
    ], [
        {"count":3, "spawnDelay":5, "enemyType":"red"},
        {"count":4, "spawnDelay":4, "enemyType":"orange"}
    ], [
        {"count":6, "spawnDelay":5, "enemyType":"red"},
        {"count":4, "spawnDelay":5, "enemyType":"orange"}
    ], [
        {"count":10,"spawnDelay":8, "enemyType":"orange"}
    ], [
        {"count":5, "spawnDelay":2, "enemyType":"orange"},
        {"count":5, "spawnDelay":2, "enemyType":"red"}
    ], [
        {"count":2, "spawnDelay":4, "enemyType":"red"},
        {"count":3, "spawnDelay":2, "enemyType":"orange"},
        {"count":1, "spawnDelay":6, "enemyType":"yellow"}
    ], [
        {"count":2, "spawnDelay":3, "enemyType":"red"},
        {"count":3, "spawnDelay":1, "enemyType":"orange"},
        {"count":1, "spawnDelay":4, "enemyType":"yellow"}
    ], [
        {"count":3, "spawnDelay":3, "enemyType":"red"},
        {"count":3, "spawnDelay":1, "enemyType":"orange"},
        {"count":2, "spawnDelay":6, "enemyType":"yellow"}
    ], [
        {"count":3, "spawnDelay":3, "enemyType":"red"},
        {"count":3, "spawnDelay":1, "enemyType":"orange"},
        {"count":2, "spawnDelay":6, "enemyType":"yellow"},
        {"count":1, "spawnDelay":8, "enemyType":"green"}
    ], [
        {"count":3, "spawnDelay":4, "enemyType":"green"},
        {"count":3, "spawnDelay":4, "enemyType":"yellow"},
    ], [
        {"count":4, "spawnDelay":3, "enemyType":"green"},
        {"count":4, "spawnDelay":3, "enemyType":"yellow"},
    ], [
        {"count":5, "spawnDelay":3, "enemyType":"green"},
        {"count":5, "spawnDelay":3, "enemyType":"yellow"},
    ], [
        {"count":5, "spawnDelay":3, "enemyType":"green"},
        {"count":10,"spawnDelay":3, "enemyType":"orange"},
    ], [
        {"count":5, "spawnDelay":3, "enemyType":"green"},
        {"count":6,"spawnDelay":5, "enemyType":"yellow"},
        {"count":6,"spawnDelay":5, "enemyType":"red"}
    ], [
        {"count":4, "spawnDelay":3, "enemyType":"green"},
        {"count":4, "spawnDelay":3, "enemyType":"yellow"},
        {"count":2, "spawnDelay":6, "enemyType":"cyan"}
    ], [
        {"count":6, "spawnDelay":4, "enemyType":"green"},
        {"count":3, "spawnDelay":6, "enemyType":"cyan"}
    ], [
        {"count":8, "spawnDelay":3, "enemyType":"green"},
        {"count":3, "spawnDelay":5, "enemyType":"cyan"}
    ], [
        {"count":10, "spawnDelay":3, "enemyType":"green"},
        {"count":4, "spawnDelay":5, "enemyType":"cyan"}
    ], [
        {"count":10, "spawnDelay":3, "enemyType":"green"},
        {"count":6, "spawnDelay":4, "enemyType":"cyan"}
    ], [
        {"count":12, "spawnDelay":2, "enemyType":"green"},
        {"count":7, "spawnDelay":8, "enemyType":"cyan"}
    ], [
        {"count":10, "spawnDelay":3, "enemyType":"green"},
        {"count":4, "spawnDelay":5, "enemyType":"cyan"},
        {"count":3, "spawnDelay":8, "enemyType":"blue"}
    ], [
        {"count":5, "spawnDelay":4, "enemyType":"cyan"},
        {"count":10, "spawnDelay":3, "enemyType":"green"},
        {"count":3, "spawnDelay":8, "enemyType":"blue"}
    ], [
        {"count":5, "spawnDelay":4, "enemyType":"cyan"},
        {"count":12, "spawnDelay":3, "enemyType":"green"},
        {"count":3, "spawnDelay":7, "enemyType":"blue"}
    ], [
        {"count":2, "spawnDelay":2, "enemyType":"purple"},
        {"count":8, "spawnDelay":1, "enemyType":"green"},
        {"count":3, "spawnDelay":7, "enemyType":"blue"}
    ], [
        {"count":3, "spawnDelay":5, "enemyType":"purple"},
        {"count":10,"spawnDelay":3, "enemyType":"yellow"},
        {"count":2, "spawnDelay":7, "enemyType":"blue"}
    ], [
        {"count":3, "spawnDelay":4, "enemyType":"purple"},
        {"count":12,"spawnDelay":3, "enemyType":"yellow"},
        {"count":3, "spawnDelay":6, "enemyType":"blue"}
    ], [
        {"count":5, "spawnDelay":4, "enemyType":"purple"},
        {"count":7, "spawnDelay":2, "enemyType":"cyan"},
    ], [
        {"count":2, "spawnDelay":4, "enemyType":"pink"},
        {"count":11, "spawnDelay":1, "enemyType":"green"},
        {"count":4, "spawnDelay":7, "enemyType":"blue"}
    ], [
        {"count":3, "spawnDelay":3, "enemyType":"pink"},
        {"count":12, "spawnDelay":1, "enemyType":"green"},
        {"count":6, "spawnDelay":5, "enemyType":"blue"}
    ], [
        {"count":3, "spawnDelay":3, "enemyType":"pink"},
        {"count":12, "spawnDelay":1, "enemyType":"green"},
        {"count":6, "spawnDelay":5, "enemyType":"purple"}
    ], [
        {"count":3, "spawnDelay":3, "enemyType":"pink"},
        {"count":12, "spawnDelay":1, "enemyType":"green"},
        {"count":6, "spawnDelay":5, "enemyType":"purple"},
        {"count":2, "spawnDelay":1, "enemyType":"cyan"}
    ], [
        {"count":7, "spawnDelay":4, "enemyType":"pink"},
        {"count":4, "spawnDelay":5, "enemyType":"red2"}
    ], [
        {"count":8, "spawnDelay":3, "enemyType":"pink"},
        {"count":6, "spawnDelay":4, "enemyType":"red2"}
    ], [
        {"count":8, "spawnDelay":3, "enemyType":"pink"},
        {"count":6, "spawnDelay":4, "enemyType":"red2"}
    ], [
        {"count":5, "spawnDelay":3, "enemyType":"pink"},
        {"count":6, "spawnDelay":1, "enemyType":"green"},
        {"count":12, "spawnDelay":5, "enemyType":"purple"},
        {"count":10, "spawnDelay":1, "enemyType":"cyan"}
    ], [
        {"count":5, "spawnDelay":3, "enemyType":"pink"},
        {"count":15,"spawnDelay":5, "enemyType":"red2"},
        {"count":3, "spawnDelay":9, "enemyType":"cyan"}
    ], [
        {"count":7, "spawnDelay":4, "enemyType":"pink"},
        {"count":9, "spawnDelay":3, "enemyType":"orange2"}
    ], [
        {"count":8, "spawnDelay":3, "enemyType":"pink"},
        {"count":10, "spawnDelay":3, "enemyType":"orange2"}
    ], [
        {"count":2, "spawnDelay":1, "enemyType":"red"},
        {"count":3, "spawnDelay":1, "enemyType":"orange"},
        {"count":4, "spawnDelay":2, "enemyType":"yellow"},
        {"count":5, "spawnDelay":2, "enemyType":"green"},
        {"count":6, "spawnDelay":3, "enemyType":"cyan"},
        {"count":7, "spawnDelay":3, "enemyType":"blue"},
        {"count":8, "spawnDelay":4, "enemyType":"purple"},
        {"count":9, "spawnDelay":4, "enemyType":"pink"}
    ], [
        {"count":2, "spawnDelay":1, "enemyType":"red"},
        {"count":4, "spawnDelay":2, "enemyType":"yellow"},
        {"count":6, "spawnDelay":3, "enemyType":"cyan"},
        {"count":8, "spawnDelay":4, "enemyType":"purple"},
        {"count":10, "spawnDelay":5, "enemyType":"orange2"}
    ]
]