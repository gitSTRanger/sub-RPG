from modules import classes
from enum import IntEnum
import os

clear = lambda: os.system('cls')


#Все Предметы
ItemList = [
classes.Item("Зелье Лечения", cost = 15, stackCount = 5, damage=0),
classes.Item("Меч", cost = 40, stackCount = 1, damage=10),
classes.Item("Лук", cost = 50, stackCount = 1,damage=15),
classes.Item("Стрела", cost = 2, stackCount = 20, damage=0),
classes.Item("Кожаная Броня", cost = 20, stackCount = 1,damage=0),
classes.Item("Стальной Доспех", cost = 20, stackCount = 1,damage=0),
classes.Item("Осколок Метеорита", cost = 50, stackCount = 3,damage=0),
    ]

class Items(IntEnum):
    HealPotion = 0
    Sword = 1
    Bow = 2
    Arrow = 3
    LeatherArmor = 4
    SteelArmor = 5
    MeteorithPiece = 6



#Все Враги
Bestiary = [
    classes.Enemy("текущий враг(может быть любым из списка далее)", HP = 1, damage = 0, missChance = 0),
    classes.Enemy("Скелет", HP = 20, damage = 5, missChance = 15),
    classes.Enemy("Скелет в броне", HP = 30, damage = 5, missChance = 15),
    classes.Enemy("Орк", HP = 40, damage = 10, missChance = 20),
    classes.Enemy("Вурдолак", HP = 35, damage = 5, missChance = 30),
    classes.Enemy("Слепой Гуль", HP = 40, damage = 20, missChance = 50),
]




#Игрок
HP = 100
ARMOR = 50
MONEY = 0

Inventory = [
    classes.Slot(ItemList[Items.Sword], count = 1, equip=False),
    classes.Slot(ItemList[Items.HealPotion], count = 2, equip=False),
    #classes.Slot(ItemList[2], count = 1, equip=False),
    #classes.Slot(ItemList[3], count = 20, equip=False),
]

Weapon = Inventory[0]


actStep = 1 #1 шаг = 1 игровое событие
curAct = 0
step = 0 #1 шаг = одно действие




#                        POOLs


TIER1_WELL_items = [
    ItemList[Items.Arrow],
    ItemList[Items.HealPotion],
    classes.Item("none", cost = 0, stackCount = 1,damage=0),
    classes.Item("none", cost = 0, stackCount = 1,damage=0),
    classes.Item("none", cost = 0, stackCount = 1,damage=0),
]

TIER1_VILLAGE_items = [
    ItemList[Items.Arrow],
    ItemList[Items.HealPotion],
    ItemList[Items.LeatherArmor],
    ItemList[Items.SteelArmor],
    ItemList[Items.Sword],
    ItemList[Items.Bow],
    classes.Item("none", cost = 0, stackCount = 1,damage=0),
    classes.Item("none", cost = 0, stackCount = 1,damage=0),
    classes.Item("none", cost = 0, stackCount = 1,damage=0),
    classes.Item("none", cost = 0, stackCount = 1,damage=0),
]
