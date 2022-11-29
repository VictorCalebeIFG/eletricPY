from util_.util import percent_line,perpendicular_point,angle_sin,get_mid_p,create_circle,get_radius_point
import tkinter as tk
from numpy import linspace
from eletric_elements.Element import Element
from util_.util import draw_text,get_mid_p

def draw_curve(A,B,curve = 100, smoth = 50,orientation = 0):
    points = []
    for ang in linspace(0,-180,smoth).tolist():
            inter_p , head = perpendicular_point(A,B,d = angle_sin(-ang)*curve,p = ang/-180, dir = orientation)
            points.append(head)
    return points

def get_line_fragments(points):
    lines = []
    for i in range(len(points)):
        try:
            lines.append([points[i],points[i+1]])
        except : return lines
    return lines

    return head2,head1,head3
        
class Condutor(Element):
    def __init__(self, pc=None,A = (0,0),B = (0,0),curve = 100, smoth = 50,orientation = 0) -> None:
        super().__init__(pc)
        self.A = A
        self.B = B
        
        self.ori = orientation
        self.canvas = pc.canvas
        self.smoth = smoth

        self.points = draw_curve(A,B,curve=curve,smoth=smoth,orientation=orientation)
        id = self.canvas.create_line(self.points) ; self.id_list.append(id)

        if A[0]>B[0]: self.p1 = B ; self.p2 = A
        else: self.p1=A ; self.p2 = B

        self.bind_all()
        self.hide_condu()

    def set_arm(self,index = None,arm_size = 30,hand_size = 50,base_angle = None):
        #print("Update ?")
        if index == None:
            index = int(self.smoth/2)
        if base_angle == None:
            if self.p1[1]> self.p2[1]:
                base_angle = 45
            else: 
                base_angle = 135
        
        arm = get_radius_point(self.points[index],radius=arm_size,angle=base_angle) 
        id = self.canvas.create_line(self.points[index],arm) ; self.id_list.append(id)

        if int(arm[0]) >= int(self.points[index][0]):
            id = self.canvas.create_line(arm,(arm[0]+hand_size,arm[1])); self.id_list.append(id)
            self.armP1 = arm
            self.armP2 = (arm[0]+hand_size,arm[1])
            self.hand_points = linspace(self.armP1,self.armP2,hand_size)
            #print('1')
        else:
            id = self.canvas.create_line(arm,(arm[0]-hand_size,arm[1])) ; self.id_list.append(id)
            self.armP1 = arm
            self.armP2 = (arm[0]-hand_size,arm[1])
            self.hand_points = linspace(self.armP1,self.armP2,hand_size)
            #print(2)
        
        

    
    def draw_fase(self,size,index):
        
        p = self.hand_points[index]
        faseP1 = p[0],p[1]-size
        faseP2 = p[0],p[1]+size

        id = self.canvas.create_line(faseP1,faseP2) ; self.id_list.append(id)
        pass

    def draw_neutro(self,size,index):
        
        p = self.hand_points[index]
        neutroP1 = p[0]-size/2,p[1]-size
        neutroP2 = p[0],p[1]-size
        neutroP3 = p[0],p[1]+size

        id = self.canvas.create_line(neutroP1,neutroP2,neutroP3) ; self.id_list.append(id)
        
        pass

    def draw_terra(self,size,index):
        
        p = self.hand_points[index]
        terraP1 = p[0],p[1]-size
        terraP2 = p[0],p[1]+size

        id = self.canvas.create_line(terraP1,terraP2) ; self.id_list.append(id)

        terraP3 = terraP1[0]-size/2,terraP1[1]
        terraP4 = terraP1[0]+size/2,terraP1[1]

        id = self.canvas.create_line(terraP3,terraP4) ; self.id_list.append(id)

        pass


    def draw_simples(self,size,index):
        
        p = self.hand_points[index][0],self.hand_points[index][1]
        simplesP1 = p[0],p[1]-size

        id = self.canvas.create_line(p,simplesP1) ; self.id_list.append(id)
        
        pass

    def draw_paralelo(self,size,index):
        
        p = self.hand_points[index][0],self.hand_points[index][1]

        neutroP3 = p[0],p[1]-size
        neutroP4 = p[0],p[1]

        id = self.canvas.create_line(neutroP3,neutroP4) ; self.id_list.append(id)
        
        p = self.hand_points[index+5]

        neutroP3 = p[0],p[1]-size
        neutroP4 = p[0],p[1]

        id = self.canvas.create_line(neutroP3,neutroP4) ; self.id_list.append(id)
        
        pass

    def draw_by_text(self,text,index,size=10,space = 2,circ = "-1-  "):
        index = index
        p1 = self.hand_points[index][0],self.hand_points[index][1] - size*1.5
        
        for t in text:
            if t == 'F':
                self.draw_fase(size,index)
                index += space
            if t == 'N':
                self.draw_neutro(size,index)
                index += space
            if t == 'T':
                self.draw_terra(size,index+2)
                index += space
            if t == 'S':
                self.draw_simples(size,index)
                index += space
            if t == 'P':
                self.draw_paralelo(size,index)
                index += space
        
        p2 = self.hand_points[index][0],self.hand_points[index][1] - size*1.5

        id = draw_text(self.canvas,get_mid_p(p1,p2),circ,size=size) ; self.id_list.append(id)
        
        return 

    def bind_all(self):
        if self.pc :
            [self.canvas.tag_bind(id,"<Button-1>",self.explode) for id in self.id_list]
    
    def explode(self,event = None):
        '''MATA O DESENHO CASO ALGUÉM CLIQUE NELE COM A BORRACHA.
        OU SEJA SÓ FUNCIONA CASO O STATE SEJA ->erase<-'''

        if self.pc.state == 'erase':
            [self.pc.draw_canvas.delete(id) for id in self.id_list]
        
    def die(self):
        ''' DELETA O DESENHO DO CANVAS SEM NECESSARIAMENTE ESTAR NO
            ESTADO ->ereas<-'''
        [self.pc.draw_canvas.delete(id) for id in self.id_list]
    
    def hide_condu(self):
        try:
            for id in self.pc.last_lamp:
                self.canvas.tag_raise(id)
        except:None
        try:
            for id in self.pc.last_inter:
                self.canvas.tag_raise(id)
        except: None
        try:
            for id in self.pc.last_quadro:
                self.canvas.tag_raise(id)
        except: None
