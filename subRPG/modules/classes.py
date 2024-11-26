

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
    def __init__(self, name, curentActions):
        self.curentActions = curentActions
        self.name = name


