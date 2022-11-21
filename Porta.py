import math
from random import random
from util_.util import draw_circle_by_angle

class Porta():
  def __init__(self, canvas, comodo, cd, w, side = "L", orientation = "O", clock = "A", pc = None):
    ##ORIENTATION -> O = OUT and I = IN.
    ##SIDE -> L = Left; R = Right; T = Top; B = Bottom.
    ## W-> Door Width; CD -> Corner Distance
    self.comodo = comodo
    self.canvas = canvas
    self.cd = cd
    self.w = w
    self.door_w = 5
    self.clock = clock
    self.id_list = []
    self.pc = pc
    if (side == "L"):
      if (orientation == "O"):
        self.create_left_outdoor()
      else:
        self.create_left_indoor()

    elif (side == "R"):
      if (orientation == "O"):
        self.create_right_outdoor()
        pass
      else:
        self.create_right_indoor()

    elif (side == "T"):
      if (orientation == "O"):
        self.create_top_outdoor()
      else:
        self.create_top_indoor()

    elif (side == "B"):
      if (orientation == "O"):
        self.create_bottom_outdoor()
      else:
        self.create_bottom_indoor()
    if self.pc :
        [self.canvas.tag_bind(id,"<Button-1>",self.explode) for id in self.id_list]
  

  def create_top_indoor(self):
        sp1,sp2 = self.create_top_space()
        if self.clock == 'A':
            points = [(x+sp1[0],(math.sqrt(self.w**2 - x**2))+sp1[1])  for x in range(int(self.w),-1,-1)]
            id = self.canvas.create_line(points,(points[-1][0],points[-1][1]-self.w-1),smooth = 1,tag = self.generate_random())
            self.id_list.append(id)
            id = self.canvas.create_rectangle(sp1,(sp1[0]+self.door_w,sp1[1]+self.w),tag = self.generate_random())
            self.id_list.append(id)
        if self.clock == 'H':
            points = [(-x+sp1[0]+self.w,(math.sqrt(self.w**2 - x**2))+sp1[1])  for x in range(int(self.w),-1,-1)]
            id = self.canvas.create_line(points,sp2,smooth = 1,tag = self.generate_random())
            self.id_list.append(id)
            id = self.canvas.create_rectangle((sp1[0]+self.w-self.door_w,sp1[1]),points[-1],tag = self.generate_random())
            self.id_list.append(id)
    
  def create_top_outdoor(self):
      sp1,sp2 = self.create_top_space()
      if self.clock == 'A':
          points = [(x+sp1[0],(-math.sqrt(self.w**2 - x**2))+sp1[1]-self.comodo.eT)  for x in range(int(self.w),-1,-1)]
          id = self.canvas.create_line(points,sp1,smooth = 1,tag = self.generate_random())
          self.id_list.append(id)
          id = self.canvas.create_rectangle((sp1[0],sp1[1]-self.w-self.comodo.eT),(sp1[0]+self.door_w,sp1[1]-self.comodo.eT),tag = self.generate_random())
          self.id_list.append(id)
      if self.clock == 'H':
          points = [(-x+sp1[0]+self.w,(-math.sqrt(self.w**2 - x**2))+sp1[1]-self.comodo.eT)  for x in range(int(self.w),-1,-1)]
          id = self.canvas.create_line(points,sp2,smooth = 1,tag = self.generate_random())
          self.id_list.append(id)
          id = self.canvas.create_rectangle((sp1[0]+self.w-self.door_w,sp1[1]-self.w-self.comodo.eT),(sp1[0]+self.w,sp1[1]-self.comodo.eT),tag = self.generate_random())
          self.id_list.append(id)

  def create_bottom_indoor(self):
      sp1,sp2 = self.create_bottom_space()
      if self.clock == 'A':
          points = [(x+sp1[0],(-math.sqrt(self.w**2 - x**2))+sp1[1])  for x in range(int(self.w),-1,-1)]
          id = self.canvas.create_line(points,sp1,smooth = 1,tag = self.generate_random())
          self.id_list.append(id)
          id = self.canvas.create_rectangle((sp1[0],sp1[1]-self.w),(sp1[0]+self.door_w,sp1[1]),tag = self.generate_random())
          self.id_list.append(id)
      if self.clock == 'H':
          points = [(-x+sp1[0]+self.w,(-math.sqrt(self.w**2 - x**2))+sp1[1])  for x in range(int(self.w),-1,-1)]
          id = self.canvas.create_line(points,sp2,smooth = 1,tag = self.generate_random())
          self.id_list.append(id)
          id = self.canvas.create_rectangle((sp1[0]+self.w-self.door_w,sp1[1]-self.w),(sp1[0]+self.w,sp1[1]),tag = self.generate_random())
          self.id_list.append(id)

  def create_bottom_outdoor(self):
      sp1,sp2 = self.create_bottom_space()
      if self.clock == 'A':
          points = [(x+sp1[0],(math.sqrt(self.w**2 - x**2))+sp1[1]+self.comodo.eB)  for x in range(int(self.w),-1,-1)]
          id = self.canvas.create_line(points,(points[-1][0],points[-1][1]-self.w-1),smooth = 1,tag = self.generate_random())
          self.id_list.append(id)
          id = self.canvas.create_rectangle((sp1[0],sp1[1]+self.comodo.eB),(sp1[0]+self.door_w,sp1[1]+self.w+self.comodo.eB),tag = self.generate_random())
          self.id_list.append(id)
      if self.clock == 'H':
          points = [(-x+sp1[0]+self.w,(math.sqrt(self.w**2 - x**2))+sp1[1]+self.comodo.eB) for x in range(int(self.w),-1,-1)]
          id = self.canvas.create_line(points,sp2,smooth = 1,tag = self.generate_random())
          self.id_list.append(id)
          id = self.canvas.create_rectangle((sp1[0]+self.w-self.door_w,sp1[1]+self.comodo.eB),points[-1],tag = self.generate_random())
          self.id_list.append(id)

  def create_left_indoor(self):
      sp1,sp2 = self.create_left_space()
      if self.clock == 'A':
          points = [(x+sp1[0],(math.sqrt(self.w**2 - x**2))+sp1[1])  for x in range(int(self.w),-1,-1)]
          id = self.canvas.create_line(sp1,points,sp2,smooth = 0,tag = self.generate_random())
          self.id_list.append(id)
          id = self.canvas.create_rectangle((sp1),(sp1[0]+self.w,sp1[1]+self.door_w),tag = self.generate_random())
          self.id_list.append(id)
      if self.clock == 'H':
          points = [(x+sp1[0],(-math.sqrt(self.w**2 - x**2))+sp1[1]+self.w)  for x in range(int(self.w),-2,-1)]
          id = self.canvas.create_line(sp2,points,smooth = 0,tag = self.generate_random())
          self.id_list.append(id)
          id = self.canvas.create_rectangle((sp2[0]+self.comodo.eL,sp2[1]),(sp2[0]+self.comodo.eL+self.w+1,sp2[1]-self.door_w),tag = self.generate_random())
          self.id_list.append(id)


  def create_left_outdoor(self):
      sp1,sp2 = self.create_left_space()
      if self.clock == 'A':
          points = draw_circle_by_angle((sp2[0], sp1[1]), self.w, 90, 180)
          id = self.canvas.create_line(points,smooth = 0,tag = self.generate_random())
          self.id_list.append(id)
          id = self.canvas.create_rectangle((sp2[0], sp1[1]),(sp2[0]-self.w,sp1[1]+self.door_w),tag = self.generate_random())
          self.id_list.append(id)
      if self.clock == 'H':
          points = draw_circle_by_angle(sp2, self.w, 180, 270)
          id = self.canvas.create_line(points,smooth = 0,tag = self.generate_random())
          self.id_list.append(id)
          id = self.canvas.create_rectangle((sp2[0],sp2[1]),(sp2[0]-self.w,sp2[1]-self.door_w),tag = self.generate_random())
          self.id_list.append(id)
   
#TODO
  def create_right_indoor(self):
      sp1,sp2 = self.create_right_space()
      if self.clock == 'A':
          points = draw_circle_by_angle(sp1, self.w, 90, 180)
          id = self.canvas.create_line(points,smooth = 1,tag = self.generate_random())
          self.id_list.append(id)
          id = self.canvas.create_rectangle((sp1[0],sp1[1]),(sp1[0]-self.w,sp1[1]-self.door_w),tag = self.generate_random())
          self.id_list.append(id)
      if self.clock == 'H':
          points = draw_circle_by_angle((sp1[0],sp2[1]), self.w, 180, 270)
          id = self.canvas.create_line(points,smooth = 1,tag = self.generate_random())
          self.id_list.append(id)
          id = self.canvas.create_rectangle((sp1[0],sp2[1]),(sp1[0]-self.w,sp2[1]-self.door_w),tag = self.generate_random())
          self.id_list.append(id)

  def create_right_outdoor(self):
      sp1,sp2 = self.create_right_space()
      if self.clock == 'A':
          points = [(x+sp2[0],(math.sqrt(self.w**2 - x**2))+sp1[1])  for x in range(int(self.w),-1,-1)]
          id = self.canvas.create_line(sp1,points,sp2,smooth = 0,tag = self.generate_random())
          self.id_list.append(id)
          id = self.canvas.create_rectangle((sp1[0]+self.comodo.eR,sp1[1]),(sp2[0]+self.w,sp1[1]+self.door_w),tag = self.generate_random())
          self.id_list.append(id)
      if self.clock == 'H':
          points = [(x+sp2[0],(-math.sqrt(self.w**2 - x**2))+sp2[1])  for x in range(int(self.w),-2,-1)]
          id = self.canvas.create_line(sp2,points,smooth = 0,tag = self.generate_random())
          self.id_list.append(id)
          id = self.canvas.create_rectangle((sp2),(sp2[0]+self.w,sp2[1]-self.door_w),tag = self.generate_random())
          self.id_list.append(id)


  ###################################### SPACE ##########################################
  def create_bottom_space(self):
        sp_1 = (self.comodo.dl_inp[0]+self.cd,self.comodo.dl_inp[1])
        sp_2 = (sp_1[0]+self.w,sp_1[1]+self.comodo.eB+1)

        id = self.canvas.create_rectangle(sp_1,sp_2,fill='white',width=0,tag = self.generate_random())
        self.id_list.append(id)
        id = self.canvas.create_line(sp_1,(sp_1[0],sp_1[1]+self.comodo.eB+1),tag = self.generate_random())
        self.id_list.append(id)
        id = self.canvas.create_line((sp_2[0],sp_2[1]-1),(sp_2[0],sp_2[1]-self.comodo.eB-1),tag = self.generate_random())
        self.id_list.append(id)

        return sp_1,sp_2
    
  def create_top_space(self):
      sp_1 = (self.comodo.tl_inp[0]+self.cd,self.comodo.tl_inp[1]+1)
      sp_2 = (sp_1[0]+self.w,sp_1[1]-self.comodo.eT-1)
      id = self.canvas.create_rectangle(sp_1,sp_2,fill='white',width=0,tag = self.generate_random())
      self.id_list.append(id)
      id = self.canvas.create_line((sp_1[0],sp_1[1]-1),(sp_1[0],sp_1[1]-self.comodo.eT-2),tag = self.generate_random())
      self.id_list.append(id)
      id = self.canvas.create_line((sp_2[0],sp_2[1]),(sp_2[0],sp_2[1]+self.comodo.eT),tag = self.generate_random())
      self.id_list.append(id)
      return sp_1,sp_2
  
  def create_left_space(self):
      sp_1 = (self.comodo.tl_inp[0]+1,self.comodo.tl_inp[1]+self.cd)
      sp_2 = (self.comodo.tl_inp[0]-self.comodo.eL,sp_1[1]+self.w)
      id = self.canvas.create_rectangle(sp_1,sp_2,fill='white',width=0,tag = self.generate_random())
      self.id_list.append(id)
      id = self.canvas.create_line((sp_1[0]-1,sp_1[1]),(sp_1[0]-self.comodo.eL-1,sp_1[1]),tag = self.generate_random())
      self.id_list.append(id)
      id = self.canvas.create_line((sp_1[0]-1,sp_1[1]+self.w),(sp_1[0]-self.comodo.eL-1,sp_1[1]+self.w),tag = self.generate_random())
      self.id_list.append(id)
      return sp_1,sp_2
  
  def create_right_space(self):
      sp_1 = (self.comodo.tr_inp[0],self.comodo.tr_inp[1]+self.cd)
      sp_2 = (self.comodo.tr_inp[0]+self.comodo.eR+1,sp_1[1]+self.w)
      id = self.canvas.create_rectangle(sp_1,sp_2,fill='white',width=0,tag = self.generate_random())
      self.id_list.append(id)
      id = self.canvas.create_line((sp_1[0]+1,sp_1[1]),(sp_1[0]+self.comodo.eL+1,sp_1[1]),tag = self.generate_random())
      self.id_list.append(id)
      id = self.canvas.create_line((sp_1[0]+1,sp_1[1]+self.w),(sp_1[0]+self.comodo.eL+1,sp_1[1]+self.w),tag = self.generate_random())
      self.id_list.append(id)
      return sp_1,sp_2

  
  def generate_random(self):
      rd = str(random())
      return rd

  def explode(self,event = None):
      if self.pc.state == 'erase':
          [self.pc.draw_canvas.delete(id) for id in self.id_list]
  def die(self):
      [self.pc.draw_canvas.delete(id) for id in self.id_list]