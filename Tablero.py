# Tablero de Ajedrez
import turtle
import os

wn=turtle.Screen()
wn.bgcolor('brown')
wn.title('Tablero de Ajedrez')

greg=turtle.Turtle()
greg.speed(0)

def casilleros(size,alternate,color):
	greg.color(color)
	greg.begin_fill()
	for i in range(4):
		greg.fd(size)
		greg.lt(90)
	greg.end_fill()
	greg.fd(size)

def filas(size,alternate,color1,color2):
	for i in range(4):
		if(alternate==True):
			casilleros(size,alternate,color1)
			casilleros(size,alternate,color2)
		else:
			casilleros(size,alternate,color2)
			casilleros(size,alternate,color1)

def tablero(size,alternate,color1,color2):
	greg.pu()
	greg.goto(-(size*4),(size*4))
	for i in range(8):
		filas(size,alternate,color1,color2)
		greg.bk(size*8)
		greg.rt(90)
		greg.fd(size)
		greg.lt(90)
		if(alternate==True):
			alternate=False
		else:
			alternate=True

tablero(45,True,'black','white')
os.system("pause")

