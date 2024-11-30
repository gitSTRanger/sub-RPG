from modules import vars
from modules import classes
from copy import deepcopy
from enum import IntEnum
import random


def ShowInventory():

    vars.Weapon.equip = True
    i = 0
    print("0: назад")
    for Islot in vars.Inventory:

        i += 1

        ExamineItemIsZeroCount(i-1)

        print("\n")
        if Islot.equip == True:
            print("[Экипировано]")
        if Islot.item.damage == 0:
            print(f' {i}: {Islot.item.name}({Islot.count}x)', "цена:", Islot.item.cost, "$")
        else:
            print(f' {i}: {Islot.item.name}({Islot.count}x) урон: {Islot.item.damage}', "цена:", Islot.item.cost, "$")

    
    a = int(input("\n действие:"))

    if a == 0:
        return

    vars.clear()

    slot = vars.Inventory[a-1]

    print(f'что вы хотите сделать с {slot.item.name}({slot.count})?')

    print("1: Назад")
    
    mayHeal = False
    mayEquip = False

    if slot.item == vars.ItemList[vars.Items.SmallHealPotion] or slot.item == vars.ItemList[vars.Items.MiddleHealPotion] or slot.item == vars.ItemList[vars.Items.LargeHealPotion]:
        print("2: Использовать Лечение")
        mayHeal = True

    if slot.item.damage != 0 and slot.equip == False:
            print("2: Экипировать")
            mayEquip = True


    b = int(input("\n действие:"))

    if b == 2:
        vars.clear()
<<<<<<< Updated upstream
        UseHealPotion(potion= slot.item)
        slot.count -= 1
        ExamineItemIsZeroCount(a-1)
=======
        if mayHeal == True:
            UseHealPotion(potion= slot.item)
            slot.count -= 1
            ExamineItemIsZeroCount(a-1)
        if mayEquip == True:
            vars.Weapon.equip = False
            vars.Weapon = vars.Inventory[a-1]
            input(f'Вы экипировали {slot.item.name}')
        vars.clear()
        ShowInventory()
>>>>>>> Stashed changes
    
    
def EquipItem():
    pass


def UnEquipItem():
    pass



def TakeItem(item = classes.Item, count = int):
    global Scene
    Scene = ZeroScene
    vars.actStep += 1

    if item == vars.ItemID.Empty:
        input("Пусто...")
        return

    print(f'\nПолучено > {item.name} ({count})')
    vars.Inventory.append(classes.Slot(item, count, False))
    input("Далее...")

def TakeRandomItem(itemPool):
    rndId = random.randint(0, len(itemPool) -1)
    item = classes.Item
    item = itemPool[rndId]
    rndCount = random.randint(1, item.stackCount)
    TakeItem(item, rndCount)


def UseHealPotion(potion = classes.Item):
    if potion == vars.ItemList[vars.Items.SmallHealPotion]:
        Heal(15)
    elif potion == vars.ItemList[vars.Items.MiddleHealPotion]:
        Heal(25)
    elif potion == vars.ItemList[vars.Items.LargeHealPotion]:
        Heal(50)
        

def Heal(healPoints):
    vars.HP += healPoints
    print(f'Вы полечились на {healPoints} ед здоровья \nТекущее здоровье:{vars.HP}')
    input("Далее...")



def ExamineItemIsZeroCount(slotNumber):
    if vars.Inventory[slotNumber].count <= 0:
        vars.Inventory.remove(vars.Inventory[slotNumber])


def ShowStore():
    print(f'Деньги:{vars.MONEY}')
    print("1. Продать\n2. Купить")
    a = int(input("Действие:"))
    

    if a == 1:
        vars.clear()
        print(f'Деньги:{vars.MONEY}')
        ShowSellMenu()
        return
    if a == 2:
        vars.clear()
        print(f'Деньги:{vars.MONEY}')
        ShowShoppingMenu()
    input("Далее...")
    
def ShowSellMenu():
    
    vars.Weapon.equip = True
    

    print("0: назад")
    i = 0
    for Islot in vars.Inventory:
        ExamineItemIsZeroCount(i-1)

        i += 1
        if Islot.equip == True:
<<<<<<< Updated upstream
            print("\n[Экипировано]")
=======
            print(f'\n {i}: {Islot.item.name} товар экипирован (нельзя продать)\n')
            continue
        
>>>>>>> Stashed changes
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

    input("Далее...")


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

    print("вы пошли дальше")
    input("Далее...")
<<<<<<< Updated upstream
    global Scene
    Scene = ZeroScene
=======
    locvars.Scene = locvars.ZeroScene
>>>>>>> Stashed changes
    vars.actStep += 1




def Attack():

    print("вы атаковали", f'{vars.curEnemy.name} на {vars.Weapon.item.damage} ед. урона')
    global Scene
    Scene = Elist[Events.OnFight]

    vars.curEnemy.HP -= vars.Weapon.item.damage

    if vars.curEnemy.HP <= 0:
        print("враг мертв, на сей раз вы победили")
        MoveOn()
        return


    hitChance = random.randint(0, 100)

    if hitChance > vars.curEnemy.missChance:
        print(f'\n{vars.curEnemy.name} атакует вас')
        TakeDamage(hit= vars.curEnemy.damage)
        return
    else:
        print(f'\n{vars.curEnemy.name} пытается атаковать, но промахивается')

    input("Далее...")




def ShowEnemyStats():
    
    print(vars.curEnemy.name, f'жизни: {vars.curEnemy.HP}')
    input("Далее...")


def TryRunAway():


    chance = random.randint(0, 100)

    if chance <= vars.curEnemy.missChance:
        vars.actStep += 1
        global Scene
        Scene = ZeroScene
        print("вы удачно сбежали!")
    else:
        Scene = Elist[Events.OnFight]
        print("вам не удалось сбежать\n")
        print(f'\n{vars.curEnemy.name} атакует вас')
        TakeDamage(hit= vars.curEnemy.damage)
        return
    
    input("Далее...")


def GoOtherWay():
    print("вы пошли другой дорогой")
    vars.actStep += 1
    rndPeacefulPlace = random.randint(0,2)
    global Scene
    Scene = Elist[rndPeacefulPlace]
    input("Далее...")


def StartFight():
    global Scene
    Scene = Elist[Events.StartFight]
    rndEnemy = random.randint(1, len(vars.Bestiary) -1)
    vars.curEnemy = deepcopy(vars.Bestiary[rndEnemy])




def TakeDamage(hit):
    vars.HP -= hit
    print("вы получили", hit, "урона")
    input("Далее...")














#Все События (Сцены)
<<<<<<< Updated upstream
Elist = [
    classes.Event("вы набрели на разрушенный пустой колодец, сдесь спокойно и можно передохнуть", curentActions=[
=======

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

    # Лед

    # Ледяной Замок
    
    # Эфир

FOREST_EVENTS = [
    classes.Event("на вашем пути появился чей то силуэт",themeColor = classes.Colors.GREEN , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Идти дальше", function = StartFight),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("вы слышите чье-то рычание впереди, осмотревшись вы видите врага",themeColor = classes.Colors.GREEN , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action(f'Атаковать врага ({vars.Weapon.item.name} {vars.Weapon.item.damage} урона)', function = Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    classes.Action("Сбежать", function = TryRunAway),
    ]),
    classes.Event(f'враг готовится нанести удар',themeColor = classes.Colors.GREEN , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action(f'Атаковать врага ({vars.Weapon.item.name} {vars.Weapon.item.damage} урона)', function = Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    classes.Action("Сбежать", function = TryRunAway),
    ]),
    classes.Event("скитаясь вы пришли к лесу", themeColor = classes.Colors.GREEN , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("вы набрели на разрушенный пустой колодец, сдесь спокойно и можно передохнуть", themeColor = classes.Colors.GREEN, curentActions=[
>>>>>>> Stashed changes
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Осмотреть", function = lambda: input("Колодец настолько стар, что едва можно разлечить его руины поросшие мхом, сомневаюсь что внутри есть вода\nДалее...")),
    classes.Action("Посмотреть в колодец", function = lambda: TakeRandomItem(vars.TIER1_WELL_items)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("скитаясь вы пришли к лесу", curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("на вашем пути появился чей то силуэт", curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Идти дальше", function = StartFight),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("вы слышите чье-то рычание впереди, осмотревшись вы видите врага", curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Атаковать врага", function = Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    classes.Action("Сбежать", function = TryRunAway),
    ]),
    classes.Event(f'враг готовится нанести удар', curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Атаковать врага", function = Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    classes.Action("Сбежать", function = TryRunAway),
    ]),
    classes.Event("скитаясь вы пришли в заброшенную деревню", curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Осмотреть дома", function = lambda: TakeRandomItem(vars.TIER1_VILLAGE_items)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
<<<<<<< Updated upstream
    classes.Event("вы замечаете растяжку", curentActions=[
=======
]

WILD_FOREST_EVENTS = [
    classes.Event("на вашем пути появился чей то силуэт",themeColor = classes.Colors.GREEN , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Идти дальше", function = StartFight),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("вы слышите чье-то рычание впереди, осмотревшись вы видите врага",themeColor = classes.Colors.GREEN , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action(f'Атаковать врага ({vars.Weapon.item.name} {vars.Weapon.item.damage} урона)', function = Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    classes.Action("Сбежать", function = TryRunAway),
    ]),
    classes.Event(f'враг готовится нанести удар',themeColor = classes.Colors.GREEN , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action(f'Атаковать врага ({vars.Weapon.item.name} {vars.Weapon.item.damage} урона)', function = Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    classes.Action("Сбежать", function = TryRunAway),
    ]),
    classes.Event("скитаясь вы пришли к лесу", themeColor = classes.Colors.GREEN , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("вы замечаете растяжку",themeColor = classes.Colors.GREEN , curentActions=[
>>>>>>> Stashed changes
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Идти дальше", function = lambda: TakeDamage(hit=15)),
    classes.Action("обойти", function = GoOtherWay),
    ]),
    classes.Event("вы резко остановились впереди в прелой листве блестает капкан", curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Магазин", function = ShowStore),
    classes.Action("Идти дальше", function = lambda: TakeDamage(hit=25)),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("земля бурлит от дыма, приглядевшись вы замечаете что стоите на упавшем метеорите", curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Взять остывший камень под ногами", function = lambda: TakeItem(vars.ItemList[vars.Items.MeteoritePiece], 1)),
    classes.Action("Потрогать землю", function = lambda: TakeDamage(100)),
    classes.Action("Идти дальше", function = MoveOn),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
<<<<<<< Updated upstream
=======
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
    classes.Action(f'Атаковать врага ({vars.Weapon.item.name} {vars.Weapon.item.damage} урона)', function = Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    ]),
    classes.Event(f'Босс готовится нанести удар',themeColor = classes.Colors.RED , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action(f'Атаковать врага ({vars.Weapon.item.name} {vars.Weapon.item.damage} урона)', function = Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    ]),
] 

CASTLE_EVENTS = [
    classes.Event("в глубине коридора виден чей то силуэт",themeColor = classes.Colors.YELLOW , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Идти дальше", function = StartFight),
    classes.Action("Пойти в другую сторону", function = GoOtherWay),
    ]),
    classes.Event("вы слышите чье-то рычание впереди, осмотревшись вы видите врага",themeColor = classes.Colors.YELLOW , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action(f'Атаковать врага ({vars.Weapon.item.name} {vars.Weapon.item.damage} урона)', function = Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    classes.Action("Сбежать", function = TryRunAway),
    ]),
    classes.Event(f'враг готовится нанести удар',themeColor = classes.Colors.YELLOW , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action(f'Атаковать врага ({vars.Weapon.item.name} {vars.Weapon.item.damage} урона)', function = Attack),
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
    
>>>>>>> Stashed changes
]

CASTLE_BOSS_EVENTS =[
    classes.Event("Наконец вы пришли в тронный зал, но на троне воссидает уже измененый король",themeColor = classes.Colors.RED , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action("Идти дальше", function = lambda: SetEvent(EventID.StartFight)),
    ]),
    classes.Event("Вы видите как из спины короля торчат щупальца, а глаза его черны.Опоздали его уже не спасти",themeColor = classes.Colors.RED , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action(f'Атаковать врага ({vars.Weapon.item.name} {vars.Weapon.item.damage} урона)', function = Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    ]),
    classes.Event(f'Король готовится нанести удар',themeColor = classes.Colors.RED , curentActions=[
    classes.Action("Инвентарь", function = ShowInventory),
    classes.Action(f'Атаковать врага ({vars.Weapon.item.name} {vars.Weapon.item.damage} урона)', function = Attack),
    classes.Action("Статы врага", function = ShowEnemyStats),
    ]),
] 

class Events(IntEnum):
    Well = 0
    Forest = 1
    PossibleFight = 2
    StartFight = 3
    OnFight = 4
    Village = 5
    Trap = 6
    BearTrap = 7
    MeteorPlace = 8


<<<<<<< Updated upstream

    #Logic
ZeroScene = Elist[Events.Forest]
Scene = ZeroScene
=======
FORK_EVENTS = [classes.Event("вы пришли к тому что охраняло чудовище к табличке с направлениями",themeColor = classes.Colors.YELLOW , curentActions=[
    classes.Action(f'{classes.Colors.YELLOW}Идти в (Замок){classes.Colors.WHITE}', function = lambda: SetLocation(events = CASTLE_EVENTS, locInt = locvars.Locations.Castle)),
    classes.Action(f'{classes.Colors.RED}Идти в (Расплавленную долину){classes.Colors.WHITE}', function = lambda: SetLocation(events = WILD_FOREST_EVENTS, locInt = locvars.Locations.MoltenValley)),
    classes.Action(f'{classes.Colors.CYAN}Идти в (Ледяное Озеро){classes.Colors.WHITE}', function = lambda: SetLocation(events = WILD_FOREST_EVENTS, locInt = locvars.Locations.IceLake)),
    classes.Action(f'{classes.Colors.PINK}Идти в (Эфирные Берега){classes.Colors.WHITE}', function = lambda: SetLocation(events = WILD_FOREST_EVENTS, locInt = locvars.Locations.EtherealShores)),
    ])]
>>>>>>> Stashed changes
