from modules import funks
from modules import vars
from modules import locvars
from modules import classes
from copy import deepcopy
import random


print("\nДОБРО ПОЖАЛОВАТЬ В subRPG (1.3)\n")


input("Нажмите ЛУБУЮ КНОПКУ, чтоб НАЧАТЬ играть \n")
vars.clear()


i = input("Нажмите 1 чтобы получить стартовый набор предметов:\n")
vars.clear()
if i == "1":
    funks.TakeRandomItem(vars.StarterPack)
    funks.TakeRandomItem(vars.StarterPack)
    funks.TakeRandomItem(vars.StarterPack)
    vars.actStep = 1


vars.clear()


locvars.ZeroScene = funks.Elist[funks.EventID.Forest]
locvars.Scene = locvars.ZeroScene





#funks.SetLocation(funks.WILD_FOREST_EVENTS, locvars.Locations.WildForest)
#vars.actStep = 32



while vars.HP > 0 and vars.WIN == False:

    funks.CheckLocation()

    if vars.ARMOR <= 0:
                vars.ARMOR = 0

    if vars.curAct != vars.actStep and locvars.Scene == locvars.ZeroScene:

        if funks.Elist != funks.FOREST_BOSS_EVENTS:

            randomEvent = random.randint(0, len(funks.Elist)-1)

            locvars.Scene = funks.Elist[randomEvent]
            curAct = vars.actStep

        
            if randomEvent == funks.EventID.StartFight or randomEvent == funks.EventID.OnFight:
                vars.clear()
                funks.StartFight()
            
            funks.CheckBuffs() 

     
    
    funks.PrintStats()

    print(f'{locvars.Scene.themeColor}{locvars.Scene.name}{classes.Colors.WHITE}', "\n")
    num = 0
    for a in locvars.Scene.curentActions:
        num += 1
        print(f'{num}: {a.name}')

    funks.Save() 

    try:
        choiceAction = int(input("Действие:"))
    except ValueError:
        print("неверное действие, введите заново\n")
        choiceAction = int(input("Действие:"))

    try:
        callFunc = locvars.Scene.curentActions[choiceAction -1].function
    except IndexError:
        print("такого действия нет, введите заново\n")
        choiceAction = int(input("Действие:"))
        callFunc = locvars.Scene.curentActions[choiceAction -1].function
        
    vars.clear()
    callFunc()
    vars.clear()
    vars.step += 1



if vars.HP <= 0:
    vars.clear()
    print(f'{classes.Colors.RED}Игра Окончена \n{classes.Colors.WHITE}')
    print("Ваше здоровье =", vars.HP)