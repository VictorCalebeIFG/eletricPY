from util_.util import generate_key

class Lampada:
    def __init__(self,canvas,centro,raio,pot,id,circ,pc = None) -> None:
        self.canvas = canvas
        self.centro = centro
        self.raio = raio
        self.pot = pot
        self.circ = circ
        self.id = id
        self.id_list = []
        self.pc = pc
        self.codekey = generate_key('lampada_')
        self.create()

    
    def create(self):
        p1x = self.centro[0] - self.raio
        p1y = self.centro[1] - self.raio
        p2x = p1x + 2*self.raio
        p2y = p1y + 2*self.raio

        id = self.canvas.create_oval(p1x,p1y,p2x,p2y,width=2,fill = 'white')
        self.id_list.append(id)

        self.left = (p1x,p1y+self.raio)                   #Pontos Tangentes Da circunferência
        self.right = (p1x + 2*self.raio,p1y+self.raio)
        self.botton = (p1x + self.raio,p2y)
        self.top = (p1x + self.raio,p1y)

        id = self.canvas.create_line(self.left,self.right)
        self.id_list.append(id)
        id = self.canvas.create_line(self.centro,self.botton)
        self.id_list.append(id)

        #ID
        idpos = (self.centro[0]+self.raio/2.5,self.centro[1]+self.raio/2.5)
        id = self.canvas.create_text(idpos,fill="black",font="Arial "+str(int(self.raio/2)),
                        text=self.id.upper())
        self.id_list.append(id)
        #Circuito
        circpos = (self.centro[0]-self.raio/2.5,self.centro[1]+self.raio/2.5)
        id = self.canvas.create_text(circpos,fill="black",font="Arial "+str(int(self.raio/2)),
                        text=self.circ.upper())
        self.id_list.append(id)
        #Pot
        potpos = (self.centro[0],self.centro[1]-self.raio/2.5)
        id = self.canvas.create_text(potpos,fill="black",font="Arial "+str(int(self.raio/2)),
                        text=str(self.pot))
        self.id_list.append(id)
        
        '''BIND NO OBJETO PRA QUANDO ALGUÉM CLICAR NELE COM A BORRACHA'''
        if self.pc :
            [self.canvas.tag_bind(id,"<Button-1>",self.explode) for id in self.id_list]
    
    def explode(self,event = None):
        '''MATA O DESENHO CASO ALGUÉM CLIQUE NELE COM A BORRACHA.
        OU SEJA SÓ FUNCIONA CASO O STATE SEJA ->erase<-'''

        self.pc.last_lamp = self.id_list

        if self.pc.state == 'erase':
            [self.pc.draw_canvas.delete(id) for id in self.id_list]
        
        if self.pc.state == 'condu':
            #self.canvas.tag_raise(self.id)
            
            if self.pc :
                self.pc.conect_p.append(self.centro)
                self.pc.conect_n += 1

    def die(self):
        [self.pc.draw_canvas.delete(id) for id in self.id_list]