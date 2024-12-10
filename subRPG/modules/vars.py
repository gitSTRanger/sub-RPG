from modules import classes
from modules import imgs
from enum import IntEnum
from tkinter import *
import os

clear = lambda: os.system('cls')


#Все Предметы
ItemList = [
# Лечение
classes.Item("none", icon= imgs.I_unknown, cost = 0, stackCount = 1,damage=0), #0
classes.Item("Мал. Зелье Лечения (15 ед.)",icon= imgs.I_smallHeal,   cost = 30, stackCount = 5, damage= 0), # 1
classes.Item("Сред. Зелье Лечения (25 ед.)",icon= imgs.I_mediumHeal,   cost = 50, stackCount = 5, damage=0), # 2
classes.Item("Бол. Зелье Лечения (50 ед.)",icon= imgs.I_largeHeal,   cost = 80, stackCount = 5, damage=0), # 3

classes.Item("Мал. Зелье Регенерации (15 ед. 3 акта)",icon= imgs.I_smallRegen,   cost = 30, stackCount = 5, damage=0), # 4
classes.Item("Сред. Зелье Регенерации (25 ед.) (15 ед. 6 актов)",icon= imgs.I_mediumRegen,   cost = 60, stackCount = 5, damage=0), # 5
classes.Item("Бол. Зелье Регенерации (45 ед.) (15 ед. 12 актов)",icon= imgs.I_largeRegen,   cost = 130, stackCount = 5, damage=0), # 6
# М Е Ч И
classes.Item("Именной Меч",icon= imgs.I_mySword,   cost = 30, stackCount = 1, damage=11), # 7
classes.Item("Меч",icon= imgs.I_sword,    cost = 30, stackCount = 1, damage=10), # 8
classes.Item("Меч Героя",icon= imgs.I_heroSword,   cost = 100, stackCount = 1, damage=20), # 9
#Замок
classes.Item("Стальной меч",icon= imgs.I_steelSword,   cost = 350, stackCount = 1, damage= 30), # 10
classes.Item("Серебрянный меч",icon= imgs.I_silverSword,   cost = 510, stackCount = 1, damage=48), # 11
# Огонь
classes.Item('Меч "Ярость"',icon= imgs.I_furySword, cost = 350, stackCount = 1, damage= 35), # 12
classes.Item("Метеоритовый Меч",icon= imgs.I_meteoriteSword,   cost = 630, stackCount = 1, damage=50), # 13
# Лед
classes.Item('Меч "Метель"',icon= imgs.I_metelSword,   cost = 180, stackCount = 1, damage= 32), # 14
classes.Item('Меч "Осколок Льда"',icon= imgs.I_iceSharpSword,   cost = 445, stackCount = 1, damage= 45), # 15
# Эфир
classes.Item("Эфирный Меч",icon= imgs.I_etherialSword,   cost = 500, stackCount = 1, damage= 65), # 16
classes.Item('Меч "Эфирная Гибель"',icon= imgs.I_etherialDoomSword,    cost = 1500, stackCount = 1, damage= 111), # 17

# Д И С Т А Н Ц И О Н Н О Е   О Р У Ж И Е
classes.Item("Стрела",icon= imgs.I_arrow,   cost = 2, stackCount = 20, damage=0), # 18

classes.Item("Лук",icon= imgs.I_bow,    cost = 50, stackCount = 1,damage=16), # 19
classes.Item("Лук Героя",icon= imgs.I_heroBow,  cost = 200, stackCount = 1,damage=30), # 20
# Замок
classes.Item("Бесконечный Лук (стрелы не нужны)",icon= imgs.I_infiniteBow,  cost = 350, stackCount = 1,damage=35), # 21
classes.Item("Посох Чародея",icon= imgs.I_sorcererStaff,  cost = 510, stackCount = 1,damage=60), # 22
# Огонь
classes.Item('Лук "Вспышка"', icon= imgs.I_flashBow,  cost = 550, stackCount = 1, damage= 50), # 23
classes.Item('Посох "Метеора"',icon= imgs.I_meteoraStaff, cost = 900, stackCount = 1, damage= 75), # 24
# Лед
classes.Item("Посох Ледянного Выстрела",icon= imgs.I_iceShotStaff, cost = 510, stackCount = 1,damage=60), # 25
classes.Item('Лук "Тайга"', icon= imgs.I_taigaBow,  cost = 700, stackCount = 1, damage= 70), # 26
# Эфир
classes.Item("Эфирный Посох", icon= imgs.I_etherialStaff, cost = 666, stackCount = 1, damage= 75), # 27
classes.Item("Эфирный Лук",icon= imgs.I_etherialBow, cost = 2250, stackCount = 1, damage= 199), # 28

# Б Р О Н Я
classes.Item("Кожаная Броня (20 ед. +защита от холода 10 актов)",icon= imgs.I_leatherArmor,  cost = 20, stackCount = 1,damage=0), # 29
classes.Item("Стальной Доспех (50 ед.)",icon= imgs.I_steelArmor, cost = 80, stackCount = 1,damage= 0), # 30
classes.Item("Серебрянные Латы (65 ед.)",icon= imgs.I_silverArmor, cost = 120, stackCount = 1,damage=0), # 31
classes.Item("Метеоритный Доспех (75 ед.)",icon= imgs.I_meteoriteArmor, cost = 250, stackCount = 1,damage=0), # 32
classes.Item("Ледяная Кольчуга (150 ед. обморожение 5 актов)",icon= imgs.I_iceArmor, cost = 300, stackCount = 1,damage=0), # 33
classes.Item("Эфирные Латы (100 ед.)",icon= imgs.I_etherialArmor, cost = 500, stackCount = 1,damage=0), # 34

# Д Р А Г О Ц Е Н Н О С Т И
classes.Item("Брилиант (Драгоценность)",icon= imgs.I_unknown,  cost = 50, stackCount = 3,damage=0), # 35
classes.Item("Кольцо с изумрудом(Драгоценность)",icon= imgs.I_emeraldRing, cost = 50, stackCount = 1,damage=0), # 36
classes.Item("Ожерелье с изумрудом(Драгоценность)", icon= imgs.I_unknown,  cost = 80, stackCount = 1,damage=0), # 37
# Замок
classes.Item("Слиток Золота(Драгоценность)",icon= imgs.I_goldBar, cost = 50, stackCount = 3,damage=0), # 38
# Огонь
classes.Item("Осколок Метеорита (Драгоценность)",icon= imgs.I_meteoritePiece, cost = 50, stackCount = 3,damage=0), # 39

classes.Item("Кольцо с топазом(Драгоценность)", icon= imgs.I_topazRing, cost = 70, stackCount = 1,damage=0), # 40
classes.Item("Ожерелье с топазом(Драгоценность)", icon= imgs.I_unknown,   cost = 100, stackCount = 1,damage=0), # 41

classes.Item("Кольцо с рубином(Драгоценность)", icon= imgs.I_rubyRing,  cost = 90, stackCount = 1,damage=0), # 42
classes.Item("Ожерелье с рубином(Драгоценность)",icon= imgs.I_unknown, cost = 120, stackCount = 1,damage=0), # 43
# Лед
classes.Item("Кристал Льда (Драгоценность)",icon= imgs.I_iceCrystal,  cost = 40, stackCount = 6,damage=0), # 44

classes.Item("Кольцо с сапфиром(Драгоценность)",icon= imgs.I_saphireRing, cost = 110, stackCount = 1,damage=0), # 45
classes.Item("Ожерелье с сапфиром(Драгоценность)",icon= imgs.I_unknown, cost = 100, stackCount = 1,damage=0), # 46

classes.Item("Кольцо с алмазом(Драгоценность)",icon= imgs.I_diamondRing, cost = 130, stackCount = 1,damage=0), # 47
classes.Item("Ожерелье с алмазом(Драгоценность)",icon= imgs.I_unknown, cost = 140, stackCount = 1,damage=0), # 48
# Эфир
classes.Item("Эфирный Сгусток (Драгоценность)",icon= imgs.I_unknown, cost = 100, stackCount = 4,damage=0), # 49

classes.Item("Ожерелье с Эфиром(Драгоценность)",icon= imgs.I_unknown, cost = 300, stackCount = 1,damage=0), # 50

# если использовать на боссе Ледяной Граф можно исцелить его
classes.Item(f'Зелье незамерзайка',icon= imgs.I_unknown,  cost = 160, stackCount = 1,damage=0), # 51

    ]

class ItemID(IntEnum):
    Empty = 0
    SmallHealPotion = 1
    MiddleHealPotion = 2
    LargeHealPotion = 3
    SmallRegenPotion = 4
    MiddleRegenPotion = 5
    LargeRegenPotion = 6

    MySword = 7
    Sword = 8
    HeroSword = 9
    SteelSword = 10
    SilverSword = 11
    FurySword = 12
    MeteoriteSword = 13
    MetelSword = 14
    IceSharpSword = 15
    EtherealSword = 16
    EtherealDoomSword = 17
    Arrow = 18
    Bow = 19
    HeroBow = 20
    InfinityBow = 21
    SorcererStaff = 22
    BowFlash = 23
    MeteoraStaff = 24
    IceShotStaff = 25
    BowTaiga = 26
    EtherealStaff = 27
    EtherealBow = 28

    LeatherArmor = 29
    SteelArmor = 30
    SilverArmor = 31
    MeteoriteArmor = 32
    IceArmor = 33
    EtherealArmor = 34

    Diamond = 35
    EmeraldRing = 36
    EmeraldNecklace = 37
    GoldBar = 38
    MeteoritePiece = 39
    TopazRing = 40
    TopazNecklace = 41
    RubyRing = 42
    RubyNecklace = 43
    IceCrystal = 44
    SapphireRing = 45
    SapphireNecklace = 46
    DiamondRing = 47
    DiamondNecklace = 48
    EtherealClot = 49
    EtherealNecklace = 50

    antiFreezePotion = 51



#Все Враги
#Все Враги
Enemies = [
    classes.Enemy("Скелет", HP = 20, damage = 5, missChance = 15), # 0
    classes.Enemy("Скелет в броне", HP = 30, damage = 5, missChance = 15), # 1
    classes.Enemy("Орк", HP = 40, damage = 10, missChance = 20), # 2
    classes.Enemy("Вурдолак", HP = 35, damage = 5, missChance = 30), # 3
    classes.Enemy("Слепой Гуль", HP = 40, damage = 20, missChance = 50), # 4
    classes.Enemy("Тролль", HP = 100, damage = 20, missChance = 30), # 5
    # Замок
    classes.Enemy("Скелет Рыцарь", HP = 50, damage = 10, missChance = 20), # 6
    classes.Enemy("Рыцарь Герой", HP = 50, damage = 20, missChance = 15), # 7
    classes.Enemy("Бронированный Скелет Рыцарь", HP = 65, damage = 10, missChance = 25), # 8
    classes.Enemy("Одержимый Королевский Страж", HP = 40, damage = 30, missChance = 10), # 9
    classes.Enemy("Каменная Горгулья", HP = 80, damage = 30, missChance = 40), # 10
    # Огонь
    classes.Enemy("Огненная Бестия", HP = 65, damage = 25, missChance = 20), # 11
    classes.Enemy("Пламенная Елементаль", HP = 60, damage = 20, missChance = 15), # 12
    classes.Enemy("Расплавленный Рыцарь", HP = 70, damage = 30, missChance = 30), # 13
    classes.Enemy("Обсидиановый Страж", HP = 70, damage = 30, missChance = 30), # 14
    # Лед
    classes.Enemy("Замороженный скелет", HP = 40, damage = 15, missChance = 20), # 15
    classes.Enemy("Ледяной Елементаль", HP = 60, damage = 40, missChance = 60), # 16
    classes.Enemy("Снеговик", HP = 30, damage = 15, missChance = 15), # 17
    classes.Enemy("Ледовик", HP = 50, damage = 20, missChance = 20), # 18
    # Эфир
    classes.Enemy("Жидкая слизь", HP = 100, damage = 35, missChance = 20), # 19
    classes.Enemy("Эфирная Елементаль", HP = 90, damage = 40, missChance = 60), # 20
    classes.Enemy("Эфирная фея", HP = 85, damage = 30, missChance = 15), # 21
    classes.Enemy("Эфирная Хватайка", HP = 100, damage = 60, missChance = 60), # 22
    classes.Enemy("Радужная Хватайка", HP = 120, damage = 80, missChance = 70), # 23
]

Bosses = [
    classes.Enemy("Гигантский Троль Людоед", HP = 120, damage = 35, missChance = 20), # 0

    classes.Enemy("Король Талунг", HP = 300, damage = 30, missChance = 10), # 1

    classes.Enemy("Дракон Пустошей", HP = 200, damage = 45, missChance = 10), # 2

    classes.Enemy("Ледяной Страж", HP = 180, damage = 35, missChance = 30), # 3
    classes.Enemy("Ледяной Граф", HP = 400, damage = 30, missChance = 30), # 4

    classes.Enemy("Зрек Перерожденный", HP = 1000, damage = 30, missChance = 20), # 5
]

class EnemyID(IntEnum):
    Skeleton = 0
    ArmoredSkeleton = 1
    Ork = 2
    Ghoul = 3
    BlindGhoul = 4
    Troll = 5

    SkeletonKnight = 6
    KinghtHero = 7
    ArmoredSkeletonKnight = 8
    PossessedRoyalGuard = 9
    StoneGargoyle = 10

    FireBeast = 11
    FlameElemental = 12
    MoltenKnight = 13
    ObsidianGuard = 14

    FrostSkeleton = 15
    IceElemental = 16
    Snowman = 17
    Iceman = 18
    
    LiquidSlime = 19
    EtherealElemental = 20
    EtherealFairy = 21
    EtherealGrabber = 22
    RainbowGrabber = 23

class BossID(IntEnum):
    GiantTroll = 0
    KingTalung = 1
    WastelandDragon = 2
    IceGuardian = 3
    IceBaron = 4
    Zrek = 5
    

curEnemy: classes.Enemy = Enemies[EnemyID.Skeleton]

# Tkinter

GUI_text_area = Label

GUI_ActionBar = [
    Button
]

# Игрок
HP = 100
ARMOR = 50
MONEY = 0

statsLine: StringVar

BUFF_regeneration = 0
BUFF_warm = 0 # согревание от брони
deBUFF_frostbite = 0 # обморожение от ледяной брони
isFrost = False # холод в ледяной локации


# Концовки

WIN = False

END_KingKiller = False
END_DragoSlayer = False
END_ColdBlooded = False
END_Noble = False
END_Zrek = False

'''
Endings = [
    ("Убийца Королей - пройти Замок", False),
    ("Драконоборец - пройти Расплавленную долину", False),
    ("Холоднокровный - пройти Ледяное Озеро", False),
    ("Благородный", False)
    ("Срубил под Корень Проблемы", False),
]
'''


Inventory: list[classes.Slot] = [
    classes.Slot(ItemList[ItemID.MySword], count = 1, equip=False),
    classes.Slot(ItemList[ItemID.SmallHealPotion], count = 2, equip=False),
    classes.Slot(ItemList[ItemID.SteelArmor], count = 2, equip=False),
]

StoreAssortment = [ classes.Item,]


Weapon: classes.Slot = Inventory[0]


actStep = 1 #1 шаг = 1 игровое событие
step = 0 #1 шаг = одно действие
curStep = -1



#                        P O O L 's


# Starter Pack

StarterPack = [
    ItemList[ItemID.SmallHealPotion],
    ItemList[ItemID.MiddleHealPotion],
    ItemList[ItemID.SmallRegenPotion],
    ItemList[ItemID.Bow],
    ItemList[ItemID.Arrow],
    ItemList[ItemID.LeatherArmor],
    ItemList[ItemID.SteelArmor],
]

#   S T O R E :
ASSORTMENT_DEFAULT = [

    ItemList[ItemID.Arrow],

    ItemList[ItemID.SmallHealPotion],
    ItemList[ItemID.MiddleHealPotion],

    ItemList[ItemID.Empty], # пробел

    ItemList[ItemID.SmallRegenPotion],

    ItemList[ItemID.Empty], # пробел

    ItemList[ItemID.Sword],
    ItemList[ItemID.HeroSword],
    ItemList[ItemID.FurySword],

    ItemList[ItemID.Empty], # пробел

    ItemList[ItemID.Bow],
    ItemList[ItemID.HeroBow],

    ItemList[ItemID.Empty], # пробел

    ItemList[ItemID.LeatherArmor],
    ItemList[ItemID.SteelArmor],
]

ASSORTMENT_CASTLE = [

    ItemList[ItemID.Arrow],

    ItemList[ItemID.SmallHealPotion],
    ItemList[ItemID.MiddleHealPotion],
    ItemList[ItemID.LargeHealPotion],

    ItemList[ItemID.Empty], # пробел

    ItemList[ItemID.SmallRegenPotion],
    ItemList[ItemID.MiddleRegenPotion],

    ItemList[ItemID.Empty], # пробел

    ItemList[ItemID.SteelSword],
    ItemList[ItemID.SilverSword],
    ItemList[ItemID.MeteoriteSword],

    ItemList[ItemID.Empty], # пробел

    ItemList[ItemID.HeroBow],
    ItemList[ItemID.InfinityBow],
    ItemList[ItemID.SorcererStaff],

    ItemList[ItemID.Empty], # пробел

    ItemList[ItemID.SteelArmor],
    ItemList[ItemID.SilverArmor],
    ItemList[ItemID.MeteoriteArmor],
]


ASSORTMENT_MOLTEN_VALLEY = [

    ItemList[ItemID.Arrow],

    ItemList[ItemID.MiddleHealPotion],
    ItemList[ItemID.LargeHealPotion],
    ItemList[ItemID.LargeHealPotion],

    ItemList[ItemID.Empty], # пробел

    ItemList[ItemID.SmallRegenPotion],
    ItemList[ItemID.MiddleRegenPotion],
    ItemList[ItemID.LargeRegenPotion],

    ItemList[ItemID.Empty], # пробел

    ItemList[ItemID.FurySword],
    ItemList[ItemID.MeteoriteSword],

    ItemList[ItemID.Empty], # пробел

    ItemList[ItemID.InfinityBow],
    ItemList[ItemID.BowFlash],
    ItemList[ItemID.MeteoraStaff],

    ItemList[ItemID.Empty], # пробел

    ItemList[ItemID.SteelArmor],
    ItemList[ItemID.MeteoriteArmor],
]

ASSORTMENT_ICE = [

    ItemList[ItemID.Arrow],

    ItemList[ItemID.MiddleHealPotion],
    ItemList[ItemID.LargeHealPotion],
    ItemList[ItemID.LargeHealPotion],

    ItemList[ItemID.Empty], # пробел

    ItemList[ItemID.SmallRegenPotion],
    ItemList[ItemID.MiddleRegenPotion],
    ItemList[ItemID.LargeRegenPotion],

    ItemList[ItemID.Empty], # пробел

    ItemList[ItemID.MetelSword],
    ItemList[ItemID.IceSharpSword],

    ItemList[ItemID.Empty], # пробел

    ItemList[ItemID.InfinityBow],
    ItemList[ItemID.IceShotStaff],
    ItemList[ItemID.BowTaiga],

    ItemList[ItemID.Empty], # пробел

    ItemList[ItemID.LeatherArmor],
    ItemList[ItemID.IceArmor],
]

ASSORTMENT_ETHERIAL = [

    ItemList[ItemID.Arrow],

    ItemList[ItemID.MiddleHealPotion],
    ItemList[ItemID.LargeHealPotion],
    ItemList[ItemID.LargeHealPotion],

    ItemList[ItemID.Empty], # пробел

    ItemList[ItemID.SmallRegenPotion],
    ItemList[ItemID.MiddleRegenPotion],
    ItemList[ItemID.LargeRegenPotion],

    ItemList[ItemID.Empty], # пробел

    ItemList[ItemID.EtherealSword],
    ItemList[ItemID.EtherealDoomSword],

    ItemList[ItemID.Empty], # пробел

    ItemList[ItemID.EtherealStaff],
    ItemList[ItemID.EtherealBow],
    ItemList[ItemID.BowTaiga],

    ItemList[ItemID.Empty], # пробел

    ItemList[ItemID.SteelArmor],
    ItemList[ItemID.MeteoriteArmor],
    ItemList[ItemID.EtherealArmor],
]



#   L O O T

TIER1_MONSTER_DROP = [
    ItemList[ItemID.SmallHealPotion],
    ItemList[ItemID.Arrow],

    ItemList[ItemID.EmeraldNecklace],
    ItemList[ItemID.EmeraldRing],

    ItemList[ItemID.LeatherArmor],
    ItemList[ItemID.SteelArmor],

    ItemList[ItemID.Empty],
    ItemList[ItemID.Empty],
    ItemList[ItemID.Empty],
]

TIER1_WELL_items = [
    ItemList[ItemID.Arrow],
    ItemList[ItemID.SmallHealPotion],
    ItemList[ItemID.MiddleHealPotion],
    ItemList[ItemID.EmeraldNecklace],
    ItemList[ItemID.EmeraldRing],

    ItemList[ItemID.Empty],
]

TIER1_VILLAGE_items = [
    ItemList[ItemID.Arrow],
    ItemList[ItemID.SmallHealPotion],
    ItemList[ItemID.MiddleHealPotion],
    ItemList[ItemID.EmeraldNecklace],
    ItemList[ItemID.EmeraldRing],
    ItemList[ItemID.LeatherArmor],
    ItemList[ItemID.SteelArmor],
    ItemList[ItemID.Sword],
    ItemList[ItemID.Bow],

    ItemList[ItemID.Empty],
]


TIER2_ARMOR_STAND = [
ItemList[ItemID.SteelArmor],
ItemList[ItemID.SteelArmor],
ItemList[ItemID.SilverArmor],
ItemList[ItemID.SilverArmor],
ItemList[ItemID.MeteoriteArmor],
]

TIER2_CHEST = [
    ItemList[ItemID.GoldBar],
    ItemList[ItemID.GoldBar],
    ItemList[ItemID.RubyRing],
    ItemList[ItemID.RubyNecklace],
    ItemList[ItemID.Diamond],
]

TIER2_MOLTEN_CORPSE = [
    ItemList[ItemID.TopazRing],
    ItemList[ItemID.TopazNecklace],
    ItemList[ItemID.RubyRing],
    ItemList[ItemID.RubyNecklace],
    ItemList[ItemID.Diamond],
]

TIER2_FROZEN_CORPSE = [
    ItemList[ItemID.SapphireRing],
    ItemList[ItemID.SapphireNecklace],
    ItemList[ItemID.DiamondRing],
    ItemList[ItemID.DiamondNecklace],
    ItemList[ItemID.Diamond],
    ItemList[ItemID.IceCrystal],

    ItemList[ItemID.MiddleHealPotion],
    ItemList[ItemID.LargeHealPotion],
    ItemList[ItemID.MiddleRegenPotion],
    ItemList[ItemID.LeatherArmor],
    ItemList[ItemID.LeatherArmor],

    ItemList[ItemID.Empty],
    ItemList[ItemID.Empty],
    ItemList[ItemID.Empty],
]

TIER3_FROZEN_CHEST = [
    ItemList[ItemID.GoldBar],
    ItemList[ItemID.GoldBar],
    ItemList[ItemID.GoldBar],
    ItemList[ItemID.SapphireRing],
    ItemList[ItemID.SapphireNecklace],
    ItemList[ItemID.DiamondRing],
    ItemList[ItemID.DiamondNecklace],
    ItemList[ItemID.Diamond],
    ItemList[ItemID.IceCrystal],
]

TIER3_FROZEN_ARMORY = [
    ItemList[ItemID.LeatherArmor],
    ItemList[ItemID.LeatherArmor],
    ItemList[ItemID.LeatherArmor],
    ItemList[ItemID.SteelArmor],
    ItemList[ItemID.MeteoriteArmor],

    ItemList[ItemID.IceArmor],
    ItemList[ItemID.IceArmor],

]


TIER4_ETHERIAL_BAG = [
    ItemList[ItemID.EtherealClot],
    ItemList[ItemID.EtherealClot],
    ItemList[ItemID.EtherealClot],
    ItemList[ItemID.EtherealNecklace],
    ItemList[ItemID.EtherealNecklace],

    ItemList[ItemID.DiamondNecklace],
    ItemList[ItemID.Diamond],
]


TIER4_ETHERIAL_COMBAT_BAG = [
    ItemList[ItemID.EtherealClot],
    ItemList[ItemID.EtherealNecklace],

    ItemList[ItemID.SilverSword],
    ItemList[ItemID.MetelSword],

    ItemList[ItemID.SilverArmor],
    ItemList[ItemID.IceArmor],
    ItemList[ItemID.EtherealArmor],
    ItemList[ItemID.EtherealArmor],
]