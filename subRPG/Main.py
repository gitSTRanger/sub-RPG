from modules import vars
from modules import classes
from modules import locvars
from modules import imgs
from copy import deepcopy
from enum import IntEnum
from tkinter import *
import sqlite3
import random
import time




class Colors:
    BLACK = '#000'
    WHITE = '#fff'

    GRAY = '#696969'
    DARK_GRAY = '#1C1C1C'

    RED = '#DC143C'
    DARK_RED = '#B22222'

    GREEN = '#3CB371'
    LIGHT_GREEN = '#98FB98'
    DARK_GREEN = '#006400'

    OLIVE = '#808000'
    DARK_OLIVE = '#556B2F'

    BLUE = '#1E90FF'
    DARK_BLUE = '#4682B4'
    LIGHT_BLUE = '#AFEEEE'

    YELLOW = '#FFD700'
    GOLDEN = '#DAA520'
    DARK_GOLDEN = '#B8860B'
    KHAKI = '#F0E68C'

    ORANGE = '#FFA500'

    CYAN = '#00FFFF'
    LIGHT_CYAN = '#D5FBFB'

    PINK = '#FF69B4'
    DARK_PINK = '#DA70D6'

    PEACH = '#FFDAB9'
    PAPER = '#dec3aa'
    BROWN = '#744c2a'




def ShowInventory():
    vars.Weapon.equip = True
    
    tk ['bg']= Colors.DARK_GRAY
    del locvars.Scene.curentActions[:]

    locvars.Scene = classes.Event(f'Инвентарь:',screen= imgs.inventoryIcon,backColor= Colors.BLACK, textColor = Colors.WHITE , curentActions=[
                classes.Action(f'Назад',icon= imgs.ring, backColor= Colors.DARK_GRAY, textColor = Colors.WHITE, function=lambda: ReturnToJourney),
                ])
    

    slotList: list[classes.Slot] = vars.Inventory


    i = 0
    for Islot in vars.Inventory:

        i += 1
        ExamineItemIsZeroCount(i-1)

        if Islot.count <= 0:
            continue

        # NOTE: rewrite to your preferred coding style
        # Lambdas do not properly capture the iterator values in `for` loops
        # This can be fixed by manually providing an optional argument with a default preferred value
        selectItemFn = \
            lambda Islot=Islot: \
            lambda: \
                SelectItem(Islot, forSale= False)
        
        if Islot.equip == True:
            locvars.Scene.curentActions.append(classes.Action(f'(Экирировано)\n{Islot.item.name}({Islot.count}x) урон:{Islot.item.damage} цена: {Islot.item.cost}$',icon= Islot.item.icon, backColor= Colors.OLIVE, textColor = Colors.WHITE, function=selectItemFn))
            continue
        if Islot.item.damage == 0:
            locvars.Scene.curentActions.append(classes.Action(f'{Islot.item.name}({Islot.count}x) цена: {Islot.item.cost}$',icon= Islot.item.icon, backColor= Colors.DARK_GRAY, textColor = Colors.WHITE, function=selectItemFn))
        else:
            locvars.Scene.curentActions.append(classes.Action(f'{Islot.item.name}({Islot.count}x) урон:{Islot.item.damage} цена: {Islot.item.cost}$',icon= Islot.item.icon, backColor= Colors.DARK_GRAY, textColor = Colors.WHITE, function=selectItemFn))

    window.ClearActionBar()
    window.UpdateScneneGUI("n")
    return


def SelectItem(slot: classes.Slot, forSale: bool):

    locvars.Scene.name = slot.item.name
    del locvars.Scene.curentActions[:]
    
    locvars.Scene = classes.Event(slot.item.name ,screen= slot.item.icon ,backColor= Colors.BLACK, textColor = Colors.WHITE , curentActions=[
                classes.Action(f'Назад',icon= imgs.ring, backColor= Colors.DARK_GRAY, textColor = Colors.WHITE, function=lambda: ReturnToJourney),
            ])


    if forSale == False:

        if slot.equip == False and slot.item.damage != 0:
            locvars.Scene.curentActions.append(classes.Action(f'Экипировать',icon= imgs.circle, backColor= Colors.OLIVE, textColor = Colors.WHITE, function= lambda: lambda: Equip(slot)))

        if slot.item == vars.ItemList[vars.ItemID.SmallHealPotion] or slot.item == vars.ItemList[vars.ItemID.MiddleHealPotion] or slot.item == vars.ItemList[vars.ItemID.LargeHealPotion]:
            locvars.Scene.curentActions.append(classes.Action(f'Лечиться',icon= imgs.circle, backColor= Colors.GREEN, textColor = Colors.WHITE, function= lambda:lambda: UseHealPotion(slot)))

        if slot.item == vars.ItemList[vars.ItemID.SmallRegenPotion] or slot.item == vars.ItemList[vars.ItemID.MiddleRegenPotion] or slot.item == vars.ItemList[vars.ItemID.LargeRegenPotion]:
            locvars.Scene.curentActions.append(classes.Action(f'Лечиться',icon= imgs.circle, backColor= Colors.GREEN, textColor = Colors.WHITE, function= lambda: lambda:UseHealPotion(slot)))

        if slot.item == vars.ItemList[vars.ItemID.LeatherArmor] or slot.item == vars.ItemList[vars.ItemID.SteelArmor] or slot.item == vars.ItemList[vars.ItemID.SilverArmor] or slot.item == vars.ItemList[vars.ItemID.MeteoriteArmor] or slot.item == vars.ItemList[vars.ItemID.IceArmor] or slot.item == vars.ItemList[vars.ItemID.EtherealArmor]:
            locvars.Scene.curentActions.append(classes.Action(f'Надеть броню',icon= imgs.circle, backColor= Colors.DARK_BLUE, textColor = Colors.LIGHT_BLUE, function= lambda: lambda:TakeArmor(slot)))
    else:
        locvars.Scene.curentActions.append(classes.Action(f'продать',icon= imgs.circle, backColor= Colors.OLIVE, textColor = Colors.WHITE, function= lambda: lambda: Sell(slot, window.Counter)))
        locvars.Scene.curentActions.append(classes.Action(f'Продать всё',icon= imgs.circle, backColor= Colors.OLIVE, textColor = Colors.WHITE, function= lambda: lambda: Sell(slot, slot.count)))
        window.Counter = 1
        window.OpenCounterWindow(slot.item.icon)
        return

    window.UpdateScneneGUI("n")



def Equip(slot: classes.Slot):
    vars.Weapon.equip = False
    vars.Weapon = slot
    vars.Weapon.equip = True
    ReturnToJourney()


def TakeItem(item = classes.Item, count = int):
    print("Take Item")

    vars.actStep += 1

    if item == vars.ItemList[vars.ItemID.Empty]:
        MinorEvent("Пусто...", "Далее", screen = imgs.none, funcion= SetNewScene)
        return

    vars.Inventory.append(classes.Slot(item, count, False))
    MinorEvent(f'Получено > {item.name} ({count}x)', "взять", screen = item.icon, funcion= SetNewScene)

def TakeRandomItem(itemPool):
    print("Take Random Item")
    rndId = random.randint(0, len(itemPool) -1)
    item = classes.Item
    item = itemPool[rndId]
    rndCount = random.randint(1, item.stackCount)
    TakeItem(item, rndCount)




def UseHealPotion(potion: classes.Slot):
    potion.count -= 1

    if potion.item == vars.ItemList[vars.ItemID.SmallHealPotion]:
        Heal(15)
    elif potion.item == vars.ItemList[vars.ItemID.MiddleHealPotion]:
        Heal(25)
    elif potion.item == vars.ItemList[vars.ItemID.LargeHealPotion]:
        Heal(50)

    
    if potion.item == vars.ItemList[vars.ItemID.SmallRegenPotion]:
        vars.BUFF_regeneration += 3
        Heal(15)
    elif potion.item == vars.ItemList[vars.ItemID.MiddleRegenPotion]:
        vars.BUFF_regeneration += 6
        Heal(25)
    elif potion.item == vars.ItemList[vars.ItemID.LargeRegenPotion]:
        vars.BUFF_regeneration += 12
        Heal(45)

    ShowInventory()

    
        

def Heal(healPoints):
    vars.HP += healPoints
    locvars.Scene.name = f'\nВы полечились на {healPoints} ед здоровья \nТекущее здоровье:{vars.HP}'
    window.UpdateScneneGUI("n")


def TakeArmor(slot: classes.Slot):
    armorPoint = 0
    slot.count -= 1

    if slot.item == vars.ItemList[vars.ItemID.LeatherArmor]:
        vars.BUFF_warm += 10
        armorPoint = 20

    if slot.item == vars.ItemList[vars.ItemID.SteelArmor]:
        armorPoint = 50

    if slot.item == vars.ItemList[vars.ItemID.SilverArmor]:
        armorPoint = 65

    if slot.item == vars.ItemList[vars.ItemID.MeteoriteArmor]:
        armorPoint = 75

    if slot.item == vars.ItemList[vars.ItemID.IceArmor]:
        vars.deBUFF_frostbite += 10
        armorPoint = 150

    if slot.item == vars.ItemList[vars.ItemID.EtherealArmor]:
        armorPoint = 100

    vars.ARMOR += armorPoint
    ShowInventory()
    locvars.Scene.name = f'Вы надели {slot.item.name}\n Получено {armorPoint} ед. брони'
    locvars.Scene.textColor = Colors.WHITE
    window.UpdateScneneGUI('n')


def ExamineItemIsZeroCount(slotNumber):
    print("examine is zero")
    if vars.Inventory[slotNumber].count <= 0:
        print("remove")
        vars.Inventory.remove(vars.Inventory[slotNumber])
    
    


def ShowStore():
    tk ['bg']= Colors.DARK_OLIVE
    locvars.Scene = classes.Event(f'Лавка торговца:',screen= imgs.storeIcon,backColor= Colors.BLACK, textColor = Colors.WHITE , curentActions=[
        classes.Action(f'Назад',icon= imgs.ring, backColor= Colors.PEACH, textColor = Colors.BROWN, function=lambda: ReturnToJourney),
        classes.Action(f'Купить',icon= imgs.circle, backColor= Colors.GOLDEN, textColor = Colors.WHITE, function=lambda: ReturnToJourney),
        classes.Action(f'Продать',icon= imgs.circle, backColor= Colors.BROWN, textColor = Colors.WHITE, function=lambda: ShowSellMenu),
    ])
    window.UpdateScneneGUI("n")
    

    
def ShowSellMenu():
    
    vars.Weapon.equip = True
    
    tk ['bg']= Colors.BROWN
    del locvars.Scene.curentActions[:]

    locvars.Scene = classes.Event(f'Продать:',screen= imgs.storeIcon,backColor= Colors.BLACK, textColor = Colors.WHITE , curentActions=[
                classes.Action(f'Назад',icon= imgs.ring, backColor= Colors.DARK_GRAY, textColor = Colors.WHITE, function=lambda: ReturnToJourney),
                ])
    

    slotList: list[classes.Slot] = vars.Inventory


    i = 0
    for Islot in vars.Inventory:

        i += 1
        ExamineItemIsZeroCount(i-1)

        if Islot.count <= 0:
            continue

        # NOTE: rewrite to your preferred coding style
        # Lambdas do not properly capture the iterator values in `for` loops
        # This can be fixed by manually providing an optional argument with a default preferred value
        selectItemFn = \
            lambda Islot=Islot: \
            lambda: \
                SelectItem(Islot, forSale= True)
        
        if Islot.equip == True:
            continue
        else:
            locvars.Scene.curentActions.append(classes.Action(f'{Islot.item.name}({Islot.count}x) ЦЕНА: {Islot.item.cost}$',icon= Islot.item.icon, backColor= Colors.DARK_GRAY, textColor = Colors.WHITE, function=selectItemFn))

    window.ClearActionBar()
    window.UpdateScneneGUI("n")
    return




def Sell(slot: classes.Slot, sellCount):
    #i = int(input(f'вы действительно хотите продать {sellCount}x?  \n 1. Да\n 2. Нет\n...'))

    if sellCount > slot.count:
        MinorEvent("у вас столько нет", "назад", screen = imgs.none, funcion= ShowSellMenu)
        return
       

    #if i == 1:
    saleMoney = slot.item.cost * sellCount
    vars.MONEY += saleMoney
    slot.count -= sellCount
    ShowSellMenu()
    print("sale money",saleMoney, "sell count",sellCount)
    #ExamineItemIsZeroCount(slotNumber)
    print("вы продали", sellCount)


def ShowShoppingMenu():
    i = 0

    assortment = [ ]

    print("0: назад")
    for Iitem in vars.StoreAssortment:

        if Iitem == vars.ItemList[vars.ItemID.Empty]:
            print("\n")
            continue

        i += 1
        
        if Iitem.damage == 0:
            print(f' {i}: {Iitem.name}', "цена:", Iitem.cost, "$")
        else:
            print(f' {i}: {Iitem.name} урон: {Iitem.damage}', "цена:", Iitem.cost, "$")
        assortment.append(Iitem)

    
    a = int(input("\n действие:"))

    if a == 0:
        return
        

    
    buyItem = assortment[a-1]

    print("1. Назад \n2. Купить")
    b = int(input("действие:"))

    if b == 2:
        
        c = int(input(f'Сколько вы хотите купить {buyItem.name}?\n'))
        Buy(buyItem, c)


    




def Buy(buyItem = classes.Item ,buyCount = int):
    if vars.MONEY < buyCount * buyItem.cost:
        input("У вас не хватает денег\n")

        
        return
    
    if buyCount > buyItem.stackCount:
        vars.Inventory.append(classes.Slot(buyItem, buyItem.stackCount, False))
        vars.Inventory.append(classes.Slot(buyItem, buyCount - buyItem.stackCount, False))
    else:
        vars.Inventory.append(classes.Slot(buyItem, buyCount, False))
    
    vars.MONEY -= buyCount * buyItem.cost
    
    input(f'Вы купили ({buyCount}) {buyItem.name} за {buyCount * buyItem.cost} денег')
    return



def MoveOn():
    vars.actStep += 1
    CheckLocation()
    SetNewScene()
    locvars.Scene.name = f'вы пошли дальше...\n' + locvars.Scene.name
    window.UpdateAll()
    


def GoOtherWay():
    vars.actStep += 1
    rndPeacefulPlace = random.randint(3, len(Elist) - 1)
    locvars.Scene = deepcopy(Elist[rndPeacefulPlace])
    locvars.curEventId = rndPeacefulPlace
    locvars.Scene.name = f'вы пошли другой дорогой\n' + locvars.Scene.name
    window.UpdateAll()
   


def Attack():

    locvars.Scene = deepcopy(Elist[EventID.OnFight])
    locvars.Scene.name = f'вы атаковали {vars.curEnemy.name} на {vars.Weapon.item.damage} ед. урона'


    vars.curEnemy.HP -= vars.Weapon.item.damage

    if vars.curEnemy.HP <= 0:
        MinorEvent("враг мертв, на сей раз вы победили", "Обыскать",screen = imgs.none, funcion=  lambda: TakeRandomItem(vars.TIER1_MONSTER_DROP))
        return


    hitChance = random.randint(0, 100)

    if hitChance > vars.curEnemy.missChance:

        locvars.Scene.name += f'\n{vars.curEnemy.name} атакует вас {TakeDamage(hit= vars.curEnemy.damage)}'
    else:
        locvars.Scene.name += f'\n{vars.curEnemy.name} пытается атаковать, но промахивается'
    window.UpdateAll()




def ShowEnemyStats():
    locvars.Scene.name = f'{vars.curEnemy.name} жизни: {vars.curEnemy.HP}'
    window.UpdateAll()


def TryRunAway():


    chance = random.randint(0, 100)

    if chance <= vars.curEnemy.missChance:
        vars.actStep += 1
        MinorEvent(f'вы удачно сбежали!', "Далее",screen = imgs.none, funcion= SetNewScene)
        return
        
    else:
        locvars.Scene = deepcopy(Elist[EventID.OnFight])
        locvars.Scene.name =  f'вам не удалось сбежать' + TakeDamage(hit= vars.curEnemy.damage)
    window.UpdateAll()




def StartFight():
    locvars.Scene = deepcopy(Elist[EventID.StartFight])

    startRange = 0
    endRange = 0

    if locvars.LOCATION == locvars.Locations.Forest:
        startRange = 0
        endRange = vars.EnemyID.Ork
    elif locvars.LOCATION == locvars.Locations.WildForest:
        startRange = 0
        endRange = vars.EnemyID.Troll
    elif locvars.LOCATION == locvars.Locations.Castle:
        startRange = vars.EnemyID.SkeletonKnight
        endRange = vars.EnemyID.StoneGargoyle
    elif locvars.LOCATION == locvars.Locations.MoltenValley:
        startRange = vars.EnemyID.FireBeast
        endRange = vars.EnemyID.ObsidianGuard
    elif locvars.LOCATION == locvars.Locations.IceLake or locvars.LOCATION == locvars.Locations.IceStronghold:
        startRange = vars.EnemyID.FrostSkeleton
        endRange = vars.EnemyID.Iceman
    elif locvars.LOCATION == locvars.Locations.EtherealShores:
        startRange = vars.EnemyID.LiquidSlime
        endRange = vars.EnemyID.RainbowGrabber

    rndEnemy = random.randint(startRange, endRange)
    vars.curEnemy = deepcopy(vars.Enemies[rndEnemy])
    window.UpdateAll()


def TakeDamage(hit):
    damage = hit
    if vars.ARMOR > 0:
        damage = int(hit * 0.5)
        vars.ARMOR -= int(vars.curEnemy.damage - damage)
        
    vars.HP -= damage
    #MinorEvent(f'вы получили {damage} урона', "Далее", ReturnToJourney)
    #input("Далее...")
    return f'вы получили {damage} урона'



def SetEvent(eventID):
    locvars.Scene = deepcopy(Elist[eventID])
    vars.actStep += 1



def SetLocation(events, locInt):
    global Elist
    Elist = events
    locvars.Scene = deepcopy(Elist[3])
    locvars.LOCATION = locInt
    MinorEvent(f'вы пошли в {locvars.stringLocation[locvars.LOCATION]}', "Далее", screen = imgs.none, funcion=SetNewScene)



def KeepWarm(warmPoint):
    vars.BUFF_warm += warmPoint
    vars.deBUFF_frostbite -= 5

    if vars.deBUFF_frostbite <= 0:
        vars.deBUFF_frostbite = 0

    print(f'вы согрелись на {warmPoint} акта')
    GoOtherWay()


def CheckBuffs():
    if vars.BUFF_regeneration != 0:
                vars.BUFF_regeneration -= 1
                Heal(15)

    if vars.isFrost == True:
        if vars.BUFF_warm != 0:
            vars.BUFF_warm -= 1
        else:
            print("\nвам очень холодно")
            TakeDamage(5)
        
    if vars.deBUFF_frostbite != 0:
        vars.deBUFF_frostbite -= 1
        print("\nу вас обморожение")
        TakeDamage(20)  



def CheckLocation():
    # Л Е С
    global Elist

    if locvars.LOCATION == locvars.Locations.Forest:
        vars.StoreAssortment = vars.ASSORTMENT_DEFAULT
        Elist = FOREST_EVENTS
        #if vars.actStep % 15 == 0:
            #SetLocation(events = WILD_FOREST_EVENTS, locInt = locvars.Locations.WildForest)
    '''
    # Д И К И Й   Л Е С
    elif locvars.LOCATION == locvars.Locations.WildForest:
        vars.StoreAssortment = vars.ASSORTMENT_DEFAULT
        
        if vars.actStep % 15 == 0:
            vars.curEnemy = deepcopy(vars.Bosses[vars.BossID.GiantTroll])
            Elist = FOREST_BOSS_EVENTS
            locvars.Scene = deepcopy(Elist[EventID.PossibleFight])
            

        if vars.actStep == 32:
                TakeItem(vars.ItemList[vars.ItemID.antiFreezePotion], 1)
                Elist = FORK_EVENTS
    # З А М О К
    elif locvars.LOCATION == locvars.Locations.Castle:
        vars.StoreAssortment = vars.ASSORTMENT_CASTLE

        if vars.actStep % 15 == 0:
            vars.curEnemy = deepcopy(vars.Bosses[vars.BossID.KingTalung])
            Elist = CASTLE_BOSS_EVENTS
            locvars.Scene = deepcopy(Elist[EventID.PossibleFight])
            

        if vars.actStep == 47:
            vars.WIN = True
            vars.END_KingKiller = True
            locvars.Scene = classes.Event("Вы прошли игру. Концовка - Убийца Королей", textColor = Colors.YELLOW , curentActions=[
                classes.Action("Завершить", function = lambda: input("Спасибо за игру!\n"))])
    # Р А С П Л А В Л Е Н Н А Я   Д А Л И Н А   
    elif locvars.LOCATION == locvars.Locations.MoltenValley:
            vars.StoreAssortment = vars.ASSORTMENT_MOLTEN_VALLEY

            if vars.actStep % 15 == 0:
                vars.curEnemy = deepcopy(vars.Bosses[vars.BossID.WastelandDragon])
                Elist = MOLTEN_VALLEY_BOSS_EVENTS
                locvars.Scene = deepcopy(Elist[EventID.PossibleFight])
                

            if vars.actStep == 47:
                vars.WIN = True
                vars.END_DragoSlayer = True
                locvars.Scene = classes.Event("Вы прошли игру. Концовка - Драконоборец", textColor = Colors.YELLOW , curentActions=[
                classes.Action("Завершить", function = lambda: input("Спасибо за игру!\n"))])
    # З А М О Р О Ж Е Н Н О Е   О З Е Р О       
    elif locvars.LOCATION == locvars.Locations.IceLake:
            vars.isFrost = True
            vars.StoreAssortment = vars.ASSORTMENT_ICE
            

            if vars.actStep % 15 == 0:
                vars.curEnemy = deepcopy(vars.Bosses[vars.BossID.IceGuardian])
                Elist = ICE_LAKE_BOSS_EVENTS
                locvars.Scene = deepcopy(Elist[EventID.PossibleFight])
                

            if vars.actStep == 47:
                SetLocation(ICE_STRONGHOLD_EVENTS, locvars.Locations.IceStronghold)
    # Л Е Д Я Н А Я    К Р Е П О С Т Ь     
    elif locvars.LOCATION == locvars.Locations.IceStronghold:
            vars.isFrost = True
            vars.StoreAssortment = vars.ASSORTMENT_ICE

            if vars.actStep % 15 == 0:
                vars.curEnemy = deepcopy(vars.Bosses[vars.BossID.IceBaron])
                Elist = ICE_STRONGHOLD_BOSS_EVENTS
                locvars.Scene = deepcopy(Elist[EventID.PossibleFight])
                

            if vars.actStep == 62:
                vars.WIN = True
                vars.END_ColdBlooded = True
                locvars.Scene = classes.Event("Вы прошли игру. Концовка - Хладнокровный", textColor = Colors.YELLOW , curentActions=[
                classes.Action("Завершить", function = lambda: input("Спасибо за игру!\n"))])
    # Э Ф И Р Н Ы Е   Б Е Р Е Г А  
    elif locvars.LOCATION == locvars.Locations.EtherealShores:
            vars.StoreAssortment = vars.ASSORTMENT_ETHERIAL

            if vars.actStep % 15 == 0:
                vars.curEnemy = deepcopy(vars.Bosses[vars.BossID.Zrek])
                Elist = ETHERIAL_SHORES_BOSS_EVENTS
                locvars.Scene = deepcopy(Elist[EventID.PossibleFight])
                

            if vars.actStep == 47:
                locvars.Scene = deepcopy(Elist[3]) # эфирное сердце
            if vars.actStep == 48:
                vars.WIN = True
                vars.END_Zrek = True
                locvars.Scene = classes.Event("Вы перерезали Сплетения сердца, земля начинает очищаться\n Вы прошли игру. Концовка - Срубил под Корень Проблемы", textColor = Colors.GREEN , curentActions=[
                classes.Action("Завершить", function = lambda: input("Спасибо за игру!\n"))])
        '''
    if vars.actStep % 10 == 0:
        locvars.curEventId = random.randint(0,1)
        Elist = STORE_EVENTS
        ReturnToJourney()





def SetNewScene():
    randomEvent = random.randint(0, len(Elist)-1)
    locvars.Scene = deepcopy(Elist[randomEvent])
    locvars.curEventId = randomEvent

    if randomEvent == EventID.StartFight or randomEvent == EventID.OnFight:
        
        locvars.curEventId = EventID.StartFight
        StartFight()

    CheckBuffs()
    vars.step += 1
    window.UpdateAll()


#TKINTER LOGIC

def MinorEvent(eventName, actionName,screen, funcion):
    locvars.Scene = classes.Event(f'{eventName}',screen= screen,backColor= Colors.BLACK, textColor = Colors.WHITE , curentActions=[
                classes.Action(f'{actionName}',icon= imgs.ring, backColor= Colors.PEACH, textColor = Colors.BROWN, function = lambda: funcion),
                ])
    vars.step += 1
    window.UpdateScneneGUI("w")
    

def ReturnToJourney():
    locvars.Scene = deepcopy(Elist[locvars.curEventId])
    CheckBuffs()
    vars.step += 1
    tk ['bg']= Colors.PAPER
    window.UpdateScneneGUI("w")






#Все События (Сцены)

class EventID(IntEnum):
    PossibleFight = 0
    StartFight = 1
    OnFight = 2

    # Лес
    Forest = 3
    Well = 5
    Village = 6
    Trap = 4
    BearTrap = 5
    MeteorPlace = 6
    UnknowPath = 7
    # Замок
    CeremonyHall = 3
    DiningRoom = 5
    CorridorChest = 6
    Armory = 7
    Library = 8
    CorridorFork1 = 9
    CorridorFork2 = 9
    # Огонь
    ObsidianPath = 7
    MoltenCorpse = 8
    # Лед
    MagicTrap = 4
    IceThree = 6
    IceSharps = 7
    FrozenCorpse = 8
    CampFire_1 = 9
    CampFire_2 = 10
    # Ледяной Замок
    FrozenArmory = 5
    FrozenChest = 6

    # Эфир
    EtherialBag = 7
    EtherialCombatBag = 8
    CoruptedCorpse = 9

STORE_EVENTS = [
    classes.Event("вы пришли в лавку торговца",
                screen= imgs.store,
                backColor=Colors.BLACK,
                textColor = Colors.GREEN ,
                curentActions=[
    classes.Action("Осмотреть",icon= imgs.look, backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: lambda: MinorEvent("Лавка торговца на колесиках - это странствующий торговец\nлибо он просто скиталец либо\nв бегах от чего то", "Назад",screen = imgs.none, funcion= ReturnToJourney)),
    classes.Action("Магазин",icon= imgs.circle, backColor= Colors.DARK_GOLDEN, textColor = Colors.GOLDEN, function = lambda: ShowStore),
    classes.Action("Инвентарь",icon= imgs.circle, backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Уйти",icon= imgs.arrowLeft, backColor= Colors.GREEN, textColor = Colors.LIGHT_GREEN, function = lambda:  MoveOn),
    
    ]),
    classes.Event("вы пришли в хижину торговца",
                screen= imgs.store_1,
                backColor=Colors.BLACK,
                textColor = Colors.GREEN ,
                curentActions=[
    classes.Action("Осмотреть",icon= imgs.look, backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: lambda: MinorEvent("Теплая уютная хижина, здесь пахнет дымом и пряностями\nНа прилавке множество ценных вещей", "Назад",screen = imgs.none, funcion= ReturnToJourney)),
    classes.Action("Магазин",icon= imgs.circle, backColor= Colors.DARK_GOLDEN, textColor = Colors.GOLDEN, function = lambda: ShowStore),
    classes.Action("Инвентарь",icon= imgs.circle, backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Уйти",icon= imgs.arrowLeft, backColor= Colors.GREEN, textColor = Colors.LIGHT_GREEN, function = lambda:  MoveOn),
   
    ]),
    
    ]


FOREST_EVENTS = [
    classes.Event("на вашем пути появился чей то силуэт",
                screen= imgs.F_possibleFight,
                backColor=Colors.BLACK,
                textColor = Colors.GREEN ,
                curentActions=[
    classes.Action("Инвентарь",icon= imgs.circle, backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Идти дальше",icon= imgs.arrowUp, backColor= Colors.GREEN, textColor = Colors.LIGHT_GREEN, function = lambda: StartFight),
    classes.Action("Пойти в другую сторону",icon= imgs.arrowLeft, backColor= Colors.GREEN, textColor = Colors.LIGHT_GREEN, function =lambda: GoOtherWay),
    ]),
    classes.Event("вы слышите чье-то рычание впереди, осмотревшись вы видите врага",
                screen= imgs.F_fight,
                backColor=Colors.BLACK,
                textColor = Colors.RED,
                curentActions=[
    classes.Action("Инвентарь",icon= imgs.circle, backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action(f'Атаковать врага',icon= imgs.attack, backColor= Colors.ORANGE, textColor = Colors.DARK_RED, function = lambda: Attack),
    classes.Action("Статы врага",icon= imgs.enemyStats, backColor= Colors.PEACH, textColor = Colors.BROWN, function = lambda: ShowEnemyStats),
    classes.Action("Сбежать",icon= imgs.arrowLeft, backColor= Colors.PEACH, textColor = Colors.BROWN, function = lambda: TryRunAway),
    ]),
    classes.Event(f'враг готовится нанести удар',
                screen= imgs.F_fight,
                backColor=Colors.BLACK,
                textColor = Colors.RED,
                curentActions=[
    classes.Action("Инвентарь",icon= imgs.circle, backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action(f'Атаковать врага',icon= imgs.attack, backColor= Colors.ORANGE, textColor = Colors.DARK_RED, function = lambda: Attack),
    classes.Action("Статы врага",icon= imgs.enemyStats, backColor= Colors.PEACH, textColor = Colors.BROWN, function = lambda: ShowEnemyStats),
    classes.Action("Сбежать",icon= imgs.arrowLeft, backColor= Colors.PEACH, textColor = Colors.BROWN, function = lambda: TryRunAway),
    ]),
    classes.Event("скитаясь вы пришли к лесу",
                screen= imgs.F_forest,
                backColor=Colors.BLACK,
                textColor = Colors.GREEN ,
                curentActions=[
    classes.Action("Инвентарь",icon= imgs.circle, backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Магазин",icon= imgs.circle, backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowStore),
    classes.Action("Идти дальше",icon= imgs.arrowUp, backColor= Colors.GREEN, textColor = Colors.LIGHT_GREEN, function = lambda:  MoveOn),
    classes.Action("Пойти в другую сторону",icon= imgs.arrowLeft, backColor= Colors.GREEN, textColor = Colors.LIGHT_GREEN, function = lambda: GoOtherWay),6
    ]),
    classes.Event("тропинка по которой вы шли обрывается",
                screen= imgs.F_forest_1,
                backColor=Colors.BLACK,
                textColor = Colors.GREEN,
                curentActions=[
    classes.Action("Инвентарь",icon= imgs.circle, backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Магазин",icon= imgs.circle, backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowStore),
    classes.Action("Идти дальше",icon= imgs.arrowUp, backColor= Colors.GREEN, textColor = Colors.LIGHT_GREEN, function = lambda:  MoveOn),
    classes.Action("Пойти в другую сторону",icon= imgs.arrowLeft, backColor= Colors.GREEN, textColor = Colors.LIGHT_GREEN, function = lambda: GoOtherWay),
    ]),
    classes.Event("скитаясь вы заблудились в лесу",
                screen= imgs.F_forest_2,
                backColor=Colors.BLACK,
                textColor = Colors.GREEN,
                curentActions=[
    classes.Action("Инвентарь",icon= imgs.circle, backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Магазин",icon= imgs.circle, backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowStore),
    classes.Action("Идти дальше",icon= imgs.arrowUp, backColor= Colors.GREEN, textColor = Colors.LIGHT_GREEN, function = lambda:  MoveOn),
    classes.Action("Пойти в другую сторону",icon= imgs.arrowLeft, backColor= Colors.GREEN, textColor = Colors.LIGHT_GREEN, function = lambda: GoOtherWay),
    ]),
    classes.Event("вы набрели на разрушенный пустой колодец. здесь спокойно и можно передохнуть",
                  screen= imgs.F_well,
                  backColor=Colors.BLACK,
                  textColor = Colors.GREEN,
                  curentActions=[
    classes.Action("Инвентарь",icon= imgs.circle, backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Осмотреть",icon= imgs.look, backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: lambda: MinorEvent("Колодец настолько стар, что едва можно разлечить\n его руины поросшие мхом, сомневаюсь что внутри\n есть вода", "Назад",screen = imgs.none, funcion= ReturnToJourney)),
    classes.Action("Обыскать",icon= imgs.look, backColor= Colors.GREEN, textColor = Colors.LIGHT_GREEN, function = lambda: lambda: TakeRandomItem(vars.TIER1_WELL_items)),
    classes.Action("Идти дальше",icon= imgs.arrowUp, backColor= Colors.GREEN, textColor = Colors.LIGHT_GREEN, function = lambda:  MoveOn),
    classes.Action("Пойти в другую сторону",icon= imgs.arrowLeft, backColor= Colors.GREEN, textColor = Colors.LIGHT_GREEN, function = lambda: GoOtherWay),
    ]),
    classes.Event("скитаясь вы пришли в заброшенную деревню",
                  screen= imgs.F_village,
                  backColor=Colors.BLACK,
                  textColor = Colors.GREEN,
                  curentActions=[
    classes.Action("Инвентарь",icon= imgs.circle, backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Обыскать дома",icon= imgs.look, backColor= Colors.GREEN, textColor = Colors.LIGHT_GREEN, function = lambda: lambda: TakeRandomItem(vars.TIER1_VILLAGE_items)),
    classes.Action("Идти дальше",icon= imgs.arrowUp, backColor= Colors.GREEN, textColor = Colors.LIGHT_GREEN, function = lambda:  MoveOn),
    classes.Action("Пойти в другую сторону",icon= imgs.arrowLeft, backColor= Colors.GREEN, textColor = Colors.LIGHT_GREEN, function = lambda: GoOtherWay),
    ]),
]

'''
WILD_FOREST_EVENTS = [
    classes.Event("на вашем пути появился чей то силуэт",
                backColor=Colors.DARK_GREEN,
                textColor = Colors.GREEN ,
                curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Идти дальше",backColor= Colors.GREEN, textColor = Colors.LIGHT_GREEN, function = lambda: StartFight),
    classes.Action("Пойти в другую сторону",backColor= Colors.GREEN, textColor = Colors.LIGHT_GREEN, function =lambda: GoOtherWay),
    ]),
    classes.Event("вы слышите чье-то рычание впереди, осмотревшись вы видите врага",
                backColor=Colors.BLACK,
                textColor = Colors.RED,
                curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action(f'Атаковать врага',backColor= Colors.RED, textColor = Colors.DARK_RED, function = lambda: Attack),
    classes.Action("Статы врага",backColor= Colors.PEACH, textColor = Colors.BROWN, function = lambda: ShowEnemyStats),
    classes.Action("Сбежать",backColor= Colors.PEACH, textColor = Colors.BROWN, function = lambda: TryRunAway),
    ]),
    classes.Event(f'враг готовится нанести удар',
                backColor=Colors.BLACK,
                textColor = Colors.RED,
                curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action(f'Атаковать врага',backColor= Colors.RED, textColor = Colors.DARK_RED, function = lambda: Attack),
    classes.Action("Статы врага",backColor= Colors.PEACH, textColor = Colors.BROWN, function = lambda: ShowEnemyStats),
    classes.Action("Сбежать",backColor= Colors.PEACH, textColor = Colors.BROWN, function = lambda: TryRunAway),
    ]),
    classes.Event("скитаясь вы пришли к лесу",
                backColor=Colors.DARK_GREEN,
                textColor = Colors.GREEN,
                curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Магазин", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowStore),
    classes.Action("Идти дальше",backColor= Colors.GREEN, textColor = Colors.LIGHT_GREEN, function = lambda:  MoveOn),
    classes.Action("Пойти в другую сторону",backColor= Colors.GREEN, textColor = Colors.LIGHT_GREEN, function = lambda: GoOtherWay),
    ]),
    classes.Event("вы замечаете растяжку", textColor = Colors.GREEN, curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Идти дальше", function = lambda: TakeDamage(hit=15)),
    classes.Action("обойти", function = GoOtherWay),
    ]),
    classes.Event("вы резко остановились впереди в прелой листве блестает капкан",textColor = Colors.GREEN, curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Идти дальше", function = lambda: TakeDamage(hit=25)),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("земля бурлит от дыма, приглядевшись вы замечаете что стоите на упавшем метеорите",textColor = Colors.GREEN, curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Взять остывший камень под ногами", function = lambda: TakeItem(vars.ItemList[vars.ItemID.MeteoritePiece], 1)),
    classes.Action("Потрогать землю", function = lambda: TakeDamage(100)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("вы замечаете чью-то протоптанную тропинку",
                backColor=Colors.DARK_GREEN,
                textColor = Colors.GREEN,
                curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Магазин", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowStore),
    classes.Action("Идти по тропинке",backColor= Colors.GREEN, textColor = Colors.LIGHT_GREEN, function = lambda:  MoveOn),
    classes.Action("Пойти в другую сторону",backColor= Colors.GREEN, textColor = Colors.LIGHT_GREEN, function = lambda: GoOtherWay),
    ]),
]

FOREST_BOSS_EVENTS =[
    classes.Event("на вашем пути появилась огромная тварь",textColor = Colors.RED , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Идти дальше", function = lambda: SetEvent(EventID.StartFight)),
    ]),
    classes.Event("вы слышите оглушающий рев, осмотревшись вы видите его",textColor = Colors.RED , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action(f'Атаковать врага',backColor= Colors.RED, textColor = Colors.DARK_RED, function = lambda: Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    ]),
    classes.Event(f'Босс готовится нанести удар',textColor = Colors.RED , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action(f'Атаковать врага',backColor= Colors.RED, textColor = Colors.DARK_RED, function = lambda: Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    ]),
] 



CASTLE_EVENTS = [
    classes.Event("в глубине коридора виден чей то силуэт",textColor = Colors.YELLOW , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Идти дальше",backColor= Colors.GREEN, textColor = Colors.LIGHT_GREEN, function = lambda: StartFight),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("вы слышите чье-то рычание впереди, осмотревшись вы видите врага",textColor = Colors.RED , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action(f'Атаковать врага',backColor= Colors.RED, textColor = Colors.DARK_RED, function = lambda: Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    classes.Action("Сбежать", function = TryRunAway),
    ]),
    classes.Event(f'враг готовится нанести удар',textColor = Colors.RED , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action(f'Атаковать врага',backColor= Colors.RED, textColor = Colors.DARK_RED, function = lambda: Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    classes.Action("Сбежать", function = TryRunAway),
    ]),
    classes.Event("в замешательстве вы пришли в огромный зал", textColor = Colors.YELLOW , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Осмотреть", function = lambda: input("Осмотревшись вы увидели табличку (Зал Церемоний)\nДалее...")),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другой коридор", function = GoOtherWay),
    ]),
    classes.Event("вы идете по корридору и замечаете странную плиту под ногами",textColor = Colors.YELLOW , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Идти дальше", function = lambda: TakeDamage(hit=25)),
    classes.Action("обойти", function = GoOtherWay),
    ]),
    classes.Event("блукая вы пришли в зал с длинными столами в ряд", textColor = Colors.YELLOW , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Осмотреть", function = lambda: input("Осмотревшись вы понимаете, вероятно это столовая\nДалее...")),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другой коридор", function = GoOtherWay),
    ]),
    classes.Event("вы пришли в длинный корридор в конце которого стоит сундук",textColor = Colors.YELLOW , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Осмотреть Коридор", function = lambda: input("длинный величественный коридор с высокими потолками, с развешанными королевскими флагами по стенам\nДалее...")),
    classes.Action("Открыть Сундук", function = lambda: TakeRandomItem(vars.TIER2_CHEST)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другой корридор", function = GoOtherWay),
    ]),
    classes.Event("кажеться вы заблудились в однообразных коридорах но наткнулись на зал с колоннами", textColor = Colors.YELLOW , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Осмотреть", function = lambda: input("Осмотревшись вы выдите стоящих вдоль колонн рыцарей, кажеться это просто стенды\nДалее...")),
    classes.Action("Снять броню со стенда", function = lambda: TakeRandomItem(vars.TIER2_ARMOR_STAND)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другой коридор", function = GoOtherWay),
    ]),
    classes.Event("Вы пришли в библиотеку, перед собой вы видите шкаф с книгами", textColor = Colors.YELLOW , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Идти дальше", function = GoOtherWay),
    classes.Action(f'Читать "Искуство Битвы или пособие рыцаря"', function = lambda: input("бегло прочитав вы остановили свой взор на строчке 'не с каждым противником стоит сражаться, чем больше шанс врагу промазать, тем больше шанс вам сбежать '\nДалее...")),
    classes.Action(f'Читать "Летопись Королевства Талунга"', function = lambda: input("из летописи вы поняли,что королевство спокойно существовало. ничего интересного, кроме упомянаний какого-то забавного незнакомца - Зрека\nДалее...")),
    classes.Action(f'Читать "Поручение от Графа"', function = lambda: input("достопочтенный король Талунг, вынужден принять меры в связи с последними событиями и заморозить свои земли до прекращения ***\nДалее...")),
    classes.Action(f'Читать неизвестную книгу', function = lambda: input("Когда шаман Зрек падет, на землю камень упадет, ну а потом шаман придет, и снова станет он силен ***рные берега он разольет [обрывается]\nДалее...")),
    ]),
    classes.Event("вы снова пришли в какой-то из коридоров ведущий в 4 направления. Вы забыли откуда пришли", textColor = Colors.YELLOW , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Осмотреть", function = lambda: input("Осмотревшись вы увидели табличку (<<Столовая, Библиотека>>)\nДалее...")),
    classes.Action("Идти прямо", function = MoveOn),
    classes.Action("Пойти налево", function = lambda: SetEvent(EventID.DiningRoom)),
    classes.Action("Пойти направо", function = lambda: SetEvent(EventID.Library)),
    classes.Action("Пойти в назад", function = GoOtherWay),
    ]),
    classes.Event("вы снова пришли в какой-то из коридоров ведущий в 4 направления. Вы забыли откуда пришли", textColor = Colors.YELLOW , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Осмотреть", function = lambda: input("Осмотревшись вы увидели табличку (<<Оружейная, Библиотека>>)\nДалее...")),
    classes.Action("Идти прямо", function = MoveOn),
    classes.Action("Пойти налево", function = lambda: SetEvent(EventID.Armory)),
    classes.Action("Пойти направо", function = lambda: SetEvent(EventID.Library)),
    classes.Action("Пойти в назад", function = GoOtherWay),
    ]),
    classes.Event("вы снова пришли в какой-то из коридоров ведущий в 4 направления. Вы забыли откуда пришли", textColor = Colors.YELLOW , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Осмотреть", function = lambda: input("Осмотревшись вы увидели табличку (<<Зал Церемоний, Хранилище>>)\nДалее...")),
    classes.Action("Идти прямо", function = MoveOn),
    classes.Action("Пойти налево", function = lambda: SetEvent(EventID.CeremonyHall)),
    classes.Action("Пойти направо", function = lambda: SetEvent(EventID.CorridorChest)),
    classes.Action("Пойти в назад", function = GoOtherWay),
    ]),
    
]

CASTLE_BOSS_EVENTS =[
    classes.Event("Наконец вы пришли в тронный зал, но на троне воссидает уже измененый король",textColor = Colors.RED , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Идти дальше", function = lambda: SetEvent(EventID.StartFight)),
    ]),
    classes.Event("Вы видите как из спины короля торчат щупальца, а глаза его черны.Опоздали его уже не спасти",textColor = Colors.RED , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action(f'Атаковать врага',backColor= Colors.RED, textColor = Colors.DARK_RED, function = lambda: Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    ]),
    classes.Event(f'Король готовится нанести удар',textColor = Colors.RED , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action(f'Атаковать врага',backColor= Colors.RED, textColor = Colors.DARK_RED, function = lambda: Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    ]),
] 



MOLTEN_VALLEY_EVENTS = [
    classes.Event("на в дыму виднеется чей то силуэт",textColor = Colors.RED , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Идти дальше",backColor= Colors.GREEN, textColor = Colors.LIGHT_GREEN, function = lambda: StartFight),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("вы слышите чье-то рычание впереди, осмотревшись вы видите врага",textColor = Colors.RED , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action(f'Атаковать врага',backColor= Colors.RED, textColor = Colors.DARK_RED, function = lambda: Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    classes.Action("Сбежать", function = TryRunAway),
    ]),
    classes.Event(f'враг готовится нанести удар',textColor = Colors.RED, curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action(f'Атаковать врага',backColor= Colors.RED, textColor = Colors.DARK_RED, function = lambda: Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    classes.Action("Сбежать", function = TryRunAway),
    ]),
    classes.Event("вы бредете в завесе дыма на ощупь", textColor = Colors.RED, curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Потрогать землю", function = lambda: TakeDamage(50)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("впереди слышен гейзер", textColor = Colors.RED, curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Потрогать землю", function = lambda: TakeDamage(50)),
    classes.Action("Идти дальше", function = lambda: TakeDamage(hit=30)),
    classes.Action("обойти", function = GoOtherWay),
    ]),
    classes.Event("впереди слышен гейзер", textColor = Colors.RED, curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Потрогать землю", function = lambda: TakeDamage(50)),
    classes.Action("Идти дальше", function = lambda: TakeDamage(hit=30)),
    classes.Action("обойти", function = GoOtherWay),
    ]),
    classes.Event("вы наконец пришли в остывшее место, где можно спокойно осмотреться",textColor = Colors.RED, curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Взять остывший камень под ногами", function = lambda: TakeItem(vars.ItemList[vars.ItemID.MeteoritePiece], 1)),
    classes.Action("Осмотреться", function = lambda: input("вы замечаете дорогу из остывшей породы в гуще дыма в другой стороне")),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = lambda: SetEvent(EventID.ObsidianPath)),
    ]),
    classes.Event("вы идете по обсидиановой дороге, вокруг вас стены дыма", textColor = Colors.RED , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("подобрать все остывшие камни под ногами", function = lambda: TakeItem(vars.ItemList[vars.ItemID.MeteoritePiece], 3)),
    classes.Action("Идти по тропинке", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("перед вами лежит скелет путника",textColor = Colors.RED, curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Осмотреть", function = lambda: TakeRandomItem(vars.TIER2_MOLTEN_CORPSE)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = lambda: SetEvent(EventID.ObsidianPath)),
    ]),
]

MOLTEN_VALLEY_BOSS_EVENTS =[
    classes.Event("перед вами огромный кратор",textColor = Colors.RED , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Спуститься", function = lambda: SetEvent(EventID.StartFight)),
    ]),
    classes.Event("в краторе спало нечто, рык пошелся по всей округе",textColor = Colors.RED , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action(f'Атаковать врага',backColor= Colors.RED, textColor = Colors.DARK_RED, function = lambda: Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    ]),
    classes.Event(f'Дракон пустошей раскрывает пасть',textColor = Colors.RED , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action(f'Атаковать врага',backColor= Colors.RED, textColor = Colors.DARK_RED, function = lambda: Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    ]),
] 



ICE_LAKE_EVENTS = [
    classes.Event("впереди в снежном тумане виднеется чей-то силуэт",textColor = Colors.CYAN , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Идти дальше",backColor= Colors.GREEN, textColor = Colors.LIGHT_GREEN, function = lambda: StartFight),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("вы слышите чье-то рычание впереди, осмотревшись вы видите врага",textColor = Colors.RED , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action(f'Атаковать врага',backColor= Colors.RED, textColor = Colors.DARK_RED, function = lambda: Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    classes.Action("Сбежать", function = TryRunAway),
    ]),
    classes.Event(f'враг готовится нанести удар',textColor = Colors.RED, curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action(f'Атаковать врага',backColor= Colors.RED, textColor = Colors.DARK_RED, function = lambda: Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    classes.Action("Сбежать", function = TryRunAway),
    ]),
    classes.Event("поднялся сильный ветер, метель близко", textColor = Colors.CYAN, curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("впереди магическая ловушка", textColor = Colors.CYAN, curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Идти дальше", function = lambda: TakeDamage(hit=30)),
    classes.Action("обойти", function = GoOtherWay),
    ]),
    classes.Event("вы резко остановились впереди в сугробе блестает капкан", textColor = Colors.CYAN, curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Идти дальше", function = lambda: TakeDamage(hit=30)),
    classes.Action("обойти", function = GoOtherWay),
    ]),
    classes.Event("вы видете перед собой ледяное дерево", textColor = Colors.CYAN , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Сорвать ледяные листья", function = lambda: TakeItem(vars.ItemList[vars.ItemID.IceCrystal], 4)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("под вашими ногами куча мелких осколков льда", textColor = Colors.CYAN , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("слепить в один кристал", function = lambda: TakeItem(vars.ItemList[vars.ItemID.IceCrystal], 1)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("перед вами лежит замороженный труп путника",textColor = Colors.CYAN, curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Осмотреть", function = lambda: TakeRandomItem(vars.TIER2_FROZEN_CORPSE)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("вы нашли чей то горящий костер", textColor = Colors.YELLOW, curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("согреться", function = lambda: KeepWarm(3)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("вы нашли чей то горящий костер", textColor = Colors.YELLOW, curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("согреться", function = lambda: KeepWarm(3)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    
]

ICE_LAKE_BOSS_EVENTS =[
    classes.Event("Вы пришли к ледяной крепости",textColor = Colors.RED , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Осмотреть", function = lambda: input("Возле ворот стоит статуя стража, сама крепость не такая уж большая")),
    classes.Action("Идти дальше", function = lambda: SetEvent(EventID.StartFight)),
    ]),
    classes.Event("Страж стоявший неподвижно вдруг зашевилился и пошагал в вашу сторону, поднялась метель",textColor = Colors.RED , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action(f'Атаковать врага',backColor= Colors.RED, textColor = Colors.DARK_RED, function = lambda: Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    ]),
    classes.Event(f'Страж замахиваеться',textColor = Colors.RED , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action(f'Атаковать врага',backColor= Colors.RED, textColor = Colors.DARK_RED, function = lambda: Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    ]),
] 

ICE_STRONGHOLD_EVENTS = [
    classes.Event("на в дыму виднеется чей то силуэт",textColor = Colors.RED , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Идти дальше",backColor= Colors.GREEN, textColor = Colors.LIGHT_GREEN, function = lambda: StartFight),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("вы слышите чье-то рычание впереди, осмотревшись вы видите врага",textColor = Colors.RED , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action(f'Атаковать врага',backColor= Colors.RED, textColor = Colors.DARK_RED, function = lambda: Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    classes.Action("Сбежать", function = TryRunAway),
    ]),
    classes.Event(f'враг готовится нанести удар',textColor = Colors.RED, curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action(f'Атаковать врага',backColor= Colors.RED, textColor = Colors.DARK_RED, function = lambda: Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    classes.Action("Сбежать", function = TryRunAway),
    ]),
    classes.Event("вы прислушались. по крепости ходит гул метели снаружи", textColor = Colors.BLUE, curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("вы резко остановились на полу странная плита", textColor = Colors.BLUE, curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Идти дальше", function = lambda: TakeDamage(30)),
    classes.Action("обойти", function = GoOtherWay),
    ]),
    classes.Event("в замешательстве вы пришли в огромный зал", textColor = Colors.BLUE , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Осмотреть", function = lambda: input("Осмотревшись вы выдите стоящих вдоль колонн рыцарей, кажеться это просто стенды\nДалее...")),
    classes.Action("Снять броню со стенда", function = lambda: TakeRandomItem(vars.TIER3_FROZEN_ARMORY)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другой коридор", function = GoOtherWay),
    ]),
    classes.Event("вы пришли в длинный корридор в конце которого стоит сундук",textColor = Colors.BLUE , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Осмотреть Коридор", function = lambda: input("длинный узкий коридор в конце которого стоит сундук\nДалее...")),
    classes.Action("Открыть Сундук", function = lambda: TakeRandomItem(vars.TIER3_FROZEN_CHEST)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другой корридор", function = GoOtherWay),
    ]),
    classes.Event("блукая вы пришли в зал с длинными столами в ряд", textColor = Colors.BLUE , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Осмотреть", function = lambda: input("Осмотревшись вы понимаете, вероятно это столовая\nДалее...")),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другой коридор", function = GoOtherWay),
    ]),
    classes.Event("перед вами лежит замороженный труп прислуги",textColor = Colors.BLUE, curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Осмотреть", function = lambda: TakeRandomItem(vars.TIER2_FROZEN_CORPSE)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("вы нашли чей то горящий костер", textColor = Colors.YELLOW, curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("согреться", function = lambda: KeepWarm(3)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("вы нашли чей то горящий костер", textColor = Colors.YELLOW, curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("согреться", function = lambda: KeepWarm(3)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    
]

ICE_STRONGHOLD_BOSS_EVENTS =[
    classes.Event("вы пришли к трону Графа, сам же покровитель воссидает на троне и смотрит на вас",textColor = Colors.RED , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Осмотреть", function = lambda: input("Граф выглядит вполне здоровым, сейчас он под чарами магии")),
    classes.Action("Идти дальше", function = lambda: SetEvent(EventID.StartFight)),
    ]),
    classes.Event(f'Граф:"Всех пришедших чужаков сдесь ждет смерть!"',textColor = Colors.CYAN , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action(f'Атаковать врага',backColor= Colors.RED, textColor = Colors.DARK_RED, function = lambda: Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    ]),
    classes.Event(f'Граф нашептывает заклинания',textColor = Colors.RED , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action(f'Атаковать врага',backColor= Colors.RED, textColor = Colors.DARK_RED, function = lambda: Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    ]),
] 



ETHERIAL_SHORES_EVENTS = [
    classes.Event("впереди в пузырчатой дымке виднеется чей-то силуэт",textColor = Colors.PINK , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Идти дальше",backColor= Colors.GREEN, textColor = Colors.LIGHT_GREEN, function = lambda: StartFight),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("вы слышите чье-то рычание впереди, осмотревшись вы видите врага",textColor = Colors.RED , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action(f'Атаковать врага',backColor= Colors.RED, textColor = Colors.DARK_RED, function = lambda: Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    classes.Action("Сбежать", function = TryRunAway),
    ]),
    classes.Event(f'враг готовится нанести удар',textColor = Colors.RED, curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action(f'Атаковать врага',backColor= Colors.RED, textColor = Colors.DARK_RED, function = lambda: Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    classes.Action("Сбежать", function = TryRunAway),
    ]),
    classes.Event("вы пришли в очень странное место, как в сказках. все какое то... волшебное", textColor = Colors.PINK, curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("впереди вы замечаете нору в земле из которой торчат щупальца", textColor = Colors.PINK, curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Осмотреться", function = lambda: input("из норы в большом кол-ве летят пузырьки, щупальца извиваясь лопают их")),
    classes.Action("Идти дальше", function = lambda: TakeDamage(hit=80)),
    classes.Action("обойти", function = GoOtherWay),
    ]),
    classes.Event("вы видете перед собой искаженное эфирное дерево", textColor = Colors.PINK , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Осмотреться", function = lambda: input("дерево очень странное, растет верх корнями и кроной уходит в густую эфирную почву")),
    classes.Action("Сорвать кору", function = lambda: TakeItem(vars.ItemList[vars.ItemID.EtherealClot], 4)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("вы остановились. Вокруг вас летают сгустки эфира", textColor = Colors.PINK , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Осмотреться", function = lambda: input("все вокруг в пузырчетой розовой пене")),
    classes.Action("Собрать все", function = lambda: TakeItem(vars.ItemList[vars.ItemID.EtherealClot], 4)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("вы остановились. Под ногами из земли появляется слизистый мешочек", textColor = Colors.PINK , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Осмотреться", function = lambda: input("Он не выглядит опасным, судя по всему он полон эфирной пеной")),
    classes.Action("Потрогать", function = lambda: TakeRandomItem(vars.TIER4_ETHERIAL_BAG)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("вы остановились. Под ногами из земли появляется слизистый мешочек", textColor = Colors.PINK , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Осмотреться", function = lambda: input("Он не выглядит опасным, судя по всему внутри что-то есть")),
    classes.Action("Потрогать", function = lambda: TakeRandomItem(vars.TIER4_ETHERIAL_COMBAT_BAG)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("перед вами лежит искаженный труп путника",textColor = Colors.PINK, curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Осмотреть", function = lambda: SetEvent(EventID.EtherialCombatBag)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),

]

ETHERIAL_SHORES_BOSS_EVENTS =[
    classes.Event("Вы пришли к эфирному холму с огромной норой",textColor = Colors.PINK , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action("Осмотреть это", function = lambda: input("Похпже на вход в пещеру")),
    classes.Action("Идти в нору", function = lambda: SetEvent(EventID.StartFight)),
    ]),
    classes.Event("перед вами стоит старик",textColor = Colors.PINK , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action(f'Атаковать врага',backColor= Colors.RED, textColor = Colors.DARK_RED, function = lambda: Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    ]),
    classes.Event(f'Старик использует магию и из пола выползают щупальца корней',textColor = Colors.RED , curentActions=[
    classes.Action("Инвентарь", backColor= Colors.KHAKI, textColor = Colors.BROWN, function = lambda: ShowInventory),
    classes.Action(f'Атаковать врага',backColor= Colors.RED, textColor = Colors.DARK_RED, function = lambda: Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    ]),
    classes.Event("После победы вы видите проход в эфирные пещеры \nСпустившись вы видите что охранял Зрек",textColor = Colors.PINK , curentActions=[
    classes.Action("Осмотреть это", function = lambda: input("Переплетение корней в один узел - Сердце Эфира, перерезав их Эфирные земли исчезнут!")),
    classes.Action("подойти и уничтожить", function = MoveOn),
    ]),
] 
'''








Elist: list[classes.Event] = deepcopy(FOREST_EVENTS) # текущие события (сцены)

'''
FORK_EVENTS = [classes.Event("вы пришли к тому что охраняло чудовище к табличке с направлениями",textColor = Colors.YELLOW , curentActions=[
    classes.Action(f'Идти в (Замок)', function = lambda: SetLocation(events = CASTLE_EVENTS, locInt = locvars.Locations.Castle)),
    classes.Action(f'Идти в (Расплавленную долину)', function = lambda: SetLocation(events = MOLTEN_VALLEY_EVENTS, locInt = locvars.Locations.MoltenValley)),
    classes.Action(f'Идти в (Замороженное Озеро)', function = lambda: SetLocation(events = ICE_LAKE_EVENTS, locInt = locvars.Locations.IceLake)),
    classes.Action(f'Идти в (Эфирные Берега)', function = lambda: SetLocation(events = ETHERIAL_SHORES_EVENTS, locInt = locvars.Locations.EtherealShores)),
    ])]

'''




class Game(Frame):
    def __init__(self,tk): 
        super(Game,self).__init__(tk)

        # Кнопки для меню прибавления и вычитания
        self.Counter = 0 # counter number
        self.AddBtn = Button(text="+",bg= Colors.PEACH,font =('ImesNewRoman',18,'bold'),fg = Colors.GREEN, command= lambda: self.ChangeCNumber(1))
        self.SubtractBtn = Button(text="-",bg= Colors.PEACH,font =('ImesNewRoman',18,'bold'),fg = Colors.RED, command= lambda: self.ChangeCNumber(-1))
        self.AddBtn.pack(anchor= "w", side= LEFT, ipadx = 30)
        self.SubtractBtn.pack(anchor= "w", side= LEFT,  ipadx = 30)

        # Вариант сцены для Tkinter
        self.TK_Scene: classes.TkScene = classes.TkScene(Label(text="Вы пришли к тому что охраняло чудовище к табличке с направлениями",font = ('ImesNewRoman',25,'bold'),bg = '#000',fg = '#fff'), curentActionsBar=[
            Button(text="Идти в (Замок)",bg='#F5DEB3',font =('ImesNewRoman',18,'bold'),fg = '#FFD700', command= lambda: print("пустое действие")),
            ])

        # Коле статов
        self.Stats_Area = Label(text=f'stats ',font = ('ImesNewRoman',20,'bold'),bg = '#000',fg = '#fff')
        self.Stats_Area.pack(anchor="w", fill= X) #padx, pady

        # Изображение локации
        self.screenImage = PhotoImage(file =imgs.startScreen).zoom(4,4)
        self.screen = Label(image= self.screenImage, bg= Colors.BLACK)
        self.screen.pack(fill = X)

        # Описание локации
        self.TK_Scene.textArea = Label(text=f'Event Name Text Area',font = ('ImesNewRoman',20,'bold'),bg = '#000',fg = '#fff')
        self.TK_Scene.textArea.pack(anchor="w", fill= X) #padx, pady

        
        # Иконки кнопок
        self.btnIcons = [PhotoImage(file=imgs.circle)]

        
        self.StartScreen()

    def StartScreen(self):

        locvars.Scene = classes.Event("ДОБРО ПОЖАЛОВАТЬ В subRPG (*Tkinter)",screen= imgs.startScreenTitle, backColor= Colors.BLACK ,textColor = Colors.LIGHT_BLUE , curentActions=[
                classes.Action("Нажмите, чтобы НАЧАТЬ играть", icon= imgs.circle,backColor= Colors.KHAKI, textColor = Colors.GREEN, function = lambda: SetNewScene),
                #classes.Action("получить стартовый набор предметов",backColor= Colors.PEACH, textColor = Colors.BROWN, function = lambda: self.GiveStarterKit),
                classes.Action("Об игре",backColor= Colors.PEACH,icon= imgs.look, textColor = Colors.BROWN, function = lambda: self.AboutGame),
                ])
        self.UpdateScneneGUI("w")

        #locvars.ZeroScene = funks.Elist[funks.EventID.Forest]
        #locvars.Scene = locvars.ZeroScene


        #Развилка
        #SetLocation(WILD_FOREST_EVENTS, locvars.Locations.WildForest)
        #vars.actStep = 32


    def UpdateScneneGUI(self, BtnAnchor):
        self.PrintStats()
        

        self.screenImage = PhotoImage(file= locvars.Scene.screen).zoom(4,4)
        self.screen.config(image= self.screenImage)

        self.TK_Scene.textArea.config(text=locvars.Scene.name, bg= locvars.Scene.backColor ,fg= locvars.Scene.textColor) #padx, pady
       

        self.ClearActionBar()

        i = 0
        for action in locvars.Scene.curentActions:
            self.btnIcons.append(PhotoImage(file = action.icon))

            btn = Button(text= f'{action.name}',bg= action.backColor, fg= action.textColor, font =('TimesNewRoman',21,'bold'), command= action.function(), image= self.btnIcons[i] ,compound="left")
            self.TK_Scene.curentActionsBar.append(btn)
            btn.pack(anchor= BtnAnchor, ipadx = 10 ) #fill= X
            i += 1


    def UpdateAll(self):
        time.sleep(0.03)
        CheckLocation()
        self.UpdateScneneGUI('w')

        if vars.ARMOR <= 0:
                        vars.ARMOR = 0


        if vars.HP <= 0:
            
            print(f'{Colors.RED}Игра Окончена \n{Colors.WHITE}')
            print("Ваше здоровье =", vars.HP)

    def OpenCounterWindow(self, screen):
        self.PrintStats()
        

        self.screenImage = PhotoImage(file= screen).zoom(4,4)
        self.screen.config(image= self.screenImage)

        self.TK_Scene.textArea.config(text= self.Counter, bg= locvars.Scene.backColor ,fg= locvars.Scene.textColor) #padx, pady
       
        self.ClearActionBar()

        self.AddBtn = Button(text="+",bg= Colors.PEACH,font =('ImesNewRoman',18,'bold'),fg = Colors.GREEN, command= lambda: self.ChangeCNumber(1))
        self.SubtractBtn = Button(text="-",bg= Colors.PEACH,font =('ImesNewRoman',18,'bold'),fg = Colors.RED, command= lambda: self.ChangeCNumber(-1))
        self.AddBtn.pack(anchor= "n", ipadx = 30)
        self.SubtractBtn.pack(anchor= "n",  ipadx = 30)

        
        i = 0
        for action in locvars.Scene.curentActions:
            self.btnIcons.append(PhotoImage(file = action.icon))

            btn = Button(text= f'{action.name}',bg= action.backColor, fg= action.textColor, font =('TimesNewRoman',21,'bold'), command= action.function(), image= self.btnIcons[i] ,compound="left")
            self.TK_Scene.curentActionsBar.append(btn)
            btn.pack(anchor= "w", ipadx = 10 ) #fill= X
            i += 1   
      
    def ChangeCNumber(self, add):
        self.Counter += add
        if self.Counter <= 0:
            self.Counter = 0
        self.TK_Scene.textArea.config(text= self.Counter, bg= locvars.Scene.backColor ,fg= locvars.Scene.textColor) #padx, pady


    def ClearActionBar(self):
        self.AddBtn.destroy()
        self.SubtractBtn.destroy()
        for btn in self.TK_Scene.curentActionsBar:
            btn.destroy()
        del self.btnIcons[:]  
        del self.TK_Scene.curentActionsBar[:]

    def PrintStats(self):
        vars.statsLine = f'step:{vars.step}    act:{vars.actStep}'
        vars.statsLine += f'\nЛокация: {locvars.stringLocation[locvars.LOCATION]}'
        vars.statsLine += f'\nЖизни:{vars.HP}    Броня:{vars.ARMOR}    Деньги:{vars.MONEY}\n'

        if vars.isFrost == True:
            vars.statsLine +=f'{Colors.BLUE}[Дебафф: Холод]{Colors.WHITE}'

        if vars.deBUFF_frostbite != 0:
            vars.statsLine += f'[Дебафф: обморожение на {Colors.CYAN}{vars.deBUFF_frostbite}{Colors.WHITE} актов]'

        if vars.BUFF_warm != 0 and vars.isFrost == True:
            vars.statsLine += f'[Бафф:вы согреты на {Colors.YELLOW}{vars.BUFF_warm}{Colors.WHITE} актов]'

        if vars.BUFF_regeneration != 0:
            vars.statsLine += f'[Бафф:Регенерация на {Colors.GREEN}{vars.BUFF_regeneration}{Colors.WHITE} актов]'
    
        self.Stats_Area.config(text= vars.statsLine, bg= Colors.DARK_GRAY)

    def GiveStarterKit(self):
        TakeRandomItem(vars.StarterPack)
        TakeRandomItem(vars.StarterPack)
        TakeRandomItem(vars.StarterPack)
        
    

    
      
    def AboutGame(self):
        textAbout = "Порт игры subRPG на Tkinter\nкроме переноса всего контента с оригинала, игра получит\nряд нового контента, что в значительной мере расширит игру"

        locvars.Scene = classes.Event(textAbout, 
                                    screen= imgs.startScreen,
                                    backColor= Colors.BLACK,
                                    textColor = Colors.LIGHT_CYAN,
                                    curentActions=[
                classes.Action("Назад",icon= imgs.ring, backColor= Colors.PEACH, textColor = Colors.BROWN, function = lambda: self.StartScreen),
                ])
        
        self.UpdateScneneGUI("c")


    




tk = Tk()
tk ['bg']= Colors.PAPER
#tk.resizable(False,False)
tk.geometry ('1200x720+200+200')
tk.title('sub_RPG')
window = Game(tk)
window.pack()
tk.mainloop()