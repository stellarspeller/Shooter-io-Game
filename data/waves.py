from data.enemyData import *
from src.waveHandler import *
#number of each type, delay between spawns, enemy type
waveData = [
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
    ]
]