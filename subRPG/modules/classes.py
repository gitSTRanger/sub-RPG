from tkinter import *

class Item:
    def __init__(self, name, icon ,  cost, stackCount):
        self.name = name
        self.icon = icon
        self.cost = cost
        self.stackCount = stackCount

class Weapon(Item):
    def __init__(self, name, icon ,  cost, stackCount , damage):
        self.name = name
        self.icon = icon
        self.cost = cost
        self.stackCount = stackCount
        self.damage = damage

class Potion(Item):
    def __init__(self, name, icon ,  cost, stackCount , effectAmount):
        self.name = name
        self.icon = icon
        self.cost = cost
        self.stackCount = stackCount
        self.effectAmount = effectAmount


class HealPotion(Item):
    def __init__(self, name, icon ,  cost, stackCount , healAmount ,regenerationAmount):
        self.name = name
        self.icon = icon
        self.cost = cost
        self.stackCount = stackCount
        self.healAmount = healAmount
        self.regenerationAmount = regenerationAmount

class Armor(Item):
    def __init__(self, name, icon ,  cost, stackCount , armorAmount):
        self.name = name
        self.icon = icon
        self.cost = cost
        self.stackCount = stackCount
        self.armorAmount = armorAmount



class Slot:
    def __init__(self, item: Item, count, equip):
        self.item = item
        self.count = count
        self.equip = equip


class Enemy:
    def __init__(self, name, image, HP, damage, missChance):
        self.name = name
        self.image = image
        self.HP = HP
        self.damage = damage
        self.missChance = missChance

class Action():
    def __init__(self, name, icon, backColor, textColor, function):
        self.name = name
        self.icon = icon
        self.backColor = backColor
        self.textColor = textColor
        self.function = function


class Event():
    def __init__(self, name, screen ,backColor, textColor, curentActions: list[Action] = Action):
        self.curentActions = curentActions
        self.screen = screen
        self.backColor = backColor
        self.textColor = textColor
        self.name = name

class TkScene():
    def __init__(self, textArea = Label, curentActionsBar: list[Button] = Button):
        self.curentActionsBar = curentActionsBar
        self.textArea = textArea
        
        



class Quest():
    def __init__(self, name , description, reward, condition: bool):
        self.name = name
        self.description = description
        self.reward = reward
        self.condition = condition
        
        
    