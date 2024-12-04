from tkinter import *
from modules import funks
from modules import vars
from modules import locvars
from modules import classes
from copy import deepcopy
import random

class Game(Frame):
    def __init__(self,tk): 
        super(Game,self).__init__(tk)

        #vars.GUI_text_area = Label(text=" Text Area",font = ('ImesNewRoman',25,'bold'),bg = '#000',fg = '#fff')
        #vars.GUI_text_area.pack(side=LEFT) #padx, pady

        self.TK_Scene: classes.TkScene = classes.TkScene(Label(text="Вы пришли к тому что охраняло чудовище к табличке с направлениями",font = ('ImesNewRoman',25,'bold'),bg = '#000',fg = '#fff'), curentActionsBar=[
            Button(text="Идти в (Замок)",bg='#F5DEB3',font =('ImesNewRoman',21,'bold'),fg = '#FFD700', command= lambda: print("пустое действие")),
            ])
        
        self.TK_Scene.textArea = Label(text=f'Event Name Text Area',font = ('ImesNewRoman',25,'bold'),bg = '#000',fg = '#fff')
        self.TK_Scene.textArea.pack(anchor="w", fill= X) #padx, pady

        self.StartScreen()
        
        funks.SetLocation(funks.WILD_FOREST_EVENTS, locvars.Locations.WildForest)
        vars.actStep = 32
    
        
    def StartScreen(self):
        #del funks.Elist[:]

        locvars.Scene = classes.Event("ДОБРО ПОЖАЛОВАТЬ В subRPG 1.6 (*Tkinter 0.2)", themeColor = classes.Colors.GREEN , curentActions=[
                classes.Action("Нажмите, чтобы НАЧАТЬ играть", function = lambda: self.GameLoop),
                classes.Action("получить стартовый набор предметов", function = lambda: self.GiveStarterKit),
                classes.Action("clear action bar", function = lambda: self.ClearActionBar),
                classes.Action("Действие 3", function = lambda: self.GiveStarterKit),
                ])
        
        
        self.UpdateWindow()

       


        #locvars.ZeroScene = funks.Elist[funks.EventID.Forest]
        #locvars.Scene = locvars.ZeroScene

    def GiveStarterKit(self):
        #funks.TakeRandomItem(vars.StarterPack)
        #funks.TakeRandomItem(vars.StarterPack)
        #funks.TakeRandomItem(vars.StarterPack)
        
        vars.actStep = 1
        #self.GameLoop()
        locvars.Scene = classes.Event("Вы получили стартовый набор предметов", themeColor = classes.Colors.GREEN , curentActions=[
                classes.Action("ок", function = lambda: self.StartScreen),
                ])
        
        self.UpdateWindow()
        

    def ClearActionBar(self):
        for btn in self.TK_Scene.curentActionsBar:
            btn.destroy()
        del self.TK_Scene.curentActionsBar[:]

    def UpdateWindow(self):
        self.TK_Scene.textArea.config(text=f'{locvars.Scene.name}') #padx, pady
        
        self.ClearActionBar()
        
        id = 0
        for action in locvars.Scene.curentActions:
            btn = Button(text= f'{action.name}',bg='#FFFACD',font =('ImesNewRoman',21,'bold'),fg = '#000', command= action.function())
            self.TK_Scene.curentActionsBar.append(btn)
            btn.pack(anchor="w")
            id += 1
    

    def GameLoop(self):
        curstep = vars.step
        while vars.HP > 0 and vars.WIN == False and curstep == vars.step:

            funks.CheckLocation()

            if vars.ARMOR <= 0:
                        vars.ARMOR = 0

            
            locvars.curEventId = funks.SetNewScene()
            self.UpdateWindow()

            vars.step += 1



        if vars.HP <= 0:
            vars.clear()
            print(f'{classes.Colors.RED}Игра Окончена \n{classes.Colors.WHITE}')
            print("Ваше здоровье =", vars.HP)




tk = Tk()
tk ['bg']='#D2B48C'
tk.resizable(False,False)
tk.geometry ('1020x720+200+200')
tk.title('sub_RPG')
app = Game(tk)
app.pack()
tk.mainloop()