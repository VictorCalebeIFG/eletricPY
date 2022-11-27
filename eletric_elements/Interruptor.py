from util_.util import create_circle,draw_text,get_radius_point,draw_curve,generate_key

class Interruptor_s1:
    def __init__(self,canvas,center,raio = 5,label = 'a',pc = None) -> None:
        # Desenha um interruptor simples no canvas
        # Recebe um canvas.
        # Recebe o centro do interruptor: "center".
        # Recebe o raio da circunferência do interruptor.
        # Recebe uma string pra identificar o interruptor: "label".

        self.center = center
        self.raio = raio
        self.label = label
        self.canvas = canvas
        self.obj = "s1" 
        self.pc = pc
        self.codekey = generate_key('interruptor_s1_')

        self.id_list = []

        id = create_circle(self.canvas,self.center,self.raio,color='white')
        self.id_list.append(id)
        
        self.botton = center[0], center[1] + raio
        self.celling = center[0], center[1] - raio
        self.right = center[0] + raio, center[1]
        self.left = center[0] - raio, center[1]
        pass

    def set_label(self,angle = 45,shift = 4):
        # Coloca label em algum lugar próximo ao interruptor.
        # Recebe um angulo que decide onde fica a label: "angle".
        # Recebe um valor "shift" que decide a distância da label para o interruptor.

        pos = get_radius_point(self.center,self.raio+shift,angle)
        id = draw_text(self.canvas,pos,self.label,self.raio)
        self.id_list.append(id)

        if self.pc : [self.canvas.tag_bind(id,"<Button-1>",self.explode) for id in self.id_list]
    
    def explode(self,event):
        ''' MATA O DESENHO CASO ALGUÉM CLIQUE NELE COM A BORRACHA.
            OU SEJA SÓ FUNCIONA CASO O STATE SEJA ->erase<-'''

        if self.pc.state == 'erase':
            [self.pc.draw_canvas.delete(id) for id in self.id_list]
        
        if self.pc.state == 'condu':
            self.pc.last_inter = self.id_list
            if self.pc :
                self.pc.conect_p.append(self.center)
                self.pc.conect_n += 1

    def die(self):
        ''' DELETA O DESENHO DO CANVAS SEM NECESSARIAMENTE ESTAR NO
            ESTADO ->ereas<-'''

        [self.pc.draw_canvas.delete(id) for id in self.id_list]
    
class Interruptor_s2:
    def __init__(self,canvas,center,raio = 5,label1 = 'a',label2='b',pc = None) -> None:
        # Desenha um interruptor simples no canvas
        # Recebe um canvas.
        # Recebe o centro do interruptor: "center".
        # Recebe o raio da circunferência do interruptor.
        # Recebe uma string pra identificar o interruptor: "label".

        self.center = center
        self.raio = raio
        self.label1 = label1
        self.label2 = label2
        self.canvas = canvas
        self.obj = "s2"
        self.pc = pc
        self.id_list = []
        self.codekey = generate_key('interruptor_s2_')

        id = create_circle(self.canvas,self.center,self.raio,color='white')
        self.id_list.append(id)
        
        self.bottom = center[0], center[1] + raio
        self.celling = center[0], center[1] - raio
        self.right = center[0] + raio, center[1]
        self.left = center[0] - raio, center[1]

        id = self.canvas.create_line(self.bottom,self.celling)
        self.id_list.append(id)

        pass

    def set_label(self,angle = 45,shift = 4):
        # Coloca label em algum lugar próximo ao interruptor.
        # Recebe um angulo que decide onde fica a label: "angle".
        # Recebe um valor "shift" que decide a distância da label para o interruptor.

        pos = get_radius_point(self.center,self.raio+shift,angle)
        draw = draw_text(self.canvas,pos,self.label1,self.raio)
        self.id_list.append(draw)

        pos = get_radius_point(self.center,self.raio+shift,angle+90)
        id = draw_text(self.canvas,pos,self.label2,self.raio)
        
        self.id_list.append(id)
        if self.pc : [self.canvas.tag_bind(id,"<Button-1>",self.explode) for id in self.id_list]
    
    def explode(self,event):
        '''MATA O DESENHO CASO ALGUÉM CLIQUE NELE COM A BORRACHA.
        OU SEJA SÓ FUNCIONA CASO O STATE SEJA ->erase<-'''

        if self.pc.state == 'erase':
            [self.pc.draw_canvas.delete(id) for id in self.id_list]
        
        if self.pc.state == 'condu':
            self.pc.last_inter = self.id_list
            if self.pc :
                self.pc.conect_p.append(self.center)
                self.pc.conect_n += 1
    
    def die(self):
        ''' DELETA O DESENHO DO CANVAS SEM NECESSARIAMENTE ESTAR NO
            ESTADO ->ereas<-'''
        [self.pc.draw_canvas.delete(id) for id in self.id_list]

class Interruptor_s3:
    def __init__(self,canvas,center,raio = 5,label1 = 'a',label2='b',label3 ='c',pc = None) -> None:
        # Desenha um interruptor simples no canvas
        # Recebe um canvas.
        # Recebe o centro do interruptor: "center".
        # Recebe o raio da circunferência do interruptor.
        # Recebe uma string pra identificar o interruptor: "label".

        self.center = center
        self.raio = raio
        self.label1 = label1
        self.label2 = label2
        self.label3 = label3
        self.canvas = canvas
        self.obj = "s3"
        self.pc = pc
        self.id_list = []
        self.codekey = generate_key('interruptor_s3_')

        id = create_circle(self.canvas,self.center,self.raio,color='white')
        self.id_list.append(id)
        
        self.botton = center[0], center[1] + raio
        self.celling = center[0], center[1] - raio
        self.right = center[0] + raio, center[1]
        self.left = center[0] - raio, center[1]

        id = self.canvas.create_line(self.celling,self.center)
        self.id_list.append(id)
        

        pos = get_radius_point(self.center,self.raio,45)
        id = self.canvas.create_line(self.center,pos)
        self.id_list.append(id)

        pos = get_radius_point(self.center,self.raio,45+90)
        id = self.canvas.create_line(self.center,pos)
        self.id_list.append(id)
        
        pass

    def set_label(self,shift = 4):
        # Coloca label em algum lugar próximo ao interruptor.
        # Recebe um angulo que decide onde fica a label: "angle".
        # Recebe um valor "shift" que decide a distância da label para o interruptor.

        pos = get_radius_point(self.center,self.raio+shift,90)
        id = draw_text(self.canvas,pos,self.label1,self.raio)
        self.id_list.append(id)

        pos = get_radius_point(self.center,self.raio+shift,-135)
        id = draw_text(self.canvas,pos,self.label2,self.raio)
        self.id_list.append(id)

        pos = get_radius_point(self.center,self.raio+shift,-45)
        id = draw_text(self.canvas,pos,self.label3,self.raio)
        self.id_list.append(id)
        
        if self.pc : [self.canvas.tag_bind(id,"<Button-1>",self.explode) for id in self.id_list]
    
    def explode(self,event):
        '''MATA O DESENHO CASO ALGUÉM CLIQUE NELE COM A BORRACHA.
        OU SEJA SÓ FUNCIONA CASO O STATE SEJA ->erase<-'''

        if self.pc.state == 'erase':
            [self.pc.draw_canvas.delete(id) for id in self.id_list]
        
        if self.pc.state == 'condu':
            self.pc.last_inter = self.id_list
            if self.pc :
                self.pc.conect_p.append(self.center)
                self.pc.conect_n += 1
    
    def die(self):
        ''' DELETA O DESENHO DO CANVAS SEM NECESSARIAMENTE ESTAR NO
            ESTADO ->ereas<-'''
        [self.pc.draw_canvas.delete(id) for id in self.id_list]

class Interruptor_3way:
    def __init__(self,canvas,center,raio = 5,label = 'a',pc = None) -> None:
        # Desenha um interruptor simples no canvas
        # Recebe um canvas.
        # Recebe o centro do interruptor: "center".
        # Recebe o raio da circunferência do interruptor.
        # Recebe uma string pra identificar o interruptor: "label".

        self.center = center
        self.raio = raio
        self.label = label
        self.canvas = canvas
        self.obj = "3way"
        self.pc = pc
        self.id_list = []
        self.codekey = generate_key('interruptor_3way_')

        id = create_circle(self.canvas,self.center,self.raio,color='black')
        self.id_list.append(id)
        
        self.bottom = center[0], center[1] + raio
        self.celling = center[0], center[1] - raio
        self.right = center[0] + raio, center[1]
        self.left = center[0] - raio, center[1]
        pass

    def set_label(self,angle = 45,shift = 4):
        # Coloca label em algum lugar próximo ao interruptor.
        # Recebe um angulo que decide onde fica a label: "angle".
        # Recebe um valor "shift" que decide a distância da label para o interruptor.

        pos = get_radius_point(self.center,self.raio+shift,angle)
        id = draw_text(self.canvas,pos,self.label,self.raio)

        self.id_list.append(id)
        if self.pc : [self.canvas.tag_bind(id,"<Button-1>",self.explode) for id in self.id_list]
    
    def explode(self,event):
        '''MATA O DESENHO CASO ALGUÉM CLIQUE NELE COM A BORRACHA.
        OU SEJA SÓ FUNCIONA CASO O STATE SEJA ->erase<-'''

        if self.pc.state == 'erase':
            [self.pc.draw_canvas.delete(id) for id in self.id_list]
        
        if self.pc.state == 'condu':
            self.pc.last_inter = self.id_list
            if self.pc :
                self.pc.conect_p.append(self.center)
                self.pc.conect_n += 1
    
    def die(self):
        [self.pc.draw_canvas.delete(id) for id in self.id_list]

class Interruptor_4way:
    def __init__(self,canvas,center,raio = 5,label = 'a',pc = None) -> None:
        # Desenha um interruptor simples no canvas
        # Recebe um canvas.
        # Recebe o centro do interruptor: "center".
        # Recebe o raio da circunferência do interruptor.
        # Recebe uma string pra identificar o interruptor: "label".

        self.center = center
        self.raio = raio
        self.label = label
        self.canvas = canvas
        self.obj = "4way" 
        self.codekey = generate_key('interruptor_4way_')

        id = create_circle(self.canvas,self.center,self.raio,color='')
        self.id_list.append(id)
        
        self.bottom = center[0], center[1] + raio
        self.celling = center[0], center[1] - raio
        self.right = center[0] + raio, center[1]
        self.left = center[0] - raio, center[1]

        points,head,angles = draw_curve(self.bottom,self.celling,0,dir=1)

        id = self.canvas.create_polygon(points)
        self.id_list.append(id)

        pass

    def set_label(self,angle = 45,shift = 4):
        # Coloca label em algum lugar próximo ao interruptor.
        # Recebe um angulo que decide onde fica a label: "angle".
        # Recebe um valor "shift" que decide a distância da label para o interruptor.

        pos = get_radius_point(self.center,self.raio+shift,angle)
        id = draw_text(self.canvas,pos,self.label,self.raio)
        self.id_list.append(id)

        '''BIND NO OBJETO PRA QUANDO ALGUÉM CLICAR NELE COM A BORRACHA'''

        self.id_list.append(id)
        if self.pc : [self.canvas.tag_bind(id,"<Button-1>",self.explode) for id in self.id_list]
    
    def explode(self,event):
        '''MATA O DESENHO CASO ALGUÉM CLIQUE NELE COM A BORRACHA.
        OU SEJA SÓ FUNCIONA CASO O STATE SEJA ->erase<-'''

        if self.pc.state == 'erase':
            [self.pc.draw_canvas.delete(id) for id in self.id_list]
        
        if self.pc.state == 'condu':
            self.pc.last_inter = self.id_list
            if self.pc :
                self.pc.conect_p.append(self.center)
                self.pc.conect_n += 1
    
    def die(self):
        ''' DELETA O DESENHO DO CANVAS SEM NECESSARIAMENTE ESTAR NO
            ESTADO ->ereas<-'''
            
        [self.pc.draw_canvas.delete(id) for id in self.id_list]