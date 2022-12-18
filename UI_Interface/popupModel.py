from util_ import util
import tkinter as tk
from tkinter import ttk

alpha_value = 0.9

class popup_ui:
    def __init__(self,pc = None,master = None, title = 'Adicionar',width = '370',height = '250',leftdis='550',topdis='200') -> None:
        self.pop_w = tk.Toplevel(master)
        self.pop_w.title(title)
        self.pop_w.geometry("{width}x{height}+{leftdis}+{topdis}".format(width = width,
                                                                        height = height,
                                                                        leftdis = leftdis,
                                                                        topdis = topdis))

        self.pop_w.attributes('-alpha', alpha_value)
        self.pc = pc
        self.pc.popup = self
        self.ui_element = None
        self.id = util.generate_key('popup')
        self.ui_elements = []
        self.pop_w.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.main_frame = tk.Frame(self.pop_w)

        self.frame1 = tk.Frame(self.main_frame)
        self.frame2 = tk.Frame(self.main_frame)
        self.last = False
        
        #----- Configurações -------

        self.padx = 20
        self.pady = 20
        self.button_label = 'Create'


    def create_popup_ui(self,popup_text):
        ''' Cria uma pop_ui baseado num txt encontrado no folder UI/POPUP '''

        util.create_double_frame_ui_by_text(frame1=self.frame1,frame2=self.frame2,self=self,txt = 'UI/POPUP/{}'.format(popup_text))

        self.frame1.grid(row=0,
                        column=0,
                        padx= self.padx,
                        pady=self.pady)
        
        self.frame2.grid(row=0,
                        column=1,
                        padx= self.padx,
                        pady=self.pady)

        self.main_frame.pack(anchor=tk.CENTER,pady=10)

        createB = ttk.Button(self.pop_w,
                            text=self.button_label,
                            command = self.on_closing)
        createB.pack()

        self.pop_w.bind_all('<Key>',self.update)
        
        pass
    
    def element_creator(self):
        '''Aqui deve ser chamado a função no UI_backend.py que cria o elemento
        Você deve sobrescrever esse método.'''
        pass
    
    
    def create(self,delete=True):
        
        if delete:
            self.pop_w.destroy()
            self.pop_w.update()
        

        self.update(None)

        if delete == True: self.on_closing

    
    def update(self,var = None):
        
        if self.ui_element :
            self.ui_element.die()

        self.ui_element = self.element_creator()
        self.ui_elements.append(self.ui_element)
    
    def on_closing(self):
        self.last = True
        self.update(None)
        self.pop_w.destroy()