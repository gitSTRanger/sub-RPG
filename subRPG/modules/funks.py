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

    if slot.item == vars.ItemList[vars.Items.SmallHealPotion] or slot.item == vars.ItemList[vars.Items.MiddleHealPotion] or slot.item == vars.ItemList[vars.Items.LargeHealPotion]:
        print("2: Использовать Лечение")
        mayHeal = True


    b = int(input("\n действие:"))

    if b == 2 and mayHeal == True:
        vars.clear()
        UseHealPotion(potion= slot.item)
        slot.count -= 1
        ExamineItemIsZeroCount(a-1)
    
    
def EquipItem():
    pass


def UnEquipItem():
    pass



def TakeItem(item = classes.Item, count = int):
    global Scene
    Scene = ZeroScene
    vars.actStep += 1

    if item.name == "none":
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
        print("Меню Покупок")
    input("Далее...")
    
def ShowSellMenu():
    print("0: назад")
    i = 0
    for Islot in vars.Inventory:
        i += 1
        ExamineItemIsZeroCount(i-1)
        if Islot.equip == True:
            print("\n[Экипировано]")
        print(f' {i}: {Islot.item.name}({Islot.count}x)', "цена:", Islot.item.cost, "$")

    a = int(input("\n Действие:"))
    vars.clear()

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


def MoveOn():

    print("вы пошли дальше")
    input("Далее...")
    global Scene
    Scene = ZeroScene
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
Elist = [
    classes.Event("вы набрели на разрушенный пустой колодец, сдесь спокойно и можно передохнуть", curentActions=[
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
    classes.Event("вы замечаете растяжку", curentActions=[
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



    #Logic
ZeroScene = Elist[Events.Forest]
Scene = ZeroScene