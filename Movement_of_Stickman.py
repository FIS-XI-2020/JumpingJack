#these statements are for including the tkinter library functionalities 
from tkinter import *
import tkinter as tk
import time


class stickman:
        #constructor saying what would be a part of the layout
        def __init__(self):
                self.canvas=None
                self.image=None
                self.currentImage=0
                self.lastTime=time.time()
                self.images_left=None
                self.images_right=None
                self.images_platforms=None
                self.newImage=0
                self.overlaps_get(self, tuple, tuple, tuple)
                self.platforms = { } 

        def overlaps_get(self,x1, y1, x2, y2):
                plank_list = [] # make a list to hold overlap objects
                c_object = self.canvas.find_overlapping(x1, y1, x2, y2)
                for k,v in platforms.items():  # iterate over ovals dict
                        if v in c_object:      # if the value of a key is in the overlap tuple
                            plank_list.append(k)# add the key to the list
                return plank_list

                
        def right(self):
                
                self.canvas.move(self.image, 25, 0)
                #print("in right")

        def right_pos(self,event):
                if((self.canvas.coords(self.image)[0] + 25 ) < 1350):
                        self.canvas.move(self.image,25,0)
                        self.canvas.update()
                        time.sleep(0.2)
                overlaptuple=self.canvas.find_overlapping(self.canvas.bbox(self.image)[0],self.canvas.bbox(self.image)[1],self.canvas.bbox(self.image)[2],self.canvas.bbox(self.image)[3])
                if len(overlaptuple)>1:
                        #self.canvas.move(self.image,25,0)
                        #self.canvas.update()
                        time.sleep(0.2)
                else:
                        self.fall_down()
                #print(tk.find_overlapping(self.image))
               # print(self.canvas.bbox(self.image))
                #print(self.canvas.find_overlapping(self.canvas.bbox(self.image)))
                if((self.canvas.coords(self.image)[0]) <= 1310):#setting the border/boundary
                        if(time.time()-self.lastTime > 0.1):#checking ang collaborating with time
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
                self.canvas.move(self.image,-25,0)
                #print("in left")
        
        def left_pos(self,event):

                
                if(((self.canvas.coords(self.image)[0])-25) >= 30):
                        self.canvas.move(self.image,-25,0)
                        self.canvas.update()
                        time.sleep(0.2)
                overlaptuple=self.canvas.find_overlapping(self.canvas.bbox(self.image)[0],self.canvas.bbox(self.image)[1],self.canvas.bbox(self.image)[2],self.canvas.bbox(self.image)[3])
                if len(overlaptuple)>1:
                        #self.canvas.move(self.image,-25,0)
                        #self.canvas.update()
                        time.sleep(0.1)
                else:
                        self.fall_down()
                        
                if((self.canvas.coords(self.image)[0]) >= 30):
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
                #declaing the tuple
                if(((self.canvas.coords(self.image)[1])-100) >100):
                        self.canvas.move(self.image,0,-100)
                        self.canvas.update()
                        time.sleep(0.1)
                overlaptuple=self.canvas.find_overlapping(self.canvas.bbox(self.image)[0],(self.canvas.bbox(self.image)[1]+100),self.canvas.bbox(self.image)[2],(self.canvas.bbox(self.image)[3]+100))
                print(overlaps_get(self.image, self.canvas.bbox(self.image)[0],self.canvas.bbox(self.image)[1],self.canvas.bbox(self.image)[2],self.canvas.bbox(self.image)[3]))
                if len(overlaptuple)>1:
                       #self.canvas.move(self.image,0,-100)
                        self.canvas.update()
                        time.sleep(0.2)
                else:
                        #self.canvas.move(self.image,0,100)
                        #self.canvas.update()
                        #time.sleep(0.1)
                        self.fall_down()
        
                        
#when the stickman falls down how it should move
        
        def fall_down(self):
                if(self.canvas.bbox(self.image)[1] < 550):
                        self.canvas.move(self.image,0,100)
                self.canvas.update()

#when stickman jumps
        def jump_pos(self, event):
                self.canvas.itemconfig(self.image,image=self.images_right[2])
                self.jump_up()
                self.canvas.itemconfig(self.image,image=self.images_left[2])
                self.canvas.update()
#movement from right and left way the stickman should move
#screen dimensions and colour
        #import image   

                #placement of platforms
         #def display_platforms(self):
        
                 
        def display_platforms_Layout1(self,event):
                p1 = self.canvas.create_image(600,300,image=self.images_platforms[1],anchor=S)#red
                p2 = self.canvas.create_image(900,250,image=self.images_platforms[1],anchor=S)#red
                p3 = self.canvas.create_image(1120,150,image=self.images_platforms[0],anchor=S)#normal
                p4 = self.canvas.create_image(720,200,image=self.images_platforms[0],anchor=S)#normal
                p5 = self.canvas.create_image(480,400,image=self.images_platforms[0],anchor=S)#normal
                p6 = self.canvas.create_image(300,350,image=self.images_platforms[0],anchor=S)#normal
                p7 = self.canvas.create_image(180,450,image=self.images_platforms[0],anchor=S)#normal
                p8 = self.canvas.create_image(60,550,image=self.images_platforms[0],anchor=S)#normal
                p9 = self.canvas.create_image(180,600,image=self.images_platforms[0],anchor=S)#start
                p10 = self.canvas.create_image(660,450,image=self.images_platforms[0],anchor=S)#normal
                p11 = self.canvas.create_image(840,400,image=self.images_platforms[0],anchor=S)#normal
                p12 = self.canvas.create_image(1120,350,image=self.images_platforms[0],anchor=S)#normal
                p13 = self.canvas.create_image(1240,250,image=self.images_platforms[2],anchor=S)#end
                p14 = self.canvas.create_image(360,650,image=self.images_platforms[0],anchor=S)#normal
                p15 = self.canvas.create_image(1000,400,image=self.images_platforms[0],anchor=S)#normal
                self.image = self.canvas.create_image(50,700,image=self.images_right[self.currentImage],anchor=S)
                
                platforms['p1'] = p1
                platforms['p2'] = p2
                platforms['p3'] = p3
                platforms['p4'] = p4
                platforms['p5'] = p5
                platforms['p6'] = p6
                platforms['p7'] = p7
                platforms['p8'] = p8
                platforms['p9'] = p9
                platforms['p10'] = p10
                platforms['p11'] = p11
                platforms['p12'] = p12
                platforms['p13'] = p13
                platforms['p14'] = p14
                platforms['p15'] = p15
                
        def main(self):
                window = tk.Tk()
                window.title(" Jumping Jack ")
                window.geometry("1500x700")
                self.canvas=Canvas(window,height=100, width=100,bg="orange")
                self.canvas.pack(expand=YES, fill=BOTH)

                
                
                self.images_left = [
                PhotoImage(file="res/runningPos1Left.png"),
                PhotoImage(file="res/runningPos2Left.png"),
                PhotoImage(file="res/runningPos3Left.png")
                ]

                self.images_right = [
                PhotoImage(file ="res/runningPos1Right.png"),
                PhotoImage(file="res/runningPos2Right.png"),
                PhotoImage(file="res/runningPos3Right.png")
                ]

                self.images_platforms = [
                PhotoImage(file ="res/stickman platforms.png"),
                PhotoImage(file="res/stickman_obstacle.png"),
                PhotoImage(file="res/stickman_destination.png")]

                

                
                
                #assigning the keys to positions
                window.bind('<Right>', self.right_pos)
                window.bind('<Left>',self.left_pos)
                window.bind('<Up>',self.jump_pos)
                window.bind('<n>',self.display_platforms_Layout1)
                                 
                
                window.mainloop()

                   
s=stickman()
s.main()
