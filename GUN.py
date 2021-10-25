from random import randrange as rnd, choice
import tkinter as tk
import math
import time


root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
l = tk.Label(root, bg='black', fg='white', width=50)
canv.pack(fill=tk.BOTH, expand=1)
points=0
n=int(input('введите количество целей: '))
targets=[]

class ball():
	def __init__(self, x=40, y=450):
		""" Конструктор класса ball
		Args:
		x - начальное положение мяча по горизонтали
		y - начальное положение мяча по вертикали
		"""
		self.x = x
		self.y = y
		self.r = 10
		self.vx = 0
		self.vy = 0
		self.color = choice(['blue', 'green', 'red', 'brown'])
		self.id = canv.create_oval(
				self.x - self.r,
				self.y - self.r,
				self.x + self.r,
				self.y + self.r,
				fill=self.color)
		self.live = 30
	def set_coords(self):
		canv.coords(
				self.id,
				self.x - self.r,
				self.y - self.r,
				self.x + self.r,
				self.y + self.r)
				
	def move(self):
		"""Переместить цель по прошествии единицы времени.
		Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
		self.x и self.y с учетом скоростей self.vx и self.vy и стен по краям окна (размер окна 800х600).
		"""
		if self.y <=0:
			self.vy = -0.4*self.vy
			self.y = 1
			self.y = self.y - self.vy 
			self.x = self.x + self.vx
		if self.y >=580:
			self.vy = -0.4*self.vy
			self.y = 579
			self.y = self.y - self.vy 
			self.x = self.x + self.vx
		if self.x >= 780:
			self.vx =-self.vx*0.4
			self.x = 779
			self.y = self.y - self.vy 
			self.x = self.x + self.vx
		if self.x <= 0:
			self.vx =-self.vx*0.4
			self.x = 1
			self.y = self.y - self.vy 
			self.x = self.x + self.vx
		else:
			self.vy = self.vy - 0.5
			self.y = self.y - self.vy + 1
			self.x = self.x + self.vx
		self.set_coords()
		
	def hittest(self, obj):
		"""Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
		Args:
		obj: Обьект, с которым проверяется столкновение.
		Returns:
		Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
		"""
		if abs(self.x - obj.x) <= abs(self.r + obj.r) and abs(self.y - obj.y) <= abs(self.r + obj.r):
			return True
		else:
			return False


class gun():
	def __init__(self):
		self.f2_power = 10
		self.f2_on = 0
		self.an = 1
		self.id = canv.create_line(20,450,50,420,width=7) 
		
	def fire2_start(self, event):
		self.f2_on = 1

	def fire2_end(self, event):
		"""Выстрел мячом.
		Происходит при отпускании кнопки мыши.
		Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
		"""
		global balls, bullet
		bullet += 1
		new_ball = ball()
		new_ball.r += 5
		self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
		new_ball.vx = self.f2_power * math.cos(self.an)
		new_ball.vy = - self.f2_power * math.sin(self.an)
		balls += [new_ball]
		self.f2_on = 0
		self.f2_power = 10

	def targetting(self, event=0):
		"""Прицеливание. Зависит от положения мыши."""
		if event:
			self.an = math.atan((event.y-450) / (event.x-20))
		if self.f2_on:
			canv.itemconfig(self.id, fill='orange')
		else:
			canv.itemconfig(self.id, fill='black')
		canv.coords(self.id, 20, 450,
					20 + max(self.f2_power, 20) * math.cos(self.an),
					450 + max(self.f2_power, 20) * math.sin(self.an))

	def power_up(self):
		if self.f2_on:
			if self.f2_power < 100:
				self.f2_power += 1
			canv.itemconfig(self.id, fill='orange')
		else:
			canv.itemconfig(self.id, fill='black')


class target():
        def __init__(self):
                global points
                self.live = 1
                x = self.x = rnd(600, 780)
                y = self.y = rnd(300, 550)
                r = self.r = rnd(2, 50)
                vy = self.vy = rnd(-3,3)
                vx = self.vx = 0
                self.id = canv.create_oval(x-r,y-r,x+r,y+r)
                self.id_points = canv.create_text(30,30,text ='Счет: ' + str(points), font = '28')
		
        def move(self):
                """Переместить мишень по прошествии единицы времени.
                Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
                self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
                и стен по краям окна (размер окна 800х600).
                """
                if self.y <=0:
                        self.vy = -1*self.vy
                        self.y = 1
                        self.y = self.y - self.vy 
                        self.x = self.x + self.vx
                if self.y >=580:
                        self.vy = -1*self.vy
                        self.y = 579
                        self.y = self.y - self.vy 
                        self.x = self.x + self.vx
                if self.x >= 780:
                        self.vx =-self.vx
                        self.x = 779
                        self.y = self.y - self.vy 
                        self.x = self.x + self.vx
                if self.x <= 0:
                        self.vx =-self.vx
                        self.x = 1
                        self.y = self.y - self.vy 
                        self.x = self.x + self.vx
                else:
                        self.vy = self.vy
                        self.y = self.y - self.vy
                        self.x = self.x + self.vx
                self.set_coords()
		

        def n_target():
                global targets
                """ Инициализация новых целей. """
                targets[:]=[]
                canv.delete(target)
                for i in range(n):
                        new_target = target()
                        new_target.x = rnd(600,700)
                        new_target.y=rnd(300,550)
                        new_target.r=rnd(2,50)
                        new_target.vy=rnd(-2,2)
                        new_target.color = 'red'
                        targets.append(new_target)
                    

        def hit(self, p=1):
                """Попадание шарика в цель."""
                global points
                canv.coords(self.id, -10, -10, -10, -10)
                points += p
                canv.itemconfig(self.id_points, text='Счет: ' + str(points))
    




screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 0
balls = []



def new_game(event=''):
        global gun, screen1, balls, bullet, l, n, targets
        bullet = 0
        balls = []
        canv.bind('<Button-1>', g1.fire2_start)
        canv.bind('<ButtonRelease-1>', g1.fire2_end)
        canv.bind('<Motion>', g1.targetting)
        z = 0.03
        target.n_target()
        for t in targets:
                t.live = 1
                t.move()
        l['text']=(' ')
        for t in targets:
                while t.live or balls:
                        for b in balls:
                                b.move()
                                if b.hittest(t) and t.live:
                                        t.live = 0
                                        t.hit()
                                        canv.delete(b.id)
                                        balls.remove(b)
                                        canv.bind('<Button-1>', '')
                                        canv.bind('<ButtonRelease-1>', '')
                                        l['text']=('Вы уничтожили цели за ' + str(bullet) + ' выстрелов')
                                        canv.update()
                canv.update()
                canv.delete(gun)
                time.sleep(0.03)
                g1.targetting()
                g1.power_up()
        canv.itemconfig(screen1, text='')
        root.after(750, new_game)

l.pack()
new_game()

tk.mainloop()
