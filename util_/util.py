from math import sin, radians,cos,atan2,degrees,acos
from tkinter import font
import tkinter
from turtle import right
from numpy import linspace,polyfit,polyval
import tkinter as tk
from tkinter import StringVar,IntVar
from tkinter import ttk
import string
import random
import json


def angle_sin(ang):
    '''Calcula o seno de um angulo'''
    return sin(radians(ang))

def angle_cos(ang):
    '''Calcula o cos de um angulo'''
    return cos(radians(ang))

def angle_vector(vec):
    '''Calcula o angulo de um vetor que inicia na origem.'''
    return degrees(atan2(vec[1],vec[0]))

def distance(A,B):
    '''Calcula a distância entre dois pontos'''
    return ((A[0]-B[0])**2 + (A[1] - B[1])**2)**(1/2)

def percent_line(A,B,p):
    '''Encontra um ponto intermediário entre A e B baseado em uma procentagem.
    Exemplo: se p = 0.5 a funcao vai retornar o ponto médio entre A e B.
    Exemplo: se p = 0 a funcao vai retornar o ponto B.
    Exemplo: se p = 1 a funcao vai retornar o ponto A.'''

    vec = B[0] - A[0] , B[1] - A[1]
    ang = angle_vector(vec)
    d = distance(A,B)
    
    if ang <=0:
        point = B[0] - p*d*angle_cos(ang), B[1] - p*d*angle_sin(ang)
    else:
        point = B[0] - p*d*angle_cos(ang), B[1] - p*d*angle_sin(ang)
    return point

def create_circle(canvas,c,r,color = 'red',tag = ''):
    # Cria uma cricunferencia vermelha, com centro "c" e rairo "r".
    # Utilizado pra debugar.

    p1 = c[0]-r,c[1]-r
    p2 = c[0]+r,c[1]+r
    return canvas.create_oval(p1,p2,fill=color,tags = tag)

def get_mid_p(A,B):
    # Obtem o midpoint da reta.
    return (A[0]+B[0])/2 , (A[1]+B[1])/2

def perpendicular_point(A,B,d,p = 0.5, dir = 0):
    # Cria um vetor perpendicular ao vetor ab.
    # O parâmetro "p" deve estrar entre 0 e 1 (float), é ele que decide quão posição começa o vetor perpendicular.
    # O parâmetro dir, decide qual lado em relação ao vetor AB a reta perpendicular vai estar.
    # Retorna (inter_point, head)

    vec = get_vec_A_B(A,B)

    inter_point = percent_line(A,B,p)

    ang_vec = angle_vector(vec) #Angulo da reta

    if (ang_vec >=0 and ang_vec<= 90) or (ang_vec>=-180 and ang_vec<=-90):
        if ang_vec>=-180 and ang_vec<=-90: ang_vec +=180
        #Cabeça do vetor no quarto quadrante ou no segundo.
        per_ang = -(90 - ang_vec)  +dir*(180) #Angulo perpendicular
        head = (inter_point[0] + d*angle_cos(per_ang), inter_point[1] + d*angle_sin(per_ang)) #Cabeça do vetor
    else:
        #Cabeça do vetor no primeiro ou no terceiro quadrante.
        if ang_vec <= -180 and ang_vec >= -270: ang_vec += 180
        per_ang = -(90 - ang_vec)  + dir*(180)
        head = (inter_point[0] + d*angle_cos(per_ang), inter_point[1] + d*angle_sin(per_ang)) #Cabeça do vetor
    
    return (inter_point,head)
    pass

def draw_curve(A,B,d,dir = 0):
    # Somente para vetores do tipo ' / ' (primeiro ou terceiro quadrante)
    # Recebe dois pontos, esses dois pontos devem formar um vetor
    # no primeiro ou no terceiro quadrante.
    #
    # O parametro "d" é o tamanho do raio da circunferência que pega os dois pontos.
    # Quanto maior o d menos curvado é aligação entre os dois pontos.
    # Caso d seja zero a curva será a semicircunferência que liga os dois pontos.
    #
    # Retorna os pontos da curva: points
    # Retorna o head do vetor perpendicular a reta AB: head.
    # Retorna os angulos utilizados pra fazer a curva.
    # Return points,head,angles

    quad = get_quadrant(get_vec_A_B(A,B))
    
    A,B = set_quad_to_1(A,B) #Garante que o vetor esteja no primeiro quadrante

    inter_point,head = perpendicular_point(A,B,d,p = 0.5,dir = dir)
    # Encontra o ponto perpendicular ao ponto médio da linha que liga os dois pontos ( A e B ).

    vec_1 = get_vec_A_B(head,A) # Obtem o vetore que vai do ponto perpendicular até o ponto A
    vec_2 = get_vec_A_B(head,B) # Obtem o vetore que vai do ponto perpendicular até o ponto B

    raio = get_vec_module(vec_1) #Tamanho do raio 

    
    ang1 = angle_vector(vec_1)
    # Ângulo inicial.
    ang2 = angle_vector(vec_2) + dir*360
    # Ângulo final.

    angles = linspace(ang1,ang2,20).tolist()
    angles = [round(a,2) for a in angles]

    points =  [(head[0]+raio*angle_cos(a),head[1]+raio*angle_sin(a)) for a in angles]
    
    points = [(round(p[0],2),round(p[1],2)) for p in points]

    if quad == 4 or quad == 2:
        print("hello")
        points = rotate_points(points,get_mid_p(A,B),90 + dir*360)
        head = rotate_points([head],get_mid_p(A,B),90 + dir*360)[0]
        angles = [a+90 + dir*360 for a in angles]

    return points,head,angles

def rotate_points(points,pivo,rot_ang = 0):
    # Rotaciona um conjunto de pontos em relação a um pivo.
    # Recebe um conjunto de pontos : 'points'.
    # Recebe um pivo (eixo de rotação).
    # Recebe um angulo de rotação: 'rot_ang'.
    #
    # Retorna os pontos rotacionados: Return rotate_points.

    raios = [distance(p,pivo) for p in points]

    angles = [angle_vector(get_vec_A_B(pivo,p)) for p in points]

    rotate_points = [(pivo[0] + raios[i]*angle_cos(rot_ang + angles[i]),
                      pivo[1] + raios[i]*angle_sin(rot_ang + angles[i]) )for i in range(len(angles))]

    return rotate_points
    pass

def get_vec_A_B(A,B):
    #Retorna o vetor AB (indo de A para B).
    return (B[0] - A[0], B[1] - A[1])
    pass

def get_vec_module(vec):
    # Retorna o módulo de um vetor
    return (vec[0]**2 + vec[1]**2)**(0.5)

def produto_escalar(A,B):
    # Retorna o produto escalar entre AB.
    return A[0]*B[0] + A[1]*B[1]

def get_angle_between(vec1,vec2):
    #Retorna o ângulo entre dois vetores.
    cos_ang = (produto_escalar(vec1,vec2))/(get_vec_module(vec1)*get_vec_module(vec2))
    return acos(cos_ang)
    pass

def get_quadrant(vec):
    #Retorna qual quadrante está o vetor.

    ang = angle_vector(vec)
    
    if (ang <=0 and ang>=-90) or (ang<=360 and ang>=270):
        return 1
    if (ang <= -90 and ang>=-180) or (ang<270 and ang>=180):
        return 2
    if (ang < -180 and ang>=-270) or (ang<180 and ang>=90):
        return 3
    if (ang < -270 and ang>=-360) or (ang<90 and ang>=0):
        return 4

def set_quad_to_1(A,B):
    #Verifica qual quadrante está o vetor AB.
    vec = get_vec_A_B(A,B) # Vetor que liga os dois pontos
    quad = get_quadrant(vec) # Quadrante do vetor calculado na linha anterior.

    if quad == 3:
        #Garante que o vetor esteja sempre no primeiro quadrante.
        a = A; b = B
        A = b; B = a
    
    if quad == 4:
        points = rotate_points([A,B],get_mid_p(A,B),-90)
        A,B = points[0],points[1]
    
    if quad == 2:
        points = rotate_points([A,B],get_mid_p(A,B),90)
        A,B = points[0],points[1]

    return A,B

def draw_radio_line(center,d1,d2,angle):
    # Desenha uma reta baseada num angulo
    # A reta começa a ser desenhada a uma distância d1 do centro
    # e termina a uma distância d2 do centro.

    A = (center[0]+d1*angle_cos(angle),center[1]+d1*angle_sin(angle))
    B = (center[0]+d2*angle_cos(angle),center[1]+d2*angle_sin(angle))

    return A,B

def draw_text(canvas,center,text,size):
    # Desenha um text em um canvas.
    # Com acora no "center".
    # Receve um "canvas".
    # Recebe uma coordenada (tupla) "centro".
    # Recebe uma string "texto".

     return canvas.create_text(center[0],center[1],text = text,font = ('Helvetica',str(size),'bold'))

def draw_circle_by_angle(center,radius,angle1,angle2):
    # Desenha um arco entre o angle1 e o angle2.
    # Recebe o centro do arco :"center".
    # Recebe o raio: "radius"
    # O ângulo inicial: "angle1"
    # O ângulo final: "angle2"
    #
    #Retorna os pontos do arco.

    angles = linspace(angle1,angle2,20).tolist()
    angles = [round(a,2) for a in angles]

    points = [(center[0] + radius*angle_cos(a),center[1] + radius*angle_sin(a)) for a in angles]
    return points

def get_radius_point(center,radius,angle):
    # Obtem um ponto dentro da circunferência através de um angulo
    # Recebe um centro: "center".
    # Recebe um raio: "radius".
    # Recebe o angulo da posição desejada: "angle".
    #
    #Retorna a posição do ponto desejado: "point".
    

    point = (center[0] + radius*angle_cos(angle),center[1] + radius*angle_sin(angle))
    return point

def get_widget_box(canvas,widget):
    #Calcula a altura (height) e a largura(width) de um widget.
    #Retorna (height,width)
    bounds  = canvas.bbox(widget) 
    width   = bounds[2] - bounds[0]
    height  = bounds[3] - bounds[1]

    return height,width

def shift_points(points,x = 0 ,y = 0):
    aux = []
    for p in points:
        aux.append((p[0]+x,p[1]+y))
    return aux

def sum_points(A,B):
    return (A[0]+B[0],A[1]+B[1])

def dif_points(A,B):
    return (A[0]-B[0],A[1]-B[1])

def get_line_paramaters(line = []):
    (x1,y1),(x2,y2) = line
    
    a = (y1-y2)/(x1-x2)
    b = y1 - a*x1

    return {'a': a , 'b':b}

def intersec_lines(line1=[],line2=[]):
    a1 = get_line_paramaters(line1)['a']
    b1 = get_line_paramaters(line1)['b']
    a2 = get_line_paramaters(line2)['a']
    b2 = get_line_paramaters(line2)['b']

    x = (b2-b1)/(a1-a2)
    y = a1*x + b1

    return (x,y)

def open_config(txt):
    with open('config/{}.txt'.format(txt),encoding="utf8") as f:
        lines = f.readlines()
        aux = []
        for l in lines:
            if not l.startswith('#'):
                aux.append(l)
        lines = aux
        return [l.strip('\n') for l in lines if not l.startswith('\n')]

def create_tk_labels(frame,labels = [],anchor = tk.NW,pady = 5,padx = 1):
    for l in labels:
        label = tk.Label(frame,text = l)
        label.pack(anchor=tk.NW,pady=pady,padx=padx)
    pass

def create_tk_drop_down(frame,self,op_list = [],var_n = '', anchor = tk.NW, pady = 5,width = 15,cmd = None):
    aux_list = []
    comand = '''
self.{} = tk.StringVar()
aux_list.append(self.{})
aux_list.append(ttk.OptionMenu(frame, aux_list[0],*op_list,command = self.{}))
                '''.format(var_n,var_n,cmd)
    
    exec(comand,{'self':self,'tk':tk,'aux_list':aux_list,'ttk':ttk,'op_list':op_list,'frame':frame})

    #op = ttk.OptionMenu(frame, aux_list[0],*op_list)
    aux_list[1].config(width=width)
    aux_list[1].pack(anchor=anchor,pady=pady,expand=True)

    pass

def create_tk_entry(frame,self,var_n = '',anchor = tk.NW, pady = 5,width = 15):
    aux_list = []

    comand = '''
self.{} = tk.StringVar()
aux_list.append(self.{})
                '''.format(var_n,var_n)
    
    exec(comand,{'self':self,'tk':tk,'aux_list':aux_list})

    en = ttk.Entry(frame,textvariable=aux_list[0],validatecommand=lambda:print("hello"))
    en.pack(anchor=anchor,pady=pady,expand=True)
    pass

def create_tk_scale(frame,self,var_n = '',from_=0,to_=100,comando = None,anchor = tk.NW, pady = 5,width = 15):
    aux_list = []

    s = None

    comand = '''
self.{} = tk.IntVar()
aux_list.append(self.{})
self.{}.set(int((from_+to_/2)))
{}s = ttk.Scale(frame,from_=from_,to=to_,orient=tk.HORIZONTAL,command=self.{},variable=self.{})
{}s.pack(anchor=tk.NW,pady=5)
                '''.format(var_n,var_n,var_n,var_n,comando,var_n,var_n)
    
    exec(comand,{'self':self,'tk':tk,'aux_list':aux_list,'from_':from_,'to_':to_,'comando':comando,'ttk':ttk,'frame':frame})

    #s = ttk.Scale(frame,from_=from_,to=to_,orient=tk.HORIZONTAL,command=comando,variable=self.pos)
    #s.pack(anchor=tk.NW,pady=5)
    
    pass

def create_double_frame_ui_by_text(frame1=None,frame2 = None,self = None,txt = None):
    commands = open_config(txt)
    label_ = [l.split('-')[0] for l in commands]
    widget_ = [l.split('-')[1] for l in commands]
    varname_ = [l.split('-')[2] for l in commands]
    comm_ = [l.split('-')[3] for l in commands]
    list_ = [l.split('/')[1].split('-') for l in commands]

    create_tk_labels(frame1,label_)

    for i in range(len(commands)):
        if widget_[i] == 'dropdown' :
            create_tk_drop_down(frame2,self=self,op_list=list_[i],var_n=varname_[i],cmd=comm_[i])
        if widget_[i] == 'entry' :
            create_tk_entry(frame2,self=self,var_n = varname_[i])
        if widget_[i] == 'scale':
            create_tk_scale(frame2,self=self,var_n=varname_[i],
                            from_ = int(list_[i][0]),to_ = int(list_[i][1]),comando=comm_[i])
    pass

def create_double_frame_ui_only_text(frame1=None,frame2 = None,self = None,txt = None):
    commands = open_config(txt)
    create_tk_labels(frame1,commands)
    pass


def generate_key(element,kn=10):
    key = random.choices(string.ascii_uppercase,k=kn)
    key = ''.join(key)
    return element+key
    pass

def get_widgets_values(dict):

    return {k:dict[k].get() for k in dict 
            if type(dict[k]).__name__ == 'StringVar'
            or type(dict[k]).__name__ == 'IntVar'}
    pass

def polynomial_fit(points = [(0,0)],order = 1,smoth = 20):
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    
    pesos = polyfit(x,y,order)
    
    xvalues = linspace(x[0],x[-1],smoth)

    yvalues = polyval(pesos,xvalues)

    return [(x,y)for x,y in zip(xvalues,yvalues)]

def get_near(point,points):

    distances = {p:distance(point,p) for p in points}

    print(min(distances, key=distances.get))

def walk(commands = None):
    '''comands = [ ('start',(100,100)),
                    ('right',100),
                    ('down',100),
                    ('right',200),
                    ('up',50),
                    ('left',200),
                    ('upright',200)] '''
    walk = []
    feet = (0,0)

    if commands == None:
        commands = [ ('start',(100,100)),
                    ('right',100),
                    ('down',100),
                    ('right',200),
                    ('up',50),
                    ('left',200),
                    ('upright',200)]
        
    for c in commands:
        if c[0] == 'start':
            walk.append(c[1])
            feet = c[1]
        if c[0] == 'right':
            feet = feet[0]+c[1],feet[1]
            walk.append(feet)
        if c[0] == 'left':
            feet = feet[0]-c[1],feet[1]
            walk.append(feet)
        if c[0] == 'down':
            feet = feet[0],feet[1]+c[1]
            walk.append(feet)
        if c[0] == 'up':
            feet = feet[0],feet[1]-c[1]
            walk.append(feet)
        if 'up'in c[0] and 'right'in c[0]:
            feet = feet[0]+c[1],feet[1]-c[1]
            walk.append(feet)
        if 'down'in c[0] and 'right'in c[0]:
            feet = feet[0]+c[1],feet[1]+c[1]
            walk.append(feet)
        if 'up'in c[0] and 'left'in c[0]:
            feet = feet[0]-c[1],feet[1]-c[1]
            walk.append(feet)
        if 'down'in c[0] and 'left'in c[0]:
            feet = feet[0]-c[1],feet[1]+c[1]
            walk.append(feet)
        if c[0]=='xy':
            feet = feet[0]+c[1],feet[1]+c[2]
            walk.append(feet)    
    
    return walk

    pass

def save(elementkey,arguments,parent = 'No Dad',popupkey = None,filename='Saving/projeto_1.json'):
    with open(filename,'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details

        file_data["ui_elements"].append({
                                        "elemetkey": elementkey,
                                        "Arguments":arguments,
                                        "parent":parent
                                        })
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)




