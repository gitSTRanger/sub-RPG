from modules import funks
from modules import vars
import random

print("\nДОБРО ПОЖАЛОВАТЬ В subRPG (1.1)\n")


input("Нажмите ЛУБУЮ КНОПКУ, чтоб НАЧАТЬ играть \n")
vars.clear()


i = input("Нажмите 1 чтобы получить стартовый набор предметов:")
vars.clear()
if i == "1":
    funks.TakeRandomItem(vars.ItemList)
    funks.TakeRandomItem(vars.ItemList)
    funks.TakeRandomItem(vars.ItemList)

vars.clear()



while vars.HP > 0:
    print(f'step:{vars.step}    act:{vars.actStep}')
    print(f'Жизни:{vars.HP}    Броня:{vars.ARMOR}\n')

    if vars.curAct != vars.actStep and funks.Scene == funks.ZeroScene:
        randomEvent = random.randint(0, len(funks.Elist)-1)

        funks.Scene = funks.Elist[randomEvent]
        curAct = vars.actStep

        if randomEvent == funks.Events.StartFight or randomEvent == funks.Events.OnFight:
            vars.clear()
            funks.StartFight()
    
    

    print(funks.Scene.name, "\n")
    num = 0
    for a in funks.Scene.curentActions:
        num += 1
        print(f'{num}: {a.name}')
    
    

    try:
        choiceAction = int(input("Действие:"))
    except ValueError:
        print("неверное действие, введите заново\n")
        choiceAction = int(input("Действие:"))

    vars.clear()
    try:
        callFunc = funks.Scene.curentActions[choiceAction -1].function
    except IndexError:
        print("такого действия нет, введите заново\n")
        choiceAction = int(input("Действие:"))
        callFunc = funks.Scene.curentActions[choiceAction -1].function

    callFunc()
    vars.clear()
    vars.step += 1


vars.clear()
print("Игра Окончена \n")
print("Ваше здоровье =", vars.HP)