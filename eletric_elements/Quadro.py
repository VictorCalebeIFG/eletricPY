from util_.util import generate_key

class Quadro:
    def __init__(self,canvas,center, size, wall, pc = None) -> None:
        # Desenha um interruptor simples no canvas
        # Recebe um canvas.
        # Recebe o centro do interruptor: "center".
        # Recebe o raio da circunferência do interruptor.
        # Recebe uma string pra identificar o interruptor: "label".

        self.center = center
        self.size = size
        self.canvas = canvas
        self.pc = pc
        self.codekey = generate_key('quadro_')

        self.id_list = []

        self.height = 0
        self.width = 0
        if (wall == "esquerda"):
            self.height = size/2
            self.width = size
        if (wall == "direita"):
            self.height = -size/2
            self.width = size 
        if (wall == "cima"):
            self.height = size
            self.width = size/2
        if (wall == "baixo"):
            self.height = size
            self.width = -size/2
        id = canvas.create_rectangle(self.center[0], self.center[1], self.center[0] + self.height, self.center[1] + self.width, fill="white")
        self.id_list.append(id)

        id = canvas.create_polygon(self.center[0], self.center[1], self.center[0] + self.height, self.center[1], fill = "black", outline = "black", width = 1)
        
        self.id_list.append(id)
        
        self.botton = center[0], center[1] + size
        self.celling = center[0], center[1] - size
        self.right = center[0] + size, center[1]
        self.left = center[0] - size, center[1]

        if self.pc :
            [self.canvas.tag_bind(id,"<Button-1>",self.explode) for id in self.id_list]
        pass

    
    def explode(self,event):
        ''' MATA O DESENHO CASO ALGUÉM CLIQUE NELE COM A BORRACHA.
            OU SEJA SÓ FUNCIONA CASO O STATE SEJA ->erase<-'''

        if self.pc.state == 'erase':
            [self.pc.draw_canvas.delete(id) for id in self.id_list]
        
        if self.pc.state == 'condu':
            self.pc.last_quadro = self.id_list
            if self.pc :
                self.pc.conect_p.append(self.center)
                self.pc.conect_n += 1

    def die(self):
        ''' DELETA O DESENHO DO CANVAS SEM NECESSARIAMENTE ESTAR NO
            ESTADO ->ereas<-'''

        [self.pc.draw_canvas.delete(id) for id in self.id_list]