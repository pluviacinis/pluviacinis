from tkinter import *
import math
from random import randrange as rnd, choice
from random import randint as rndi
import time
root = Tk()
root.geometry('800x600')
l = Label(root, bg='black', fg='white', width=50)
canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)
colors = ['red','orange','yellow','green','blue']
balls=[]
superballs=[]

n=int(input('Введите количество мишеней: '))
m=rndi(1,n//4)
n -= m

class Ball(object):
        # Класс цветных шариков.
        # x, y - координаты, r - радиус
        # Color - цвет
        # vx, vy - проекции скорости на x и на y соответственно
        
        def __init__(self, x, y, r, color, vx, vy):
                self.color = color
                self.x = x
                self.y = y
                self.r = r
                self.vx = vx
                self.vy = vy

class SuperBall(object):
        # Класс особый цветных шариков.
        # x, y - координаты, r - радиус
        # Color1, color2 -внутренний и внешний цвета соответственно
        # vx, vy - проекции скорости на x и на y соответственно
        
        def __init__(self, x, y, r, vx, vy, color1='red', color2='black'):
                self.color1 = color1
                self.color2 = color2
                self.x = x
                self.y = y
                self.r = r
                self.vx = vx
                self.vy = vy

for i in range(n):
        balls.append(Ball(rnd(100, 700), rnd(100, 500), rnd(30, 50), choice(colors), rndi(-3,3), rndi(-3,3)))
for i in range(m):
        superballs.append(SuperBall(rnd(100,700), rnd(100,500), rnd(20,35), rndi(-4,4), rndi(-4,4)))

def new_balls():
        global balls
        canv.delete(Ball)
        balls[:] = []
        for i in range(n):
                balls.append(Ball(rnd(100, 700), rnd(100, 500), rnd(30, 50), choice(colors), rndi(-3,3), rndi(-3,3)))
                canv.create_oval(balls[i].x - balls[i].r, balls[i].y - balls[i].r, balls[i].x + balls[i].r, balls[i].y + balls[i].r, fill=balls[i].color, width=0)
def new_superballs():
        global superballs
        canv.delete(SuperBall)
        superballs[:] = []
        for i in range (m):
                superballs.append(SuperBall(rnd(100,700), rnd(100,500), rnd(20,35), rndi(-4,4), rndi(-4,4)))
                canv.create_oval(superballs[i].x - superballs[i].r, superballs[i].y - superballs[i].r, superballs[i].x + superballs[i].r, superballs[i].y + superballs[i].r, fill=superballs[i].color2, width=0)
                canv.create_oval(superballs[i].x - 0.5*superballs[i].r, superballs[i].y - 0.5*superballs[i].r, superballs[i].x + 0.5*superballs[i].r, superballs[i].y + 0.5*superballs[i].r, fill=superballs[i].color1, width=0)



points=0

def motion():
        for i in range(len(balls)):
                balls[i].y += balls[i].vy
                balls[i].x += balls[i].vx
                if balls[i].x >=(800 - balls[i].r):
                        balls[i].vx = balls[i].vx*(-1)
                if balls[i].x <=(0 + balls[i].r):
                        balls[i].vx = balls[i].vx*(-1)
                if balls[i].y >= 600 - balls[i].r:
                        balls[i].vy *= -1
                if balls[i].y <= 0 + balls[i].r:
                        balls[i].vy *= -1
        for i in range(len(superballs)):
                superballs[i].y += superballs[i].vy
                superballs[i].x += superballs[i].vx
                if superballs[i].x >=(800 - superballs[i].r):
                        superballs[i].vx = superballs[i].vx*(-1)
                if superballs[i].x <=(0 + superballs[i].r):
                        superballs[i].vx = superballs[i].vx*(-1)
                if superballs[i].y >= 600 - superballs[i].r:
                        superballs[i].vy *= -1
                if superballs[i].y <= 0 + superballs[i].r:
                        superballs[i].vy *= -1
        canv.delete(ALL)
        for i in range(len(balls)):
                canv.create_oval(balls[i].x - balls[i].r, balls[i].y - balls[i].r, balls[i].x + balls[i].r, balls[i].y + balls[i].r, fill=balls[i].color, width=0)
        for i in range (len(superballs)):
                canv.create_oval(superballs[i].x - superballs[i].r, superballs[i].y - superballs[i].r, superballs[i].x + superballs[i].r, superballs[i].y + superballs[i].r, fill=superballs[i].color2, width=0)
                canv.create_oval(superballs[i].x - 0.5*superballs[i].r, superballs[i].y - 0.5*superballs[i].r, superballs[i].x + 0.5*superballs[i].r, superballs[i].y + 0.5*superballs[i].r, fill=superballs[i].color1, width=0)


        root.after(3, motion)

def click(event):
        global points
        for i in range(len(balls)):
                if math.sqrt((balls[i].x - event.x)**2+(balls[i].y - event.y)**2) <= balls[i].r:
                        points += 1
                        canv.delete(balls[i])
                        balls.pop(i)
        for i in range(len(superballs)):
                if math.sqrt((superballs[i].x - event.x)**2+(superballs[i].y - event.y)**2) <= superballs[i].r:
                        points += 3
                        canv.delete(superballs[i])
                        superballs.pop(i)
                l['text']=('Счет: ',str(points))
        if len(balls)==0:
                new_balls()
        elif len(superballs)==0:
                new_superballs()
l.pack()
motion()

canv.bind('<Button-1>', click)
canv.bind('<Button-3>', new_balls)

mainloop()
