from tkinter import *

# from random import *
# import matplotlib.pyplot as plt


WIDTH = 48
HEIGHT = 27
SIZE = 30
MODES = 5
movey = [-1, -1, 0, 1, 1, 1, 0, -1]
movex = [0, 1, 1, 1, 0, -1, -1, -1]
MAP = open("map.evo", "r")
plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
plt.show()
root = Tk()
canv = Canvas(root, width=1440, height=810, bg="black")
canv.pack()
genomes = [list(map(int, open("genom.evo", "r").readline().split())) for i in range(64)]
bots = [[20 + i // 8, 10 + i % 8, 20, 0, 0] for i in range(64)]
#[0] - y
#[1] - x
#[2] - HP
#[3] - orientation:
#7 0 1
#6 b 2
#5 4 3
#[4] - genome pointer
#[5] - graphic rectangle
alive = 64
map1 = []
botnum = 1                          #Номер текущего бота 
turn_end = False                        #Флаг на окончание хода               
overload = 0                        #Число ботов
gen_time = 0

for i in range(HEIGHT):
    map1.append(list(MAP.readline()))
for i in range(64):
    map1[10 + i % 8][20 + i // 8] = "b"


# 0 = empty
# * = wall
# p = poison
# f = food
# b = bot
def handover():
    global botnum, overload, turn_end,bots,genomes
    bots[botnum][2] -= 1        #Скушал хп у бота
    if bots[botnum][2] == 0:
        dead(botnum)
    if numbot == alive:
        numbot = 1
        gen_time += 1
    else 
        numbot += 1
    overload = 0
    turn_end = False
        
        
def create_field():  # 20-27x10-17
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if map1[i][j] == '*':
                canv.create_rectangle(j * SIZE,
                                      i * SIZE,
                                      (j + 1) * SIZE,
                                      (i + 1) * SIZE,
                                      fill="brown")
            else:
                canv.create_rectangle(j * SIZE,
                                      i * SIZE,
                                      (j + 1) * SIZE,
                                      (i + 1) * SIZE,
                                      fill="lightblue")
    for i in range(64):
        bots[i].append(canv.create_rectangle(SIZE * (20 + i // 8),
                                             SIZE * (10 + i % 8),
                                             SIZE * ((20 + i // 8) + 1),
                                             SIZE * ((10 + i % 8) + 1),
                                             fill="red"))


# def step1():


def mainfunc():
    global botnum, overload, turn_end,bots,genomes # Объявление глобальных переменных
    if botnum == 1:
        gen_food()                     # Генерация еды
    while genomes[bots[numbot][4]]>39:
        overload += 1
        bots[numbot][4] = (bots[numbot][4] + genomes[bots[numbot][4]]) % 80
        if overload == 10:
            handover()                 #Вызов функции передачи хода
    act = genomes[bots[numbot][4]] // 8
    switcher = {  # Словарь который послужит переключателем команд
        1: grab,  # Тут написаны имена мини-функций
        2: attack,
        3: turn,
        4: move,
        5: look,
    }
    root.after(10,switcher[act]())  # По ключу переходит к функции, аргументы функции задаются в ()
    if turn_end or overload == 10:  # Смена хода
        handover()    
    mainfunc()


create_field()
mainloop()
