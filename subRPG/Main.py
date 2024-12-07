from modules import vars
from modules import classes
from modules import locvars
from copy import deepcopy
from enum import IntEnum
from tkinter import *
import sqlite3
import random
import time


def ShowInventory():
    vars.Weapon.equip = True
    
    locvars.Scene.name = "Инвентарь:"
    del locvars.Scene.curentActions[:]
    locvars.Scene.curentActions.append(classes.Action(f'<- Назад',lambda: ReturnToJourney))

    i = 0
    for Islot in vars.Inventory:

        i += 1

        ExamineItemIsZeroCount(i-1)

        if Islot.equip == True:
            locvars.Scene.curentActions.append(classes.Action(f'(Экирировано)\n{Islot.item.name}({Islot.count}x) урон:{Islot.item.damage} цена: {Islot.item.cost}$',lambda: ReturnToJourney))
            continue
        if Islot.item.damage == 0:
            locvars.Scene.curentActions.append(classes.Action(f'{Islot.item.name}({Islot.count}x) цена: {Islot.item.cost}$',lambda: ReturnToJourney))
        else:
            locvars.Scene.curentActions.append(classes.Action(f'{Islot.item.name}({Islot.count}x) урон:{Islot.item.damage} цена: {Islot.item.cost}$',lambda: ReturnToJourney))

    window.UpdateAll()

    
    

def TakeItem(item = classes.Item, count = int):
    print("Take Item")

    vars.actStep += 1

    if item == vars.ItemList[vars.ItemID.Empty]:
        MinorEvent("Пусто...", "Далее", SetNewScene)
        return

    vars.Inventory.append(classes.Slot(item, count, False))
    MinorEvent(f'Получено > {item.name} ({count}x)', "взять", SetNewScene)

def TakeRandomItem(itemPool):
    print("Take Random Item")
    rndId = random.randint(0, len(itemPool) -1)
    item = classes.Item
    item = itemPool[rndId]
    rndCount = random.randint(1, item.stackCount)
    TakeItem(item, rndCount)




def UseHealPotion(potion = classes.Item):
    if potion == vars.ItemList[vars.ItemID.SmallHealPotion]:
        Heal(15)
    elif potion == vars.ItemList[vars.ItemID.MiddleHealPotion]:
        Heal(25)
    elif potion == vars.ItemList[vars.ItemID.LargeHealPotion]:
        Heal(50)

    
    if potion == vars.ItemList[vars.ItemID.SmallRegenPotion]:
        vars.BUFF_regeneration += 3
        Heal(15)
    elif potion == vars.ItemList[vars.ItemID.MiddleRegenPotion]:
        vars.BUFF_regeneration += 6
        Heal(25)
    elif potion == vars.ItemList[vars.ItemID.LargeRegenPotion]:
        vars.BUFF_regeneration += 12
        Heal(45)
        

def Heal(healPoints):
    vars.HP += healPoints
    print(f'\nВы полечились на {healPoints} ед здоровья \nТекущее здоровье:{vars.HP}')
    #input("Далее...")


def TakeArmor(item: classes.Item):
    armorPoint = 0


    if item == vars.ItemList[vars.ItemID.LeatherArmor]:
        vars.BUFF_warm += 10
        armorPoint = 20

    if item == vars.ItemList[vars.ItemID.SteelArmor]:
        armorPoint = 50

    if item == vars.ItemList[vars.ItemID.SilverArmor]:
        armorPoint = 65

    if item == vars.ItemList[vars.ItemID.MeteoriteArmor]:
        armorPoint = 75

    if item == vars.ItemList[vars.ItemID.IceArmor]:
        vars.deBUFF_frostbite += 10
        armorPoint = 150

    if item == vars.ItemList[vars.ItemID.EtherealArmor]:
        armorPoint = 100

    vars.ARMOR += armorPoint
    print(f'Вы надели {item.name}')
    #input(f'Получено {armorPoint} ед. брони \nТекущая Броня:{vars.ARMOR}\n')



def ExamineItemIsZeroCount(slotNumber):
    if vars.Inventory[slotNumber].count <= 0:
        vars.Inventory.remove(vars.Inventory[slotNumber])


def ShowStore():
    print(f'Деньги:{vars.MONEY}')
    print("1. Продать\n2. Купить")
    
    

    
def ShowSellMenu():
    
    vars.Weapon.equip = True
    

    print("0: назад")
    i = 0
    for Islot in vars.Inventory:
        ExamineItemIsZeroCount(i-1)

        i += 1
        if Islot.equip == True:
            print(f'\n {i}: {Islot.item.name} товар экипирован (нельзя продать)\n')
            continue
        
        print(f' {i}: {Islot.item.name}({Islot.count}x)', "цена:", Islot.item.cost, "$")

    a = int(input("\n Действие:"))
    vars.clear()

    if a == 0:
        return
    if vars.Inventory[a-1].equip == True:
        input("вы не можете продать экипированный предмет")
        return

    slot = vars.Inventory[a-1]
    

    print(f'что вы хотите сделать с {slot.item.name}({slot.count})?')
    print("1: Назад\n2. Продать \n3. Продать всё")
    
    b = int(input("\n Действие:"))

    if b == 2:
        c = int(input(f'Сколько вы хотите продать из {slot.count}?\n...'))
        
        if c > slot.count:
            vars.clear()
            input("У вас столько нет")
            ShowSellMenu()
            return
        
        Sell(sellCount = c,slotNumber = a-1, cost = slot.item.cost)

    elif b == 3:
        Sell(sellCount = slot.count,slotNumber = a-1, cost = slot.item.cost)


def Sell(sellCount, slotNumber, cost):
    #i = int(input(f'вы действительно хотите продать {sellCount}x?  \n 1. Да\n 2. Нет\n...'))

    #if i == 1:
    saleMoney = cost * sellCount
    vars.MONEY += saleMoney
    vars.Inventory[slotNumber].count -= sellCount
    ExamineItemIsZeroCount(slotNumber)
    print("вы продали", sellCount)

    #input("Далее...")


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
        

    vars.clear()
    buyItem = assortment[a-1]

    print("1. Назад \n2. Купить")
    b = int(input("действие:"))

    if b == 2:
        vars.clear()
        c = int(input(f'Сколько вы хотите купить {buyItem.name}?\n'))
        Buy(buyItem, c)


    




def Buy(buyItem = classes.Item ,buyCount = int):
    if vars.MONEY < buyCount * buyItem.cost:
        input("У вас не хватает денег\n")

        vars.clear()
        return
    
    if buyCount > buyItem.stackCount:
        vars.Inventory.append(classes.Slot(buyItem, buyItem.stackCount, False))
        vars.Inventory.append(classes.Slot(buyItem, buyCount - buyItem.stackCount, False))
    else:
        vars.Inventory.append(classes.Slot(buyItem, buyCount, False))
    
    vars.MONEY -= buyCount * buyItem.cost
    vars.clear()
    input(f'Вы купили ({buyCount}) {buyItem.name} за {buyCount * buyItem.cost} денег')
    return



def MoveOn():
    vars.actStep += 1
    SetNewScene()
    locvars.Scene.name = f'вы пошли дальше...\n' + locvars.Scene.name
    window.UpdateAll()
    


def GoOtherWay():
    vars.actStep += 1
    rndPeacefulPlace = random.randint(3, len(Elist) - 1)
    locvars.Scene = deepcopy(Elist[rndPeacefulPlace])
    locvars.curEventId = rndPeacefulPlace
    CheckLocation()
    locvars.Scene.name = f'вы пошли другой дорогой\n' + locvars.Scene.name
    window.UpdateAll()
   


def Attack():

    locvars.Scene = deepcopy(Elist[EventID.OnFight])
    locvars.Scene.name = f'вы атаковали {vars.curEnemy.name} на {vars.Weapon.item.damage} ед. урона'


    vars.curEnemy.HP -= vars.Weapon.item.damage

    if vars.curEnemy.HP <= 0:
        MinorEvent("враг мертв, на сей раз вы победили\nВы осматриваете врага", "Далее", lambda: TakeRandomItem(vars.TIER1_MONSTER_DROP))
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
        MinorEvent(f'вы удачно сбежали!', "Далее", SetNewScene)
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
    MinorEvent(f'вы пошли в {locvars.stringLocation[locvars.LOCATION]}', "Далее", SetNewScene)



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
    if locvars.LOCATION == locvars.Locations.Forest:
        vars.StoreAssortment = vars.ASSORTMENT_DEFAULT
        if vars.actStep % 15 == 0:
            SetLocation(events = WILD_FOREST_EVENTS, locInt = locvars.Locations.WildForest)
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
            locvars.Scene = classes.Event("Вы прошли игру. Концовка - Убийца Королей", themeColor = classes.Colors.YELLOW , curentActions=[
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
                locvars.Scene = classes.Event("Вы прошли игру. Концовка - Драконоборец", themeColor = classes.Colors.YELLOW , curentActions=[
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
                locvars.Scene = classes.Event("Вы прошли игру. Концовка - Хладнокровный", themeColor = classes.Colors.YELLOW , curentActions=[
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
                locvars.Scene = classes.Event("Вы перерезали Сплетения сердца, земля начинает очищаться\n Вы прошли игру. Концовка - Срубил под Корень Проблемы", themeColor = classes.Colors.GREEN , curentActions=[
                classes.Action("Завершить", function = lambda: input("Спасибо за игру!\n"))])



def PrintStats():
    #vars.clear()
    vars.statsLine = f'step:{vars.step}    act:{vars.actStep}'
    vars.statsLine += f'\nЛокация: {locvars.stringLocation[locvars.LOCATION]}'
    vars.statsLine += f'\nЖизни:{vars.HP}    Броня:{vars.ARMOR}    Деньги:{vars.MONEY}\n'

    if vars.isFrost == True:
        vars.statsLine +=f'{classes.Colors.BLUE}[Дебафф: Холод]{classes.Colors.WHITE}'

    if vars.deBUFF_frostbite != 0:
        vars.statsLine += f'[Дебафф: обморожение на {classes.Colors.CYAN}{vars.deBUFF_frostbite}{classes.Colors.WHITE} актов]'

    if vars.BUFF_warm != 0 and vars.isFrost == True:
        vars.statsLine += f'[Бафф:вы согреты на {classes.Colors.YELLOW}{vars.BUFF_warm}{classes.Colors.WHITE} актов]'

    if vars.BUFF_regeneration != 0:
        vars.statsLine += f'[Бафф:Регенерация на {classes.Colors.GREEN}{vars.BUFF_regeneration}{classes.Colors.WHITE} актов]'



def SetNewScene():
    randomEvent = random.randint(0, len(Elist)-1)
    locvars.Scene = deepcopy(Elist[randomEvent])
    locvars.curEventId = randomEvent

    if randomEvent == EventID.StartFight or randomEvent == EventID.OnFight:
        vars.clear()
        locvars.curEventId = EventID.StartFight
        StartFight()

    CheckLocation()  
    CheckBuffs()
    vars.step += 1
    window.UpdateAll()


#TKINTER LOGIC

def MinorEvent(eventName, actionName, funcion):
    locvars.Scene = classes.Event(f'{eventName}', themeColor = classes.Colors.GREEN , curentActions=[
                classes.Action(f'{actionName}', function = lambda: funcion),
                ])
    vars.step += 1
    window.UpdateAll()
    

def ReturnToJourney():
    locvars.Scene = deepcopy(Elist[locvars.curEventId])
    print(locvars.curEventId)
    print(Elist[locvars.curEventId].name)
    CheckLocation()  
    CheckBuffs()
    vars.step += 1
    window.UpdateAll()






#Все События (Сцены)

class EventID(IntEnum):
    PossibleFight = 0
    StartFight = 1
    OnFight = 2

    # Лес
    Forest = 3
    Well = 4
    Village = 5
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

FOREST_EVENTS = [
    classes.Event("на вашем пути появился чей то силуэт",themeColor = classes.Colors.GREEN , curentActions=[
    classes.Action("Инвентарь", function = lambda: ShowInventory),
    classes.Action("Идти дальше", function = lambda: StartFight),
    classes.Action("Пойти в другую сторону", function =lambda: GoOtherWay),
    ]),
    classes.Event("вы слышите чье-то рычание впереди, осмотревшись вы видите врага",themeColor = classes.Colors.RED , curentActions=[
    classes.Action("Инвентарь", function = lambda: ShowInventory),
    classes.Action(f'Атаковать врага', function = lambda: Attack),
    classes.Action("Статы врага", function = lambda: ShowEnemyStats),
    classes.Action("Сбежать", function = lambda: TryRunAway),
    ]),
    classes.Event(f'враг готовится нанести удар',themeColor = classes.Colors.RED , curentActions=[
    classes.Action("Инвентарь", function =  lambda: ShowInventory),
    classes.Action(f'Атаковать врага', function = lambda: Attack),
    classes.Action("Статы врага", function = lambda: ShowEnemyStats),
    classes.Action("Сбежать", function = lambda: TryRunAway),
    ]),
    classes.Event("скитаясь вы пришли к лесу", themeColor = classes.Colors.GREEN , curentActions=[
    classes.Action("Инвентарь", function =  lambda: ShowInventory),
    classes.Action("Магазин", function = lambda: ShowStore),
    classes.Action("Идти дальше", function = lambda:  MoveOn),
    classes.Action("Пойти в другую сторону", function = lambda: GoOtherWay),
    ]),
    classes.Event("вы набрели на разрушенный пустой колодец. здесь спокойно и можно передохнуть", themeColor = classes.Colors.GREEN, curentActions=[
    classes.Action("Инвентарь", function = lambda: ShowInventory),
    classes.Action("Осмотреть", function = lambda: MinorEvent("Колодец настолько стар, что едва можно разлечить\n его руины поросшие мхом, сомневаюсь что внутри\n есть вода\nДалее...", "Назад", ReturnToJourney)),
    classes.Action("Посмотреть в колодец", function = lambda: TakeRandomItem(vars.TIER1_WELL_items)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = lambda: GoOtherWay),
    ]),
    classes.Event("скитаясь вы пришли к лесу", themeColor = classes.Colors.GREEN, curentActions=[
    classes.Action("Инвентарь", function = lambda: ShowInventory),
    classes.Action("Магазин", function = lambda:ShowStore),
    classes.Action("Идти дальше", function = lambda:  MoveOn),
    classes.Action("Пойти в другую сторону", function = lambda: GoOtherWay),
    ]),
    classes.Event("скитаясь вы пришли в заброшенную деревню",themeColor = classes.Colors.GREEN, curentActions=[
    classes.Action("Инвентарь", function = lambda: ShowInventory),
    classes.Action("Осмотреть дома", function = lambda: lambda: TakeRandomItem(vars.TIER1_VILLAGE_items)),
    classes.Action("Идти дальше", function = lambda: MoveOn),
    classes.Action("Пойти в другую сторону", function = lambda: GoOtherWay),
    ]),
]

WILD_FOREST_EVENTS = [
    classes.Event("на вашем пути появился чей то силуэт",themeColor = classes.Colors.GREEN , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Идти дальше", function = StartFight),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("вы слышите чье-то рычание впереди, осмотревшись вы видите врага",themeColor = classes.Colors.RED , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action(f'Атаковать врага', function = Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    classes.Action("Сбежать", function = TryRunAway),
    ]),
    classes.Event(f'враг готовится нанести удар',themeColor = classes.Colors.RED, curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action(f'Атаковать врага', function = Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    classes.Action("Сбежать", function = TryRunAway),
    ]),
    classes.Event("скитаясь вы пришли к лесу", themeColor = classes.Colors.GREEN, curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("вы замечаете растяжку", themeColor = classes.Colors.GREEN, curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Идти дальше", function = lambda: TakeDamage(hit=15)),
    classes.Action("обойти", function = GoOtherWay),
    ]),
    classes.Event("вы резко остановились впереди в прелой листве блестает капкан",themeColor = classes.Colors.GREEN, curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Идти дальше", function = lambda: TakeDamage(hit=25)),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("земля бурлит от дыма, приглядевшись вы замечаете что стоите на упавшем метеорите",themeColor = classes.Colors.GREEN, curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Взять остывший камень под ногами", function = lambda: TakeItem(vars.ItemList[vars.ItemID.MeteoritePiece], 1)),
    classes.Action("Потрогать землю", function = lambda: TakeDamage(100)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("вы замечаете чью-то протоптанную тропинку", themeColor = classes.Colors.GREEN , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Идти по тропинке", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
]

FOREST_BOSS_EVENTS =[
    classes.Event("на вашем пути появилась огромная тварь",themeColor = classes.Colors.RED , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Идти дальше", function = lambda: SetEvent(EventID.StartFight)),
    ]),
    classes.Event("вы слышите оглушающий рев, осмотревшись вы видите его",themeColor = classes.Colors.RED , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action(f'Атаковать врага', function = Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    ]),
    classes.Event(f'Босс готовится нанести удар',themeColor = classes.Colors.RED , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action(f'Атаковать врага', function = Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    ]),
] 



CASTLE_EVENTS = [
    classes.Event("в глубине коридора виден чей то силуэт",themeColor = classes.Colors.YELLOW , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Идти дальше", function = StartFight),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("вы слышите чье-то рычание впереди, осмотревшись вы видите врага",themeColor = classes.Colors.RED , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action(f'Атаковать врага', function = Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    classes.Action("Сбежать", function = TryRunAway),
    ]),
    classes.Event(f'враг готовится нанести удар',themeColor = classes.Colors.RED , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action(f'Атаковать врага', function = Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    classes.Action("Сбежать", function = TryRunAway),
    ]),
    classes.Event("в замешательстве вы пришли в огромный зал", themeColor = classes.Colors.YELLOW , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Осмотреть", function = lambda: input("Осмотревшись вы увидели табличку (Зал Церемоний)\nДалее...")),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другой коридор", function = GoOtherWay),
    ]),
    classes.Event("вы идете по корридору и замечаете странную плиту под ногами",themeColor = classes.Colors.YELLOW , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Идти дальше", function = lambda: TakeDamage(hit=25)),
    classes.Action("обойти", function = GoOtherWay),
    ]),
    classes.Event("блукая вы пришли в зал с длинными столами в ряд", themeColor = classes.Colors.YELLOW , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Осмотреть", function = lambda: input("Осмотревшись вы понимаете, вероятно это столовая\nДалее...")),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другой коридор", function = GoOtherWay),
    ]),
    classes.Event("вы пришли в длинный корридор в конце которого стоит сундук",themeColor = classes.Colors.YELLOW , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Осмотреть Коридор", function = lambda: input("длинный величественный коридор с высокими потолками, с развешанными королевскими флагами по стенам\nДалее...")),
    classes.Action("Открыть Сундук", function = lambda: TakeRandomItem(vars.TIER2_CHEST)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другой корридор", function = GoOtherWay),
    ]),
    classes.Event("кажеться вы заблудились в однообразных коридорах но наткнулись на зал с колоннами", themeColor = classes.Colors.YELLOW , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Осмотреть", function = lambda: input("Осмотревшись вы выдите стоящих вдоль колонн рыцарей, кажеться это просто стенды\nДалее...")),
    classes.Action("Снять броню со стенда", function = lambda: TakeRandomItem(vars.TIER2_ARMOR_STAND)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другой коридор", function = GoOtherWay),
    ]),
    classes.Event("Вы пришли в библиотеку, перед собой вы видите шкаф с книгами", themeColor = classes.Colors.YELLOW , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Идти дальше", function = GoOtherWay),
    classes.Action(f'Читать "Искуство Битвы или пособие рыцаря"', function = lambda: input("бегло прочитав вы остановили свой взор на строчке 'не с каждым противником стоит сражаться, чем больше шанс врагу промазать, тем больше шанс вам сбежать '\nДалее...")),
    classes.Action(f'Читать "Летопись Королевства Талунга"', function = lambda: input("из летописи вы поняли,что королевство спокойно существовало. ничего интересного, кроме упомянаний какого-то забавного незнакомца - Зрека\nДалее...")),
    classes.Action(f'Читать "Поручение от Графа"', function = lambda: input("достопочтенный король Талунг, вынужден принять меры в связи с последними событиями и заморозить свои земли до прекращения ***\nДалее...")),
    classes.Action(f'Читать неизвестную книгу', function = lambda: input("Когда шаман Зрек падет, на землю камень упадет, ну а потом шаман придет, и снова станет он силен ***рные берега он разольет [обрывается]\nДалее...")),
    ]),
    classes.Event("вы снова пришли в какой-то из коридоров ведущий в 4 направления. Вы забыли откуда пришли", themeColor = classes.Colors.YELLOW , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Осмотреть", function = lambda: input("Осмотревшись вы увидели табличку (<<Столовая, Библиотека>>)\nДалее...")),
    classes.Action("Идти прямо", function = MoveOn),
    classes.Action("Пойти налево", function = lambda: SetEvent(EventID.DiningRoom)),
    classes.Action("Пойти направо", function = lambda: SetEvent(EventID.Library)),
    classes.Action("Пойти в назад", function = GoOtherWay),
    ]),
    classes.Event("вы снова пришли в какой-то из коридоров ведущий в 4 направления. Вы забыли откуда пришли", themeColor = classes.Colors.YELLOW , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Осмотреть", function = lambda: input("Осмотревшись вы увидели табличку (<<Оружейная, Библиотека>>)\nДалее...")),
    classes.Action("Идти прямо", function = MoveOn),
    classes.Action("Пойти налево", function = lambda: SetEvent(EventID.Armory)),
    classes.Action("Пойти направо", function = lambda: SetEvent(EventID.Library)),
    classes.Action("Пойти в назад", function = GoOtherWay),
    ]),
    classes.Event("вы снова пришли в какой-то из коридоров ведущий в 4 направления. Вы забыли откуда пришли", themeColor = classes.Colors.YELLOW , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Осмотреть", function = lambda: input("Осмотревшись вы увидели табличку (<<Зал Церемоний, Хранилище>>)\nДалее...")),
    classes.Action("Идти прямо", function = MoveOn),
    classes.Action("Пойти налево", function = lambda: SetEvent(EventID.CeremonyHall)),
    classes.Action("Пойти направо", function = lambda: SetEvent(EventID.CorridorChest)),
    classes.Action("Пойти в назад", function = GoOtherWay),
    ]),
    
]

CASTLE_BOSS_EVENTS =[
    classes.Event("Наконец вы пришли в тронный зал, но на троне воссидает уже измененый король",themeColor = classes.Colors.RED , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Идти дальше", function = lambda: SetEvent(EventID.StartFight)),
    ]),
    classes.Event("Вы видите как из спины короля торчат щупальца, а глаза его черны.Опоздали его уже не спасти",themeColor = classes.Colors.RED , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action(f'Атаковать врага', function = Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    ]),
    classes.Event(f'Король готовится нанести удар',themeColor = classes.Colors.RED , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action(f'Атаковать врага', function = Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    ]),
] 



MOLTEN_VALLEY_EVENTS = [
    classes.Event("на в дыму виднеется чей то силуэт",themeColor = classes.Colors.RED , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Идти дальше", function = StartFight),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("вы слышите чье-то рычание впереди, осмотревшись вы видите врага",themeColor = classes.Colors.RED , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action(f'Атаковать врага', function = Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    classes.Action("Сбежать", function = TryRunAway),
    ]),
    classes.Event(f'враг готовится нанести удар',themeColor = classes.Colors.RED, curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action(f'Атаковать врага', function = Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    classes.Action("Сбежать", function = TryRunAway),
    ]),
    classes.Event("вы бредете в завесе дыма на ощупь", themeColor = classes.Colors.RED, curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Потрогать землю", function = lambda: TakeDamage(50)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("впереди слышен гейзер", themeColor = classes.Colors.RED, curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Потрогать землю", function = lambda: TakeDamage(50)),
    classes.Action("Идти дальше", function = lambda: TakeDamage(hit=30)),
    classes.Action("обойти", function = GoOtherWay),
    ]),
    classes.Event("впереди слышен гейзер", themeColor = classes.Colors.RED, curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Потрогать землю", function = lambda: TakeDamage(50)),
    classes.Action("Идти дальше", function = lambda: TakeDamage(hit=30)),
    classes.Action("обойти", function = GoOtherWay),
    ]),
    classes.Event("вы наконец пришли в остывшее место, где можно спокойно осмотреться",themeColor = classes.Colors.RED, curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Взять остывший камень под ногами", function = lambda: TakeItem(vars.ItemList[vars.ItemID.MeteoritePiece], 1)),
    classes.Action("Осмотреться", function = lambda: input("вы замечаете дорогу из остывшей породы в гуще дыма в другой стороне")),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = lambda: SetEvent(EventID.ObsidianPath)),
    ]),
    classes.Event("вы идете по обсидиановой дороге, вокруг вас стены дыма", themeColor = classes.Colors.RED , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("подобрать все остывшие камни под ногами", function = lambda: TakeItem(vars.ItemList[vars.ItemID.MeteoritePiece], 3)),
    classes.Action("Идти по тропинке", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("перед вами лежит скелет путника",themeColor = classes.Colors.RED, curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Осмотреть", function = lambda: TakeRandomItem(vars.TIER2_MOLTEN_CORPSE)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = lambda: SetEvent(EventID.ObsidianPath)),
    ]),
]

MOLTEN_VALLEY_BOSS_EVENTS =[
    classes.Event("перед вами огромный кратор",themeColor = classes.Colors.RED , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Спуститься", function = lambda: SetEvent(EventID.StartFight)),
    ]),
    classes.Event("в краторе спало нечто, рык пошелся по всей округе",themeColor = classes.Colors.RED , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action(f'Атаковать врага', function = Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    ]),
    classes.Event(f'Дракон пустошей раскрывает пасть',themeColor = classes.Colors.RED , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action(f'Атаковать врага', function = Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    ]),
] 



ICE_LAKE_EVENTS = [
    classes.Event("впереди в снежном тумане виднеется чей-то силуэт",themeColor = classes.Colors.CYAN , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Идти дальше", function = StartFight),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("вы слышите чье-то рычание впереди, осмотревшись вы видите врага",themeColor = classes.Colors.RED , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action(f'Атаковать врага', function = Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    classes.Action("Сбежать", function = TryRunAway),
    ]),
    classes.Event(f'враг готовится нанести удар',themeColor = classes.Colors.RED, curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action(f'Атаковать врага', function = Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    classes.Action("Сбежать", function = TryRunAway),
    ]),
    classes.Event("поднялся сильный ветер, метель близко", themeColor = classes.Colors.CYAN, curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("впереди магическая ловушка", themeColor = classes.Colors.CYAN, curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Идти дальше", function = lambda: TakeDamage(hit=30)),
    classes.Action("обойти", function = GoOtherWay),
    ]),
    classes.Event("вы резко остановились впереди в сугробе блестает капкан", themeColor = classes.Colors.CYAN, curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Идти дальше", function = lambda: TakeDamage(hit=30)),
    classes.Action("обойти", function = GoOtherWay),
    ]),
    classes.Event("вы видете перед собой ледяное дерево", themeColor = classes.Colors.CYAN , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Сорвать ледяные листья", function = lambda: TakeItem(vars.ItemList[vars.ItemID.IceCrystal], 4)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("под вашими ногами куча мелких осколков льда", themeColor = classes.Colors.CYAN , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("слепить в один кристал", function = lambda: TakeItem(vars.ItemList[vars.ItemID.IceCrystal], 1)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("перед вами лежит замороженный труп путника",themeColor = classes.Colors.CYAN, curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Осмотреть", function = lambda: TakeRandomItem(vars.TIER2_FROZEN_CORPSE)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("вы нашли чей то горящий костер", themeColor = classes.Colors.YELLOW, curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("согреться", function = lambda: KeepWarm(3)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("вы нашли чей то горящий костер", themeColor = classes.Colors.YELLOW, curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("согреться", function = lambda: KeepWarm(3)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    
]

ICE_LAKE_BOSS_EVENTS =[
    classes.Event("Вы пришли к ледяной крепости",themeColor = classes.Colors.RED , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Осмотреть", function = lambda: input("Возле ворот стоит статуя стража, сама крепость не такая уж большая")),
    classes.Action("Идти дальше", function = lambda: SetEvent(EventID.StartFight)),
    ]),
    classes.Event("Страж стоявший неподвижно вдруг зашевилился и пошагал в вашу сторону, поднялась метель",themeColor = classes.Colors.RED , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action(f'Атаковать врага', function = Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    ]),
    classes.Event(f'Страж замахиваеться',themeColor = classes.Colors.RED , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action(f'Атаковать врага', function = Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    ]),
] 

ICE_STRONGHOLD_EVENTS = [
    classes.Event("на в дыму виднеется чей то силуэт",themeColor = classes.Colors.RED , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Идти дальше", function = StartFight),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("вы слышите чье-то рычание впереди, осмотревшись вы видите врага",themeColor = classes.Colors.RED , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action(f'Атаковать врага', function = Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    classes.Action("Сбежать", function = TryRunAway),
    ]),
    classes.Event(f'враг готовится нанести удар',themeColor = classes.Colors.RED, curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action(f'Атаковать врага', function = Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    classes.Action("Сбежать", function = TryRunAway),
    ]),
    classes.Event("вы прислушались. по крепости ходит гул метели снаружи", themeColor = classes.Colors.BLUE, curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("вы резко остановились на полу странная плита", themeColor = classes.Colors.BLUE, curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Идти дальше", function = lambda: TakeDamage(30)),
    classes.Action("обойти", function = GoOtherWay),
    ]),
    classes.Event("в замешательстве вы пришли в огромный зал", themeColor = classes.Colors.BLUE , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Осмотреть", function = lambda: input("Осмотревшись вы выдите стоящих вдоль колонн рыцарей, кажеться это просто стенды\nДалее...")),
    classes.Action("Снять броню со стенда", function = lambda: TakeRandomItem(vars.TIER3_FROZEN_ARMORY)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другой коридор", function = GoOtherWay),
    ]),
    classes.Event("вы пришли в длинный корридор в конце которого стоит сундук",themeColor = classes.Colors.BLUE , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Осмотреть Коридор", function = lambda: input("длинный узкий коридор в конце которого стоит сундук\nДалее...")),
    classes.Action("Открыть Сундук", function = lambda: TakeRandomItem(vars.TIER3_FROZEN_CHEST)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другой корридор", function = GoOtherWay),
    ]),
    classes.Event("блукая вы пришли в зал с длинными столами в ряд", themeColor = classes.Colors.BLUE , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Осмотреть", function = lambda: input("Осмотревшись вы понимаете, вероятно это столовая\nДалее...")),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другой коридор", function = GoOtherWay),
    ]),
    classes.Event("перед вами лежит замороженный труп прислуги",themeColor = classes.Colors.BLUE, curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Осмотреть", function = lambda: TakeRandomItem(vars.TIER2_FROZEN_CORPSE)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("вы нашли чей то горящий костер", themeColor = classes.Colors.YELLOW, curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("согреться", function = lambda: KeepWarm(3)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("вы нашли чей то горящий костер", themeColor = classes.Colors.YELLOW, curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("согреться", function = lambda: KeepWarm(3)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    
]

ICE_STRONGHOLD_BOSS_EVENTS =[
    classes.Event("вы пришли к трону Графа, сам же покровитель воссидает на троне и смотрит на вас",themeColor = classes.Colors.RED , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Осмотреть", function = lambda: input("Граф выглядит вполне здоровым, сейчас он под чарами магии")),
    classes.Action("Идти дальше", function = lambda: SetEvent(EventID.StartFight)),
    ]),
    classes.Event(f'Граф:"Всех пришедших чужаков сдесь ждет смерть!"',themeColor = classes.Colors.CYAN , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action(f'Атаковать врага', function = Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    ]),
    classes.Event(f'Граф нашептывает заклинания',themeColor = classes.Colors.RED , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action(f'Атаковать врага', function = Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    ]),
] 



ETHERIAL_SHORES_EVENTS = [
    classes.Event("впереди в пузырчатой дымке виднеется чей-то силуэт",themeColor = classes.Colors.PINK , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Идти дальше", function = StartFight),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("вы слышите чье-то рычание впереди, осмотревшись вы видите врага",themeColor = classes.Colors.RED , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action(f'Атаковать врага', function = Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    classes.Action("Сбежать", function = TryRunAway),
    ]),
    classes.Event(f'враг готовится нанести удар',themeColor = classes.Colors.RED, curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action(f'Атаковать врага', function = Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    classes.Action("Сбежать", function = TryRunAway),
    ]),
    classes.Event("вы пришли в очень странное место, как в сказках. все какое то... волшебное", themeColor = classes.Colors.PINK, curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("впереди вы замечаете нору в земле из которой торчат щупальца", themeColor = classes.Colors.PINK, curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Осмотреться", function = lambda: input("из норы в большом кол-ве летят пузырьки, щупальца извиваясь лопают их")),
    classes.Action("Идти дальше", function = lambda: TakeDamage(hit=80)),
    classes.Action("обойти", function = GoOtherWay),
    ]),
    classes.Event("вы видете перед собой искаженное эфирное дерево", themeColor = classes.Colors.PINK , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Осмотреться", function = lambda: input("дерево очень странное, растет верх корнями и кроной уходит в густую эфирную почву")),
    classes.Action("Сорвать кору", function = lambda: TakeItem(vars.ItemList[vars.ItemID.EtherealClot], 4)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("вы остановились. Вокруг вас летают сгустки эфира", themeColor = classes.Colors.PINK , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Осмотреться", function = lambda: input("все вокруг в пузырчетой розовой пене")),
    classes.Action("Собрать все", function = lambda: TakeItem(vars.ItemList[vars.ItemID.EtherealClot], 4)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("вы остановились. Под ногами из земли появляется слизистый мешочек", themeColor = classes.Colors.PINK , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Осмотреться", function = lambda: input("Он не выглядит опасным, судя по всему он полон эфирной пеной")),
    classes.Action("Потрогать", function = lambda: TakeRandomItem(vars.TIER4_ETHERIAL_BAG)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("вы остановились. Под ногами из земли появляется слизистый мешочек", themeColor = classes.Colors.PINK , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Осмотреться", function = lambda: input("Он не выглядит опасным, судя по всему внутри что-то есть")),
    classes.Action("Потрогать", function = lambda: TakeRandomItem(vars.TIER4_ETHERIAL_COMBAT_BAG)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("перед вами лежит искаженный труп путника",themeColor = classes.Colors.PINK, curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Осмотреть", function = lambda: SetEvent(EventID.EtherialCombatBag)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),

]

ETHERIAL_SHORES_BOSS_EVENTS =[
    classes.Event("Вы пришли к эфирному холму с огромной норой",themeColor = classes.Colors.PINK , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Осмотреть это", function = lambda: input("Похпже на вход в пещеру")),
    classes.Action("Идти в нору", function = lambda: SetEvent(EventID.StartFight)),
    ]),
    classes.Event("перед вами стоит старик",themeColor = classes.Colors.PINK , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action(f'Атаковать врага', function = Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    ]),
    classes.Event(f'Старик использует магию и из пола выползают щупальца корней',themeColor = classes.Colors.RED , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action(f'Атаковать врага', function = Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    ]),
    classes.Event("После победы вы видите проход в эфирные пещеры \nСпустившись вы видите что охранял Зрек",themeColor = classes.Colors.PINK , curentActions=[
    classes.Action("Осмотреть это", function = lambda: input("Переплетение корней в один узел - Сердце Эфира, перерезав их Эфирные земли исчезнут!")),
    classes.Action("подойти и уничтожить", function = MoveOn),
    ]),
] 


Elist: list[classes.Event] = deepcopy(FOREST_EVENTS) # текущие события (сцены)

"""

FORK_EVENTS = [classes.Event(Label(text="Вы пришли к тому что охраняло чудовище к табличке с направлениями",font = ('ImesNewRoman',25,'bold'),bg = '#000',fg = '#fff'), curentActions=[
    Button(text="Идти в (Замок)",bg='#F5DEB3',font =('ImesNewRoman',21,'bold'),fg = '#FFD700', command= lambda: SetLocation(events = CASTLE_EVENTS, locInt = locvars.Locations.Castle)),
    Button(text="Идти в (Расплавленную долину)",bg='#8B0000',font =('ImesNewRoman',21,'bold'),fg = '#FFD700', command= lambda: SetLocation(events = MOLTEN_VALLEY_EVENTS, locInt = locvars.Locations.MoltenValley)),
    Button(text="Идти в (Замороженное Озеро)",bg='#87CEEB',font =('ImesNewRoman',21,'bold'),fg = '#AFEEEE', command= lambda: SetLocation(events = MOLTEN_VALLEY_EVENTS, locInt = locvars.Locations.MoltenValley)),
    Button(text="Идти в (Эфирные Берега)",bg='#BA55D3',font =('ImesNewRoman',21,'bold'),fg = '#FF1493', command= lambda: SetLocation(events = MOLTEN_VALLEY_EVENTS, locInt = locvars.Locations.MoltenValley)),
    ])]

"""





Elist: list[classes.Event] = deepcopy(FOREST_EVENTS) # текущие события (сцены)


FORK_EVENTS = [classes.Event("вы пришли к тому что охраняло чудовище к табличке с направлениями",themeColor = classes.Colors.YELLOW , curentActions=[
    classes.Action(f'{classes.Colors.YELLOW}Идти в (Замок){classes.Colors.WHITE}', function = lambda: SetLocation(events = CASTLE_EVENTS, locInt = locvars.Locations.Castle)),
    classes.Action(f'{classes.Colors.RED}Идти в (Расплавленную долину){classes.Colors.WHITE}', function = lambda: SetLocation(events = MOLTEN_VALLEY_EVENTS, locInt = locvars.Locations.MoltenValley)),
    classes.Action(f'{classes.Colors.CYAN}Идти в (Замороженное Озеро){classes.Colors.WHITE}', function = lambda: SetLocation(events = ICE_LAKE_EVENTS, locInt = locvars.Locations.IceLake)),
    classes.Action(f'{classes.Colors.PINK}Идти в (Эфирные Берега){classes.Colors.WHITE}', function = lambda: SetLocation(events = ETHERIAL_SHORES_EVENTS, locInt = locvars.Locations.EtherealShores)),
    ])]




class Game(Frame):
    def __init__(self,tk): 
        super(Game,self).__init__(tk)

        #vars.GUI_text_area = Label(text=" Text Area",font = ('ImesNewRoman',25,'bold'),bg = '#000',fg = '#fff')
        #vars.GUI_text_area.pack(side=LEFT) #padx, pady

        self.TK_Scene: classes.TkScene = classes.TkScene(Label(text="Вы пришли к тому что охраняло чудовище к табличке с направлениями",font = ('ImesNewRoman',25,'bold'),bg = '#000',fg = '#fff'), curentActionsBar=[
            Button(text="Идти в (Замок)",bg='#F5DEB3',font =('ImesNewRoman',18,'bold'),fg = '#FFD700', command= lambda: print("пустое действие")),
            ])
        
        self.Stats_Area = Label(text=f'stats ',font = ('ImesNewRoman',20,'bold'),bg = '#000',fg = '#fff')
        self.Stats_Area.pack(anchor="w", fill= X) #padx, pady

        self.TK_Scene.textArea = Label(text=f'Event Name Text Area',font = ('ImesNewRoman',20,'bold'),bg = '#000',fg = '#fff')
        self.TK_Scene.textArea.pack(anchor="w", fill= X) #padx, pady

        self.UpdateBtn = Button(text= f'Update',bg='#FFFACD',font =('ImesNewRoman',21,'bold'),fg = '#000', command= self.UpdateScneneGUI)
        self.UpdateBtn.pack()
        self.StartScreen()
        
       

    def StartScreen(self):
        #del funks.Elist[:]

        locvars.Scene = classes.Event("ДОБРО ПОЖАЛОВАТЬ В subRPG 1.6 (*Tkinter 0.2)", themeColor = classes.Colors.GREEN , curentActions=[
                classes.Action("Нажмите, чтобы НАЧАТЬ играть", function = lambda: SetNewScene),
                classes.Action("получить стартовый набор предметов", function = lambda: self.GiveStarterKit),
                classes.Action("Об игре", function = lambda: self.AboutGame),
                classes.Action("clear action bar", function = lambda: self.ClearActionBar),
                ])
        
        
        self.UpdateScneneGUI()

       


        #locvars.ZeroScene = funks.Elist[funks.EventID.Forest]
        #locvars.Scene = locvars.ZeroScene


        #Развилка
        #SetLocation(WILD_FOREST_EVENTS, locvars.Locations.WildForest)
        #vars.actStep = 32
    

    def GiveStarterKit(self):
        TakeRandomItem(vars.StarterPack)
        TakeRandomItem(vars.StarterPack)
        TakeRandomItem(vars.StarterPack)
        
     
        
    def AboutGame(self):
        textAbout = "Порт игры subRPG на Tkinter\nкроме переноса всего контента с оригинала, игра получит\nряд нового контента, что в значительной мере расширит игру"

        locvars.Scene = classes.Event(textAbout, themeColor = classes.Colors.GREEN , curentActions=[
                classes.Action("Назад", function = lambda: self.StartScreen),
                ])
        
        self.UpdateScneneGUI()


    def UpdateScneneGUI(self):
        self.TK_Scene.textArea.config(text=locvars.Scene.name) #padx, pady
        PrintStats()
        self.Stats_Area.config(text= vars.statsLine)

        self.ClearActionBar()
        
        for action in locvars.Scene.curentActions:
            #print(action.name)
            
            btn = Button(text= f'{action.name}',bg='#f7ddbe',font =('ImesNewRoman',21,'bold'),fg = '#744c2a', command= action.function())
            self.TK_Scene.curentActionsBar.append(btn)
            btn.pack(anchor="w")


    def UpdateAll(self):
        time.sleep(0.03)
        self.UpdateScneneGUI()

        if vars.ARMOR <= 0:
                        vars.ARMOR = 0


        if vars.HP <= 0:
            vars.clear()
            print(f'{classes.Colors.RED}Игра Окончена \n{classes.Colors.WHITE}')
            print("Ваше здоровье =", vars.HP)


    def ClearActionBar(self):
        for btn in self.TK_Scene.curentActionsBar:
            btn.destroy()
        del self.TK_Scene.curentActionsBar[:]





tk = Tk()
tk ['bg']='#dec3aa'
tk.resizable(False,False)
tk.geometry ('1200x720+200+200')
tk.title('sub_RPG')
window = Game(tk)
window.pack()
tk.mainloop()