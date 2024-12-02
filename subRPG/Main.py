from modules import funks
from modules import vars
from modules import locvars
from modules import classes
from copy import deepcopy
import sqlite3
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

#недписано (пока не работает)
def Save():
    data = sqlite3.connect('SavedScene.db')
    cursor = data.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS playerData (
                  Hp integer, 
                  Armor integer,
                  Money integer,
                  Buff_warm integer,
                  BuffRegeneration integer,
                  deBuff_frostbite integer
                  )""")
    
    cursor.execute(f'INSERT INTO playerData VALUES ({vars.HP}, {vars.ARMOR}, {vars.BUFF_warm}, {vars.BUFF_regeneration}, {vars.deBUFF_frostbite})')
    
    data.commit()

    data.close()


def CheckLocation():
    # Л Е С
    if locvars.LOCATION == locvars.Locations.Forest:
        vars.StoreAssortment = vars.ASSORTMENT_DEFAULT
        if vars.actStep % 15 == 0:
            funks.SetLocation(events = funks.WILD_FOREST_EVENTS, locInt = locvars.Locations.WildForest)
    # Д И К И Й   Л Е С
    elif locvars.LOCATION == locvars.Locations.WildForest:
        vars.StoreAssortment = vars.ASSORTMENT_DEFAULT
        
        if vars.actStep % 15 == 0:
            vars.curEnemy = deepcopy(vars.Bosses[vars.BossID.GiantTroll])
            funks.Elist = funks.FOREST_BOSS_EVENTS
            locvars.Scene = funks.Elist[funks.EventID.PossibleFight]
            

        if vars.actStep == 32:
                funks.TakeItem(vars.ItemList[vars.ItemID.antiFreezePotion], 1)
                funks.Elist = funks.FORK_EVENTS
    # З А М О К
    elif locvars.LOCATION == locvars.Locations.Castle:
        vars.StoreAssortment = vars.ASSORTMENT_CASTLE

        if vars.actStep % 15 == 0:
            vars.curEnemy = deepcopy(vars.Bosses[vars.BossID.KingTalung])
            funks.Elist = funks.CASTLE_BOSS_EVENTS
            locvars.Scene = funks.Elist[funks.EventID.PossibleFight]
            

        if vars.actStep == 47:
            vars.WIN = True
            vars.END_KingKiller = True
            locvars.Scene = classes.Event("Вы прошли игру. Концовка - Убийца Королей", themeColor = classes.Colors.YELLOW , curentActions=[
                classes.Action("Завершить", function = lambda: input("Спасибо за игру!\n"))])
    # Р А С П Л А В Л Е Н Н А Я   Д А Л И Н А   
    elif locvars.LOCATION == locvars.Locations.MoltenValley:
            vars.StoreAssortment = vars.ASSORTMENT_MOLTEN_VALLEY

            if vars.actStep % 15 == 0:
                vars.curEnemy = deepcopy(vars.Bosses[vars.BossID.WastelandDragon])
                funks.Elist = funks.MOLTEN_VALLEY_BOSS_EVENTS
                locvars.Scene = funks.Elist[funks.EventID.PossibleFight]
                

            if vars.actStep == 47:
                vars.WIN = True
                vars.END_DragoSlayer = True
                locvars.Scene = classes.Event("Вы прошли игру. Концовка - Драконоборец", themeColor = classes.Colors.YELLOW , curentActions=[
                classes.Action("Завершить", function = lambda: input("Спасибо за игру!\n"))])
    # З А М О Р О Ж Е Н Н О Е   О З Е Р О       
    elif locvars.LOCATION == locvars.Locations.IceLake:
            vars.isFrost = True
            vars.StoreAssortment = vars.ASSORTMENT_ICE
            

            if vars.actStep % 15 == 0:
                vars.curEnemy = deepcopy(vars.Bosses[vars.BossID.IceGuardian])
                funks.Elist = funks.ICE_LAKE_BOSS_EVENTS
                locvars.Scene = funks.Elist[funks.EventID.PossibleFight]
                

            if vars.actStep == 47:
                funks.SetLocation(funks.ICE_STRONGHOLD_EVENTS, locvars.Locations.IceStronghold)
    # Л Е Д Я Н А Я    К Р Е П О С Т Ь     
    elif locvars.LOCATION == locvars.Locations.IceStronghold:
            vars.isFrost = True
            vars.StoreAssortment = vars.ASSORTMENT_ICE

            if vars.actStep % 15 == 0:
                vars.curEnemy = deepcopy(vars.Bosses[vars.BossID.IceBaron])
                funks.Elist = funks.ICE_STRONGHOLD_BOSS_EVENTS
                locvars.Scene = funks.Elist[funks.EventID.PossibleFight]
                

            if vars.actStep == 62:
                vars.WIN = True
                vars.END_ColdBlooded = True
                locvars.Scene = classes.Event("Вы прошли игру. Концовка - Хладнокровный", themeColor = classes.Colors.YELLOW , curentActions=[
                classes.Action("Завершить", function = lambda: input("Спасибо за игру!\n"))])
    # Э Ф И Р Н Ы Е   Б Е Р Е Г А  
    elif locvars.LOCATION == locvars.Locations.EtherealShores:
            vars.StoreAssortment = vars.ASSORTMENT_ETHERIAL

            if vars.actStep % 15 == 0:
                vars.curEnemy = deepcopy(vars.Bosses[vars.BossID.Zrek])
                funks.Elist = funks.ETHERIAL_SHORES_BOSS_EVENTS
                locvars.Scene = funks.Elist[funks.EventID.PossibleFight]
                

            if vars.actStep == 47:
                locvars.Scene = funks.Elist[3] # эфирное сердце
            if vars.actStep == 48:
                vars.WIN = True
                vars.END_Zrek = True
                locvars.Scene = classes.Event("Вы перерезали Сплетения сердца, земля начинает очищаться\n Вы прошли игру. Концовка - Срубил под Корень Проблемы", themeColor = classes.Colors.GREEN , curentActions=[
                classes.Action("Завершить", function = lambda: input("Спасибо за игру!\n"))])



def PrintStats():
    vars.clear()
    print(f'step:{vars.step}    act:{vars.actStep}')
    print(f'Локация: {locvars.stringLocation[locvars.LOCATION]}')
    print(f'Жизни:{vars.HP}    Броня:{vars.ARMOR}    Деньги:{vars.MONEY}\n')

    if vars.isFrost == True:
        print(f'{classes.Colors.BLUE}[Дебафф: Холод]{classes.Colors.WHITE}')

    if vars.deBUFF_frostbite != 0:
        print(f'[Дебафф: обморожение на {classes.Colors.CYAN}{vars.deBUFF_frostbite}{classes.Colors.WHITE} актов]')

    if vars.BUFF_warm != 0 and vars.isFrost == True:
        print(f'[Бафф:вы согреты на {classes.Colors.YELLOW}{vars.BUFF_warm}{classes.Colors.WHITE} актов]')

    if vars.BUFF_regeneration != 0:
        print(f'[Бафф:Регенерация на {classes.Colors.GREEN}{vars.BUFF_regeneration}{classes.Colors.WHITE} актов]')
    print("\n")





#funks.SetLocation(funks.WILD_FOREST_EVENTS, locvars.Locations.WildForest)
#vars.actStep = 32



while vars.HP > 0 and vars.WIN == False:

    CheckLocation()

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

     
    
    PrintStats()

    print(f'{locvars.Scene.themeColor}{locvars.Scene.name}{classes.Colors.WHITE}', "\n")
    num = 0
    for a in locvars.Scene.curentActions:
        num += 1
        print(f'{num}: {a.name}')

    Save() 

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