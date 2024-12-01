from modules import classes
from enum import IntEnum


#Logic
ZeroScene = classes.Event
Scene: classes.Event = ZeroScene


class Locations(IntEnum):
    Forest = 0
    WildForest = 1
    Castle = 2
    MoltenValley = 3
    IceLake = 4
    IceCastle = 5
    EtherealShores = 6

LOCATION = Locations.Forest

stringLocation =[
    f'{classes.Colors.GREEN}Лес{classes.Colors.WHITE}',
    f'{classes.Colors.GREEN}Дикий Лес{classes.Colors.WHITE}',
    f'{classes.Colors.YELLOW}Замок{classes.Colors.WHITE}',
    f'{classes.Colors.RED}Расплавленная долина{classes.Colors.WHITE}',
    f'{classes.Colors.CYAN}Ледяное Озеро{classes.Colors.WHITE}',
    f'{classes.Colors.BLUE}Ледяной Замок{classes.Colors.WHITE}',
    f'{classes.Colors.PINK}Эфирные Берега{classes.Colors.WHITE}',
    
]
