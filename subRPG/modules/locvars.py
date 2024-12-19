from modules import classes
from enum import IntEnum

#Logic
ZeroScene = classes.Event
Scene: classes.Event = ZeroScene

curEventId = 0

class Locations(IntEnum):
    Forest = 0
    WildForest = 1
    SpiderForest = 2
    Castle = 3
    MoltenValley = 4
    IceLake = 5
    IceStronghold = 6
    EtherealShores = 7

LOCATION = Locations.Forest

stringLocation =[
    f'Лес',
    f'Дикий Лес',
    f'Паучий Лес',
    f'Замок',
    f'Расплавленная долина',
    f'Замороженное Озеро',
    f'Ледяная Крепость',
    f'Эфирные Берега',
    
]
