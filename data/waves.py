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
    #[ {"count":1, "spawnDelay":1, "enemyType":"pink"} ],
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
        {"count":10, "spawnDelay":8, "enemyType":"orange"}
    ], [
        {"count":5, "spawnDelay":2, "enemyType":"orange"},
        {"count":5, "spawnDelay":2, "enemyType":"red"}
    ], [
        {"count":2, "spawnDelay":4, "enemyType":"red"},
        {"count":3, "spawnDelay":2, "enemyType":"orange"},
        {"count":1, "spawnDelay":6, "enemyType":"yellow"}
    ]
]