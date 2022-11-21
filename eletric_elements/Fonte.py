from util_.util import get_mid_p
class Fonte:
    def __init__(self,canvas,w =30,h = 10,center = (100,100), pc = None) -> None:

        self.id_list = []
        self.pc = pc
        
        self.canvas         = canvas
        self.top_left       = self.tl = center[0] - w/2,center[1] + h/2
        self.botton_right   = self.br = self.tl[0]+w , self.tl[1]+h
        self.top_right      = self.tr = self.br[0],self.tl[1]
        self.botton_left    = self.bl = self.tl[0],self.br[1]

        self.middle_top     = self.mt = get_mid_p(self.tl,self.tr)
        self.middle_botton  = self.mb = get_mid_p(self.br,self.bl)
        self.middle_right   = self.mr = get_mid_p(self.tr,self.br)
        self.middle_left    = self.ml = get_mid_p(self.tl,self.bl)

        self.id_list.append(canvas.create_rectangle(self.tl,self.br,fill = 'white',width = 2))
        self.id_list.append(canvas.create_polygon(self.tl,self.br,self.bl))

        self.id_list.append(id)

        '''BIND NO OBJETO PRA QUANDO ALGUÉM CLICAR NELE COM A BORRACHA'''

        if self.pc : [self.canvas.tag_bind(id,"<Button-1>",self.explode) for id in self.id_list]
    
    def explode(self,event):
        '''MATA O DESENHO CASO ALGUÉM CLIQUE NELE COM A BORRACHA.
        OU SEJA SÓ FUNCIONA CASO O STATE SEJA ->erase<-'''
        
        if self.pc.state == 'erase':
            [self.pc.draw_canvas.delete(id) for id in self.id_list]
        pass

    def deletar(self):
        '''DELETA O DESENHO DO CANVAS SEM NECESSARIAMENTE ESTAR NO
        ESTADO ->ereas<-'''

        for id in self.id_list:
            self.canvas.delete(id)