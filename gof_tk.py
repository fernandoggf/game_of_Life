import numpy as np
import time
from tkinter import *


# ---------- Window Tk --------- #

source = Tk()
source.title("Game of Life")
source.resizable(0,0)
source.geometry("600x600") 


# Get size
frame_par = Frame(source, width="100", height="20")
frame_par.pack()

Label(frame_par, text='Tamaño:').grid(row=0, column=0)

grid_size_entry = Entry(frame_par)
grid_size_entry.grid(row=0, column=1)

def ok_clicked():
	ok_bttn = 1
	grid_size = grid_size_entry.get() 
	return grid_size


button_pass = Button(source, text='Ok', command=ok_clicked)
button_pass.pack()	
#button_pass.wait_variable(ok_clicked())


# ---------- First Board --------- #

length = 50
width = 50
Y_size = (length, width)
Y = np.random.choice([0, 1], size=(length, width), p=[9./10, 1./10])

NY = np.zeros(Y_size)
GY = np.zeros(Y_size)
n=0


canvas = Canvas(source, width=length*10, height=width*10, bg='white')
canvas.pack()


while(n<101):
	for i in range(length):				# by ROWS
		for j in range(width):			# by COLUMNS
			cell_state = Y[i,j]
			# Corners
			if(i==0)&(j==0): #c_1
				sum_state = Y[i,j+1] + Y[i+1,j] + Y[i+1,j+1]
				
			elif(i==0)&(j==width-1): #c_2
				sum_state = Y[i,j-1] + Y[i+1,j-1] + Y[i+1,j]
				
			elif(i==length-1)&(j==0): #c_3
				sum_state = Y[i-1,j] + Y[i-1,j+1] + Y[i,j+1]
				
			elif(i==length-1)&(j==width-1): #c_4
				sum_state = Y[i-1,j-1] + Y[i-1,j] + Y[i,j-1]
				
			#upper
			elif(i==0)&(j>0)&(j<(width-1)):
				sum_state = Y[i,j-1] + Y[i,j+1] + Y[i+1,j-1] + Y[i+1,j] + Y[i+1,j+1]
			#lower
			elif(i==length-1)&(j>0)&(j<(width-1)):
				sum_state = Y[i-1,j-1] + Y[i-1,j] + Y[i-1,j+1] + Y[i,j-1] + Y[i,j+1]
			#lad_left
			elif(i>0)&(i<(length-1))&(j==0): 
				sum_state = Y[i-1,j] + Y[i-1,j+1] + Y[i,j+1] + Y[i+1,j] + Y[i+1,j+1]
			#lad_right
			elif(i>0)&(i<(length-1))&(j==width-1):
				sum_state = Y[i-1,j-1] + Y[i-1,j] + Y[i,j-1] + Y[i+1,j-1] + Y[i+1,j]
			#any dot · 
			else:
				sum_state = Y[i-1,j-1] + Y[i-1,j] + Y[i-1,j+1] + Y[i,j-1] + Y[i,j+1] + Y[i+1,j-1] + Y[i+1,j] + Y[i+1,j+1]

			#Rules
			if(sum_state<2)&(cell_state != 0):
				cell_state = 0
				NY[i,j] = cell_state 
			elif(sum_state>3)&(cell_state != 0):
				cell_state = 0
				NY[i,j] = cell_state 
			elif(sum_state>=3)&(cell_state == 0):
				cell_state = 1
				NY[i,j] = cell_state 

	Y = NY
	n+=1

	for k in range(length):
		for l in range(width):
				k_g = k*10
				l_g = l*10

				if(NY[k,l]==1):
					canvas.create_rectangle(k_g, l_g, k_g+10, l_g+10, width=1, fill="black")

				elif(NY[k,l]==0):
					canvas.create_rectangle(k_g, l_g, k_g+10, l_g+10, width=1, fill="white")
				#time.sleep(0.01)
	source.update()








