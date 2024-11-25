from modules import classes
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
    ]

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
    classes.Slot(ItemList[1], count = 1, equip=False),
    classes.Slot(ItemList[0], count = 2, equip=False),
    classes.Slot(ItemList[2], count = 1, equip=False),
    classes.Slot(ItemList[3], count = 20, equip=False),
]




actStep = 1 #1 шаг = 1 игровое событие
curAct = 0
step = 0 #1 шаг = одно действие





Weapon = Inventory[0]
