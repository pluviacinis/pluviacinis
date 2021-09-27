import math
from graph import*
windowSize(800, 1000)
canvasSize(800, 1000)
brushColor("MidnightBlue")
penColor("MidnightBlue")
rectangle(0, 0, 800, 500)
brushColor("DarkGreen")
penColor("DarkGreen")
rectangle(0, 500, 800, 1000)
brushColor("white")
penColor("white")
oval(450, 150, 650, 325)
brushColor("DarkGrey")
penColor("DarkGrey")
oval(577,-20, 1033, 80)
oval(375, 125, 1175, 250)
oval(300, 275, 1350, 400)
oval(-200, 25, 500, 175)
oval(-200, 250, 500, 350)
brushColor("DimGrey")
penColor("DimGrey")
oval(-150, 225, 350, 300)
oval(175, 80, 850, 180)
oval(200, 350, 820, 450)

def ufo(x,y,r):
	brushColor("white")
	penColor("white")
	polygon([(x,y-17.5*r), (x-90*r, y+350*r), (x+90*r, y+350*r)])
	brushColor("gray")
	penColor("gray")
	oval(x-125*r, y-37.5*r, x+125*r, y+37.5*r)
	brushColor("silver")
	penColor("silver")
	oval(x-75*r, y-47.5*r, x+75*r, y+12.5*r)
	brushColor("white")
	penColor("white")
	oval(x-105*r, y-7.5*r, x-80*r, y+2.5*r) 
	oval(x-75*r, y+7.5*r, x-50*r, y+17.5*r) 
	oval(x-35*r, y+17.5*r, x-10*r, y+27.5*r) 

	oval(x+105*r, y-7.5*r, x+80*r, y+2.5*r) 
	oval(x+75*r, y+7.5*r, x+50*r, y+17.5*r) 
	oval(x+35*r, y+17.5*r, x+10*r, y+27.5*r) 
	


ufo(130, 337.5, 1)
ufo(600, 337.5, 0.5)
ufo(350, 450, 0.25)



def et(x,y,r):	
	brushColor("DarkSeaGreen")
	penColor("DarkSeaGreen")
	oval(x+30*r, y, x+80*r, y+100*r)

	oval(x+65*r, y+80*r, x+90*r, y+120*r)
	oval(x+75*r, y+115*r, x+100*r, y+160*r)
	oval(x+90*r, y+150*r, x+150*r, y+175*r) 

	oval(x+20*r, y+70*r, x+45*r, y+110*r)
	oval(x+10*r, y+105*r, x+35*r, y+150*r)
	oval(x+20*r, y+140*r, x-10*r, y+165*r)

	oval (x+15*r, y, x+45*r, y+30*r)
	oval (x, y+25*r, x+25*r, y+40*r)
	oval (x-15*r, y+40*r, x-5*r, y+50*r) 

	oval (x+65*r, y+5*r, x+95*r, y+35*r)
	oval (x+85*r, y+25*r, x+110*r, y+45*r)
	oval (x+110*r, y+35*r, x+135*r, y+50*r)


	brushColor("DarkSeaGreen")
	polygon([(x+55*r, y+5*r), (x+60*r, y+8*r), (x+65*r, y+5*r), (x+70*r,y+1*r), (x+75*r, y-5*r), (x+80*r, y-10*r), (x+85*r, y-13*r), (x+90*r,y-20*r), (x+93*r, y-29*r), (x+95*r, y-40*r), (x+97*r, y-50*r), (x+95*r, y-55*r), (x+90*r, y-60*r), (x+85*r, y-65*r), (x+80*r, y-70*r), (x+70*r, y-73*r), (x+65*r, y-75*r), (x+60*r, y-72*r), (x+55*r, y-70*r), (x+50*r, y-67*r), (x+45*r, y-65*r), (x+40*r, y-67*r), (x+35*r, y-70*r), (x+30*r, y-73*r), (x+25*r, y-74*r), (x+22*r, y-74*r), (x+17*r, y-75*r), (x+15*r, y-76*r), (x+12*r, y-76*r), (x+9*r, y-76*r), (x+8*r, y-73*r), (x+7*r, y-67*r), (x+8*r,y-62*r), (x+10*r, y-55*r), (x+15*r, y-45*r), (x+20*r, y-35*r), (x+25*r, y-20*r), (x+30*r, y-15*r), (x+35*r, y-13*r), (x+40*r, y-7*r), (x+45*r, y-4*r), (x+50*r, y)])
	oval(x+25*r, y-75*r, x+85*r, y-50*r)
	oval(x+5*r, y-80*r, x+35*r, y-55*r)
	oval(x+47*r, y-5*r, x+70*r, y+5*r) 

	oval(x+10*r, y-100*r, x+25*r, y-80*r) 
	oval(x, y-115*r, x+15*r, y-100*r) 
	oval(x-10*r, y-125*r, x+5*r, y-115*r)
	oval(x-15*r, y-140*r, x+5*r, y-125*r)

	oval(x+75*r, y-85*r, x+95*r, y-65*r)
	oval(x+85*r, y-100*r, x+95*r, y-80*r)
	oval(x+90*r, y-120*r, x+105*r, y-105*r) 
	oval(x+107*r, y-132*r, x+125*r, y-122*r)
	oval(x+130*r, y-135*r, x+143*r, y-115*r)

	brushColor("black")
	circle(x+40*r, y-45*r, 15*r)
	circle(x+75*r, y-40*r, 10*r)
	brushColor("white")
	circle(x+44*r, y-41*r, 4*r)
	circle(x+79*r, y-36*r, 4*r)

	brushColor("red")
	penColor("red")
	circle(x+145*r, y+22.5*r, 20*r) 
	brushColor("lime")
	penColor("black")
	penSize(3*abs(r))
	line((x+145*r), (y+5*r), (x+155*r), (y-5*r))
	line(x+155*r, y-5*r, x+162*r, y-8*r)
	penSize(1*abs(r))
	polygon([(x+155*r, y-5*r), (x+150*r, y-10*r), (x+145*r, y-20*r), (x+155*r, y-13*r)])
	
et(500,700,0.9)
et(150,650,0.5)
et(300,600,0.2)
et(250,550, 0.2)

run()
