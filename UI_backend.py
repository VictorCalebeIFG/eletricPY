from ast import arg
from ssl import ALERT_DESCRIPTION_UNEXPECTED_MESSAGE
import tkinter as tk
from eletric_elements.Comodo import Square_comodo_in_dim as sqr_com
from eletric_elements.Lampada import Lampada
import eletric_elements.Tomada as Tomada
from eletric_elements.Fonte import Fonte
from Porta import Porta
from Janela import Janela
from eletric_elements.Interruptor import Interruptor_s1
from eletric_elements.Curva import Condutor
from util_.util import create_circle,get_widgets_values,save
from eletric_elements.BlankSpace import Space
from eletric_elements.Curva import Condutor

scale = 100

e   = None
eL  = None
eR  = None
eT  = None
eB  = None

horizontal_dim = None
vertical_dim = None

# Ponto inicial do comodo
x = None
y = None

grid = None
pc = None

current_project = 'Saving/projeto_1.json'


def create_comodo(canvas,pc):
    comodo = sqr_com(e=e*scale,horizotal_dim = horizontal_dim*scale, vertical_dim = vertical_dim*scale,
                        s_x = x, s_y = y, canvas=canvas,scale=scale,pc=pc)


    args = get_widgets_values(pc.popup.__dict__)

    save(comodo.codekey,args,False,filename = current_project)
    
    return comodo

def create_lamp(pc):

    args = get_widgets_values(pc.popup.__dict__)

    lampada = pc.current_obj.add_lamp(**args,pc=pc)


    if pc.popup.last == True:
        save(
            popupkey = "",
            elementkey = lampada.codekey,
            arguments = args,
            parent = pc.current_obj.codekey,
            filename = current_project)
    
    return lampada

def create_tom(pc):

    args = get_widgets_values(pc.popup.__dict__)

    tipo = args['tipo']
    lado = args['lado']

    if tipo == 'media': tipo = Tomada.Tomada_media
    if tipo == 'baixa': tipo = Tomada.Tomada_baixa
    if tipo == 'alta': tipo = Tomada.Tomada_alta

    args['amount'] = int(args['amount'])
    args['percent'] = args['percent']/100
    args['font_size'] = 8

    if lado == 'right':
        tomada = pc.current_obj.add_right_tug(tipo,**args)
    if lado == 'left':
        tomada = pc.current_obj.add_left_tug(tipo,**args)
    if lado == 'top':
        tomada = pc.current_obj.add_top_tug(tipo,**args)
    if lado == 'botton':
        tomada = pc.current_obj.add_botton_tug(tipo,**args)
    
    pc.popup_objects[pc.popup.id] = tomada

    if pc.popup.last == True:
        save(
            popupkey = pc.popup.id,
            elementkey = tomada.codekey,
            arguments = args,
            parent = pc.current_obj.codekey,
            filename = current_project)

    return tomada

def create_interr(pc):

    pop = pc.popup.__dict__

    interr = pc.current_obj.add_interruptor(wall    = pop['wall'].get()         ,
                                            inter   = pop['tipo'].get()         ,
                                            shift   = pop['dis'].get()          ,
                                            percent = pop['percent'].get()/100  ,
                                            radius  = pop['radius'].get()       ,
                                            label1  = pop['label1'].get()       ,
                                            label2  = pop['label2'].get()       ,
                                            label3  = pop['label3'].get()       ,
                                            pc = pc)
    
    if pc.popup.last == True:
        save(
            popupkey = pc.popup.id,
            elementkey = interr.codekey,
            arguments = get_widgets_values(pop),
            parent = pc.current_obj.codekey,
            filename = current_project)
    
    
    return interr

def create_space(pc):

    popdict = get_widgets_values(pc.popup.__dict__)
    
    comodo = pc.current_obj

    try: dis1 = float(popdict['dis1'])*scale
    except:
        popdict['dis1'] = 0.0

    try:dis2 = float(popdict['dis2'])*scale
    except:
        popdict['dis2'] = 0.0

    space = Space(
                    comodo=comodo,
                    wall= popdict['lado'],
                    dist1 = popdict['dis1'],
                    dist2 = popdict['dis2'],
                    pc=pc)

    
    if pc.popup.last == True:
        save(
            popupkey = pc.popup.id,
            elementkey = space.codekey,
            arguments = popdict,
            parent = pc.current_obj.codekey,
            filename = current_project)


    return space

def create_connection(pc):
    
    pop = get_widgets_values(pc.popup.__dict__)

    pop['A'] = pc.popup.__dict__['A']
    pop['B'] = pc.popup.__dict__['B']

    curva = abs(pop['curva']-100)
    
    orientation = 0

    if pop['curva']-100 <=0 :
        orientation = -1

    condutor = Condutor(pc,pop['A'],pop['B'],curve=curva,orientation= orientation)
    condutor.set_arm(pop['index'])

    return condutor

def create_door(canvas, pc, cd = 0.8, w = 0.3, side = "esquerdo", orientation = "fora", clock = "antihorário"):
    lados = {
        "direito": "R",
        "esquerdo": "L",
        "cima": "T",
        "baixo": "B"
    }
    orientacoes = {
        "fora": "O",
        "dentro": "I"
    }
    sentidos = {
        "antihorário": "A",
        "horário": "H"
    }
    if cd == "":
        cd = 0.8
    if w == "":
        w = 0.3
    porta = Porta(canvas, pc.current_obj, float(cd)*scale, float(w)*scale, lados.get(side), orientacoes.get(orientation), sentidos.get(clock), pc)
    return porta

def create_window(canvas, pc, side, dim):
    lados = {
        "direito": "R",
        "esquerdo": "L",
        "cima": "T",
        "baixo": "B"
    }
    if dim == "":
        dim = 1
    janela = Janela(canvas, pc.current_obj, float(dim)*scale , lados.get(side), pc)
    return janela