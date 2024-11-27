from modules import classes
from enum import IntEnum
import os

clear = lambda: os.system('cls')


#Все Предметы
ItemList = [
# Лечение
classes.Item("Мал. Зелье Лечения (15 ед.)", cost = 20, stackCount = 5, damage= 0), # 0
classes.Item("Сред. Зелье Лечения (25 ед.)", cost = 50, stackCount = 5, damage=0), # 1
classes.Item("Бол. Зелье Лечения (50 ед.)", cost = 100, stackCount = 5, damage=0), # 2

classes.Item("Мал. Зелье Регенерации (15 ед. 3 акта)", cost = 30, stackCount = 5, damage=0), # 3
classes.Item("Сред. Зелье Регенерации (25 ед. 6 актов)", cost = 60, stackCount = 5, damage=0), # 4
classes.Item("Бол. Зелье Регенерации (45 ед. 12 актов)", cost = 150, stackCount = 5, damage=0), # 5
# М Е Ч И
classes.Item("Именной Меч", cost = 30, stackCount = 1, damage=11), # 6
classes.Item("Меч", cost = 30, stackCount = 1, damage=10), # 7
classes.Item("Меч Героя", cost = 45, stackCount = 1, damage=20), # 8
#Замок
classes.Item("Стальной меч", cost = 150, stackCount = 1, damage= 30), # 9
classes.Item("Серебрянный меч", cost = 410, stackCount = 1, damage=48), # 10
# Огонь
classes.Item('Меч "Ярость"', cost = 350, stackCount = 1, damage= 30), # 11
classes.Item("Метеоритовый Меч", cost = 830, stackCount = 1, damage=50), # 12
# Лед
classes.Item('Меч "Метель"', cost = 180, stackCount = 1, damage= 35), # 13
classes.Item('Меч "Осколок Льда"', cost = 445, stackCount = 1, damage= 45), # 14
# Эфир
classes.Item("Эфирный Меч", cost = 500, stackCount = 1, damage= 65), # 15
classes.Item('Меч "Эфирная Гибель"', cost = 1500, stackCount = 1, damage= 111), # 16

# Д И С Т А Н Ц И О Н Н О Е   О Р У Ж И Е
classes.Item("Стрела", cost = 2, stackCount = 20, damage=0), # 17

classes.Item("Лук", cost = 50, stackCount = 1,damage=16), # 18
classes.Item("Лук Героя", cost = 200, stackCount = 1,damage=30), # 19
# Замок
classes.Item("Бесконечный Лук", cost = 350, stackCount = 1,damage=35), # 20
classes.Item("Посох Чародея", cost = 510, stackCount = 1,damage=60), # 21
# Огонь
classes.Item('Лук "Вспышка"', cost = 510, stackCount = 1, damage= 50), # 22
classes.Item('Посох "Метеора"', cost = 900, stackCount = 1, damage= 75), # 23
# Лед
classes.Item("Посох Ледянного Выстрела", cost = 510, stackCount = 1,damage=60), # 24
classes.Item('Лук "Тайга"', cost = 700, stackCount = 1, damage= 70), # 25
# Эфир
classes.Item("Эфирный Посох", cost = 666, stackCount = 1, damage= 75), # 26
classes.Item("Эфирный Лук", cost = 2250, stackCount = 1, damage= 199), # 27

# Б Р О Н Я
classes.Item("Кожаная Броня (20 ед. +защита от холода 10 актов)", cost = 20, stackCount = 1,damage=0), # 28
classes.Item("Стальной Доспех (50 ед.)", cost = 80, stackCount = 1,damage=0), # 29
classes.Item("Серебрянные Латы (65 ед.)", cost = 120, stackCount = 1,damage=0), # 30
classes.Item("Метеоритный Доспех (75 ед.)", cost = 250, stackCount = 1,damage=0), # 31
classes.Item("Ледяная Кольчуга (85 ед.)", cost = 300, stackCount = 1,damage=0), # 32
classes.Item("Эфирные Латы (100 ед.)", cost = 500, stackCount = 1,damage=0), # 33

# Д Р А Г О Ц Е Н Н О С Т И

classes.Item("Кольцо с изумрудом(Драгоценность)", cost = 50, stackCount = 1,damage=0), # 34
classes.Item("Ожерелье с изумрудом(Драгоценность)", cost = 80, stackCount = 1,damage=0), # 35
# Замок
classes.Item("Слиток Золота(Драгоценность)", cost = 50, stackCount = 3,damage=0), # 36
# Огонь
classes.Item("Осколок Метеорита (Драгоценность)", cost = 50, stackCount = 3,damage=0), # 37

classes.Item("Кольцо с топазом(Драгоценность)", cost = 70, stackCount = 1,damage=0), # 38
classes.Item("Ожерелье с топазом(Драгоценность)", cost = 100, stackCount = 1,damage=0), # 39

classes.Item("Кольцо с рубином(Драгоценность)", cost = 90, stackCount = 1,damage=0), # 40
classes.Item("Ожерелье с рубином(Драгоценность)", cost = 120, stackCount = 1,damage=0), # 41
# Лед
classes.Item("Кристал Льда (Драгоценность)", cost = 40, stackCount = 3,damage=0), # 42

classes.Item("Кольцо с сапфиром(Драгоценность)", cost = 110, stackCount = 1,damage=0), # 43
classes.Item("Ожерелье с сапфиром(Драгоценность)", cost = 100, stackCount = 1,damage=0), # 44

classes.Item("Кольцо с алмазом(Драгоценность)", cost = 130, stackCount = 1,damage=0), # 45
classes.Item("Ожерелье с алмазом(Драгоценность)", cost = 140, stackCount = 1,damage=0), # 46
# Эфир
classes.Item("Эфирный Сгусток (Драгоценность)", cost = 100, stackCount = 3,damage=0), # 47

classes.Item("Ожерелье с Эфиром(Драгоценность)", cost = 160, stackCount = 1,damage=0), # 48

    ]

class Items(IntEnum):
    SmallHealPotion = 0
    MiddleHealPotion = 1
    LargeHealPotion = 2
    SmallRegenPotion = 3
    MiddleRegenPotion = 4
    LargeRegenPotion = 5

    MySword = 6
    Sword = 7
    HeroSword = 8
    SteelSword = 9
    SilverSword = 10
    FurySword = 11
    MeteoriteSword = 12
    MetelSword = 13
    IceSharpSword = 14
    EtherealSword = 15
    EtherealDoomSword = 16
    Arrow = 17
    Bow = 18
    HeroBow = 19
    InfinityBow = 20
    SorcererStaff = 21
    BowFlash = 22
    MeteoraStaff = 23
    IceShotStaff = 24
    BowTaiga = 25
    EtherealStaff = 26
    EtherealBow = 27

    LeatherArmor = 28
    SteelArmor = 29
    SilverArmor = 30
    MeteoriteArmor = 31
    IceArmor = 32
    EtherealArmor = 33

    EmeraldRing = 34
    EmeraldNecklace = 35
    GlodBar = 36
    MeteoritePiece = 37
    TopazRing = 38
    TopazNecklace = 39
    RubyRing = 40
    RubyNecklace = 41
    IceCrystal = 42
    SapphireRing = 43
    SapphireNecklace = 44
    DiamondRing = 45
    DiamondNecklace = 46
    EtherealClot = 47
    EtherealNecklace = 48



#Все Враги
Bestiary = [
    classes.Enemy("текущий враг(может быть любым из списка далее)", HP = 1, damage = 0, missChance = 0),
    classes.Enemy("Скелет", HP = 20, damage = 5, missChance = 15),
    classes.Enemy("Скелет в броне", HP = 30, damage = 5, missChance = 15),
    classes.Enemy("Орк", HP = 40, damage = 10, missChance = 20),
    classes.Enemy("Вурдолак", HP = 35, damage = 5, missChance = 30),
    classes.Enemy("Слепой Гуль", HP = 40, damage = 20, missChance = 50),
]

curEnemy = classes.Enemy


#Игрок
HP = 100
ARMOR = 50
MONEY = 0

BUFF_regeneration = 0
BUFF_warm = 0 # согревание от брони
deBUFF_frostbite = 0 # обморожение от брони
isFrost = False # холод в ледяной локации

Inventory = [
    classes.Slot(ItemList[Items.Sword], count = 1, equip=False),
    classes.Slot(ItemList[Items.SmallHealPotion], count = 2, equip=False),
]

Weapon = Inventory[0]


actStep = 1 #1 шаг = 1 игровое событие
curAct = 1
step = 0 #1 шаг = одно действие




#                        P O O L 's


# Starter Pack

StarterPack = [
    ItemList[Items.SmallHealPotion],
    ItemList[Items.MiddleHealPotion],
    ItemList[Items.SmallRegenPotion],
    ItemList[Items.Bow],
    ItemList[Items.Arrow],
    ItemList[Items.LeatherArmor],
    ItemList[Items.SteelArmor],
]

#   S T O R E :

STORE_DEFAULT = [
    ItemList[Items.SmallHealPotion],
    ItemList[Items.Bow],
    ItemList[Items.Arrow],
    ItemList[Items.Sword],
    ItemList[Items.LeatherArmor],
    ItemList[Items.SteelArmor],
]

#   L O O T

TIER1_WELL_items = [
    ItemList[Items.Arrow],
    ItemList[Items.SmallHealPotion],
    classes.Item("none", cost = 0, stackCount = 1,damage=0),
    classes.Item("none", cost = 0, stackCount = 1,damage=0),
    classes.Item("none", cost = 0, stackCount = 1,damage=0),
]

TIER1_VILLAGE_items = [
    ItemList[Items.Arrow],
    ItemList[Items.SmallHealPotion],
    ItemList[Items.MiddleHealPotion],
    ItemList[Items.LeatherArmor],
    ItemList[Items.SteelArmor],
    ItemList[Items.Sword],
    ItemList[Items.Bow],
    classes.Item("none", cost = 0, stackCount = 1,damage=0),
    classes.Item("none", cost = 0, stackCount = 1,damage=0),
    classes.Item("none", cost = 0, stackCount = 1,damage=0),
    classes.Item("none", cost = 0, stackCount = 1,damage=0),
]
