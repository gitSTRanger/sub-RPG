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
    f'{classes.Colors.GREEN}Лес{classes.Colors.WHITE}',
    f'{classes.Colors.GREEN}Дикий Лес{classes.Colors.WHITE}',
    f'{classes.Colors.YELLOW}Замок{classes.Colors.WHITE}',
    f'{classes.Colors.RED}Расплавленная долина{classes.Colors.WHITE}',
    f'{classes.Colors.CYAN}Замороженное Озеро{classes.Colors.WHITE}',
    f'{classes.Colors.BLUE}Ледяная Крепость{classes.Colors.WHITE}',
    f'{classes.Colors.PINK}Эфирные Берега{classes.Colors.WHITE}',
    
]
