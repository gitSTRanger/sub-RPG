from modules import classes
from modules import imgs
from enum import IntEnum
from copy import deepcopy
from tkinter import *
import os


clear = lambda: os.system('cls')


#Все Предметы
class ItemList:
# Лечение
    empty = classes.Item("none", icon= imgs.I_unknown, cost = 0, stackCount = 1)
    smallHealPotion=classes.HealPotion("Мал. Зелье Лечения (15 ед.)",icon=imgs.I_smallHeal, cost=30, stackCount=5, healAmount=15, regenerationAmount=0)
    mediumHealPotion=classes.HealPotion("Сред. Зелье Лечения (25 ед.)",icon= imgs.I_mediumHeal,   cost = 50, stackCount = 5, healAmount=25, regenerationAmount=0)
    largeHealPotion=classes.HealPotion("Бол. Зелье Лечения (50 ед.)",icon= imgs.I_largeHeal,   cost = 80, stackCount = 5, healAmount=50, regenerationAmount=0)

    smallRegenPotion=classes.HealPotion("Мал. Зелье Регенерации (15 ед.) (15 ед. 3 акта)",icon= imgs.I_smallRegen,   cost = 100, stackCount = 5, healAmount=15, regenerationAmount=3)
    mediumRegenPotion=classes.HealPotion("Сред. Зелье Регенерации (25 ед.) (15 ед. 6 актов)",icon= imgs.I_mediumRegen,   cost = 200, stackCount = 5, healAmount=25, regenerationAmount=6)
    largeRegenPotion=classes.HealPotion("Бол. Зелье Регенерации (45 ед.) (15 ед. 12 актов)",icon= imgs.I_largeRegen,   cost = 350, stackCount = 5, healAmount=45, regenerationAmount=12)
    # М Е Ч И
    mySword=classes.Weapon("Именной Меч",icon= imgs.I_mySword,   cost = 30, stackCount = 1, damage=11)
    sword=classes.Weapon("Меч",icon= imgs.I_sword,    cost = 30, stackCount = 1, damage=10)
    heroSword=classes.Weapon("Меч Героя",icon= imgs.I_heroSword,   cost = 100, stackCount = 1, damage=20)
    #Замок
    steelSword=classes.Weapon("Стальной меч",icon= imgs.I_steelSword,   cost = 400, stackCount = 1, damage= 30)
    silverSword=classes.Weapon("Серебрянный меч",icon= imgs.I_silverSword,   cost = 600, stackCount = 1, damage=48)
    # Огонь
    furySword=classes.Weapon('Меч "Ярость"',icon= imgs.I_furySword, cost = 500, stackCount = 1, damage= 35)
    meteoriteSword=classes.Weapon("Метеоритовый Меч",icon= imgs.I_meteoriteSword,   cost = 750, stackCount = 1, damage=50)
    # Лед
    metelSword=classes.Weapon('Меч "Метель"',icon= imgs.I_metelSword,   cost = 450, stackCount = 1, damage= 32)
    iceSharpSword=classes.Weapon('Меч "Осколок Льда"',icon= imgs.I_iceSharpSword,   cost = 555, stackCount = 1, damage= 45)
    # Эфир
    etherealSword=classes.Weapon("Эфирный Меч",icon= imgs.I_etherialSword,   cost = 1000, stackCount = 1, damage= 75)
    etherealDoomSword=classes.Weapon('Меч "Эфирная Гибель"',icon= imgs.I_etherialDoomSword,    cost = 1500, stackCount = 1, damage= 120)

    # Д И С Т А Н Ц И О Н Н О Е   О Р У Ж И Е
    arrow=classes.Item("Стрела",icon= imgs.I_arrow,   cost = 2, stackCount = 20)

    bow=classes.Weapon("Лук",icon= imgs.I_bow,    cost = 50, stackCount = 1,damage=16)
    heroBow=classes.Weapon("Лук Героя",icon= imgs.I_heroBow,  cost = 200, stackCount = 1,damage=30)
    # Замок
    infinityBow=classes.Weapon("Бесконечный Лук (стрелы не нужны)",icon= imgs.I_infiniteBow,  cost = 600, stackCount = 1,damage=35)
    sorcererStaff=classes.Weapon("Посох Чародея",icon= imgs.I_sorcererStaff,  cost = 800, stackCount = 1,damage=60)
    # Огонь
    flashBow=classes.Weapon('Лук "Вспышка"', icon= imgs.I_flashBow,  cost = 650, stackCount = 1, damage= 50)
    meteoraStaff=classes.Weapon('Посох "Метеора"',icon= imgs.I_meteoraStaff, cost = 1000, stackCount = 1, damage= 75)
    # Лед
    iceShotStaff=classes.Weapon("Посох Ледянного Выстрела",icon= imgs.I_iceShotStaff, cost = 750, stackCount = 1,damage=60)
    taigaBow=classes.Weapon('Лук "Тайга"', icon= imgs.I_taigaBow,  cost = 950, stackCount = 1, damage= 70)
    # Эфир
    etherealBow=classes.Weapon("Эфирный Лук", icon= imgs.I_etherialBow, cost = 1000, stackCount = 1, damage= 75)
    etherealStaff=classes.Weapon("Эфирный Посох",icon= imgs.I_etherialStaff, cost = 2250, stackCount = 1, damage= 199)

    CyclonBow = classes.Weapon('"Циклон"', icon= imgs.I_cyclonBow, cost=9999, stackCount=1, damage=666)

    # Б Р О Н Я
    leatherArmor=classes.Armor("Кожаная Броня (20 ед. +защита от холода 10 актов)",icon= imgs.I_leatherArmor,  cost = 50, stackCount = 1, armorAmount=20)
    steelArmor=classes.Armor("Стальной Доспех (50 ед.)",icon= imgs.I_steelArmor, cost = 100, stackCount = 1, armorAmount=50)
    silverArmor=classes.Armor("Серебрянные Латы (65 ед.)",icon= imgs.I_silverArmor, cost = 130, stackCount = 1, armorAmount=65)
    meteoriteArmor=classes.Armor("Метеоритный Доспех (75 ед.)",icon= imgs.I_meteoriteArmor, cost = 145, stackCount = 1, armorAmount=75)
    iceArmor=classes.Armor("Ледяная Кольчуга (150 ед. обморожение 5 актов)",icon= imgs.I_iceArmor, cost = 250, stackCount = 1, armorAmount=150)
    etherealArmor=classes.Armor("Эфирные Латы (100 ед.)",icon= imgs.I_etherialArmor, cost = 200, stackCount = 1, armorAmount=100)

    # Д Р А Г О Ц Е Н Н О С Т И
    diamond=classes.Item("Брилиант (Драгоценность)",icon= imgs.I_unknown,  cost = 50, stackCount = 3)
    emeraldRing=classes.Item("Кольцо с изумрудом(Драгоценность)",icon= imgs.I_emeraldRing, cost = 25, stackCount = 1)
    emeraldNecklace=classes.Item("Ожерелье с изумрудом(Драгоценность)", icon= imgs.I_unknown,  cost = 50, stackCount = 1)
    # Замок
    goldBar=classes.Item("Слиток Золота(Драгоценность)",icon= imgs.I_goldBar, cost = 50, stackCount = 3)
    # Огонь
    meteoritePiece=classes.Item("Осколок Метеорита (Драгоценность)",icon= imgs.I_meteoritePiece, cost = 30, stackCount = 6)

    topazRing=classes.Item("Кольцо с топазом(Драгоценность)", icon= imgs.I_topazRing, cost = 40, stackCount = 1)
    topazNecklace=classes.Item("Ожерелье с топазом(Драгоценность)", icon= imgs.I_unknown,   cost = 70, stackCount = 1)

    rubyRing=classes.Item("Кольцо с рубином(Драгоценность)", icon= imgs.I_rubyRing,  cost = 60, stackCount = 1)
    rubyNecklace=classes.Item("Ожерелье с рубином(Драгоценность)",icon= imgs.I_unknown, cost = 80, stackCount = 1)
    # Лед
    iceCrystal=classes.Item("Кристал Льда (Драгоценность)",icon= imgs.I_iceCrystal,  cost = 20, stackCount = 6)

    sapphireRing=classes.Item("Кольцо с сапфиром(Драгоценность)",icon= imgs.I_saphireRing, cost = 60, stackCount = 1)
    sapphireNecklace=classes.Item("Ожерелье с сапфиром(Драгоценность)",icon= imgs.I_unknown, cost = 70, stackCount = 1)

    diamondRing=classes.Item("Кольцо с алмазом(Драгоценность)",icon= imgs.I_diamondRing, cost = 90, stackCount = 1)
    diamondNecklace=classes.Item("Ожерелье с алмазом(Драгоценность)",icon= imgs.I_unknown, cost = 110, stackCount = 1)
    # Эфир
    etherealClot=classes.Item("Эфирный Сгусток (Драгоценность)",icon= imgs.I_unknown, cost = 70, stackCount = 4)

    etherealNecklace=classes.Item("Ожерелье с Эфиром(Драгоценность)",icon= imgs.I_unknown, cost = 200, stackCount = 1)

    # если использовать на боссе Ледяной Граф можно исцелить его
    antifreezePotion=classes.Item(f'Зелье "незамерзайка"',icon= imgs.I_unknown,  cost = 160, stackCount = 1)


    # Exclucive Items

    invisPotion=classes.Potion(f'Зелье Невидимости',icon= imgs.I_invisPotion,  cost = 40, stackCount = 5, effectAmount=5)
    invisRing=classes.Potion(f'Кольцо Невидимости',icon= imgs.I_invisRing,  cost = 1, stackCount = 1,effectAmount=3)

    
    




#Все Враги
Enemies = [
    classes.Enemy("Скелет", image= imgs.M_skeleton,HP = 20, damage = 5, missChance = 15), # 0
    classes.Enemy("Скелет в броне", image= imgs.M_armoredSkeleton, HP = 30, damage = 5, missChance = 15), # 1
    classes.Enemy("злоцвет", image= imgs.M_eviflover, HP = 15, damage = 15, missChance = 20), # 2
    classes.Enemy("Пыльник", image= imgs.M_duster, HP = 40, damage = 5, missChance = 20), # 3
    classes.Enemy("Орк", image= imgs.M_ork, HP = 40, damage = 10, missChance = 30), # 4
    classes.Enemy("Вурдолак", image= imgs.M_ghoul, HP = 35, damage = 5, missChance = 30), # 5
    classes.Enemy("Слепой Гуль", image= imgs.M_blindGhoul, HP = 40, damage = 20, missChance = 50), # 6
    classes.Enemy("змеи-древ", image= imgs.M_snakeThree, HP = 60, damage = 10, missChance = 20), # 7
    classes.Enemy("Тролль", image= imgs.M_troll, HP = 100, damage = 20, missChance = 30), # 8
    # Паучий Лес
    classes.Enemy("рой пауков", image= imgs.M_spidersSwarm, HP = 30, damage = 40, missChance = 0), # 9
    classes.Enemy("малый паук", image= imgs.M_youngSpider, HP = 35, damage = 20, missChance = 15), # 10
    classes.Enemy("Гигантский паук", image= imgs.M_adultSpider, HP = 40, damage = 30, missChance = 20), # 11
    
    # Замок
    classes.Enemy("Скелет Рыцарь", image= None, HP = 50, damage = 10, missChance = 20), # 12
    classes.Enemy("Рыцарь Герой", image= None, HP = 50, damage = 20, missChance = 15), # 13
    classes.Enemy("Бронированный Скелет Рыцарь", image= None, HP = 65, damage = 10, missChance = 25), # 14
    classes.Enemy("Одержимый Королевский Страж", image= None, HP = 40, damage = 30, missChance = 10), # 15
    classes.Enemy("Каменная Горгулья", image= None, HP = 80, damage = 30, missChance = 40), # 16
    # Огонь
    classes.Enemy("Огненная Бестия", image= None, HP = 65, damage = 25, missChance = 20), # 17
    classes.Enemy("Пламенная Елементаль", image= None, HP = 60, damage = 20, missChance = 15), # 18
    classes.Enemy("Расплавленный Рыцарь", image= None, HP = 70, damage = 30, missChance = 30), # 19
    classes.Enemy("Обсидиановый Страж", image= None, HP = 70, damage = 30, missChance = 30), # 20
    # Лед
    classes.Enemy("Замороженный скелет", image= None, HP = 40, damage = 15, missChance = 20), # 21
    classes.Enemy("Ледяной Елементаль", image= None, HP = 60, damage = 40, missChance = 60), # 22
    classes.Enemy("Снеговик", image= None, HP = 30, damage = 15, missChance = 15), # 23
    classes.Enemy("Ледовик", image= None, HP = 50, damage = 20, missChance = 20), # 24
    # Эфир
    classes.Enemy("Жидкая слизь", image= None, HP = 100, damage = 35, missChance = 20), # 25
    classes.Enemy("Эфирная Елементаль", image= None, HP = 90, damage = 40, missChance = 60), # 26
    classes.Enemy("Эфирная фея", image= None, HP = 85, damage = 30, missChance = 15), # 27
    classes.Enemy("Эфирная Хватайка", image= None, HP = 100, damage = 60, missChance = 60), # 28
    classes.Enemy("Радужная Хватайка", image= None, HP = 120, damage = 80, missChance = 70), # 29
]

Bosses = [
    classes.Enemy("Гигантский Троль Людоед", image= imgs.Boss_Troll, HP = 120, damage = 35, missChance = 20), # 0

    classes.Enemy("Арахнеус Императрикс", image= imgs.Boss_Spider, HP = 200, damage = 45, missChance = 40), # 1

    classes.Enemy("Король Талунг", image= None, HP = 300, damage = 30, missChance = 10), # 2

    classes.Enemy("Дракон Пустошей", image= None, HP = 200, damage = 45, missChance = 10), # 3

    classes.Enemy("Ледяной Страж", image= None, HP = 180, damage = 35, missChance = 30), # 4
    classes.Enemy("Ледяной Граф", image= None, HP = 400, damage = 30, missChance = 30), # 5

    classes.Enemy("Зрек Перерожденный", image= None, HP = 1000, damage = 30, missChance = 20), # 6
]

class EnemyID(IntEnum):
    Skeleton = 0
    ArmoredSkeleton = 1
    eviflover = 2
    duster = 3
    Ork = 4
    Ghoul = 5
    BlindGhoul = 6
    snakeThree = 7
    Troll = 8
    
    SpidersSwarm = 9
    YoungSpider = 10
    AdultSpider = 11
    

    SkeletonKnight = 12
    KinghtHero = 13
    ArmoredSkeletonKnight = 14
    PossessedRoyalGuard = 15
    StoneGargoyle = 16

    FireBeast = 17
    FlameElemental = 18
    MoltenKnight = 19
    ObsidianGuard = 20

    FrostSkeleton = 21
    IceElemental = 22
    Snowman = 23
    Iceman = 24
    
    LiquidSlime = 25
    EtherealElemental = 26
    EtherealFairy = 27
    EtherealGrabber = 28
    RainbowGrabber = 29

class BossID(IntEnum):
    GiantTroll = 0
    SpiderQueen = 1
    KingTalung = 2
    WastelandDragon = 3
    IceGuardian = 4
    IceBaron = 5
    Zrek = 6
    

curEnemy: classes.Enemy = Enemies[EnemyID.Skeleton]

# Tkinter

GUI_text_area = Label

GUI_ActionBar = [
    Button
]

# Игрок


HP = 0
startHP = 100
ARMOR = 0
startArmor = 35
MONEY = 0

statsLine: StringVar

BUFF_regeneration = 0
BUFF_warm = 0 # согревание от брони
BUFF_invisibility = 0 # невидимость
deBUFF_frostbite = 0 # обморожение от ледяной брони
deBuff_datura = 0 # дурман от леса пауков, позволяет видить неправельную реальность
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

# Starter Pack

StarterPack = [
    classes.Slot(ItemList.mySword, count = 1, equip=False),
    classes.Slot(ItemList.smallHealPotion, count = 2, equip=False),
]


Inventory: list[classes.Slot] = deepcopy(StarterPack)
StoreAssortment = [ classes.Item,]


Weapon: classes.Slot = Inventory[0]


actStep = 1 #1 шаг = 1 игровое событие
step = 0 #1 шаг = одно действие
curStep = -1



#                        P O O L 's


#   S T O R E :
ASSORTMENT_DEFAULT = [

    ItemList.arrow,

    ItemList.smallHealPotion,
    ItemList.mediumHealPotion,

    ItemList.smallRegenPotion,

    ItemList.sword,
    ItemList.heroSword,
    ItemList.furySword,

    ItemList.bow,
    ItemList.heroBow,

    ItemList.leatherArmor,
    ItemList.steelArmor,
]

ASSORTMENT_SPIDER = [

    ItemList.arrow,

    ItemList.smallHealPotion,
    ItemList.mediumHealPotion,
    ItemList.largeHealPotion,

    ItemList.smallRegenPotion,
    ItemList.mediumRegenPotion,
    
    ItemList.invisPotion,

    ItemList.meteoriteSword,

    ItemList.heroBow,
    ItemList.infinityBow,
    ItemList.sorcererStaff,

    ItemList.leatherArmor,
    ItemList.steelArmor,
]


ASSORTMENT_CASTLE = [

    ItemList.arrow,

    ItemList.smallHealPotion,
    ItemList.mediumHealPotion,
    ItemList.largeHealPotion,

    ItemList.smallRegenPotion,
    ItemList.mediumRegenPotion,

    ItemList.steelSword,
    ItemList.silverSword,
    ItemList.meteoriteSword,

    ItemList.heroBow,
    ItemList.infinityBow,
    ItemList.sorcererStaff,

    ItemList.steelArmor,
    ItemList.silverArmor,
    ItemList.meteoriteArmor,
]


ASSORTMENT_MOLTEN_VALLEY = [

    ItemList.arrow,

    ItemList.mediumHealPotion,
    ItemList.largeHealPotion,
    ItemList.largeHealPotion,

    ItemList.smallRegenPotion,
    ItemList.mediumRegenPotion,
    ItemList.largeRegenPotion,

    ItemList.furySword,
    ItemList.meteoriteSword,

    ItemList.infinityBow,
    ItemList.flashBow,
    ItemList.meteoraStaff,

    ItemList.steelArmor,
    ItemList.meteoriteArmor,
]

ASSORTMENT_ICE = [

    ItemList.arrow,

    ItemList.mediumHealPotion,
    ItemList.largeHealPotion,
    ItemList.largeHealPotion,

    ItemList.smallRegenPotion,
    ItemList.mediumRegenPotion,
    ItemList.largeRegenPotion,

    ItemList.metelSword,
    ItemList.iceSharpSword,

    ItemList.infinityBow,
    ItemList.iceShotStaff,
    ItemList.taigaBow,

    ItemList.leatherArmor,
    ItemList.iceArmor,
]

ASSORTMENT_ETHERIAL = [

    ItemList.arrow,

    ItemList.mediumHealPotion,
    ItemList.largeHealPotion,
    ItemList.largeHealPotion,

    ItemList.smallRegenPotion,
    ItemList.mediumRegenPotion,
    ItemList.largeRegenPotion,

    ItemList.etherealSword,
    ItemList.etherealDoomSword,

    ItemList.etherealStaff,
    ItemList.etherealBow,
    ItemList.taigaBow,

    ItemList.steelArmor,
    ItemList.meteoriteArmor,
    ItemList.etherealArmor,
]



#   L O O T

TIER1_MONSTER_DROP = [
    ItemList.smallHealPotion,
    ItemList.arrow,

    ItemList.emeraldNecklace,
    ItemList.emeraldRing,

    ItemList.leatherArmor,
    ItemList.steelArmor,

    ItemList.empty,
    ItemList.empty,
    ItemList.empty,
]

TIER1_WELL_items = [
    ItemList.arrow,
    ItemList.smallHealPotion,
    ItemList.mediumHealPotion,
    ItemList.emeraldNecklace,
    ItemList.emeraldRing,

    ItemList.empty,
]

TIER1_VILLAGE_items = [
    ItemList.arrow,
    ItemList.smallHealPotion,
    ItemList.mediumHealPotion,
    ItemList.emeraldNecklace,
    ItemList.emeraldRing,
    ItemList.leatherArmor,
    ItemList.sword,
    ItemList.heroSword,
    ItemList.bow,

    ItemList.empty,
]

TIER2_SPIDER_CORPSE = [
    ItemList.arrow,
    ItemList.smallHealPotion,
    ItemList.mediumHealPotion,
    ItemList.emeraldNecklace,
    ItemList.topazRing,
    ItemList.leatherArmor,
    ItemList.heroSword,
    ItemList.bow,
    ItemList.invisPotion,

    ItemList.empty,
]

TIER2_ARMOR_STAND = [
ItemList.steelArmor,
ItemList.steelArmor,
ItemList.silverArmor,
ItemList.silverArmor,
ItemList.meteoriteArmor,
]

TIER2_CHEST = [
    ItemList.goldBar,
    ItemList.goldBar,
    ItemList.rubyRing,
    ItemList.rubyNecklace,
    ItemList.diamond,
]



TIER2_MOLTEN_CORPSE = [
    ItemList.topazRing,
    ItemList.topazNecklace,
    ItemList.rubyRing,
    ItemList.rubyNecklace,
    ItemList.diamond,
]

TIER2_FROZEN_CORPSE = [
    ItemList.sapphireRing,
    ItemList.sapphireNecklace,
    ItemList.diamondRing,
    ItemList.diamondNecklace,
    ItemList.diamond,
    ItemList.iceCrystal,

    ItemList.mediumHealPotion,
    ItemList.largeHealPotion,
    ItemList.mediumRegenPotion,
    ItemList.leatherArmor,
    ItemList.leatherArmor,

    ItemList.empty,
    ItemList.empty,
    ItemList.empty,
]

TIER3_FROZEN_CHEST = [
    ItemList.goldBar,
    ItemList.goldBar,
    ItemList.goldBar,
    ItemList.sapphireRing,
    ItemList.sapphireNecklace,
    ItemList.diamondRing,
    ItemList.diamondNecklace,
    ItemList.diamond,
    ItemList.iceCrystal,
]

TIER3_FROZEN_ARMORY = [
    ItemList.leatherArmor,
    ItemList.leatherArmor,
    ItemList.leatherArmor,
    ItemList.steelArmor,
    ItemList.meteoriteArmor,

    ItemList.iceArmor,
    ItemList.iceArmor,

]


TIER4_ETHERIAL_BAG = [
    ItemList.etherealClot,
    ItemList.etherealClot,
    ItemList.etherealClot,
    ItemList.etherealNecklace,
    ItemList.etherealNecklace,

    ItemList.diamondNecklace,
    ItemList.diamond,
]


TIER4_ETHERIAL_COMBAT_BAG = [
    ItemList.etherealClot,
    ItemList.etherealNecklace,

    ItemList.silverSword,
    ItemList.metelSword,

    ItemList.silverArmor,
    ItemList.iceArmor,
    ItemList.etherealArmor,
    ItemList.etherealArmor,
]


# Q U E S T S

def FindQuestItem(item):
    amount = 0

    for slot in Inventory:
        
        if slot.item == item and slot != Weapon:
                Inventory.remove(slot)
                return True
        
    return False

        
                
            


CurentQuestList = [
    classes.Quest(name='[элексир здоровья]' ,description=f'Я собираюсь сварить партию зелей регенерации, отдам 1 штуку если принесешь {ItemList.largeHealPotion.name}', reward=ItemList.largeRegenPotion, condition= lambda: FindQuestItem(ItemList.largeHealPotion)),
    classes.Quest(name='[кольцо всевластия]' ,description=f'я нашел кольцо и оно проклято, отдам его тебе за {ItemList.heroSword.name}', reward=ItemList.invisRing, condition= lambda: FindQuestItem(ItemList.heroSword))
]


