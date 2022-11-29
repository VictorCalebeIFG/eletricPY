import tkinter as tk
from Tools import tool
import UI_Interface.UI_insert as UI_insert
from util_.util import open_config

mouse_follow = open_config('follow_mouse')

class ProjectCanvas:
    def __init__(self,master,user_w,user_h,project_w,project_h):

        canvas_frame = tk.Frame(master=master)
        vscrollbar = tk.Scrollbar(canvas_frame)
        hscrollbar = tk.Scrollbar(canvas_frame,orient='horizontal')


        canvas = tk.Canvas(canvas_frame,yscrollcommand=vscrollbar.set, xscrollcommand= hscrollbar.set,
                    width = user_w ,height = user_h)
        

        vscrollbar.config(command=canvas.yview)
        vscrollbar.pack(side=tk.RIGHT,fill=tk.Y) 
        hscrollbar.config(command=canvas.xview)
        hscrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        project_canvas = tk.Canvas(canvas,width = project_w , height = project_h , bg = 'white') 

        canvas.pack()
        canvas.create_window(0,0,window = project_canvas, anchor='nw')


        master.update()
        canvas_frame.pack(expand=True)
        canvas.config(scrollregion=canvas.bbox("all"))

        self.frame = canvas_frame
        self.draw_canvas = project_canvas
        self.canvas = project_canvas
        self.insert_ui = None
        self.insert_ui_id = None
        self.state = 'normal'
        self.tool_mouse = None
        self.current_obj = None
        self.mouse_follow = mouse_follow
        self.master = master
        self.popup = None
        self.conect_p = [] ; self.conect_n = 0
        self.mouse_position = (0,0)
        self.elements = []
        self.canvas_functions = []    #Funções que são chamadas ao clicar com o esquerdo no CANVAS
        self.change_state_functions = []   #Funções que são chamadas ao clicar com o esquerdo nos botões
        self.popup_objects = {}
        self.last_lamp = None
        self.last_inter = None

        self.change_state_functions.append(self.do_nothing)
        self.canvas_functions.append(self.do_nothing)

        self.bind_all()
        pass
    
    def click_left(self,event):
        
        [f() for f in self.canvas_functions] #executa todas as funções na lista canvas_functions
        
        element = self.draw_canvas.gettags("current")

        if self.insert_ui:
            self.draw_canvas.coords(self.insert_ui_id,-100,0)
            self.insert_ui.delete()
            self.insert_ui = None
        
        print('\n'+'Class:EletricPyCanvas/ProjectCanvas'+"\n"+'Function:click_left'+'\n'+'x:{} ; y:{}'.format(event.x,event.y))
        
        if self.conect_n == 2:
            self.conect_n = 0
            UI_insert.connection_ui(self,self.master)
            self.set_state('normal')
        pass
    
    def bind_all(self):
        self.draw_canvas.bind("<Button-1>",self.click_left)
        pass
    
    def pack(self):
        self.frame.pack()
    
    def unpack(self):
        self.frame.pack_forget()
    
    def set_state(self,bt_state):
        for st in self.mouse_follow:
            self.verfiy_state(bt_state,v_state=st)
        if bt_state == 'normal':
            self.draw_canvas.delete(self.tool_mouse.label)
            self.state = 'normal'
    
        [f() for f in self.change_state_functions] # Executa todas as funções na lista click_buttons_functios

    
    def verfiy_state(self,bt_state,v_state):
        if bt_state == v_state and self.state != bt_state:
            self.tool_mouse = tool(self.draw_canvas,v_state)
            self.state = bt_state
        elif bt_state == v_state and self.state == v_state:
            self.draw_canvas.delete(self.tool_mouse.label)
            self.state = 'normal'
            pass

    def new_comodo_ui(self,pos):
        self.set_state('normal')
        insert_ui = UI_insert.new_comodo(self,self.master,pos)
        pass

    def do_nothing(self):
        None