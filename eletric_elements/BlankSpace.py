from util_.util import get_mid_p,generate_key

config = {'fill':'white','outline':'white'}

class Space:
    def __init__(self,wall,comodo,dist1,dist2,pc = None) -> None:

        self.id_list = []
        self.pc = pc
        self.canvas = pc.canvas
        self.codekey = generate_key('space_')


        if wall=='esquerda':
            x1,y1 = comodo.tl_inp
            x2,y2 = comodo.E

            if dist1>=comodo.l_dim:
                dist1 = comodo.l_dim
            if dist2>=comodo.l_dim:
                dist2 = comodo.l_dim

            id = self.canvas.create_rectangle(x1+1,y1+dist1+1,x2,y2-dist2,fill=config['fill'],outline = config['outline'],width = 0)
            self.id_list.append(id)
            comodo.delete_list.append(id)

        if wall=='direita':
            x1,y1 = comodo.tr_inp
            x2,y2 = comodo.H

            if dist1>=comodo.r_dim:
                dist1 = comodo.r_dim
            if dist2>=comodo.r_dim:
                dist2 = comodo.r_dim
            
            id = self.canvas.create_rectangle(x1,y1+dist1+1,x2,y2-dist2,fill=config['fill'],outline = config['outline'],width = 0)
            self.id_list.append(id)
            comodo.delete_list.append(id)
        
        if wall=='cima':
            x1,y1 = comodo.B
            x2,y2 = comodo.tr_inp

            if dist1>=comodo.t_dim:
                dist1 = comodo.t_dim
            if dist2>=comodo.t_dim:
                dist2 = comodo.t_dim
            
            id = self.canvas.create_rectangle(x1+dist1+1,y1,x2-dist2,y2+1,fill=config['fill'],outline = config['outline'],width = 0)
            self.id_list.append(id)
            comodo.delete_list.append(id)

        if wall=='baixo':
            x1,y1 = comodo.bl_inp
            x2,y2 = comodo.G
            
            if dist1>=comodo.d_dim:
                dist1 = comodo.d_dim
            if dist2>=comodo.d_dim:
                dist2 = comodo.d_dim


            id = self.canvas.create_rectangle(x1+dist1+1,y1,x2-dist2,y2,fill=config['fill'],outline = config['outline'],width = 0)
            self.id_list.append(id)
            comodo.delete_list.append(id)

        self.id_list.append(id)
        
        '''BIND NO OBJETO PRA QUANDO ALGUÉM CLICAR NELE COM A BORRACHA'''
        if self.pc :
            [self.canvas.tag_bind(id,"<Button-1>",self.explode) for id in self.id_list]
    
    def explode(self,event):
        '''MATA O DESENHO CASO ALGUÉM CLIQUE NELE COM A BORRACHA.
        OU SEJA SÓ FUNCIONA CASO O STATE SEJA ->erase<-'''

        if self.pc.state == 'erase':
            [self.pc.draw_canvas.delete(id) for id in self.id_list]
        pass

    def die(self):
        '''DELETA O DESENHO DO CANVAS SEM NECESSARIAMENTE ESTAR NO
        ESTADO ->ereas<-'''
        
        for id in self.id_list:
            self.canvas.delete(id)