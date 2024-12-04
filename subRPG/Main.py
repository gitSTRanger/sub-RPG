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
        
        self.TK_Scene.label = Label(text=f'Event Name Text Area',font = ('ImesNewRoman',25,'bold'),bg = '#000',fg = '#fff')
        self.TK_Scene.label.pack(anchor="w", fill= X) #padx, pady

        self.StartScreen()
        
        funks.SetLocation(funks.WILD_FOREST_EVENTS, locvars.Locations.WildForest)
        vars.actStep = 32
    
        
    def StartScreen(self):
        #del funks.Elist[:]

        locvars.Scene = classes.Event("ДОБРО ПОЖАЛОВАТЬ В subRPG (1.6 *Tkinter)", themeColor = classes.Colors.GREEN , curentActions=[
                classes.Action("Нажмите, чтобы НАЧАТЬ играть", function = lambda: self.GameLoop),
                classes.Action("получить стартовый набор предметов", function = lambda: self.GiveStarterKit),
                classes.Action("Действие 1", function = lambda: self.GiveStarterKit),
                classes.Action("Действие 2", function = lambda: self.GiveStarterKit),
                classes.Action("Действие 3", function = lambda: self.GiveStarterKit),
                ])
        
        
        self.UpdateWindow()

       


        #locvars.ZeroScene = funks.Elist[funks.EventID.Forest]
        #locvars.Scene = locvars.ZeroScene

    def GiveStarterKit(self):
        funks.TakeRandomItem(vars.StarterPack)
        funks.TakeRandomItem(vars.StarterPack)
        funks.TakeRandomItem(vars.StarterPack)
        vars.actStep = 1
        #self.GameLoop()
        locvars.Scene.name = "Вы получили стартовый набор"
        self.UpdateWindow()
        


    

    def UpdateWindow(self):
        #self.TK_Scene.label = Label(text=f'{locvars.Scene.name}',font = ('ImesNewRoman',25,'bold'),bg = '#000',fg = '#fff')
        self.TK_Scene.label.config(text=f'{locvars.Scene.name}') #padx, pady
        
        del self.TK_Scene.curentActionsBar[:]
        id = 0
        for action in locvars.Scene.curentActions:
            self.TK_Scene.curentActionsBar.append(Button(text= f'{action.name}',bg='#FFFACD',font =('ImesNewRoman',21,'bold'),fg = '#000', command= lambda: action.function))
            self.TK_Scene.curentActionsBar[id].pack(anchor="w")
            id += 1
    

    def GameLoop(self):

        while vars.HP > 0 and vars.WIN == False:

            funks.CheckLocation()

            if vars.ARMOR <= 0:
                        vars.ARMOR = 0

            if vars.curAct != vars.actStep and locvars.Scene == locvars.ZeroScene:

                if funks.Elist != funks.FOREST_BOSS_EVENTS:

                    randomEvent = random.randint(0, len(funks.Elist)-1)

                    locvars.Scene = funks.Elist[randomEvent]
                    curAct = vars.actStep

                
                    if randomEvent == funks.EventID.StartFight or randomEvent == funks.EventID.OnFight:
                        vars.clear()
                        funks.StartFight()
                    
                    funks.CheckBuffs() 

            
            
            funks.PrintStats()

            print(f'{locvars.Scene.themeColor}{locvars.Scene.name}{classes.Colors.WHITE}', "\n")
            num = 0
            for a in locvars.Scene.curentActions:
                num += 1
                print(f'{num}: {a.name}')

            #funks.Save() 

            try:
                choiceAction = int(input("Действие:"))
            except ValueError:
                print("неверное действие, введите заново\n")
                choiceAction = int(input("Действие:"))

            try:
                callFunc = locvars.Scene.curentActions[choiceAction -1].function
            except IndexError:
                print("такого действия нет, введите заново\n")
                choiceAction = int(input("Действие:"))
                callFunc = locvars.Scene.curentActions[choiceAction -1].function
                
            vars.clear()
            callFunc()
            vars.clear()
            vars.step += 1



        if vars.HP <= 0:
            vars.clear()
            print(f'{classes.Colors.RED}Игра Окончена \n{classes.Colors.WHITE}')
            print("Ваше здоровье =", vars.HP)




tk = Tk()
tk ['bg']='#fff'
tk.resizable(False,False)
tk.geometry ('1020x720+200+200')
tk.title('sub_RPG')
app = Game(tk)
app.pack()
tk.mainloop()