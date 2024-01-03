import numpy as np
import time


## Definition of the grid
length = 5
width = 5
size = (length, width)
#Y = np.zeros(size)
Y = np.array([[0,1,0,0,0],
	[1,1,0,1,0],
	[0,1,1,0,0],
	[1,0,1,0,0],
	[1,0,0,1,0]])
NY = np.zeros(size)
GY = np.array([[" "," "," "," "," "],
	[" "," "," "," "," "],
	[" "," "," "," "," "],
	[" "," "," "," "," "],
	[" "," "," "," "," "]])
n = 0

# 0   * up up up *
# 1 lad ·  ·  ·  lad
# 2 lad ·  ·  ·  lad
# 3 lad ·  ·  ·  lad
# 4 lad ·  ·  ·  lad
# 5   * lo lo lo *

# 5 different states:
# * -> corner in 4 conditions [0,0] [0,-1] [-1, 0] [-1, -1]  
# up -> upper border in [0, N]
# lad_left -> left border in [N, 0]
# lad_right -> right border in [N, -1]
# lo -> lower border in [-1, N] 

# Coordinates and states of the cell
# 	A  B  C  	A[i-1,j-1]  B[i-1,j]  C[i-1,j+1]
#   D  0  E  	D[i,j-1]    0[i,j]    E[i,j+1]
#   F  G  H  	F[i+1,j-1]  G[i+1,j]  H[i+1,j+1]

# Corners
# *1 c_1 [0, 0]  states in 0 - E G H
# *2 c_2 [0,-1]  states in 0 - D F G
# *3 c_3 [-1,0]  states in 0 - B C E
# *4 c_4 [-1,-1] states in 0 - A B D
# 
# Upper
# up1 up_1 [0,N] states in 0 - D E F G H
# 
# Lower
# lo1 lo_1 [-1,N] states in 0 - A B C D E
# 
# lad
# lad_left lad_l [N,0] states in 0 - B C E G H 
# lad_right lad_r [N,-1] states in 0 - A B D F G
 
while(n<101):
	for i in range(length):				# by ROWS
		for j in range(width):			# by COLUMNS
			cell_state = Y[i,j]
			#print(cell_state, i, j)
			# Corners
			if(i==0)&(j==0): #c_1
				sum_state = Y[i,j+1] + Y[i+1,j] + Y[i+1,j+1]
				#print("flag1")
			elif(i==0)&(j==width-1): #c_2
				sum_state = Y[i,j-1] + Y[i+1,j-1] + Y[i+1,j]
				#print("flag2")
			elif(i==length-1)&(j==0): #c_3
				sum_state = Y[i-1,j] + Y[i-1,j+1] + Y[i,j+1]
				#print("flag3")
			elif(i==length-1)&(j==width-1): #c_4
				sum_state = Y[i-1,j-1] + Y[i-1,j] + Y[i,j-1]
				#print("flag4")
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
	#print(Y)
	#print(NY)
	Y = NY
	n+=1
	print(Y)
	for k in range(length):
		for l in range(width):
			if(NY[k,l]==1):
				GY[k,l]="X"
			elif(NY[k,l]==0):
				GY[k,l]="_"

	time.sleep(0.2)

