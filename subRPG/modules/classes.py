from tkinter import *

class Item:
    def __init__(self, name, icon ,  cost, stackCount, damage):
        self.name = name
        self.icon = icon
        self.cost = cost
        self.stackCount = stackCount
        self.damage = damage


class Slot:
    def __init__(self, item: Item, count, equip):
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
    def __init__(self, name, icon, backColor, textColor, function):
        self.name = name
        self.icon = icon
        self.backColor = backColor
        self.textColor = textColor
        self.function = function


class Event():
    def __init__(self, name, backColor, textColor, curentActions: list[Action] = Action):
        self.curentActions = curentActions
        self.backColor = backColor
        self.textColor = textColor
        self.name = name

class TkScene():
    def __init__(self, textArea = Label, curentActionsBar: list[Button] = Button):
        self.curentActionsBar = curentActionsBar
        self.textArea = textArea
        
        




    