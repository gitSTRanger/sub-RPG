from modules import classes
from enum import IntEnum

#Logic
ZeroScene = classes.Event
Scene: classes.Event = ZeroScene

curEventId = 0

class Locations(IntEnum):
    Forest = 0
    WildForest = 1
    Castle = 2
    MoltenValley = 3
    IceLake = 4
    IceStronghold = 5
    EtherealShores = 6

LOCATION = Locations.Forest

stringLocation =[
    f'Лес',
    f'Дикий Лес',
    f'Замок',
    f'Расплавленная долина',
    f'Замороженное Озеро',
    f'Ледяная Крепость',
    f'Эфирные Берега',
    
]
