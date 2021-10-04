from tkinter import *
import math
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')
l = Label(root, bg='black', fg='white', width=50)
canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)
colors = ['red','orange','yellow','green','blue']
e=Entry(text=('Количество шаров: '),width=100)
balls=[]
def new_ball():
	global x,y,r,vx,vy,balls,e
	canv.delete(ALL)
	vx = rnd(-2,2)
	vy = rnd(-2,2)
	x = rnd(100,700)
	y = rnd(100,500)
	r = rnd(30,50)
	clr=choice(colors)
	balls = [canv.create_oval(x-r, y-r, x+r, y+r, fill=choice(colors), width=0) for i in range(int(e.get()))]

def motion():
	global vx,vy,e
	for unit in balls:
		canv.move(unit,vx,vy)
		if ((canv.coords(unit)[2])>=800)or((canv.coords(unit)[0])<=0):
			vx=-vx
		if ((canv.coords(unit)[3])>=600)or((canv.coords(unit)[1])<=0):
			vy=-vy
		root.after(50, motion)

N=0
vx=0
vy=0

def click(event):
	global N
	for unit in balls:
		if math.sqrt((canv.coords(unit)[2]-r-event.x)**2+(canv.coords(unit)[3]-r-event.y)**2)<r:
			N=N+1
		l['text']=('Счет: ',str(N))
	new_ball()
	motion()
e.pack()
l.pack()

canv.bind('<Button-1>', click)
canv.bind('<Button-3>', new_ball)

mainloop()
