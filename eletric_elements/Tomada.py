from .Element import Element
from util_.util import get_mid_p, rotate_points,draw_text,get_radius_point,distance,get_widget_box,shift_points,walk,get_near,create_circle,get_mid_p
from eletric_elements.Element import Element


class Tomada(Element):
    def __init__(
                self, pc=None,
                angle = 0,
                tail_pos = (0,0),
                tail_size = 10,
                label = '',
                font_size = 10,
                amount = 1,) -> None:
        
        super().__init__(pc)

        self.canvas = self.pc.canvas
        self.tail = tail_pos
        self.label = label
        self.angle = angle
        self.amount = amount
        self.width = 2
        self.tail_size = tail_size
        self.last = None
        self.balls_on = False
        self.headBall = None
        self.tailBall = None

        commands = [('start',(tail_pos)),
                    ('up',tail_size),
                    ('right',tail_size),
                    ('xy',-tail_size,-tail_size*2),
                    ('xy',-tail_size,+tail_size*2),
                    ('right',tail_size)]

        self.points = walk(commands= commands)

        self.points = rotate_points(points=self.points,pivo = tail_pos,rot_ang = angle)

        self.head = self.points[3]

        self.arrow_height = distance(self.head,self.tail)
        
        self.triangle_height = self.arrow_height - tail_size

        self.pc.change_state_functions.append(self.delete_fakes)
        self.pc.change_state_functions.append(self.create_balls)


    def explode(self,event):
        '''MATA O DESENHO CASO ALGUÉM CLIQUE NELE COM A BORRACHA.
        OU SEJA SÓ FUNCIONA CASO O STATE SEJA ->erase<-'''

        if self.pc.state == 'erase':
            self.die()
        pass

    def create_balls(self):
        if self.last :
            if self.pc.state == 'condu':
                self.balls_on = True
            else: self.balls_on = False

            if self.balls_on:
                self.headBall = create_circle(self.canvas,self.head,self.tail_size/2,'blue')
                self.tailBall = create_circle(self.canvas,self.tail,self.tail_size/2,'blue')
                
                self.canvas.tag_bind(self.headBall,"<Button-1>",self.conection_head)
                self.canvas.tag_bind(self.tailBall,"<Button-1>",self.conection_tail)
            
            else:
                if self.headBall:
                    self.canvas.delete(self.headBall)
                    self.canvas.delete(self.tailBall)
    
    
    def delete_fakes(self):
        self.last = True
        for k in self.pc.popup_objects:
            if self.pc.popup_objects[k] is self:
                self.last = True
                break
            else: self.last = False
    
    def conection_head(self,event):
        self.pc.conect_p.append(self.head)
        self.pc.conect_n += 1
    
    def conection_tail(self,event):
        self.pc.conect_p.append(self.tail)
        self.pc.conect_n += 1
        

class Tomada_baixa(Tomada):
    def __init__(self,canvas,angle = 0,tail_pos = (100,100),tail_size = 10,label = '',font_size = 10,amount = 1, pc = None) -> None:
        
        super().__init__(pc,angle,tail_pos,
                        tail_size,label,
                        font_size,amount)
        
        self.codekey = 'tomada_baixa_'+self.codekey

        self.multipy_tugs()

        '''BIND NO OBJETO PRA QUANDO ALGUÉM CLICAR NELE COM A BORRACHA'''
        
        


    def multipy_tugs(self):

        if self.angle == 0:
            self.head = self.head[0],self.head[1]-self.triangle_height*(self.amount-1)
        if self.angle == 180:
            self.head = self.head[0],self.head[1]+self.triangle_height*(self.amount-1)
        if self.angle == 90:
            self.head = self.head[0]+self.triangle_height*(self.amount-1),self.head[1]
        if self.angle ==-90:
            self.head = self.head[0]-self.triangle_height*(self.amount-1),self.head[1]

        for n in range(self.amount):
            
            self.create_line(self.points,width=self.width)

            self.create_polygon(self.points[1:-1],fill='white',width=self.width)

            id = self.id_list[-1]
            
            if self.angle == 0 :
                self.pc.canvas.move(id,0,-self.triangle_height*n)
                
            if self.angle == 180:
                self.pc.canvas.move(id,0,+self.triangle_height*n)
                
            if self.angle == 90:
                self.pc.canvas.move(id,self.triangle_height*n,0)
                
            if self.angle == -90:
                self.pc.canvas.move(id,-self.triangle_height*n,0)
                
        
        self.bind_left(self.explode)


class Tomada_media(Tomada):
    def __init__(self,canvas,angle = 0,tail_pos = (100,100),tail_size = 10,label = '',font_size = 10,amount = 1, pc = None) -> None:
        
        super().__init__(pc,angle,tail_pos,
                        tail_size,label,
                        font_size,amount)


        self.codekey = 'tomada_media_'+self.codekey

        self.multipy_tugs()

        '''BIND NO OBJETO PRA QUANDO ALGUÉM CLICAR NELE COM A BORRACHA'''
        
        self.bind_left(self.explode)


    def multipy_tugs(self):

        if self.angle == 0:
            self.head = self.head[0],self.head[1]-self.triangle_height*(self.amount-1)
        if self.angle == 180:
            self.head = self.head[0],self.head[1]+self.triangle_height*(self.amount-1)
        if self.angle == 90:
            self.head = self.head[0]+self.triangle_height*(self.amount-1),self.head[1]
        if self.angle ==-90:
            self.head = self.head[0]-self.triangle_height*(self.amount-1),self.head[1]

        for n in range(self.amount):
            
            self.create_line(self.points,width=self.width)

            self.create_polygon(self.points[1:4],fill='black',width=self.width,outline='black')

            id = self.id_list[-1]
            id2 = self.id_list[-2]
            
            if self.angle == 0 :
                self.pc.canvas.move(id,0,-self.triangle_height*n)
                self.pc.canvas.move(id2,0,-self.triangle_height*n)
            if self.angle == 180:
                self.pc.canvas.move(id,0,+self.triangle_height*n)
                self.pc.canvas.move(id2,0,+self.triangle_height*n)
            if self.angle == 90:
                self.pc.canvas.move(id,self.triangle_height*n,0)
                self.pc.canvas.move(id2,self.triangle_height*n,0)
            if self.angle == -90:
                self.pc.canvas.move(id,-self.triangle_height*n,0)    
                self.pc.canvas.move(id2,-self.triangle_height*n,0)

        self.bind_left(self.explode) 
        
        

class Tomada_alta(Tomada):
    def __init__(self,canvas,angle = 0,tail_pos = (100,100),tail_size = 10,label = '',font_size = 10,amount = 1, pc = None) -> None:
        
        super().__init__(pc,angle,tail_pos,
                        tail_size,label,
                        font_size,amount)

        self.multipy_tugs()

        '''BIND NO OBJETO PRA QUANDO ALGUÉM CLICAR NELE COM A BORRACHA'''
        
        self.bind_left(self.explode)

        self.codekey = 'tomada_alta_'+self.codekey


    def multipy_tugs(self):

        if self.angle == 0:
            self.head = self.head[0],self.head[1]-self.triangle_height*(self.amount-1)
        if self.angle == 180:
            self.head = self.head[0],self.head[1]+self.triangle_height*(self.amount-1)
        if self.angle == 90:
            self.head = self.head[0]+self.triangle_height*(self.amount-1),self.head[1]
        if self.angle ==-90:
            self.head = self.head[0]-self.triangle_height*(self.amount-1),self.head[1]

        for n in range(self.amount):
            
            self.create_line(self.points,width=self.width)

            self.create_polygon(self.points[1:-1],fill='black',width=self.width)

            id = self.id_list[-1]
            
            if self.angle == 0 :
                self.pc.canvas.move(id,0,-self.triangle_height*n)
            if self.angle == 180:
                self.pc.canvas.move(id,0,+self.triangle_height*n)
            if self.angle == 90:
                self.pc.canvas.move(id,self.triangle_height*n,0)
            if self.angle == -90:
                self.pc.canvas.move(id,-self.triangle_height*n,0)  

        self.bind_left(self.explode) 