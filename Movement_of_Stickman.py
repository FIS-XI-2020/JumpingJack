#to create window
from tkinter import *
import tkinter as tk
import time


class stickman:
	#constructor
	def __init__(self):
		self.canvas=None
		self.image=None
		self.currentImage=0
		self.lastTime=time.time()
		self.images_left=None
		self.images_right=None
		self.newImage=0

	#movement of stickman to right
	def right(self):
		self.canvas.move(self.image, 35, 0)
		#print("in right")

	def right_pos(self,event):		
		if(time.time()-self.lastTime > 0.1):
			if(self.currentImage>=2):
				self.newImage=-1
			if(self.currentImage==0):
				self.newImage=1
			self.currentImage= self.currentImage+self.newImage
			self.lastTime=time.time()
		#print(self.currentImage)
		
		self.canvas.itemconfig(self.image,image=self.images_right[self.currentImage])
		#print("In right_pos")
		self.right()
		self.canvas.update()
	
	#movement of stickman to left 
	def left(self):
		self.canvas.move(self.image,-35,0)
		#print("in left")
	
	def left_pos(self,event):		
		if(time.time()-self.lastTime > 0.1):
			if(self.currentImage>=2):
				self.newImage=-1
			if(self.currentImage==0):
				self.newImage=1
			self.currentImage= self.currentImage+self.newImage
			self.lastTime=time.time()
		#print(self.currentImage)
		
		self.canvas.itemconfig(self.image,image=self.images_left[self.currentImage])
		#print("In right_pos")
		self.left()
		self.canvas.update()
	
	#stickman jumping
	def jump_up(self):
		self.canvas.move(self.image,0,-100)
		self.canvas.update()
		time.sleep(0.2)
		self.fall_down()

	def fall_down(self):
		self.canvas.move(self.image,0,100)
		self.canvas.update()

	def jump_pos(self, event):
		self.canvas.itemconfig(self.image,image=self.images_right[2])
		self.jump_up()
		self.canvas.itemconfig(self.image,image=self.images_left[2])
		self.canvas.update()

	def main(self):
		window = tk.Tk()
		window.title(" Jumping Jack ")
		window.geometry("1500x700")
		self.canvas=Canvas(window,height=100, width=100,bg="sky blue")
		self.canvas.pack(expand=YES, fill=BOTH)

		self.images_left = [
		PhotoImage(file="runningPos1Left.png"),
		PhotoImage(file="runningPos2Left.png"),
		PhotoImage(file="runningPos3Left.png")
		]

		self.images_right = [
		PhotoImage(file ="runningPos1Right.png"),
		PhotoImage(file="runningPos2Right.png"),
		PhotoImage(file="runningPos3Right.png")
		]
		self.image = self.canvas.create_image(50,550,image=self.images_right[self.currentImage],anchor=S)
		window.bind('<Right>', self.right_pos)
		window.bind('<Left>',self.left_pos)
		window.bind('<Up>',self.jump_pos)
		window.mainloop()


s=stickman()
s.main()
