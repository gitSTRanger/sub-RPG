from modules import funks
from modules import vars
<<<<<<< Updated upstream
=======
from modules import locvars
from modules import classes
from copy import deepcopy
>>>>>>> Stashed changes
import random

print("\nДОБРО ПОЖАЛОВАТЬ В subRPG (1.1)\n")


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


<<<<<<< Updated upstream
=======
locvars.ZeroScene = funks.Elist[funks.EventID.Forest]
locvars.Scene = locvars.ZeroScene




def CheckLocation():

    if locvars.LOCATION == locvars.Locations.Forest:
        vars.StoreAssortment = vars.ASSORTMENT_DEFAULT
        if vars.actStep % 15 == 0:
            funks.SetLocation(events = funks.WILD_FOREST_EVENTS, locInt = locvars.Locations.WildForest)

    elif locvars.LOCATION == locvars.Locations.WildForest:
        vars.StoreAssortment = vars.ASSORTMENT_DEFAULT
        
        if vars.actStep % 15 == 0:
            funks.Elist = funks.FOREST_BOSS_EVENTS
            locvars.Scene = funks.Elist[funks.EventID.PossibleFight]
            vars.curEnemy = deepcopy(vars.Bosses[vars.BossID.GiantTroll])

        if vars.actStep == 32:
                funks.Elist = funks.FORK_EVENTS

    elif locvars.LOCATION == locvars.Locations.Castle:
        vars.StoreAssortment = vars.ASSORTMENT_CASTLE

        if vars.actStep % 15 == 0:
            funks.Elist = funks.CASTLE_BOSS_EVENTS
            locvars.Scene = funks.Elist[funks.EventID.PossibleFight]
            vars.curEnemy = deepcopy(vars.Bosses[vars.BossID.KingTalung])

        if vars.actStep == 47:
            vars.WIN = True
            vars.END_KingKiller = True
            locvars.Scene = classes.Event("Вы прошли игру. Концовка - Убийца Королей", themeColor = classes.Colors.GREEN , curentActions=[
                classes.Action("Завершить", function = lambda: input("Спастбо за игру"))])
            


#funks.SetLocation(funks.CASTLE_EVENTS, locvars.Locations.Castle)
#vars.actStep = 45


>>>>>>> Stashed changes

while vars.HP > 0 and vars.WIN == False:
    print(f'step:{vars.step}    act:{vars.actStep}')
    print(f'Жизни:{vars.HP}    Броня:{vars.ARMOR}\n')

    if vars.curAct != vars.actStep and funks.Scene == funks.ZeroScene:
        randomEvent = random.randint(0, len(funks.Elist)-1)

        funks.Scene = funks.Elist[randomEvent]
        curAct = vars.actStep

        if randomEvent == funks.Events.StartFight or randomEvent == funks.Events.OnFight:
            vars.clear()
            funks.StartFight()
    
    

    print(funks.Scene.name, "\n")
    num = 0
    for a in funks.Scene.curentActions:
        num += 1
        print(f'{num}: {a.name}')
    
    

    try:
        choiceAction = int(input("Действие:"))
    except ValueError:
        print("неверное действие, введите заново\n")
        choiceAction = int(input("Действие:"))

    vars.clear()
    try:
        callFunc = funks.Scene.curentActions[choiceAction -1].function
    except IndexError:
        print("такого действия нет, введите заново\n")
        choiceAction = int(input("Действие:"))
        callFunc = funks.Scene.curentActions[choiceAction -1].function

    callFunc()
    vars.clear()
    vars.step += 1



if vars.HP <= 0:
    vars.clear()
    print(f'{classes.Colors.RED}Игра Окончена \n{classes.Colors.WHITE}')
    print("Ваше здоровье =", vars.HP)