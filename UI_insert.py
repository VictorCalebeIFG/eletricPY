import tkinter as tk
from tkinter import ttk
import UI_backend
from util import open_config,create_tk_labels,create_tk_drop_down,create_double_frame_ui_by_text

comodo_options_list = open_config('comodo_options_list')
lamp_option_list = open_config('lamp_option_list')
tom_option_list = open_config('tom_option_list')
tom_lado_option_list = open_config('tom_lado_option_list')

class new_comodo:
    def __init__(self,pc,master,pos = None) -> None:
        self.pop_w = tk.Toplevel(master)
        self.pop_w.title("Criar Novo Comodo")
        self.pop_w.geometry("300x250+550+200")
        self.pos = pos
        self.pc = pc

        main_frame = tk.Frame(self.pop_w)

        frameL = tk.Frame(main_frame)
        frameE = tk.Frame(main_frame)
        #LABELS
        opcomodoL = tk.Label(frameL,text='Tipo de Comodo:')
        opcomodoL.pack(anchor=tk.NW,pady=5)
        espL = tk.Label(frameL,text='Espessura:')
        espL.pack(anchor=tk.NW,pady=5)
        larguraL = tk.Label(frameL,text='Largura:')
        larguraL.pack(anchor=tk.NW,pady=5)
        AlturaL = tk.Label(frameL,text='Altura:')
        AlturaL.pack(anchor=tk.NW,pady=5)
        #DROP DOWN MENU
        self.comodo_id = tk.StringVar(master)
        self.comodo_id.set('quarto')
        opcomodo = ttk.OptionMenu(frameE, self.comodo_id,*comodo_options_list)
        opcomodo.config(width=15)
        opcomodo.pack(anchor=tk.NW,pady=5,expand=True)
        # ENTRYS
        self.esp  = tk.StringVar()
        self.esp.set('0.1')
        espE = ttk.Entry(frameE,textvariable = self.esp)
        espE.pack(anchor=tk.NW,pady=5)
        self.largura = tk.StringVar()
        self.largura.set('3')
        larguraE = ttk.Entry(frameE,textvariable = self.largura)
        larguraE.pack(anchor=tk.NW,pady=5)
        self.altura = tk.StringVar()
        self.altura.set('3')
        alturaE = ttk.Entry(frameE , textvariable= self.altura)
        alturaE.pack(anchor=tk.NW,pady=5)

        

        frameL.grid(row=0,column=0,padx=20,pady=20)
        frameE.grid(row=0,column=1,padx=20,pady=20)

        main_frame.pack(anchor=tk.CENTER,pady=10)

        createB = ttk.Button(self.pop_w,text='create',command=self.create_comodo)
        createB.pack()
        pass
    
    def create_comodo(self):
        self.pop_w.destroy()
        self.pop_w.update()

        UI_backend.e = float(self.esp.get()) ; UI_backend.horizontal_dim = float(self.largura.get())
        UI_backend.vertical_dim = float(self.altura.get()) ; UI_backend.x = float(self.pos[0]) 
        UI_backend.y = float(self.pos[1])
        
        UI_backend.create_comodo(canvas=self.pc.draw_canvas,pc = self.pc)

class new_lamp:
    def __init__(self,pc = None,master = None) -> None:
        self.pop_w = tk.Toplevel(master)
        self.pop_w.title("Adicionar Nova Lampada")
        self.pop_w.geometry("370x250+550+200")
        self.pc = pc
        self.lamp = None

        main_frame = tk.Frame(self.pop_w)

        frameL = tk.Frame(main_frame)
        frameE = tk.Frame(main_frame)
        #LABELS
        lampL = tk.Label(frameL,text='Posi????o da L??mpada:')
        lampL.pack(anchor=tk.NW,pady=5)
        raioL = tk.Label(frameL,text='Raio:')
        raioL.pack(anchor=tk.NW,pady=5)
        potL = tk.Label(frameL,text='Pot??ncia:')
        potL.pack(anchor=tk.NW,pady=5)
        circL = tk.Label(frameL,text='Circuito:')
        circL.pack(anchor=tk.NW,pady=5)
        comL = tk.Label(frameL,text='Comando:')
        comL.pack(anchor=tk.NW,pady=5)
        #DROP DOWN MENU
        self.lamp_pos = tk.StringVar(master)
        self.lamp_pos.set('centro')
        oplamp = ttk.OptionMenu(frameE, self.lamp_pos,*lamp_option_list)
        oplamp.config(width=15)
        oplamp.pack(anchor=tk.NW,pady=5,expand=True)
        #ENTRYS
        self.raio  = tk.IntVar()
        raioS = ttk.Scale(frameE,from_=0,to=100,orient=tk.HORIZONTAL,command=self.lamp_update,variable=self.raio)
        raioS.pack(anchor=tk.NW,pady=5)
        self.pot  = tk.StringVar()
        potE = ttk.Entry(frameE,textvariable = self.pot)
        potE.pack(anchor=tk.NW,pady=5)
        self.circ = tk.StringVar()
        circE = ttk.Entry(frameE,textvariable = self.circ)
        circE.pack(anchor=tk.NW,pady=5)
        self.com = tk.StringVar()
        comE = ttk.Entry(frameE , textvariable= self.com)
        comE.pack(anchor=tk.NW,pady=5)

        frameL.grid(row=0,column=0,padx=20,pady=20)
        frameE.grid(row=0,column=1,padx=20,pady=20)

        main_frame.pack(anchor=tk.CENTER,pady=10)

        createB = ttk.Button(self.pop_w,text='ADD LAMP',command = self.create_lamp)
        createB.pack()
        pass
    def create_lamp(self):
        self.pop_w.destroy()
        self.pop_w.update()
        
        if self.lamp : self.lamp.die()

        UI_backend.create_lamp(canvas=self.pc.draw_canvas,pc = self.pc,
                                raio=int(self.raio.get()),pot=self.pot.get(),
                                com=self.com.get(),circ=self.circ.get())
    def lamp_update(self,var):
        if self.lamp : self.lamp.die()
        self.lamp = UI_backend.create_lamp(canvas=self.pc.draw_canvas,pc = self.pc,
                                    raio=int(self.raio.get()),pot=self.pot.get(),
                                    com=self.com.get(),circ=self.circ.get())

class new_tom:
    def __init__(self,pc = None,master = None) -> None:
        self.pop_w = tk.Toplevel(master)
        self.pop_w.title("Adicionar Nova Tomada")
        self.pop_w.geometry("370x250+550+200")
        self.pc = pc
        self.lamp = None

        main_frame = tk.Frame(self.pop_w)

        frameL = tk.Frame(main_frame)
        frameE = tk.Frame(main_frame)

        create_double_frame_ui_by_text(frameL,frameE,self=self,txt='tom_ui')
        
        frameL.grid(row=0,column=0,padx=20,pady=20)
        frameE.grid(row=0,column=1,padx=20,pady=20)

        main_frame.pack(anchor=tk.CENTER,pady=10)

        createB = ttk.Button(self.pop_w,text='ADD TUG',command = self.create_tom)
        createB.pack()
        pass
    def create_tom(self):
        self.pop_w.destroy()
        self.pop_w.update()
        
        UI_backend.create_tom(self.pc.draw_canvas,self.pc,self.tipo.get(),
        self.lado.get(),self.pos.get(),self.pot.get())

    def lamp_update(self,var):
        if self.lamp : self.lamp.die()
        self.lamp = UI_backend.create_lamp(canvas=self.pc.draw_canvas,pc = self.pc,
                                    raio=int(self.raio.get()),pot=self.pot.get(),
                                    com=self.com.get(),circ=self.circ.get())
    def teste(self,var):
        print(':)')
#master = tk.Tk()
#tk.Button(master,command=lambda: new_lamp(pc=None,master=master),text= 'teste').pack()

#master.mainloop()
