class Item:
    def __init__(self, name, cost, stackCount, damage):
        self.name = name
        self.cost = cost
        self.stackCount = stackCount
        self.damage = damage


class Slot:
    def __init__(self, item, count, equip):
        self.item = item
        self.count = count
        self.equip = equip


class Enemy:
    def __init__(self, name, HP, damage, missChance):
        self.name = name
        self.HP = HP
        self.damage = damage
        self.missChance = missChance


class Action():
    def __init__(self, name, function):
        self.name = name
        self.function = function


class Event():
    def __init__(self, name, themeColor, curentActions):
        self.curentActions = curentActions
        self.themeColor = themeColor
        self.name = name
        


class Colors:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'