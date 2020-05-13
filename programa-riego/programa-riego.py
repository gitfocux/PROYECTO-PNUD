import tkinter as tk
from tkinter import messagebox
import json
import time
from gpiozero import LED
from gpiozero import Button
from time import sleep
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

maestra_01= LED(22)
maestra_01.on()
zona_01= LED(10)
zona_01.on()
zona_02= LED(9)
zona_02.on()
zona_03= LED(11)
zona_03.on()
zona_04= LED(5)
zona_04.on()

maestra_02= LED(6)
maestra_02.on()
zona_05= LED(13)
zona_05.on()
zona_06= LED(19)
zona_06.on()
zona_07= LED(26)
zona_07.on()
zona_08= LED(12)
zona_08.on()

electrobomba_01= LED(20)
electrobomba_01.on()
electrobomba_02= LED(21)
electrobomba_02.on()


ventana=tk.Tk()
#ventana.title("Sistema de riego")
#ventana.geometry('350x200')

ventana.bind("<Escape>",exit)
def exit():
    ventana.quit() 

ventana.attributes("-fullscreen",True)
#ventana.geometry('1280x720') #anchoxalto
ventana.configure(background="#000000")
#logo
image_1=tk.PhotoImage(file="/home/pi/Documents/riego/logo-negro.gif")
image_1=image_1.subsample(2,2)
label=tk.Label(ventana,image=image_1,bd=0)
label.grid(row=1, column=1, columnspan=2)
boton_zona=tk.Button(ventana,text ="ZONAS",fg = "#FFFFFF", bg="#04BF9D", font=("Helvetica",40),width=19,height=3)
boton_zona.grid(row=2,column=1,padx=20,pady=20)
boton_sensores=tk.Button(ventana,text="PROGRAMAR",fg = "#FFFFFF",bg="#04BF9D",font=("Helvetica",40),width=19,height=3)
boton_sensores.grid(row=2, column=2,padx=20,pady=20)
boton_estado=tk.Button(ventana,text ="PROGRAMAS",fg = "#FFFFFF", bg="#04BF9D", font=("Helvetica",40),width=19,height=3)
boton_estado.grid(row=3, column=1,padx=20,pady=20)
boton_configuracion=tk.Button(ventana,text ="MANUAL",fg ="#FFFFFF",bg="#04BF9D",font=("Helvetica",40),width=19,height=3)
boton_configuracion.grid(row=3, column=2,padx=20,pady=20)
ventana.config(cursor="none") #borrar cursor

with open('/home/pi/Documents/riego/programas_riego.json') as file:
    programas_riego=json.load(file)

encender = True
tiempo_pasado=0
tiempos_segundos=0

def times():
    global encender,tiempo_pasado,tiempos_segundos
    
    current_time=time.strftime("%d/%m/%Y %H:%M:%S")
    clock.config(text=current_time,fg = "#FFFFFF", bg="#000000", font=("Helvetica",24),width=19,height=1)
    
    with open('/home/pi/Documents/riego/programas_riego.json') as file:
        programas_riego=json.load(file)
    
    dia_now=time.strftime('%w')
    hora_now=time.strftime('%H')
    minutos_now=time.strftime('%M')
    segundos_now=time.strftime('%S')
    
    if dia_now=='0':
        #viernes_regar()
        print("domingo")
        if programas_riego["programa-01"]["dia"][6]=="D" and programas_riego["programa-01"]["hora"][0:2]==hora_now:
            print("lunes-programa-01")
            if programas_riego["programa-01"]["hora"][3:5]==minutos_now and encender==True:
                encender=False                
                if programas_riego["programa-01"]["zona"][0:2] == "01":
                    maestra_01.off()
                    zona_01.off()
                if programas_riego["programa-01"]["zona"][2:4] == "02":
                    maestra_01.off()
                    zona_02.off()
                if programas_riego["programa-01"]["zona"][4:6] == "03":
                    maestra_01.off()
                    zona_03.off()
                if programas_riego["programa-01"]["zona"][6:8] == "04":
                    maestra_01.off()
                    zona_04.off()
                if programas_riego["programa-01"]["zona"][8:10] == "05":
                    maestra_02.off()
                    zona_05.off()
                if programas_riego["programa-01"]["zona"][10:12] == "06":
                    maestra_02.off()
                    zona_06.off()
                if programas_riego["programa-01"]["zona"][12:14] == "07":
                    maestra_02.off()
                    zona_07.off()
                if programas_riego["programa-01"]["zona"][8:10] == "08":
                    maestra_02.off()
                    zona_08.off()
                if programas_riego["programa-01"]["bomba"][0:2] == "01":
                    electrobomba_01.off()
                if programas_riego["programa-01"]["bomba"][2:4] == "04":
                    electrobomba_02.off()
                    
                tiempo_pasado= int(minutos_now)+ int(programas_riego["programa-01"]["tiempo"])
                tiempos_segundos = int(segundos_now)
                #print("regar")
            elif tiempo_pasado==int(minutos_now) and int(segundos_now)>=tiempos_segundos and encender==False:
                encender=True
                maestra_01.on()
                zona_01.on()
                zona_02.on()
                zona_03.on()
                zona_04.on()
                zona_05.on()
                zona_06.on()
                zona_07.on()
                zona_08.on()
                electrobomba_01.on()
                electrobomba_02.on()
                
        elif programas_riego["programa-02"]["dia"][6]=="D" and programas_riego["programa-02"]["hora"][0:2]==hora_now:
            print("lunes-programa-02")
            if programas_riego["programa-02"]["hora"][3:5]==minutos_now and encender==True:
                encender=False                
                if programas_riego["programa-02"]["zona"][0:2] == "01":
                    maestra_01.off()
                    zona_01.off()
                if programas_riego["programa-02"]["zona"][2:4] == "02":
                    maestra_01.off()
                    zona_02.off()
                if programas_riego["programa-02"]["zona"][4:6] == "03":
                    maestra_01.off()
                    zona_03.off()
                if programas_riego["programa-02"]["zona"][6:8] == "04":
                    maestra_01.off()
                    zona_04.off()
                if programas_riego["programa-02"]["zona"][8:10] == "05":
                    maestra_02.off()
                    zona_05.off()
                if programas_riego["programa-02"]["zona"][10:12] == "06":
                    maestra_02.off()
                    zona_06.off()
                if programas_riego["programa-02"]["zona"][12:14] == "07":
                    maestra_02.off()
                    zona_07.off()
                if programas_riego["programa-02"]["zona"][8:10] == "08":
                    maestra_02.off()
                    zona_08.off()
                if programas_riego["programa-02"]["bomba"][0:2] == "01":
                    electrobomba_01.off()
                if programas_riego["programa-02"]["bomba"][2:4] == "04":
                    electrobomba_02.off()
                    
                tiempo_pasado= int(minutos_now)+ int(programas_riego["programa-02"]["tiempo"])
                tiempos_segundos = int(segundos_now)
                #print("regar")
            elif tiempo_pasado==int(minutos_now) and int(segundos_now)>=tiempos_segundos and encender==False:
                encender=True
                maestra_01.on()
                zona_01.on()
                zona_02.on()
                zona_03.on()
                zona_04.on()
                zona_05.on()
                zona_06.on()
                zona_07.on()
                zona_08.on()
                electrobomba_01.on()
                electrobomba_02.on()
                
        elif programas_riego["programa-03"]["dia"][6]=="D" and programas_riego["programa-03"]["hora"][0:2]==hora_now:
            print("lunes-programa-03")
            if programas_riego["programa-03"]["hora"][3:5]==minutos_now and encender==True:
                encender=False                
                if programas_riego["programa-03"]["zona"][0:2] == "01":
                    maestra_01.off()
                    zona_01.off()
                if programas_riego["programa-03"]["zona"][2:4] == "02":
                    maestra_01.off()
                    zona_02.off()
                if programas_riego["programa-03"]["zona"][4:6] == "03":
                    maestra_01.off()
                    zona_03.off()
                if programas_riego["programa-03"]["zona"][6:8] == "04":
                    maestra_01.off()
                    zona_04.off()
                if programas_riego["programa-03"]["zona"][8:10] == "05":
                    maestra_02.off()
                    zona_05.off()
                if programas_riego["programa-03"]["zona"][10:12] == "06":
                    maestra_02.off()
                    zona_06.off()
                if programas_riego["programa-03"]["zona"][12:14] == "07":
                    maestra_02.off()
                    zona_07.off()
                if programas_riego["programa-03"]["zona"][8:10] == "08":
                    maestra_02.off()
                    zona_08.off()
                if programas_riego["programa-03"]["bomba"][0:2] == "01":
                    electrobomba_01.off()
                if programas_riego["programa-03"]["bomba"][2:4] == "02":
                    electrobomba_02.off()
                    
                tiempo_pasado= int(minutos_now)+ int(programas_riego["programa-03"]["tiempo"])
                tiempos_segundos = int(segundos_now)
                #print("regar")
            elif tiempo_pasado==int(minutos_now) and int(segundos_now)>=tiempos_segundos and encender==False:
                encender=True
                maestra_01.on()
                zona_01.on()
                zona_02.on()
                zona_03.on()
                zona_04.on()
                zona_05.on()
                zona_06.on()
                zona_07.on()
                zona_08.on()
                electrobomba_01.on()
                electrobomba_02.on()
    
    
    
    elif dia_now=='1':
        #viernes_regar()
        print("lunes")
        if programas_riego["programa-01"]["dia"][0]=="L" and programas_riego["programa-01"]["hora"][0:2]==hora_now:
            print("lunes-programa-01")
            if programas_riego["programa-01"]["hora"][3:5]==minutos_now and encender==True:
                encender=False                
                if programas_riego["programa-01"]["zona"][0:2] == "01":
                    maestra_01.off()
                    zona_01.off()
                if programas_riego["programa-01"]["zona"][2:4] == "02":
                    maestra_01.off()
                    zona_02.off()
                if programas_riego["programa-01"]["zona"][4:6] == "03":
                    maestra_01.off()
                    zona_03.off()
                if programas_riego["programa-01"]["zona"][6:8] == "04":
                    maestra_01.off()
                    zona_04.off()
                if programas_riego["programa-01"]["zona"][8:10] == "05":
                    maestra_02.off()
                    zona_05.off()
                if programas_riego["programa-01"]["zona"][10:12] == "06":
                    maestra_02.off()
                    zona_06.off()
                if programas_riego["programa-01"]["zona"][12:14] == "07":
                    maestra_02.off()
                    zona_07.off()
                if programas_riego["programa-01"]["zona"][8:10] == "08":
                    maestra_02.off()
                    zona_08.off()
                if programas_riego["programa-01"]["bomba"][0:2] == "01":
                    electrobomba_01.off()
                if programas_riego["programa-01"]["bomba"][2:4] == "04":
                    electrobomba_02.off()
                    
                tiempo_pasado= int(minutos_now)+ int(programas_riego["programa-01"]["tiempo"])
                tiempos_segundos = int(segundos_now)
                #print("regar")
            elif tiempo_pasado==int(minutos_now) and int(segundos_now)>=tiempos_segundos and encender==False:
                encender=True
                maestra_01.on()
                zona_01.on()
                zona_02.on()
                zona_03.on()
                zona_04.on()
                zona_05.on()
                zona_06.on()
                zona_07.on()
                zona_08.on()
                electrobomba_01.on()
                electrobomba_02.on()
                
        elif programas_riego["programa-02"]["dia"][0]=="L" and programas_riego["programa-02"]["hora"][0:2]==hora_now:
            print("lunes-programa-02")
            if programas_riego["programa-02"]["hora"][3:5]==minutos_now and encender==True:
                encender=False                
                if programas_riego["programa-02"]["zona"][0:2] == "01":
                    maestra_01.off()
                    zona_01.off()
                if programas_riego["programa-02"]["zona"][2:4] == "02":
                    maestra_01.off()
                    zona_02.off()
                if programas_riego["programa-02"]["zona"][4:6] == "03":
                    maestra_01.off()
                    zona_03.off()
                if programas_riego["programa-02"]["zona"][6:8] == "04":
                    maestra_01.off()
                    zona_04.off()
                if programas_riego["programa-02"]["zona"][8:10] == "05":
                    maestra_02.off()
                    zona_05.off()
                if programas_riego["programa-02"]["zona"][10:12] == "06":
                    maestra_02.off()
                    zona_06.off()
                if programas_riego["programa-02"]["zona"][12:14] == "07":
                    maestra_02.off()
                    zona_07.off()
                if programas_riego["programa-02"]["zona"][8:10] == "08":
                    maestra_02.off()
                    zona_08.off()
                if programas_riego["programa-02"]["bomba"][0:2] == "01":
                    electrobomba_01.off()
                if programas_riego["programa-02"]["bomba"][2:4] == "04":
                    electrobomba_02.off()
                    
                tiempo_pasado= int(minutos_now)+ int(programas_riego["programa-02"]["tiempo"])
                tiempos_segundos = int(segundos_now)
                #print("regar")
            elif tiempo_pasado==int(minutos_now) and int(segundos_now)>=tiempos_segundos and encender==False:
                encender=True
                maestra_01.on()
                zona_01.on()
                zona_02.on()
                zona_03.on()
                zona_04.on()
                zona_05.on()
                zona_06.on()
                zona_07.on()
                zona_08.on()
                electrobomba_01.on()
                electrobomba_02.on()
                
        elif programas_riego["programa-03"]["dia"][0]=="L" and programas_riego["programa-03"]["hora"][0:2]==hora_now:
            print("lunes-programa-03")
            if programas_riego["programa-03"]["hora"][3:5]==minutos_now and encender==True:
                encender=False                
                if programas_riego["programa-03"]["zona"][0:2] == "01":
                    maestra_01.off()
                    zona_01.off()
                if programas_riego["programa-03"]["zona"][2:4] == "02":
                    maestra_01.off()
                    zona_02.off()
                if programas_riego["programa-03"]["zona"][4:6] == "03":
                    maestra_01.off()
                    zona_03.off()
                if programas_riego["programa-03"]["zona"][6:8] == "04":
                    maestra_01.off()
                    zona_04.off()
                if programas_riego["programa-03"]["zona"][8:10] == "05":
                    maestra_02.off()
                    zona_05.off()
                if programas_riego["programa-03"]["zona"][10:12] == "06":
                    maestra_02.off()
                    zona_06.off()
                if programas_riego["programa-03"]["zona"][12:14] == "07":
                    maestra_02.off()
                    zona_07.off()
                if programas_riego["programa-03"]["zona"][8:10] == "08":
                    maestra_02.off()
                    zona_08.off()
                if programas_riego["programa-03"]["bomba"][0:2] == "01":
                    electrobomba_01.off()
                if programas_riego["programa-03"]["bomba"][2:4] == "02":
                    electrobomba_02.off()
                    
                tiempo_pasado= int(minutos_now)+ int(programas_riego["programa-03"]["tiempo"])
                tiempos_segundos = int(segundos_now)
                #print("regar")
            elif tiempo_pasado==int(minutos_now) and int(segundos_now)>=tiempos_segundos and encender==False:
                encender=True
                maestra_01.on()
                zona_01.on()
                zona_02.on()
                zona_03.on()
                zona_04.on()
                zona_05.on()
                zona_06.on()
                zona_07.on()
                zona_08.on()
                electrobomba_01.on()
                electrobomba_02.on()
                
    elif dia_now=='2':
        #viernes_regar()
        print("martes")
        if programas_riego["programa-01"]["dia"][1]=="M" and programas_riego["programa-01"]["hora"][0:2]==hora_now:
            print("lunes-programa-01")
            if programas_riego["programa-01"]["hora"][3:5]==minutos_now and encender==True:
                encender=False                
                if programas_riego["programa-01"]["zona"][0:2] == "01":
                    maestra_01.off()
                    zona_01.off()
                if programas_riego["programa-01"]["zona"][2:4] == "02":
                    maestra_01.off()
                    zona_02.off()
                if programas_riego["programa-01"]["zona"][4:6] == "03":
                    maestra_01.off()
                    zona_03.off()
                if programas_riego["programa-01"]["zona"][6:8] == "04":
                    maestra_01.off()
                    zona_04.off()
                if programas_riego["programa-01"]["zona"][8:10] == "05":
                    maestra_02.off()
                    zona_05.off()
                if programas_riego["programa-01"]["zona"][10:12] == "06":
                    maestra_02.off()
                    zona_06.off()
                if programas_riego["programa-01"]["zona"][12:14] == "07":
                    maestra_02.off()
                    zona_07.off()
                if programas_riego["programa-01"]["zona"][8:10] == "08":
                    maestra_02.off()
                    zona_08.off()
                if programas_riego["programa-01"]["bomba"][0:2] == "01":
                    electrobomba_01.off()
                if programas_riego["programa-01"]["bomba"][2:4] == "04":
                    electrobomba_02.off()
                    
                tiempo_pasado= int(minutos_now)+ int(programas_riego["programa-01"]["tiempo"])
                tiempos_segundos = int(segundos_now)
                #print("regar")
            elif tiempo_pasado==int(minutos_now) and int(segundos_now)>=tiempos_segundos and encender==False:
                encender=True
                maestra_01.on()
                zona_01.on()
                zona_02.on()
                zona_03.on()
                zona_04.on()
                zona_05.on()
                zona_06.on()
                zona_07.on()
                zona_08.on()
                electrobomba_01.on()
                electrobomba_02.on()
                
        elif programas_riego["programa-02"]["dia"][1]=="M" and programas_riego["programa-02"]["hora"][0:2]==hora_now:
            print("lunes-programa-02")
            if programas_riego["programa-02"]["hora"][3:5]==minutos_now and encender==True:
                encender=False                
                if programas_riego["programa-02"]["zona"][0:2] == "01":
                    maestra_01.off()
                    zona_01.off()
                if programas_riego["programa-02"]["zona"][2:4] == "02":
                    maestra_01.off()
                    zona_02.off()
                if programas_riego["programa-02"]["zona"][4:6] == "03":
                    maestra_01.off()
                    zona_03.off()
                if programas_riego["programa-02"]["zona"][6:8] == "04":
                    maestra_01.off()
                    zona_04.off()
                if programas_riego["programa-02"]["zona"][8:10] == "05":
                    maestra_02.off()
                    zona_05.off()
                if programas_riego["programa-02"]["zona"][10:12] == "06":
                    maestra_02.off()
                    zona_06.off()
                if programas_riego["programa-02"]["zona"][12:14] == "07":
                    maestra_02.off()
                    zona_07.off()
                if programas_riego["programa-02"]["zona"][8:10] == "08":
                    maestra_02.off()
                    zona_08.off()
                if programas_riego["programa-02"]["bomba"][0:2] == "01":
                    electrobomba_01.off()
                if programas_riego["programa-02"]["bomba"][2:4] == "04":
                    electrobomba_02.off()
                    
                tiempo_pasado= int(minutos_now)+ int(programas_riego["programa-02"]["tiempo"])
                tiempos_segundos = int(segundos_now)
                #print("regar")
            elif tiempo_pasado==int(minutos_now) and int(segundos_now)>=tiempos_segundos and encender==False:
                encender=True
                maestra_01.on()
                zona_01.on()
                zona_02.on()
                zona_03.on()
                zona_04.on()
                zona_05.on()
                zona_06.on()
                zona_07.on()
                zona_08.on()
                electrobomba_01.on()
                electrobomba_02.on()
                
        elif programas_riego["programa-03"]["dia"][1]=="M" and programas_riego["programa-03"]["hora"][0:2]==hora_now:
            print("lunes-programa-03")
            if programas_riego["programa-03"]["hora"][3:5]==minutos_now and encender==True:
                encender=False                
                if programas_riego["programa-03"]["zona"][0:2] == "01":
                    maestra_01.off()
                    zona_01.off()
                if programas_riego["programa-03"]["zona"][2:4] == "02":
                    maestra_01.off()
                    zona_02.off()
                if programas_riego["programa-03"]["zona"][4:6] == "03":
                    maestra_01.off()
                    zona_03.off()
                if programas_riego["programa-03"]["zona"][6:8] == "04":
                    maestra_01.off()
                    zona_04.off()
                if programas_riego["programa-03"]["zona"][8:10] == "05":
                    maestra_02.off()
                    zona_05.off()
                if programas_riego["programa-03"]["zona"][10:12] == "06":
                    maestra_02.off()
                    zona_06.off()
                if programas_riego["programa-03"]["zona"][12:14] == "07":
                    maestra_02.off()
                    zona_07.off()
                if programas_riego["programa-03"]["zona"][8:10] == "08":
                    maestra_02.off()
                    zona_08.off()
                if programas_riego["programa-03"]["bomba"][0:2] == "01":
                    electrobomba_01.off()
                if programas_riego["programa-03"]["bomba"][2:4] == "02":
                    electrobomba_02.off()
                    
                tiempo_pasado= int(minutos_now)+ int(programas_riego["programa-03"]["tiempo"])
                tiempos_segundos = int(segundos_now)
                #print("regar")
            elif tiempo_pasado==int(minutos_now) and int(segundos_now)>=tiempos_segundos and encender==False:
                encender=True
                maestra_01.on()
                zona_01.on()
                zona_02.on()
                zona_03.on()
                zona_04.on()
                zona_05.on()
                zona_06.on()
                zona_07.on()
                zona_08.on()
                electrobomba_01.on()
                electrobomba_02.on()
                
    elif dia_now=='3':
        #viernes_regar()
        print("miercoles")
        if programas_riego["programa-01"]["dia"][2]=="M" and programas_riego["programa-01"]["hora"][0:2]==hora_now:
            print("lunes-programa-01")
            if programas_riego["programa-01"]["hora"][3:5]==minutos_now and encender==True:
                encender=False                
                if programas_riego["programa-01"]["zona"][0:2] == "01":
                    maestra_01.off()
                    zona_01.off()
                if programas_riego["programa-01"]["zona"][2:4] == "02":
                    maestra_01.off()
                    zona_02.off()
                if programas_riego["programa-01"]["zona"][4:6] == "03":
                    maestra_01.off()
                    zona_03.off()
                if programas_riego["programa-01"]["zona"][6:8] == "04":
                    maestra_01.off()
                    zona_04.off()
                if programas_riego["programa-01"]["zona"][8:10] == "05":
                    maestra_02.off()
                    zona_05.off()
                if programas_riego["programa-01"]["zona"][10:12] == "06":
                    maestra_02.off()
                    zona_06.off()
                if programas_riego["programa-01"]["zona"][12:14] == "07":
                    maestra_02.off()
                    zona_07.off()
                if programas_riego["programa-01"]["zona"][8:10] == "08":
                    maestra_02.off()
                    zona_08.off()
                if programas_riego["programa-01"]["bomba"][0:2] == "01":
                    electrobomba_01.off()
                if programas_riego["programa-01"]["bomba"][2:4] == "04":
                    electrobomba_02.off()
                    
                tiempo_pasado= int(minutos_now)+ int(programas_riego["programa-01"]["tiempo"])
                tiempos_segundos = int(segundos_now)
                #print("regar")
            elif tiempo_pasado==int(minutos_now) and int(segundos_now)>=tiempos_segundos and encender==False:
                encender=True
                maestra_01.on()
                zona_01.on()
                zona_02.on()
                zona_03.on()
                zona_04.on()
                zona_05.on()
                zona_06.on()
                zona_07.on()
                zona_08.on()
                electrobomba_01.on()
                electrobomba_02.on()
                
        elif programas_riego["programa-02"]["dia"][2]=="M" and programas_riego["programa-02"]["hora"][0:2]==hora_now:
            print("lunes-programa-02")
            if programas_riego["programa-02"]["hora"][3:5]==minutos_now and encender==True:
                encender=False                
                if programas_riego["programa-02"]["zona"][0:2] == "01":
                    maestra_01.off()
                    zona_01.off()
                if programas_riego["programa-02"]["zona"][2:4] == "02":
                    maestra_01.off()
                    zona_02.off()
                if programas_riego["programa-02"]["zona"][4:6] == "03":
                    maestra_01.off()
                    zona_03.off()
                if programas_riego["programa-02"]["zona"][6:8] == "04":
                    maestra_01.off()
                    zona_04.off()
                if programas_riego["programa-02"]["zona"][8:10] == "05":
                    maestra_02.off()
                    zona_05.off()
                if programas_riego["programa-02"]["zona"][10:12] == "06":
                    maestra_02.off()
                    zona_06.off()
                if programas_riego["programa-02"]["zona"][12:14] == "07":
                    maestra_02.off()
                    zona_07.off()
                if programas_riego["programa-02"]["zona"][8:10] == "08":
                    maestra_02.off()
                    zona_08.off()
                if programas_riego["programa-02"]["bomba"][0:2] == "01":
                    electrobomba_01.off()
                if programas_riego["programa-02"]["bomba"][2:4] == "04":
                    electrobomba_02.off()
                    
                tiempo_pasado= int(minutos_now)+ int(programas_riego["programa-02"]["tiempo"])
                tiempos_segundos = int(segundos_now)
                #print("regar")
            elif tiempo_pasado==int(minutos_now) and int(segundos_now)>=tiempos_segundos and encender==False:
                encender=True
                maestra_01.on()
                zona_01.on()
                zona_02.on()
                zona_03.on()
                zona_04.on()
                zona_05.on()
                zona_06.on()
                zona_07.on()
                zona_08.on()
                electrobomba_01.on()
                electrobomba_02.on()
                
        elif programas_riego["programa-03"]["dia"][2]=="M" and programas_riego["programa-03"]["hora"][0:2]==hora_now:
            print("lunes-programa-03")
            if programas_riego["programa-03"]["hora"][3:5]==minutos_now and encender==True:
                encender=False                
                if programas_riego["programa-03"]["zona"][0:2] == "01":
                    maestra_01.off()
                    zona_01.off()
                if programas_riego["programa-03"]["zona"][2:4] == "02":
                    maestra_01.off()
                    zona_02.off()
                if programas_riego["programa-03"]["zona"][4:6] == "03":
                    maestra_01.off()
                    zona_03.off()
                if programas_riego["programa-03"]["zona"][6:8] == "04":
                    maestra_01.off()
                    zona_04.off()
                if programas_riego["programa-03"]["zona"][8:10] == "05":
                    maestra_02.off()
                    zona_05.off()
                if programas_riego["programa-03"]["zona"][10:12] == "06":
                    maestra_02.off()
                    zona_06.off()
                if programas_riego["programa-03"]["zona"][12:14] == "07":
                    maestra_02.off()
                    zona_07.off()
                if programas_riego["programa-03"]["zona"][8:10] == "08":
                    maestra_02.off()
                    zona_08.off()
                if programas_riego["programa-03"]["bomba"][0:2] == "01":
                    electrobomba_01.off()
                if programas_riego["programa-03"]["bomba"][2:4] == "02":
                    electrobomba_02.off()
                    
                tiempo_pasado= int(minutos_now)+ int(programas_riego["programa-03"]["tiempo"])
                tiempos_segundos = int(segundos_now)
                #print("regar")
            elif tiempo_pasado==int(minutos_now) and int(segundos_now)>=tiempos_segundos and encender==False:
                encender=True
                maestra_01.on()
                zona_01.on()
                zona_02.on()
                zona_03.on()
                zona_04.on()
                zona_05.on()
                zona_06.on()
                zona_07.on()
                zona_08.on()
                electrobomba_01.on()
                electrobomba_02.on()
                
                
    elif dia_now=='4':
        #viernes_regar()
        print("jueves")
        if programas_riego["programa-01"]["dia"][3]=="J" and programas_riego["programa-01"]["hora"][0:2]==hora_now:
            print("lunes-programa-01")
            if programas_riego["programa-01"]["hora"][3:5]==minutos_now and encender==True:
                encender=False                
                if programas_riego["programa-01"]["zona"][0:2] == "01":
                    maestra_01.off()
                    zona_01.off()
                if programas_riego["programa-01"]["zona"][2:4] == "02":
                    maestra_01.off()
                    zona_02.off()
                if programas_riego["programa-01"]["zona"][4:6] == "03":
                    maestra_01.off()
                    zona_03.off()
                if programas_riego["programa-01"]["zona"][6:8] == "04":
                    maestra_01.off()
                    zona_04.off()
                if programas_riego["programa-01"]["zona"][8:10] == "05":
                    maestra_02.off()
                    zona_05.off()
                if programas_riego["programa-01"]["zona"][10:12] == "06":
                    maestra_02.off()
                    zona_06.off()
                if programas_riego["programa-01"]["zona"][12:14] == "07":
                    maestra_02.off()
                    zona_07.off()
                if programas_riego["programa-01"]["zona"][8:10] == "08":
                    maestra_02.off()
                    zona_08.off()
                if programas_riego["programa-01"]["bomba"][0:2] == "01":
                    electrobomba_01.off()
                if programas_riego["programa-01"]["bomba"][2:4] == "04":
                    electrobomba_02.off()
                    
                tiempo_pasado= int(minutos_now)+ int(programas_riego["programa-01"]["tiempo"])
                tiempos_segundos = int(segundos_now)
                #print("regar")
            elif tiempo_pasado==int(minutos_now) and int(segundos_now)>=tiempos_segundos and encender==False:
                encender=True
                maestra_01.on()
                zona_01.on()
                zona_02.on()
                zona_03.on()
                zona_04.on()
                zona_05.on()
                zona_06.on()
                zona_07.on()
                zona_08.on()
                electrobomba_01.on()
                electrobomba_02.on()
                
        elif programas_riego["programa-02"]["dia"][3]=="J" and programas_riego["programa-02"]["hora"][0:2]==hora_now:
            print("lunes-programa-02")
            if programas_riego["programa-02"]["hora"][3:5]==minutos_now and encender==True:
                encender=False                
                if programas_riego["programa-02"]["zona"][0:2] == "01":
                    maestra_01.off()
                    zona_01.off()
                if programas_riego["programa-02"]["zona"][2:4] == "02":
                    maestra_01.off()
                    zona_02.off()
                if programas_riego["programa-02"]["zona"][4:6] == "03":
                    maestra_01.off()
                    zona_03.off()
                if programas_riego["programa-02"]["zona"][6:8] == "04":
                    maestra_01.off()
                    zona_04.off()
                if programas_riego["programa-02"]["zona"][8:10] == "05":
                    maestra_02.off()
                    zona_05.off()
                if programas_riego["programa-02"]["zona"][10:12] == "06":
                    maestra_02.off()
                    zona_06.off()
                if programas_riego["programa-02"]["zona"][12:14] == "07":
                    maestra_02.off()
                    zona_07.off()
                if programas_riego["programa-02"]["zona"][8:10] == "08":
                    maestra_02.off()
                    zona_08.off()
                if programas_riego["programa-02"]["bomba"][0:2] == "01":
                    electrobomba_01.off()
                if programas_riego["programa-02"]["bomba"][2:4] == "04":
                    electrobomba_02.off()
                    
                tiempo_pasado= int(minutos_now)+ int(programas_riego["programa-03"]["tiempo"])
                tiempos_segundos = int(segundos_now)
                #print("regar")
            elif tiempo_pasado==int(minutos_now) and int(segundos_now)>=tiempos_segundos and encender==False:
                encender=True
                maestra_01.on()
                zona_01.on()
                zona_02.on()
                zona_03.on()
                zona_04.on()
                zona_05.on()
                zona_06.on()
                zona_07.on()
                zona_08.on()
                electrobomba_01.on()
                electrobomba_02.on()
                
        elif programas_riego["programa-03"]["dia"][3]=="J" and programas_riego["programa-03"]["hora"][0:2]==hora_now:
            print("lunes-programa-03")
            if programas_riego["programa-03"]["hora"][3:5]==minutos_now and encender==True:
                encender=False                
                if programas_riego["programa-03"]["zona"][0:2] == "01":
                    maestra_01.off()
                    zona_01.off()
                if programas_riego["programa-03"]["zona"][2:4] == "02":
                    maestra_01.off()
                    zona_02.off()
                if programas_riego["programa-03"]["zona"][4:6] == "03":
                    maestra_01.off()
                    zona_03.off()
                if programas_riego["programa-03"]["zona"][6:8] == "04":
                    maestra_01.off()
                    zona_04.off()
                if programas_riego["programa-03"]["zona"][8:10] == "05":
                    maestra_02.off()
                    zona_05.off()
                if programas_riego["programa-03"]["zona"][10:12] == "06":
                    maestra_02.off()
                    zona_06.off()
                if programas_riego["programa-03"]["zona"][12:14] == "07":
                    maestra_02.off()
                    zona_07.off()
                if programas_riego["programa-03"]["zona"][8:10] == "08":
                    maestra_02.off()
                    zona_08.off()
                if programas_riego["programa-03"]["bomba"][0:2] == "01":
                    electrobomba_01.off()
                if programas_riego["programa-03"]["bomba"][2:4] == "02":
                    electrobomba_02.off()
                    
                tiempo_pasado= int(minutos_now)+ int(programas_riego["programa-03"]["tiempo"])
                tiempos_segundos = int(segundos_now)
                #print("regar")
            elif tiempo_pasado==int(minutos_now) and int(segundos_now)>=tiempos_segundos and encender==False:
                encender=True
                maestra_01.on()
                zona_01.on()
                zona_02.on()
                zona_03.on()
                zona_04.on()
                zona_05.on()
                zona_06.on()
                zona_07.on()
                zona_08.on()
                electrobomba_01.on()
                electrobomba_02.on()
                
    elif dia_now=='5':
        #viernes_regar()
        print("viernes")
        if programas_riego["programa-01"]["dia"][4]=="J" and programas_riego["programa-01"]["hora"][0:2]==hora_now:
            print("lunes-programa-01")
            if programas_riego["programa-01"]["hora"][3:5]==minutos_now and encender==True:
                encender=False                
                if programas_riego["programa-01"]["zona"][0:2] == "01":
                    maestra_01.off()
                    zona_01.off()
                if programas_riego["programa-01"]["zona"][2:4] == "02":
                    maestra_01.off()
                    zona_02.off()
                if programas_riego["programa-01"]["zona"][4:6] == "03":
                    maestra_01.off()
                    zona_03.off()
                if programas_riego["programa-01"]["zona"][6:8] == "04":
                    maestra_01.off()
                    zona_04.off()
                if programas_riego["programa-01"]["zona"][8:10] == "05":
                    maestra_02.off()
                    zona_05.off()
                if programas_riego["programa-01"]["zona"][10:12] == "06":
                    maestra_02.off()
                    zona_06.off()
                if programas_riego["programa-01"]["zona"][12:14] == "07":
                    maestra_02.off()
                    zona_07.off()
                if programas_riego["programa-01"]["zona"][8:10] == "08":
                    maestra_02.off()
                    zona_08.off()
                if programas_riego["programa-01"]["bomba"][0:2] == "01":
                    electrobomba_01.off()
                if programas_riego["programa-01"]["bomba"][2:4] == "04":
                    electrobomba_02.off()
                    
                tiempo_pasado= int(minutos_now)+ int(programas_riego["programa-01"]["tiempo"])
                tiempos_segundos = int(segundos_now)
                #print("regar")
            elif tiempo_pasado==int(minutos_now) and int(segundos_now)>=tiempos_segundos and encender==False:
                encender=True
                maestra_01.on()
                zona_01.on()
                zona_02.on()
                zona_03.on()
                zona_04.on()
                zona_05.on()
                zona_06.on()
                zona_07.on()
                zona_08.on()
                electrobomba_01.on()
                electrobomba_02.on()
                
        elif programas_riego["programa-02"]["dia"][4]=="J" and programas_riego["programa-02"]["hora"][0:2]==hora_now:
            print("lunes-programa-02")
            if programas_riego["programa-02"]["hora"][3:5]==minutos_now and encender==True:
                encender=False                
                if programas_riego["programa-02"]["zona"][0:2] == "01":
                    maestra_01.off()
                    zona_01.off()
                if programas_riego["programa-02"]["zona"][2:4] == "02":
                    maestra_01.off()
                    zona_02.off()
                if programas_riego["programa-02"]["zona"][4:6] == "03":
                    maestra_01.off()
                    zona_03.off()
                if programas_riego["programa-02"]["zona"][6:8] == "04":
                    maestra_01.off()
                    zona_04.off()
                if programas_riego["programa-02"]["zona"][8:10] == "05":
                    maestra_02.off()
                    zona_05.off()
                if programas_riego["programa-02"]["zona"][10:12] == "06":
                    maestra_02.off()
                    zona_06.off()
                if programas_riego["programa-02"]["zona"][12:14] == "07":
                    maestra_02.off()
                    zona_07.off()
                if programas_riego["programa-02"]["zona"][8:10] == "08":
                    maestra_02.off()
                    zona_08.off()
                if programas_riego["programa-02"]["bomba"][0:2] == "01":
                    electrobomba_01.off()
                if programas_riego["programa-02"]["bomba"][2:4] == "04":
                    electrobomba_02.off()
                    
                tiempo_pasado= int(minutos_now)+ int(programas_riego["programa-02"]["tiempo"])
                tiempos_segundos = int(segundos_now)
                #print("regar")
            elif tiempo_pasado==int(minutos_now) and int(segundos_now)>=tiempos_segundos and encender==False:
                encender=True
                maestra_01.on()
                zona_01.on()
                zona_02.on()
                zona_03.on()
                zona_04.on()
                zona_05.on()
                zona_06.on()
                zona_07.on()
                zona_08.on()
                electrobomba_01.on()
                electrobomba_02.on()
                
        elif programas_riego["programa-03"]["dia"][4]=="J" and programas_riego["programa-03"]["hora"][0:2]==hora_now:
            print("lunes-programa-03")
            if programas_riego["programa-03"]["hora"][3:5]==minutos_now and encender==True:
                encender=False                
                if programas_riego["programa-03"]["zona"][0:2] == "01":
                    maestra_01.off()
                    zona_01.off()
                if programas_riego["programa-03"]["zona"][2:4] == "02":
                    maestra_01.off()
                    zona_02.off()
                if programas_riego["programa-03"]["zona"][4:6] == "03":
                    maestra_01.off()
                    zona_03.off()
                if programas_riego["programa-03"]["zona"][6:8] == "04":
                    maestra_01.off()
                    zona_04.off()
                if programas_riego["programa-03"]["zona"][8:10] == "05":
                    maestra_02.off()
                    zona_05.off()
                if programas_riego["programa-03"]["zona"][10:12] == "06":
                    maestra_02.off()
                    zona_06.off()
                if programas_riego["programa-03"]["zona"][12:14] == "07":
                    maestra_02.off()
                    zona_07.off()
                if programas_riego["programa-03"]["zona"][8:10] == "08":
                    maestra_02.off()
                    zona_08.off()
                if programas_riego["programa-03"]["bomba"][0:2] == "01":
                    electrobomba_01.off()
                if programas_riego["programa-03"]["bomba"][2:4] == "02":
                    electrobomba_02.off()
                    
                tiempo_pasado= int(minutos_now)+ int(programas_riego["programa-03"]["tiempo"])
                tiempos_segundos = int(segundos_now)
                #print("regar")
            elif tiempo_pasado==int(minutos_now) and int(segundos_now)>=tiempos_segundos and encender==False:
                encender=True
                maestra_01.on()
                zona_01.on()
                zona_02.on()
                zona_03.on()
                zona_04.on()
                zona_05.on()
                zona_06.on()
                zona_07.on()
                zona_08.on()
                electrobomba_01.on()
                electrobomba_02.on()
                
    elif dia_now=='5':
        #viernes_regar()
        print("viernes")
        if programas_riego["programa-01"]["dia"][4]=="V" and programas_riego["programa-01"]["hora"][0:2]==hora_now:
            print("lunes-programa-01")
            if programas_riego["programa-01"]["hora"][3:5]==minutos_now and encender==True:
                encender=False                
                if programas_riego["programa-01"]["zona"][0:2] == "01":
                    maestra_01.off()
                    zona_01.off()
                if programas_riego["programa-01"]["zona"][2:4] == "02":
                    maestra_01.off()
                    zona_02.off()
                if programas_riego["programa-01"]["zona"][4:6] == "03":
                    maestra_01.off()
                    zona_03.off()
                if programas_riego["programa-01"]["zona"][6:8] == "04":
                    maestra_01.off()
                    zona_04.off()
                if programas_riego["programa-01"]["zona"][8:10] == "05":
                    maestra_02.off()
                    zona_05.off()
                if programas_riego["programa-01"]["zona"][10:12] == "06":
                    maestra_02.off()
                    zona_06.off()
                if programas_riego["programa-01"]["zona"][12:14] == "07":
                    maestra_02.off()
                    zona_07.off()
                if programas_riego["programa-01"]["zona"][8:10] == "08":
                    maestra_02.off()
                    zona_08.off()
                if programas_riego["programa-01"]["bomba"][0:2] == "01":
                    electrobomba_01.off()
                if programas_riego["programa-01"]["bomba"][2:4] == "04":
                    electrobomba_02.off()
                    
                tiempo_pasado= int(minutos_now)+ int(programas_riego["programa-01"]["tiempo"])
                tiempos_segundos = int(segundos_now)
                #print("regar")
            elif tiempo_pasado==int(minutos_now) and int(segundos_now)>=tiempos_segundos and encender==False:
                encender=True
                maestra_01.on()
                zona_01.on()
                zona_02.on()
                zona_03.on()
                zona_04.on()
                zona_05.on()
                zona_06.on()
                zona_07.on()
                zona_08.on()
                electrobomba_01.on()
                electrobomba_02.on()
                
        elif programas_riego["programa-02"]["dia"][4]=="V" and programas_riego["programa-02"]["hora"][0:2]==hora_now:
            print("lunes-programa-02")
            if programas_riego["programa-02"]["hora"][3:5]==minutos_now and encender==True:
                encender=False                
                if programas_riego["programa-02"]["zona"][0:2] == "01":
                    maestra_01.off()
                    zona_01.off()
                if programas_riego["programa-02"]["zona"][2:4] == "02":
                    maestra_01.off()
                    zona_02.off()
                if programas_riego["programa-02"]["zona"][4:6] == "03":
                    maestra_01.off()
                    zona_03.off()
                if programas_riego["programa-02"]["zona"][6:8] == "04":
                    maestra_01.off()
                    zona_04.off()
                if programas_riego["programa-02"]["zona"][8:10] == "05":
                    maestra_02.off()
                    zona_05.off()
                if programas_riego["programa-02"]["zona"][10:12] == "06":
                    maestra_02.off()
                    zona_06.off()
                if programas_riego["programa-02"]["zona"][12:14] == "07":
                    maestra_02.off()
                    zona_07.off()
                if programas_riego["programa-02"]["zona"][8:10] == "08":
                    maestra_02.off()
                    zona_08.off()
                if programas_riego["programa-02"]["bomba"][0:2] == "01":
                    electrobomba_01.off()
                if programas_riego["programa-02"]["bomba"][2:4] == "04":
                    electrobomba_02.off()
                    
                tiempo_pasado= int(minutos_now)+ int(programas_riego["programa-02"]["tiempo"])
                tiempos_segundos = int(segundos_now)
                #print("regar")
            elif tiempo_pasado==int(minutos_now) and int(segundos_now)>=tiempos_segundos and encender==False:
                encender=True
                maestra_01.on()
                zona_01.on()
                zona_02.on()
                zona_03.on()
                zona_04.on()
                zona_05.on()
                zona_06.on()
                zona_07.on()
                zona_08.on()
                electrobomba_01.on()
                electrobomba_02.on()
                
        elif programas_riego["programa-03"]["dia"][4]=="V" and programas_riego["programa-03"]["hora"][0:2]==hora_now:
            print("lunes-programa-03")
            if programas_riego["programa-03"]["hora"][3:5]==minutos_now and encender==True:
                encender=False                
                if programas_riego["programa-03"]["zona"][0:2] == "01":
                    maestra_01.off()
                    zona_01.off()
                if programas_riego["programa-03"]["zona"][2:4] == "02":
                    maestra_01.off()
                    zona_02.off()
                if programas_riego["programa-03"]["zona"][4:6] == "03":
                    maestra_01.off()
                    zona_03.off()
                if programas_riego["programa-03"]["zona"][6:8] == "04":
                    maestra_01.off()
                    zona_04.off()
                if programas_riego["programa-03"]["zona"][8:10] == "05":
                    maestra_02.off()
                    zona_05.off()
                if programas_riego["programa-03"]["zona"][10:12] == "06":
                    maestra_02.off()
                    zona_06.off()
                if programas_riego["programa-03"]["zona"][12:14] == "07":
                    maestra_02.off()
                    zona_07.off()
                if programas_riego["programa-03"]["zona"][8:10] == "08":
                    maestra_02.off()
                    zona_08.off()
                if programas_riego["programa-03"]["bomba"][0:2] == "01":
                    electrobomba_01.off()
                if programas_riego["programa-03"]["bomba"][2:4] == "02":
                    electrobomba_02.off()
                    
                tiempo_pasado= int(minutos_now)+ int(programas_riego["programa-03"]["tiempo"])
                tiempos_segundos = int(segundos_now)
                #print("regar")
            elif tiempo_pasado==int(minutos_now) and int(segundos_now)>=tiempos_segundos and encender==False:
                encender=True
                maestra_01.on()
                zona_01.on()
                zona_02.on()
                zona_03.on()
                zona_04.on()
                zona_05.on()
                zona_06.on()
                zona_07.on()
                zona_08.on()
                electrobomba_01.on()
                electrobomba_02.on()
                
    elif dia_now=='6':
        #viernes_regar()
        print("sabado")
        if programas_riego["programa-01"]["dia"][5]=="S" and programas_riego["programa-01"]["hora"][0:2]==hora_now:
            print("lunes-programa-01")
            if programas_riego["programa-01"]["hora"][3:5]==minutos_now and encender==True:
                encender=False                
                if programas_riego["programa-01"]["zona"][0:2] == "01":
                    maestra_01.off()
                    zona_01.off()
                if programas_riego["programa-01"]["zona"][2:4] == "02":
                    maestra_01.off()
                    zona_02.off()
                if programas_riego["programa-01"]["zona"][4:6] == "03":
                    maestra_01.off()
                    zona_03.off()
                if programas_riego["programa-01"]["zona"][6:8] == "04":
                    maestra_01.off()
                    zona_04.off()
                if programas_riego["programa-01"]["zona"][8:10] == "05":
                    maestra_02.off()
                    zona_05.off()
                if programas_riego["programa-01"]["zona"][10:12] == "06":
                    maestra_02.off()
                    zona_06.off()
                if programas_riego["programa-01"]["zona"][12:14] == "07":
                    maestra_02.off()
                    zona_07.off()
                if programas_riego["programa-01"]["zona"][8:10] == "08":
                    maestra_02.off()
                    zona_08.off()
                if programas_riego["programa-01"]["bomba"][0:2] == "01":
                    electrobomba_01.off()
                if programas_riego["programa-01"]["bomba"][2:4] == "04":
                    electrobomba_02.off()
                    
                tiempo_pasado= int(minutos_now)+ int(programas_riego["programa-01"]["tiempo"])
                tiempos_segundos = int(segundos_now)
                #print("regar")
            elif tiempo_pasado==int(minutos_now) and int(segundos_now)>=tiempos_segundos and encender==False:
                encender=True
                maestra_01.on()
                zona_01.on()
                zona_02.on()
                zona_03.on()
                zona_04.on()
                zona_05.on()
                zona_06.on()
                zona_07.on()
                zona_08.on()
                electrobomba_01.on()
                electrobomba_02.on()
                
        elif programas_riego["programa-02"]["dia"][5]=="S" and programas_riego["programa-02"]["hora"][0:2]==hora_now:
            print("lunes-programa-02")
            if programas_riego["programa-02"]["hora"][3:5]==minutos_now and encender==True:
                encender=False                
                if programas_riego["programa-02"]["zona"][0:2] == "01":
                    maestra_01.off()
                    zona_01.off()
                if programas_riego["programa-02"]["zona"][2:4] == "02":
                    maestra_01.off()
                    zona_02.off()
                if programas_riego["programa-02"]["zona"][4:6] == "03":
                    maestra_01.off()
                    zona_03.off()
                if programas_riego["programa-02"]["zona"][6:8] == "04":
                    maestra_01.off()
                    zona_04.off()
                if programas_riego["programa-02"]["zona"][8:10] == "05":
                    maestra_02.off()
                    zona_05.off()
                if programas_riego["programa-02"]["zona"][10:12] == "06":
                    maestra_02.off()
                    zona_06.off()
                if programas_riego["programa-02"]["zona"][12:14] == "07":
                    maestra_02.off()
                    zona_07.off()
                if programas_riego["programa-02"]["zona"][8:10] == "08":
                    maestra_02.off()
                    zona_08.off()
                if programas_riego["programa-02"]["bomba"][0:2] == "01":
                    electrobomba_01.off()
                if programas_riego["programa-02"]["bomba"][2:4] == "04":
                    electrobomba_02.off()
                    
                tiempo_pasado= int(minutos_now)+ int(programas_riego["programa-02"]["tiempo"])
                tiempos_segundos = int(segundos_now)
                #print("regar")
            elif tiempo_pasado==int(minutos_now) and int(segundos_now)>=tiempos_segundos and encender==False:
                encender=True
                maestra_01.on()
                zona_01.on()
                zona_02.on()
                zona_03.on()
                zona_04.on()
                zona_05.on()
                zona_06.on()
                zona_07.on()
                zona_08.on()
                electrobomba_01.on()
                electrobomba_02.on()
                
        elif programas_riego["programa-03"]["dia"][5]=="S" and programas_riego["programa-03"]["hora"][0:2]==hora_now:
            print("lunes-programa-03")
            if programas_riego["programa-03"]["hora"][3:5]==minutos_now and encender==True:
                encender=False                
                if programas_riego["programa-03"]["zona"][0:2] == "01":
                    maestra_01.off()
                    zona_01.off()
                if programas_riego["programa-03"]["zona"][2:4] == "02":
                    maestra_01.off()
                    zona_02.off()
                if programas_riego["programa-03"]["zona"][4:6] == "03":
                    maestra_01.off()
                    zona_03.off()
                if programas_riego["programa-03"]["zona"][6:8] == "04":
                    maestra_01.off()
                    zona_04.off()
                if programas_riego["programa-03"]["zona"][8:10] == "05":
                    maestra_02.off()
                    zona_05.off()
                if programas_riego["programa-03"]["zona"][10:12] == "06":
                    maestra_02.off()
                    zona_06.off()
                if programas_riego["programa-03"]["zona"][12:14] == "07":
                    maestra_02.off()
                    zona_07.off()
                if programas_riego["programa-03"]["zona"][8:10] == "08":
                    maestra_02.off()
                    zona_08.off()
                if programas_riego["programa-03"]["bomba"][0:2] == "01":
                    electrobomba_01.off()
                if programas_riego["programa-03"]["bomba"][2:4] == "02":
                    electrobomba_02.off()
                    
                tiempo_pasado= int(minutos_now)+ int(programas_riego["programa-03"]["tiempo"])
                tiempos_segundos = int(segundos_now)
                #print("regar")
            elif tiempo_pasado==int(minutos_now) and int(segundos_now)>=tiempos_segundos and encender==False:
                encender=True
                maestra_01.on()
                zona_01.on()
                zona_02.on()
                zona_03.on()
                zona_04.on()
                zona_05.on()
                zona_06.on()
                zona_07.on()
                zona_08.on()
                electrobomba_01.off()
                electrobomba_02.off()
             
    clock.after(1000,times)

clock=tk.Label(ventana)
clock.grid(row=4,column=2,padx=1,pady=1)
times()
 
# if dia_now=='0':
#     domingo_regar()
# elif dia_now=='1':
#     lunes_regar()
# elif dia_now=='2':
#     martes_regar()
# elif dia_now=='3':
#     miercoles_regar()
# elif dia_now=='4':    
#     jueves_regar()
# elif dia_now=='5':
#     #viernes_regar()
#     print("...")
# elif dia_now=='6':
#     sabado_regar()

    
ubicacion=1
boton_zona.config(bg="#F26D3D")
ubicacion_zonas=1
zonas=1
e_1=e_2=e_3=e_4=e_5=e_6=e_7=e_8=e_9=e_10=b_1=b_2=boton_zona_guardar=boton_zona_regresar=1
e_1_s=e_2_s=e_3_s=e_4_s=e_5_s=e_6_s=e_7_s=e_8_s=e_9_s=e_10_s=b_1_s=b_2_s=boton_zona_guardar_s=boton_zona_regresar_s=False 

programar=1
programas=1
ubicacion_programar=1
regar=no_regar=regresar=1
p_1=p_2=p_3=1
e_1_p=e_2_p=e_3_p=e_4_p=e_5_p=e_6_p=e_7_p=e_8_p=e_9_p=e_10_p=b_1_p=b_2_p=1
lunes=martes=miercoles=jueves=viernes=sabado=domingo=1
seis_am=siete_am=cinco_pm=seis_pm=siete_pm=1
cinco_min=diez_min=quince_min=veinte_min=treinta_min=1

p_1_s=p_2_s=p_3_s=False
lunes_s=martes_s=miercoles_s=jueves_s=viernes_s=sabado_s=domingo_s=False
seis_am_s=siete_am_s=cinco_pm_s=seis_pm_s=siete_pm_s=False
cinco_min_s=diez_min_s=quince_min_s=veinte_min_s=treinta_min_s=False
regar_s=no_regar_s=regresar_s=False
e_1_p_s=e_2_p_s=e_3_p_s=e_4_p_s=e_5_p_s=e_6_p_s=e_7_p_s=e_8_p_s=e_9_p_s=e_10_p_s=b_1_p_s=b_2_p_s=False
dia=["-","-","-","-","-","-","-"]
hora=["-----"]
tiempo=["--"]
zona=["--","--","--","--","--","--","--","--"]
bomba=["--","--"]

ubicacion_manual=1
e_1_m=e_2_m=e_3_m=e_4_m=e_5_m=e_6_m=e_7_m=e_8_m=e_9_m=e_10_m=b_1_m=b_2_m=1
regar_m=regresar_m=1
e_1_m_s=e_2_m_s=e_3_m_s=e_4_m_s=e_5_m_s=e_6_m_s=e_7_m_s=e_8_m_s=e_9_m_s=e_10_m_s=b_1_m_s=b_2_m_s=False
regar_m_s=regresar_m_s=False
manual=1

with open('/home/pi/Documents/riego/equipos_habilitados.json') as file:
        equipos_habilitados=json.load(file)
    
e_1_s=equipos_habilitados['electrovalvulas'][0]['electrovalvula_01']    
e_2_s=equipos_habilitados['electrovalvulas'][1]['electrovalvula_02']
e_3_s=equipos_habilitados['electrovalvulas'][2]['electrovalvula_03']
e_4_s=equipos_habilitados['electrovalvulas'][3]['electrovalvula_04']
e_5_s=equipos_habilitados['electrovalvulas'][4]['electrovalvula_05']
e_6_s=equipos_habilitados['electrovalvulas'][5]['electrovalvula_06']
e_7_s=equipos_habilitados['electrovalvulas'][6]['electrovalvula_07']
e_8_s=equipos_habilitados['electrovalvulas'][7]['electrovalvula_08']
e_9_s=equipos_habilitados['electrovalvulas'][8]['electrovalvula_09']
e_10_s=equipos_habilitados['electrovalvulas'][9]['electrovalvula_10']
b_1_s=equipos_habilitados['electrobombas'][0]['electrobomba_01']
b_2_s=equipos_habilitados['electrobombas'][1]['electrobomba_02']

#PRIMERA VENTANA
#VENTANA ZONAS

def guardar_zonas():
    equipos_habilitados={}
    equipos_habilitados['electrovalvulas']=[]
    equipos_habilitados['electrovalvulas'].append({
     'electrovalvula_01':e_1_s
    }) 
    equipos_habilitados['electrovalvulas'].append({
     'electrovalvula_02':e_2_s
    })
    equipos_habilitados['electrovalvulas'].append({
     'electrovalvula_03':e_3_s
    })    
    equipos_habilitados['electrovalvulas'].append({
     'electrovalvula_04':e_4_s
    })    
    equipos_habilitados['electrovalvulas'].append({
     'electrovalvula_05':e_5_s
    })
    equipos_habilitados['electrovalvulas'].append({
     'electrovalvula_06':e_6_s
    })
    equipos_habilitados['electrovalvulas'].append({
     'electrovalvula_07':e_7_s
    })
    equipos_habilitados['electrovalvulas'].append({
     'electrovalvula_08':e_8_s
    })
    equipos_habilitados['electrovalvulas'].append({
     'electrovalvula_09':e_9_s
    })
    equipos_habilitados['electrovalvulas'].append({
     'electrovalvula_10':e_10_s
    })
    
    equipos_habilitados['electrobombas']=[]
    equipos_habilitados['electrobombas'].append({
     'electrobomba_01':b_1_s
    })
    equipos_habilitados['electrobombas'].append({
     'electrobomba_02':b_2_s
    })
    with open('/home/pi/Documents/riego/equipos_habilitados.json','w') as fp:
        json.dump(equipos_habilitados,fp)
   
def zonas_cursor(event):
    #print("hola")
    global ubicacion_zonas
    global e_1_s,e_2_s,e_3_s,e_4_s,e_5_s,e_6_s,e_7_s,e_8_s,e_9_s,e_10_s,b_1_s,b_2_s,boton_zona_guardar_s,boton_zona_regresar_s
    
    
    if (event.keysym=="KP_Up"):        
            ubicacion_zonas=ubicacion_zonas-1
            if ubicacion_zonas <=14 and ubicacion_zonas>0:
                print("")
            else:
                ubicacion_zonas = 1
                if e_1_s == False:
                    e_1.config(bg="#F26D3D")
                if e_2_s == False:
                    e_2.config(bg="#000000")
                if e_3_s == False:
                    e_3.config(bg="#000000")
                if e_4_s == False:
                    e_4.config(bg="#000000")
                if e_5_s == False:
                    e_5.config(bg="#000000")
                if e_6_s == False:
                    e_6.config(bg="#000000")
                if e_7_s == False:
                    e_7.config(bg="#000000")
                if e_8_s == False:
                    e_8.config(bg="#000000")
                if e_9_s == False:
                    e_9.config(bg="#000000")
                if e_10_s == False:
                    e_10.config(bg="#000000")
                if b_1_s == False:
                    b_1.config(bg="#000000")
                if b_2_s == False:
                    b_2.config(bg="#000000")
                if boton_zona_guardar_s == False:
                    boton_zona_guardar.config(bg="#000000")
                if boton_zona_regresar_s == False:
                    boton_zona_regresar.config(bg="#000000")
                    
    elif (event.keysym=="KP_Down"):
            ubicacion_zonas=ubicacion_zonas+1
            if ubicacion_zonas <=14 and ubicacion_zonas>0:
                print("")
            else:
                ubicacion_zonas = 1
                if e_1_s == False:
                    e_1.config(bg="#F26D3D")
                if e_2_s == False:
                    e_2.config(bg="#000000")
                if e_3_s == False:
                    e_3.config(bg="#000000")
                if e_4_s == False:
                    e_4.config(bg="#000000")
                if e_5_s == False:
                    e_5.config(bg="#000000")
                if e_6_s == False:
                    e_6.config(bg="#000000")
                if e_7_s == False:
                    e_7.config(bg="#000000")
                if e_8_s == False:
                    e_8.config(bg="#000000")
                if e_9_s == False:
                    e_9.config(bg="#000000")
                if e_10_s == False:
                    e_10.config(bg="#000000")
                if b_1_s == False:
                    b_1.config(bg="#000000")
                if b_2_s == False:
                    b_2.config(bg="#000000")
                if boton_zona_guardar_s == False:
                    boton_zona_guardar.config(bg="#000000")
                if boton_zona_regresar_s == False:
                    boton_zona_regresar.config(bg="#000000")              
               
    if ubicacion_zonas == 1:
                if e_1_s == False:
                    e_1.config(bg="#F26D3D")
                if e_2_s == False:
                    e_2.config(bg="#000000")
                if e_3_s == False:
                    e_3.config(bg="#000000")
                if e_4_s == False:
                    e_4.config(bg="#000000")
                if e_5_s == False:
                    e_5.config(bg="#000000")
                if e_6_s == False:
                    e_6.config(bg="#000000")
                if e_7_s == False:
                    e_7.config(bg="#000000")
                if e_8_s == False:
                    e_8.config(bg="#000000")
                if e_9_s == False:
                    e_9.config(bg="#000000")
                if e_10_s == False:
                    e_10.config(bg="#000000")
                if b_1_s == False:
                    b_1.config(bg="#000000")
                if b_2_s == False:
                    b_2.config(bg="#000000")
                if boton_zona_guardar_s == False:
                    boton_zona_guardar.config(bg="#000000")
                if boton_zona_regresar_s == False:
                    boton_zona_regresar.config(bg="#000000")        
            
    elif ubicacion_zonas == 2:
                if e_1_s == False:
                    e_1.config(bg="#000000")
                if e_2_s == False:
                    e_2.config(bg="#F26D3D")
                if e_3_s == False:
                    e_3.config(bg="#000000")
                if e_4_s == False:
                    e_4.config(bg="#000000")
                if e_5_s == False:
                    e_5.config(bg="#000000")
                if e_6_s == False:
                    e_6.config(bg="#000000")
                if e_7_s == False:
                    e_7.config(bg="#000000")
                if e_8_s == False:
                    e_8.config(bg="#000000")
                if e_9_s == False:
                    e_9.config(bg="#000000")
                if e_10_s == False:
                    e_10.config(bg="#000000")
                if b_1_s == False:
                    b_1.config(bg="#000000")
                if b_2_s == False:
                    b_2.config(bg="#000000")
                if boton_zona_guardar_s == False:
                    boton_zona_guardar.config(bg="#000000")
                if boton_zona_regresar_s == False:
                    boton_zona_regresar.config(bg="#000000")
            
                    
    elif ubicacion_zonas == 3:
                if e_1_s == False:
                    e_1.config(bg="#000000")
                if e_2_s == False:
                    e_2.config(bg="#000000")                    
                if e_3_s == False:
                    e_3.config(bg="#F26D3D")
                    print(e_2_s)
                if e_4_s == False:
                    e_4.config(bg="#000000")
                if e_5_s == False:
                    e_5.config(bg="#000000")
                if e_6_s == False:
                    e_6.config(bg="#000000")
                if e_7_s == False:
                    e_7.config(bg="#000000")
                if e_8_s == False:
                    e_8.config(bg="#000000")
                if e_9_s == False:
                    e_9.config(bg="#000000")
                if e_10_s == False:
                    e_10.config(bg="#000000")
                if b_1_s == False:
                    b_1.config(bg="#000000")
                if b_2_s == False:
                    b_2.config(bg="#000000")
                if boton_zona_guardar_s == False:
                    boton_zona_guardar.config(bg="#000000")
                if boton_zona_regresar_s == False:
                    boton_zona_regresar.config(bg="#000000")           
                         
    elif ubicacion_zonas == 4:
                if e_1_s == False:
                    e_1.config(bg="#000000")
                if e_2_s == False:
                    e_2.config(bg="#000000")
                if e_3_s == False:
                    e_3.config(bg="#000000")
                if e_4_s == False:
                    e_4.config(bg="#F26D3D")
                if e_5_s == False:
                    e_5.config(bg="#000000")
                if e_6_s == False:
                    e_6.config(bg="#000000")
                if e_7_s == False:
                    e_7.config(bg="#000000")
                if e_8_s == False:
                    e_8.config(bg="#000000")
                if e_9_s == False:
                    e_9.config(bg="#000000")
                if e_10_s == False:
                    e_10.config(bg="#000000")
                if b_1_s == False:
                    b_1.config(bg="#000000")
                if b_2_s == False:
                    b_2.config(bg="#000000")
                if boton_zona_guardar_s == False:
                    boton_zona_guardar.config(bg="#000000")
                if boton_zona_regresar_s == False:
                    boton_zona_regresar.config(bg="#000000")
            
    elif ubicacion_zonas == 5:
                if e_1_s == False:
                    e_1.config(bg="#000000")
                if e_2_s == False:
                    e_2.config(bg="#000000")
                if e_3_s == False:
                    e_3.config(bg="#000000")
                if e_4_s == False:
                    e_4.config(bg="#000000")
                if e_5_s == False:
                    e_5.config(bg="#F26D3D")
                if e_6_s == False:
                    e_6.config(bg="#000000")
                if e_7_s == False:
                    e_7.config(bg="#000000")
                if e_8_s == False:
                    e_8.config(bg="#000000")
                if e_9_s == False:
                    e_9.config(bg="#000000")
                if e_10_s == False:
                    e_10.config(bg="#000000")
                if b_1_s == False:
                    b_1.config(bg="#000000")
                if b_2_s == False:
                    b_2.config(bg="#000000")
                if boton_zona_guardar_s == False:
                    boton_zona_guardar.config(bg="#000000")
                if boton_zona_regresar_s == False:
                    boton_zona_regresar.config(bg="#000000")               
    
    elif ubicacion_zonas == 6:
                if e_1_s == False:
                    e_1.config(bg="#000000")
                if e_2_s == False:
                    e_2.config(bg="#000000")
                if e_3_s == False:
                    e_3.config(bg="#000000")
                if e_4_s == False:
                    e_4.config(bg="#000000")
                if e_5_s == False:
                    e_5.config(bg="#000000")
                if e_6_s == False:
                    e_6.config(bg="#F26D3D")
                if e_7_s == False:
                    e_7.config(bg="#000000")
                if e_8_s == False:
                    e_8.config(bg="#000000")
                if e_9_s == False:
                    e_9.config(bg="#000000")
                if e_10_s == False:
                    e_10.config(bg="#000000")
                if b_1_s == False:
                    b_1.config(bg="#000000")
                if b_2_s == False:
                    b_2.config(bg="#000000")
                if boton_zona_guardar_s == False:
                    boton_zona_guardar.config(bg="#000000")
                if boton_zona_regresar_s == False:
                    boton_zona_regresar.config(bg="#000000")
            
    elif ubicacion_zonas == 7:
                if e_1_s == False:
                    e_1.config(bg="#000000")
                if e_2_s == False:
                    e_2.config(bg="#000000")
                if e_3_s == False:
                    e_3.config(bg="#000000")
                if e_4_s == False:
                    e_4.config(bg="#000000")
                if e_5_s == False:
                    e_5.config(bg="#000000")
                if e_6_s == False:
                    e_6.config(bg="#000000")
                if e_7_s == False:
                    e_7.config(bg="#F26D3D")
                if e_8_s == False:
                    e_8.config(bg="#000000")
                if e_9_s == False:
                    e_9.config(bg="#000000")
                if e_10_s == False:
                    e_10.config(bg="#000000")
                if b_1_s == False:
                    b_1.config(bg="#000000")
                if b_2_s == False:
                    b_2.config(bg="#000000")
                if boton_zona_guardar_s == False:
                    boton_zona_guardar.config(bg="#000000")
                if boton_zona_regresar_s == False:
                    boton_zona_regresar.config(bg="#000000")
                    
    elif ubicacion_zonas == 8:
                if e_1_s == False:
                    e_1.config(bg="#000000")
                if e_2_s == False:
                    e_2.config(bg="#000000")
                if e_3_s == False:
                    e_3.config(bg="#000000")
                if e_4_s == False:
                    e_4.config(bg="#000000")
                if e_5_s == False:
                    e_5.config(bg="#000000")
                if e_6_s == False:
                    e_6.config(bg="#000000")
                if e_7_s == False:
                    e_7.config(bg="#000000")
                if e_8_s == False:
                    e_8.config(bg="#F26D3D")
                if e_9_s == False:
                    e_9.config(bg="#000000")
                if e_10_s == False:
                    e_10.config(bg="#000000")
                if b_1_s == False:
                    b_1.config(bg="#000000")
                if b_2_s == False:
                    b_2.config(bg="#000000")
                if boton_zona_guardar_s == False:
                    boton_zona_guardar.config(bg="#000000")
                if boton_zona_regresar_s == False:
                    boton_zona_regresar.config(bg="#000000")
            
    elif ubicacion_zonas == 9:
                if e_1_s == False:
                    e_1.config(bg="#000000")
                if e_2_s == False:
                    e_2.config(bg="#000000")
                if e_3_s == False:
                    e_3.config(bg="#000000")
                if e_4_s == False:
                    e_4.config(bg="#000000")
                if e_5_s == False:
                    e_5.config(bg="#000000")
                if e_6_s == False:
                    e_6.config(bg="#000000")
                if e_7_s == False:
                    e_7.config(bg="#000000")
                if e_8_s == False:
                    e_8.config(bg="#000000")
                if e_9_s == False:
                    e_9.config(bg="#F26D3D")
                if e_10_s == False:
                    e_10.config(bg="#000000")
                if b_1_s == False:
                    b_1.config(bg="#000000")
                if b_2_s == False:
                    b_2.config(bg="#000000")
                if boton_zona_guardar_s == False:
                    boton_zona_guardar.config(bg="#000000")
                if boton_zona_regresar_s == False:
                    boton_zona_regresar.config(bg="#000000")
                    
    elif ubicacion_zonas == 9:
                if e_1_s == False:
                    e_1.config(bg="#000000")
                if e_2_s == False:
                    e_2.config(bg="#000000")
                if e_3_s == False:
                    e_3.config(bg="#000000")
                if e_4_s == False:
                    e_4.config(bg="#000000")
                if e_5_s == False:
                    e_5.config(bg="#000000")
                if e_6_s == False:
                    e_6.config(bg="#000000")
                if e_7_s == False:
                    e_7.config(bg="#000000")
                if e_8_s == False:
                    e_8.config(bg="#000000")
                if e_9_s == False:
                    e_9.config(bg="#F26D3D")
                if e_10_s == False:
                    e_10.config(bg="#000000")
                if b_1_s == False:
                    b_1.config(bg="#000000")
                if b_2_s == False:
                    b_2.config(bg="#000000")
                if boton_zona_guardar_s == False:
                    boton_zona_guardar.config(bg="#000000")
                if boton_zona_regresar_s == False:
                    boton_zona_regresar.config(bg="#000000")
            
    elif ubicacion_zonas == 10:
                if e_1_s == False:
                    e_1.config(bg="#000000")
                if e_2_s == False:
                    e_2.config(bg="#000000")
                if e_3_s == False:
                    e_3.config(bg="#000000")
                if e_4_s == False:
                    e_4.config(bg="#000000")
                if e_5_s == False:
                    e_5.config(bg="#000000")
                if e_6_s == False:
                    e_6.config(bg="#000000")
                if e_7_s == False:
                    e_7.config(bg="#000000")
                if e_8_s == False:
                    e_8.config(bg="#000000")
                if e_9_s == False:
                    e_9.config(bg="#000000")
                if e_10_s == False:
                    e_10.config(bg="#F26D3D")
                if b_1_s == False:
                    b_1.config(bg="#000000")
                if b_2_s == False:
                    b_2.config(bg="#000000")
                if boton_zona_guardar_s == False:
                    boton_zona_guardar.config(bg="#000000")
                if boton_zona_regresar_s == False:
                    boton_zona_regresar.config(bg="#000000")
            
    elif ubicacion_zonas == 11:
                if e_1_s == False:
                    e_1.config(bg="#000000")
                if e_2_s == False:
                    e_2.config(bg="#000000")
                if e_3_s == False:
                    e_3.config(bg="#000000")
                if e_4_s == False:
                    e_4.config(bg="#000000")
                if e_5_s == False:
                    e_5.config(bg="#000000")
                if e_6_s == False:
                    e_6.config(bg="#000000")
                if e_7_s == False:
                    e_7.config(bg="#000000")
                if e_8_s == False:
                    e_8.config(bg="#000000")
                if e_9_s == False:
                    e_9.config(bg="#000000")
                if e_10_s == False:
                    e_10.config(bg="#000000")
                if b_1_s == False:
                    b_1.config(bg="#F26D3D")
                if b_2_s == False:
                    b_2.config(bg="#000000")
                if boton_zona_guardar_s == False:
                    boton_zona_guardar.config(bg="#000000")
                if boton_zona_regresar_s == False:
                    boton_zona_regresar.config(bg="#000000")
            
    elif ubicacion_zonas == 12:
                if e_1_s == False:
                    e_1.config(bg="#000000")
                if e_2_s == False:
                    e_2.config(bg="#000000")
                if e_3_s == False:
                    e_3.config(bg="#000000")
                if e_4_s == False:
                    e_4.config(bg="#000000")
                if e_5_s == False:
                    e_5.config(bg="#000000")
                if e_6_s == False:
                    e_6.config(bg="#000000")
                if e_7_s == False:
                    e_7.config(bg="#000000")
                if e_8_s == False:
                    e_8.config(bg="#000000")
                if e_9_s == False:
                    e_9.config(bg="#000000")
                if e_10_s == False:
                    e_10.config(bg="#000000")
                if b_1_s == False:
                    b_1.config(bg="#000000")
                if b_2_s == False:
                    b_2.config(bg="#F26D3D")
                if boton_zona_guardar_s == False:
                    boton_zona_guardar.config(bg="#000000")
                if boton_zona_regresar_s == False:
                    boton_zona_regresar.config(bg="#000000")
                    
    elif ubicacion_zonas == 13:
                if e_1_s == False:
                    e_1.config(bg="#000000")
                if e_2_s == False:
                    e_2.config(bg="#000000")
                if e_3_s == False:
                    e_3.config(bg="#000000")
                if e_4_s == False:
                    e_4.config(bg="#000000")
                if e_5_s == False:
                    e_5.config(bg="#000000")
                if e_6_s == False:
                    e_6.config(bg="#000000")
                if e_7_s == False:
                    e_7.config(bg="#000000")
                if e_8_s == False:
                    e_8.config(bg="#000000")
                if e_9_s == False:
                    e_9.config(bg="#000000")
                if e_10_s == False:
                    e_10.config(bg="#000000")
                if b_1_s == False:
                    b_1.config(bg="#000000")
                if b_2_s == False:
                    b_2.config(bg="#000000")
                if boton_zona_guardar_s == False:
                    boton_zona_guardar.config(bg="#F26D3D")
                if boton_zona_regresar_s == False:
                    boton_zona_regresar.config(bg="#000000")
            
    elif ubicacion_zonas == 14:
                if e_1_s == False:
                    e_1.config(bg="#000000")
                if e_2_s == False:
                    e_2.config(bg="#000000")
                if e_3_s == False:
                    e_3.config(bg="#000000")
                if e_4_s == False:
                    e_4.config(bg="#000000")
                if e_5_s == False:
                    e_5.config(bg="#000000")
                if e_6_s == False:
                    e_6.config(bg="#000000")
                if e_7_s == False:
                    e_7.config(bg="#000000")
                if e_8_s == False:
                    e_8.config(bg="#000000")
                if e_9_s == False:
                    e_9.config(bg="#000000")
                if e_10_s == False:
                    e_10.config(bg="#000000")
                if b_1_s == False:
                    b_1.config(bg="#000000")
                if b_2_s == False:
                    b_2.config(bg="#000000")
                if boton_zona_guardar_s == False:
                    boton_zona_guardar.config(bg="#000000")
                if boton_zona_regresar_s == False:
                    boton_zona_regresar.config(bg="#F26D3D")        
    #guardar zonas    
    if (event.keysym=="KP_Begin"):     
        
        if ubicacion_zonas == 2:
            if e_2_s==False:
                e_2.config(bg="#04BF9D")
                e_2_s=True
                e_1.config(bg="#04BF9D")
                e_1_s=True                
            else:
                e_2.config(bg="#000000")
                e_2_s=False
                if e_3_s==False and e_4_s==False and e_5_s==False:
                    e_1.config(bg="#000000")
                    e_1_s=False                    
                
        elif ubicacion_zonas == 3:
            if e_3_s==False:
                e_3.config(bg="#04BF9D")
                e_3_s=True
                e_1.config(bg="#04BF9D")
                e_1_s=True
                
            else:
                e_3.config(bg="#000000")
                e_3_s=False
                if e_2_s==False and e_4_s==False and e_5_s==False:
                    e_1.config(bg="#000000")
                    e_1_s=False
                    
        elif ubicacion_zonas == 4:
            if e_4_s==False:
                e_4.config(bg="#04BF9D")
                e_4_s=True
                e_1.config(bg="#04BF9D")
                e_1_s=True
                
            else:
                e_4.config(bg="#000000")
                e_4_s=False
                if e_2_s==False and e_3_s==False and e_5_s==False:
                    e_1.config(bg="#000000")
                    e_1_s=False
                    
        elif ubicacion_zonas == 5:
            if e_5_s==False:
                e_5.config(bg="#04BF9D")
                e_5_s=True
                e_1.config(bg="#04BF9D")
                e_1_s=True
                
            else:
                e_5.config(bg="#000000")
                e_5_s=False
                if e_2_s==False and e_3_s==False and e_4_s==False:
                    e_1.config(bg="#000000")
                    e_1_s=False
                    
        elif ubicacion_zonas == 7:
            if e_7_s==False:
                e_7.config(bg="#04BF9D")
                e_7_s=True
                e_6.config(bg="#04BF9D")
                e_6_s=True
            else:
                e_7.config(bg="#000000")
                e_7_s=False
                if e_8_s==False and e_9_s==False and e_10_s==False:
                    e_6.config(bg="#000000")
                    e_6_s=False
        elif ubicacion_zonas == 8:
            if e_8_s==False:
                e_8.config(bg="#04BF9D")
                e_8_s=True
                e_6.config(bg="#04BF9D")
                e_6_s=True
            else:
                e_8.config(bg="#000000")
                e_8_s=False
                if e_7_s==False and e_9_s==False and e_10_s==False:
                    e_6.config(bg="#000000")
                    e_6_s=False
        elif ubicacion_zonas == 9:
            if e_9_s==False:
                e_9.config(bg="#04BF9D")
                e_9_s=True
                e_6.config(bg="#04BF9D")
                e_6_s=True
            else:
                e_9.config(bg="#000000")
                e_9_s=False
                if e_8_s==False and e_9_s==False and e_10_s==False:
                    e_6.config(bg="#000000")
                    e_6_s=False
        elif ubicacion_zonas == 10:
            if e_10_s==False:
                e_10.config(bg="#04BF9D")
                e_10_s=True
                e_6.config(bg="#04BF9D")
                e_6_s=True
            else:
                e_10.config(bg="#000000")
                e_10_s=False            
        elif ubicacion_zonas == 11:
            if b_1_s==False:
                b_1.config(bg="#04BF9D")
                b_1_s=True
            else:
                b_1.config(bg="#000000")
                b_1_s=False                
        elif ubicacion_zonas == 12:
            if b_2_s==False:
                b_2.config(bg="#04BF9D")
                b_2_s=True
            else:
                b_2.config(bg="#000000")
                b_2_s=False
        elif ubicacion_zonas == 13:
            guardar_zonas()
            
        elif ubicacion_zonas == 14:
            zonas.destroy()
            
def ventana_zonas():
    global e_1,e_2,e_3,e_4,e_5,e_6,e_7,e_8,e_9,e_10,b_1,b_2,boton_zona_guardar,boton_zona_regresar
    global zonas
    ventana.deiconify()
    zonas=tk.Toplevel()
    zonas.attributes("-fullscreen",True)
    zonas.config(cursor="none") 
    #zonas.geometry('350x200')
    zonas.configure(background="#000000")
#     image_zonas=tk.PhotoImage(file="/home/pi/Documents/riego/logo-negro.gif")
#     image_zonas=image_zonas.subsample(4,4)
#     label_image_zonas=tk.Label(zonas,image=image_zonas)
#     label_image_zonas.grid(row=9,column=2,rowspan=2)
    
    #label_zonas.pack()
    label_electrovalvula=tk.Label(zonas,text="ELECTROVALVULAS",font=("Helvetica",35),fg ="#F26D3D",bg="#000000",width=22,height=2)
    label_electrovalvula.grid(row=1,column=1)
    
    e_1=tk.Button(zonas,text ="MAESTRA 01",fg ="#FFFFFF",bg="#000000",font=("Helvetica",25),width=19,height=1)
    e_1.grid(row=3, column=1,padx=20,pady=1)
    e_1.config(bg="#F26D3D")
    print(type(e_1))
    e_2=tk.Button(zonas,text ="ELECTROVALVULA 01",fg ="#FFFFFF",bg="#000000",font=("Helvetica",25),width=19,height=1)
    e_2.grid(row=4, column=1,padx=20,pady=1)
    e_3=tk.Button(zonas,text ="ELECTROVALVULA 02",fg ="#FFFFFF",bg="#000000",font=("Helvetica",25),width=19,height=1)
    e_3.grid(row=5, column=1,padx=20,pady=1)
    e_4=tk.Button(zonas,text ="ELECTROVALVULA 03",fg ="#FFFFFF",bg="#000000",font=("Helvetica",25),width=19,height=1)
    e_4.grid(row=6, column=1,padx=20,pady=1)
    e_5=tk.Button(zonas,text ="ELECTROVALVULA 04",fg ="#FFFFFF",bg="#000000",font=("Helvetica",25),width=19,height=1)
    e_5.grid(row=7, column=1,padx=20,pady=1)
    e_6=tk.Button(zonas,text ="MAESTRA 02",fg ="#FFFFFF",bg="#000000",font=("Helvetica",25),width=19,height=1)
    e_6.grid(row=8, column=1,padx=20,pady=1)
    e_7=tk.Button(zonas,text ="ELECTROVALVULA 05",fg ="#FFFFFF",bg="#000000",font=("Helvetica",25),width=19,height=1)
    e_7.grid(row=9, column=1,padx=20,pady=1)
    e_8=tk.Button(zonas,text ="ELECTROVALVULA 06",fg ="#FFFFFF",bg="#000000",font=("Helvetica",25),width=19,height=1)
    e_8.grid(row=10, column=1,padx=20,pady=1)
    e_9=tk.Button(zonas,text ="ELECTROVALVULA 07",fg ="#FFFFFF",bg="#000000",font=("Helvetica",25),width=19,height=1)
    e_9.grid(row=11, column=1,padx=20,pady=1)
    e_10=tk.Button(zonas,text ="ELECTROVALVULA 08",fg ="#FFFFFF",bg="#000000",font=("Helvetica",25),width=19,height=1)
    e_10.grid(row=12, column=1,padx=20,pady=1)
     
    label_electrobomba=tk.Label(zonas,text="ELECTROBOMBAS",font=("Helvetica",35),fg ="#F26D3D",bg="#000000",width=22,height=2)
    label_electrobomba.grid(row=1,column=2)
    
    b_1=tk.Button(zonas,text ="1",fg ="#FFFFFF",bg="#000000",font=("Helvetica",25),width=19,height=1)
    b_1.grid(row=3, column=2,padx=20,pady=1)
    b_2=tk.Button(zonas,text ="2",fg ="#FFFFFF",bg="#000000",font=("Helvetica",25),width=19,height=1)
    b_2.grid(row=4, column=2,padx=20,pady=1)
    
    boton_zona_guardar=tk.Button(zonas,text="GUARDAR",fg ="#FFFFFF",bg="#000000",font=("Helvetica",25),width=19,height=1,relief="groove",borderwidth=15)
    boton_zona_guardar.grid(row=6,column=2,padx=20,pady=1)
    boton_zona_regresar=tk.Button(zonas,text="REGRESAR",fg ="#FFFFFF",bg="#000000",font=("Helvetica",25),width=19,height=1,relief="groove",borderwidth=15)                                                                                                                                                 
    boton_zona_regresar.grid(row=8,column=2,padx=20,pady=1)   
    e_1.config(bg="#04BF9D") if e_1_s == True else print('')
    e_2.config(bg="#04BF9D") if e_2_s == True else print('')
    e_3.config(bg="#04BF9D") if e_3_s == True else print('')
    e_4.config(bg="#04BF9D") if e_4_s == True else print('')
    e_5.config(bg="#04BF9D") if e_5_s == True else print('')
    e_6.config(bg="#04BF9D") if e_6_s == True else print('')
    e_7.config(bg="#04BF9D") if e_7_s == True else print('')
    e_8.config(bg="#04BF9D") if e_8_s == True else print('')
    e_9.config(bg="#04BF9D") if e_9_s == True else print('')
    e_10.config(bg="#04BF9D") if e_10_s == True else print('')
    b_1.config(bg="#04BF9D") if b_1_s == True else print('')
    b_2.config(bg="#04BF9D") if b_2_s == True else print('')
    zonas.bind("<KeyPress>", zonas_cursor)           

#SEGUNDA VENTANA
#VENTANA PROGRAMAR
def guardar_programas():    
    #tk.messagebox.showinfo(programar,message="mensaje",title="titulo")
       
    with open('/home/pi/Documents/riego/programas_riego.json') as file:
        programas_riego=json.load(file)
    
    dia_string="".join(dia)
    hora_string="".join(hora)
    tiempo_string="".join(tiempo)
    zona_string="".join(zona)
    bomba_string="".join(bomba)    
    
    if p_1_s==True:
        programas_riego["programa-01"]["dia"]=dia_string
        programas_riego["programa-01"]["hora"]=hora_string
        programas_riego["programa-01"]["tiempo"]=tiempo_string
        programas_riego["programa-01"]["zona"]=zona_string
        programas_riego["programa-01"]["bomba"]=bomba_string
    elif p_2_s==True:
        programas_riego["programa-02"]["dia"]=dia_string
        programas_riego["programa-02"]["hora"]=hora_string
        programas_riego["programa-02"]["tiempo"]=tiempo_string
        programas_riego["programa-02"]["zona"]=zona_string
        programas_riego["programa-02"]["bomba"]=bomba_string
        
        
    elif p_3_s==True:
        programas_riego["programa-03"]["dia"]=dia_string
        programas_riego["programa-03"]["hora"]=hora_string
        programas_riego["programa-03"]["tiempo"]=tiempo_string
        programas_riego["programa-03"]["zona"]=zona_string
        programas_riego["programa-03"]["bomba"]=bomba_string       
        
        
    
    with open('/home/pi/Documents/riego/programas_riego.json','w') as fp:
        json.dump(programas_riego,fp)
        
def programar_cursor(event):
    global p_1_s,p_2_s,p_3_s
    global e_1_p_s,e_2_p_s,e_3_p_s,e_4_p_s,e_5_p_s,e_6_p_s,e_7_p_s,e_8_p_s,e_9_p_s,e_10_p_s,b_1_p_s,b_2_p_s
    global ubicacion_programar 
    global lunes_s,martes_s,miercoles_s,jueves_s,viernes_s,sabado_s,domingo_s
    global seis_am_s,siete_am_s,cinco_pm_s,seis_pm_s,siete_pm_s
    global cinco_min_s,diez_min_s,quince_min_s,veinte_min_s,treinta_min_s
    global regar_s,regresar_s
    global dia,hora,tiempo,zona,bomba  
    
    if (event.keysym=="KP_Right"):
        ubicacion_programar=ubicacion_programar+1
        if ubicacion_programar <=34 and ubicacion_programar>0:
            print("")
        else:
            ubicacion_programar = 1    
            
    elif (event.keysym=="KP_Left"):
        ubicacion_programar=ubicacion_programar-1
        if ubicacion_programar <=34  and ubicacion_programar>0:
            print("")
        else:
            ubicacion_programar = 1
        
    if ubicacion_programar == 1:          
        if p_1_s == False:
            p_1.config(bg="#F26D3D")  
        if p_2_s == False:
            p_2.config(bg="#000000")        
        if regresar_s == False :
            regresar.config(bg="#000000")
           
    elif ubicacion_programar == 2:
        if p_1_s == False:
            p_1.config(bg="#000000") 
        if p_2_s == False:
            p_2.config(bg="#F26D3D") 
        if p_3_s == False:
            p_3.config(bg="#000000")        
    elif ubicacion_programar == 3:
        if p_2_s == False:
            p_2.config(bg="#000000") 
        if p_3_s == False:
            p_3.config(bg="#F26D3D") 
        if e_1_p_s == False:
            e_1_p.config(bg="#000000")     
        
    elif ubicacion_programar == 4: 
        if p_3_s == False:
            p_3.config(bg="#000000") 
        if e_1_p_s == False:
            e_1_p.config(bg="#F26D3D")
        if e_2_p_s == False:
            e_2_p.config(bg="#000000")       
           
    elif ubicacion_programar == 5:        
        if e_1_p_s == False:
            e_1_p.config(bg="#000000")
        if e_2_p_s == False:
            e_2_p.config(bg="#F26D3D")
        if e_3_p_s == False:
            e_3_p.config(bg="#000000")        
    elif ubicacion_programar == 6:        
        if e_2_p_s == False:
            e_2_p.configure(bg="#000000")
        if e_3_p_s == False:
            e_3_p.config(bg="#F26D3D")
        if e_4_p_s == False:
            e_4_p.config(bg="#000000")     
       
    elif ubicacion_programar == 7: 
        if e_3_p_s == False:
            e_3_p.configure(bg="#000000")
        if e_4_p_s == False:
            e_4_p.config(bg="#F26D3D")
        if e_5_p_s == False:
            e_5_p.config(bg="#000000")
            
    elif ubicacion_programar == 8:  
        if e_4_p_s == False:
            e_4_p.config(bg="#000000")
        if e_5_p_s == False:
            e_5_p.config(bg="#F26D3D")
        if e_6_p_s == False:
            e_6_p.config(bg="#000000")
            
    elif ubicacion_programar == 9:
        if e_5_p_s == False:
            e_5_p.config(bg="#000000")
        if e_6_p_s == False:
            e_6_p.config(bg="#F26D3D")
        if e_7_p_s == False:
            e_7_p.config(bg="#000000")       
           
    elif ubicacion_programar == 10:   
        if e_6_p_s == False:
            e_6_p.config(bg="#000000")
        if e_7_p_s == False:
            e_7_p.config(bg="#F26D3D")
        if e_8_p_s == False:
            e_8_p.config(bg="#000000")
            
    elif ubicacion_programar == 11: 
        if e_7_p_s == False:
            e_7_p.config(bg="#000000")
        if e_8_p_s == False:
            e_8_p.config(bg="#F26D3D")
        if e_9_p_s == False:
            e_9_p.config(bg="#000000")       
    elif ubicacion_programar == 12: 
        if e_8_p_s == False:
            e_8_p.config(bg="#000000")
        if e_9_p_s == False:
            e_9_p.config(bg="#F26D3D")
        if e_10_p_s == False:
            e_10_p.config(bg="#000000")        
            
    elif ubicacion_programar ==13: 
        if e_9_p_s == False:
            e_9_p.config(bg="#000000")
        if e_10_p_s == False:
            e_10_p.config(bg="#F26D3D")
        if b_1_p_s == False:
            b_1_p.config(bg="#000000")
        
    elif ubicacion_programar == 14: 
        if e_10_p_s == False:
            e_10_p.config(bg="#000000")
        if b_1_p_s == False:
            b_1_p.config(bg="#F26D3D")
        if b_2_p_s == False:
            b_2_p.config(bg="#000000")
            
    elif ubicacion_programar == 15:  
        if b_1_p_s == False:
            b_1_p.config(bg="#000000")
        if b_2_p_s == False:
            b_2_p.config(bg="#F26D3D")
        if lunes_s == False:
            lunes.config(bg="#000000")
            
    elif ubicacion_programar == 16:         
        if b_2_p_s == False:
            b_2_p.config(bg="#000000")
        if lunes_s == False:
            lunes.config(bg="#F26D3D")
        if martes_s == False:
            martes.config(bg="#000000")
        
    elif ubicacion_programar == 17: 
        if lunes_s == False:
            lunes.config(bg="#000000")
        if martes_s == False:
            martes.config(bg="#F26D3D")
        if miercoles_s == False:
            miercoles.config(bg="#000000")
            
    elif ubicacion_programar == 18: 
        if martes_s == False:
            martes.config(bg="#000000")
        if miercoles_s == False:
            miercoles.config(bg="#F26D3D")
        if jueves_s == False:
            jueves.config(bg="#000000") 
        
    elif ubicacion_programar == 19:  
        if miercoles_s == False:
            miercoles.config(bg="#000000")
        if jueves_s == False:
            jueves.config(bg="#F26D3D")  
        if viernes_s == False:
            viernes.config(bg="#000000") 
        
    elif ubicacion_programar == 20:
        if jueves_s == False:
            jueves.config(bg="#000000")  
        if viernes_s == False:
            viernes.config(bg="#F26D3D")  
        if sabado_s == False:
            sabado.config(bg="#000000")
            
    elif ubicacion_programar == 21: 
        if viernes_s == False:
            viernes.config(bg="#000000")  
        if sabado_s == False:
            sabado.config(bg="#F26D3D")  
        if domingo_s == False:
            domingo.config(bg="#000000") 
   
    elif ubicacion_programar == 22: 
        if sabado_s == False:
            sabado.config(bg="#000000")  
        if domingo_s == False:
            domingo.config(bg="#F26D3D")  
        if seis_am_s == False:
            seis_am.config(bg="#000000")
    elif ubicacion_programar == 23:
        if domingo_s == False:
            domingo.config(bg="#000000")  
        if seis_am_s == False:
            seis_am.config(bg="#F26D3D")  
        if siete_am_s == False:
            siete_am.config(bg="#000000")
            
    elif ubicacion_programar == 24: 
        if seis_am_s == False:
            seis_am.config(bg="#000000")  
        if siete_am_s == False:
            siete_am.config(bg="#F26D3D")  
        if cinco_pm_s == False:
            cinco_pm.config(bg="#000000")
            
    elif ubicacion_programar == 25: 
        if siete_am_s == False:
            siete_am.config(bg="#000000")  
        if cinco_pm_s == False:
            cinco_pm.config(bg="#F26D3D")  
        if seis_pm_s == False:
            seis_pm.config(bg="#000000")   
        
    elif ubicacion_programar == 26: 
        if cinco_pm_s == False:
            cinco_pm.config(bg="#000000")  
        if seis_pm_s == False:
            seis_pm.config(bg="#F26D3D")   
        if siete_pm_s == False:
            siete_pm.config(bg="#000000")
            
    elif ubicacion_programar == 27:
        if seis_pm_s == False:
            seis_pm.config(bg="#000000")   
        if siete_pm_s == False:
            siete_pm.config(bg="#F26D3D")   
        if cinco_min_s == False:
            cinco_min.config(bg="#000000")   
        
    elif ubicacion_programar == 28:   
        if siete_pm_s == False:
            siete_pm.config(bg="#000000")   
        if cinco_min_s == False:
            cinco_min.config(bg="#F26D3D")   
        if diez_min_s == False :
            diez_min.config(bg="#000000")
            
    elif ubicacion_programar == 29: 
        if cinco_min_s == False:
            cinco_min.config(bg="#000000")   
        if diez_min_s == False :
            diez_min.config(bg="#F26D3D")  
        if quince_min_s == False:
            quince_min.config(bg="#000000")
            
    elif ubicacion_programar == 30: 
        if diez_min_s == False :
            diez_min.config(bg="#000000")  
        if quince_min_s == False:
            quince_min.config(bg="#F26D3D")  
        if veinte_min_s == False:
            veinte_min.config(bg="#000000") 
       
    elif ubicacion_programar == 31: 
        if quince_min_s == False:
            quince_min.config(bg="#000000")  
        if veinte_min_s == False:
            veinte_min.config(bg="#F26D3D")  
        if treinta_min_s == False:
            treinta_min.config(bg="#000000")
            
    elif ubicacion_programar == 32: 
        if veinte_min_s == False:
            veinte_min.config(bg="#000000")  
        if treinta_min_s == False:
            treinta_min.config(bg="#F26D3D")  
        if regar_s == False:
            regar.config(bg="#000000")  
       
    elif ubicacion_programar == 33:
        regresar.config(bg="#000000")
        if treinta_min_s == False:
            treinta_min.config(bg="#000000")  
        if regar_s == False:
            regar.config(bg="#F26D3D")  
     
            
            
             
    elif ubicacion_programar == 34: 
        if regar_s == False or regresar_s == False:
            regar.config(bg="#000000")        
            regresar.config(bg="#F26D3D")
           
    #guardar programa   
    if (event.keysym=="KP_Begin"):      
        if ubicacion_programar == 1:
            if p_1_s==False:
                p_1.config(bg="#04BF9D")
                p_1_s=True
                
            else:
                p_1.config(bg="#000000")
                p_1_s=False
                
        elif ubicacion_programar == 2:
            if p_2_s==False:
                p_2.config(bg="#04BF9D")
                p_2_s=True                                
            else:
                p_2.config(bg="#000000")
                p_2_s=False
        elif ubicacion_programar == 3:
            if p_3_s==False:
                p_3.config(bg="#04BF9D")
                p_3_s=True                                
            else:
                p_3.config(bg="#000000")
                p_3_s=False
#         elif ubicacion_programar == 4:
#             if e_1_p_s==False:
#                 e_1_p.config(bg="#04BF9D")
#                 e_1_p_s=True                                
#             else:
#                 e_1_p.config(bg="#000000")
#                 e_1_p_s=False
        elif ubicacion_programar == 5:
            if e_2_p_s==False:
                e_2_p.config(bg="#04BF9D")
                e_2_p_s=True
                zona[0]="01"
                e_1_p.config(bg="#04BF9D")
                e_1_p_s=True
            else:
                e_2_p.config(bg="#000000")
                e_2_p_s=False
                zona[0]="--"
                e_1_p.config(bg="#000000")
                e_1_p_s=False
        elif ubicacion_programar == 6:
            if e_3_p_s==False:
                e_3_p.config(bg="#04BF9D")
                e_3_p_s=True
                zona[1]="02"
                e_1_p.config(bg="#04BF9D")
                e_1_p_s=True
            else:
                e_3_p.config(bg="#000000")
                e_3_p_s=False
                zona[1]="--"
                e_1_p.config(bg="#000000")
                e_1_p_s=False
        elif ubicacion_programar == 7:
            if e_4_p_s==False:
                e_4_p.config(bg="#04BF9D")
                e_4_p_s=True
                zona[2]="03"
                e_1_p.config(bg="#04BF9D")
                e_1_p_s=True
            else:
                e_4_p.config(bg="#000000")
                e_4_p_s=False
                zona[2]="--"
                e_1_p.config(bg="#000000")
                e_1_p_s=False
        elif ubicacion_programar == 8:
            if e_5_p_s==False:
                e_5_p.config(bg="#04BF9D")
                e_5_p_s=True
                zona[3]="04"
                e_1_p.config(bg="#04BF9D")
                e_1_p_s=True
            else:
                e_5_p.config(bg="#000000")
                e_5_p_s=False
                zona[3]="--"
                e_1_p.config(bg="#000000")
                e_1_p_s=False
#         elif ubicacion_programar == 9:
#             if e_6_p_s==False:
#                 e_6_p.config(bg="#04BF9D")
#                 e_6_p_s=True                                
#             else:
#                 e_6_p.config(bg="#000000")
#                 e_6_p_s=False
        elif ubicacion_programar == 10:
            if e_7_p_s==False:
                e_7_p.config(bg="#04BF9D")
                e_7_p_s=True
                zona[4]="05"
                e_6_p.config(bg="#04BF9D")
                e_6_p_s=True
            else:
                e_7_p.config(bg="#000000")
                e_7_p_s=False
                zona[4]="--"
                e_5_p.config(bg="#000000")
                e_5_p_s=False
        elif ubicacion_programar == 11:
            if e_8_p_s==False:
                e_8_p.config(bg="#04BF9D")
                e_8_p_s=True
                zona[5]="06"
                e_6_p.config(bg="#04BF9D")
                e_6_p_s=True
            else:
                e_8_p.config(bg="#000000")
                e_8_p_s=False
                zona[5]="--"
                e_5_p.config(bg="#000000")
                e_5_p_s=False
        elif ubicacion_programar == 12:
            if e_9_p_s==False:
                e_9_p.config(bg="#04BF9D")
                e_9_p_s=True
                zona[6]="07"
                e_6_p.config(bg="#04BF9D")
                e_6_p_s=True
            else:
                e_9_p.config(bg="#000000")
                e_9_p_s=False
                zona[6]="--"
                e_5_p.config(bg="#000000")
                e_5_p_s=False
        elif ubicacion_programar == 13:
            if e_10_p_s==False:
                e_10_p.config(bg="#04BF9D")
                e_10_p_s=True
                zona[7]="08"
                e_6_p.config(bg="#04BF9D")
                e_6_p_s=True
            else:
                e_10_p.config(bg="#000000")
                e_10_p_s=False
                zona[7]="--"
                e_5_p.config(bg="#000000")
                e_5_p_s=False
        elif ubicacion_programar == 14:
            if b_1_p_s==False:
                b_1_p.config(bg="#04BF9D")
                b_1_p_s=True
                bomba[0]="01"
            else:
                b_1_p.config(bg="#000000")
                b_1_p_s=False
                bomba[0]="--"
        elif ubicacion_programar == 15:
            if b_2_p_s==False:
                b_2_p.config(bg="#04BF9D")
                b_2_p_s=True
                bomba[1]="02"
            else:
                b_2_p.config(bg="#000000")
                b_2_p_s=False
                bomba[1]="--"
        elif ubicacion_programar == 16:
            if lunes_s==False:
                lunes.config(bg="#04BF9D")
                lunes_s=True
                dia[0]="L"
            else:
                lunes.config(bg="#000000")
                lunes_s=False
                dia[0]="-"
        elif ubicacion_programar == 17:
            if martes_s==False:
                martes.config(bg="#04BF9D")
                martes_s=True
                dia[1]="M"
            else:
                martes.config(bg="#000000")
                martes_s=False
                dia[1]="-"
        elif ubicacion_programar == 18:
            if miercoles_s==False:
                miercoles.config(bg="#04BF9D")
                miercoles_s=True
                dia[2]="M"
            else:
                miercoles.config(bg="#000000")
                miercoles_s=False
                dia[2]="-"
        elif ubicacion_programar == 19:
            if jueves_s==False:
                jueves.config(bg="#04BF9D")
                jueves_s=True
                dia[3]="J"
            else:
                jueves.config(bg="#000000")
                jueves_s=False
                dia[3]="-"
        elif ubicacion_programar == 20:
            if viernes_s==False:
                viernes.config(bg="#04BF9D")
                viernes_s=True
                dia[4]="V"
            else:
                viernes.config(bg="#000000")
                viernes_s=False
                dia[4]="-"
        elif ubicacion_programar == 21:
            if sabado_s==False:
                sabado.config(bg="#04BF9D")
                sabado_s=True
                dia[5]="S"
            else:
                sabado.config(bg="#000000")
                sabado_s=False
                dia[5]="-"
        elif ubicacion_programar == 22:
            if domingo_s==False:
                domingo.config(bg="#04BF9D")
                domingo_s=True
                dia[6]="D"
            else:
                domingo.config(bg="#000000")
                domingo_s=False
                dia[6]="-"
        elif ubicacion_programar == 23:
            if seis_am_s==False:
                seis_am.config(bg="#04BF9D")
                seis_am_s=True
                hora[0]="06:00"
                
            else:
                seis_am.config(bg="#000000")
                seis_am_s=False
                hora[0]="-----"
        elif ubicacion_programar == 24:
            if siete_am_s==False:
                siete_am.config(bg="#04BF9D")
                siete_am_s=True
                hora[0]="07:00"
            else:
                siete_am.config(bg="#000000")
                siete_am_s=False
                hora[0]="-----"
        elif ubicacion_programar == 25:
            if cinco_pm_s==False:
                cinco_pm.config(bg="#04BF9D")
                cinco_pm_s=True
                hora[0]="17:00"
            else:
                cinco_pm.config(bg="#000000")
                cinco_pm_s=False
                hora[0]="-----"
        elif ubicacion_programar == 26:
            if seis_pm_s==False:
                seis_pm.config(bg="#04BF9D")
                seis_pm_s=True
                hora[0]="18:00"
            else:
                seis_pm.config(bg="#000000")
                seis_pm_s=False
                hora[0]="-----"
        elif ubicacion_programar == 27:
            if siete_pm_s==False:
                siete_pm.config(bg="#04BF9D")
                siete_pm_s=True
                hora[0]="19:00"
            else:
                siete_pm.config(bg="#000000")
                siete_pm_s=False
                hora[0]="-----"
        elif ubicacion_programar == 28:
            if cinco_min_s==False:
                cinco_min.config(bg="#04BF9D")
                cinco_min_s=True
                tiempo[0]="05"
            else:
                cinco_min.config(bg="#000000")
                cinco_min_s=False
                tiempo[0]="--"
        elif ubicacion_programar == 29:
            if diez_min_s==False:
                diez_min.config(bg="#04BF9D")
                diez_min_s=True
                tiempo[0]="10"
            else:
                diez_min.config(bg="#000000")
                diez_min_s=False
                tiempo[0]="--"
        elif ubicacion_programar == 30:
            if quince_min_s==False:
                quince_min.config(bg="#04BF9D")
                quince_min_s=True
                tiempo[0]="15"
            else:
                quince_min.config(bg="#000000")
                quince_min_s=False
                tiempo[0]="--"
        elif ubicacion_programar == 31:
            if veinte_min_s==False:
                veinte_min.config(bg="#04BF9D")
                veinte_min_s=True
                tiempo[0]="20"
            else:
                veinte_min.config(bg="#000000")
                veinte_min_s=False
                tiempo[0]="--"
        elif ubicacion_programar == 32:
            if treinta_min_s==False:
                treinta_min.config(bg="#04BF9D")
                treinta_min_s=True
                tiempo[0]="30"
            else:
                treinta_min.config(bg="#000000")
                treinta_min_s=False
                tiempo[0]="--"
        elif ubicacion_programar == 33:
            regar.config(bg="#04BF9D")
            guardar_programas()
            p_1_s=p_2_s=p_3_s=False
            e_1_p_s=e_2_p_s=e_3_p_s=e_4_p_s=e_5_p_s=e_6_p_s=e_7_p_s=e_8_p_s=e_9_p_s=e_10_p_s=False
            b_1_p_s=b_2_p_s=False
            lunes_s=martes_s=miercoles_s=jueves_s=viernes_s=sabado_s=domingo_s=False
            seis_am_s=siete_am_s=cinco_pm_s=seis_pm_s=siete_pm_s=False
            cinco_min_s=diez_min_s=quince_min_s=veinte_min_s=treinta_min_s=False
            p_1.config(bg="#000000")
            p_2.config(bg="#000000")
            p_3.config(bg="#000000")
            e_1_p.config(bg="#000000")
            e_2_p.config(bg="#000000")
            e_3_p.config(bg="#000000")
            e_4_p.config(bg="#000000")
            e_5_p.config(bg="#000000")
            e_6_p.config(bg="#000000")
            e_7_p.config(bg="#000000")
            e_8_p.config(bg="#000000")
            e_9_p.config(bg="#000000")
            e_10_p.config(bg="#000000")
            b_1_p.config(bg="#000000")
            b_2_p.config(bg="#000000")
            lunes.config(bg="#000000")
            martes.config(bg="#000000")
            miercoles.config(bg="#000000")
            jueves.config(bg="#000000")
            viernes.config(bg="#000000")
            sabado.config(bg="#000000")
            domingo.config(bg="#000000")
            seis_am.config(bg="#000000")
            siete_am.config(bg="#000000")
            cinco_pm.config(bg="#000000")
            seis_pm.config(bg="#000000")
            siete_pm.config(bg="#000000")
            cinco_min.config(bg="#000000")
            diez_min.config(bg="#000000")
            quince_min.config(bg="#000000")
            veinte_min.config(bg="#000000")
            treinta_min.config(bg="#000000")
            dia=["-","-","-","-","-","-","-"]
            hora=["-----"]
            tiempo=["--"]
            zona=["--","--","--","--","--","--","--","--"]
            bomba=["--","--"]
            
        elif ubicacion_programar == 34:
            p_1_s=p_2_s=p_3_s=False
            e_1_p_s=e_2_p_s=e_3_p_s=e_4_p_s=e_5_p_s=e_6_p_s=e_7_p_s=e_8_p_s=e_9_p_s=e_10_p_s=False
            b_1_p_s=b_2_p_s=False
            lunes_s=martes_s=miercoles_s=jueves_s=viernes_s=sabado_s=domingo_s=False
            seis_am_s=siete_am_s=cinco_pm_s=seis_pm_s=siete_pm_s=False
            cinco_min_s=diez_min_s=quince_min_s=veinte_min_s=treinta_min_s=False
            p_1.config(bg="#000000")
            p_2.config(bg="#000000")
            p_3.config(bg="#000000")
            e_1_p.config(bg="#000000")
            e_2_p.config(bg="#000000")
            e_3_p.config(bg="#000000")
            e_4_p.config(bg="#000000")
            e_5_p.config(bg="#000000")
            e_6_p.config(bg="#000000")
            e_7_p.config(bg="#000000")
            e_8_p.config(bg="#000000")
            e_9_p.config(bg="#000000")
            e_10_p.config(bg="#000000")
            b_1_p.config(bg="#000000")
            b_2_p.config(bg="#000000")
            lunes.config(bg="#000000")
            martes.config(bg="#000000")
            miercoles.config(bg="#000000")
            jueves.config(bg="#000000")
            viernes.config(bg="#000000")
            sabado.config(bg="#000000")
            domingo.config(bg="#000000")
            seis_am.config(bg="#000000")
            siete_am.config(bg="#000000")
            cinco_pm.config(bg="#000000")
            seis_pm.config(bg="#000000")
            siete_pm.config(bg="#000000")
            cinco_min.config(bg="#000000")
            diez_min.config(bg="#000000")
            quince_min.config(bg="#000000")
            veinte_min.config(bg="#000000")
            treinta_min.config(bg="#000000")
            programar.destroy()
            
        
          
       
def ventana_programar():    
    global p_1,p_2,p_3
    global e_1_p,e_2_p,e_3_p,e_4_p,e_5_p,e_6_p,e_7_p,e_8_p,e_9_p,e_10_p,b_1_p,b_2_p
    global lunes,martes,miercoles,jueves,viernes,sabado,domingo
    global seis_am,siete_am,cinco_pm,seis_pm,siete_pm
    global cinco_min,diez_min,quince_min,veinte_min,treinta_min
    global regar,regresar
    global programar
    ventana.deiconify()
    programar=tk.Toplevel()
    programar.attributes("-fullscreen",True)
    programar.config(cursor="none") 
    #programar.geometry('350x200')
    programar.configure(background="#000000")    
    label_pagina=tk.Label(programar,text="PROGRAMAR RIEGO",font=("Helvetica",34),fg ="#A64B29",bg="#000000",width=28,height=2)
    label_pagina.grid(row=1,column=1,columnspan=5)
    #NUMERO DE PROGRAMA
    label_electrovalvula=tk.Label(programar,text="NUMERO DE PROGRAMA",font=("Helvetica",24),fg ="#A64B29",bg="#000000",width=28,height=1)
    label_electrovalvula.grid(row=2,column=1,columnspan=2)    
    p_1=tk.Button(programar,text =" 01 ",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    p_1.grid(row=2, column=3,padx=2,pady=1)
    p_1.config(bg="#F26D3D")    
    p_2=tk.Button(programar,text =" 02 ",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    p_2.grid(row=2, column=4,padx=2,pady=1)    
    p_3=tk.Button(programar,text =" 03 ",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    p_3.grid(row=2, column=5,padx=2,pady=1)    
    #ELECTROVALVULAS
    label_electrovalvula=tk.Label(programar,text="ELECTROVALVULAS",font=("Helvetica",24),fg ="#A64B29",bg="#000000",width=20,height=1)
    label_electrovalvula.grid(row=3,column=1,columnspan=2)    
    e_1_p=tk.Button(programar,text ="MAESTRA 01",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    e_1_p.grid(row=4, column=1,padx=2,pady=1)
    if e_1_s==False:
        e_1_p.config(fg="#283040")
    
    e_2_p=tk.Button(programar,text ="ZONA 01",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    if e_2_s==False:
        e_2_p.config(fg="#283040")
    e_2_p.grid(row=4, column=2,padx=2,pady=1)    
    
    e_3_p=tk.Button(programar,text ="ZONA 02",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    if e_3_s==False:
        e_3_p.config(fg="#283040")
    e_3_p.grid(row=4, column=3,padx=2,pady=1)    
    
    e_4_p=tk.Button(programar,text ="ZONA 03",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    if e_4_s==False:
        e_4_p.config(fg="#283040")
    e_4_p.grid(row=4, column=4,padx=2,pady=1)    
    
    e_5_p=tk.Button(programar,text ="ZONA 04",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    if e_5_s==False:
        e_5_p.config(fg="#283040")
    e_5_p.grid(row=4, column=5,padx=2,pady=1)    
    
    e_6_p=tk.Button(programar,text ="MAESTRA 02",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    if e_6_s==False:
        e_6_p.config(fg="#283040")
    e_6_p.grid(row=5, column=1,padx=2,pady=1)       
    
    e_7_p=tk.Button(programar,text ="ZONA 05",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    if e_7_s==False:
        e_7_p.config(fg="#283040")
    e_7_p.grid(row=5, column=2,padx=2,pady=1)    
    
    e_8_p=tk.Button(programar,text ="ZONA 06",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    if e_8_s==False:
        e_8_p.config(fg="#283040")
    e_8_p.grid(row=5, column=3,padx=2,pady=1)    
    
    e_9_p=tk.Button(programar,text ="ZONA 07",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    if e_9_s==False:
        e_9_p.config(fg="#283040")
    e_9_p.grid(row=5, column=4,padx=2,pady=1)    
    
    e_10_p=tk.Button(programar,text ="ZONA 08",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    if e_10_s==False:
        e_10_p.config(fg="#283040")
    e_10_p.grid(row=5, column=5,padx=2,pady=1)    
    #ELECTROBOMBAS
    label_electrovalvula=tk.Label(programar,text="ELECTROBOMBAS",font=("Helvetica",24),fg ="#A64B29",bg="#000000",width=20,height=1)
    label_electrovalvula.grid(row=6,column=1,columnspan=2)    
    b_1_p=tk.Button(programar,text ="ELECTROBOMBA 01",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=18,height=1)
    if b_1_s==False:
        b_1_p.config(fg="#283040")
    b_1_p.grid(row=7, column=1,padx=2,pady=1)       
    
    b_2_p=tk.Button(programar,text ="ELECTROBOMBA 02",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=18,height=1)
    if b_2_s==False:
        b_2_p.config(fg="#283040")
    b_2_p.grid(row=7, column=2,padx=2,pady=1,columnspan=2)    
    #DIAS
    label_electrovalvula=tk.Label(programar,text="DIAS",font=("Helvetica",24),fg ="#A64B29",bg="#000000",width=20,height=1)
    label_electrovalvula.grid(row=8,column=1,columnspan=2)    
    lunes=tk.Button(programar,text ="LUNES",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    lunes.grid(row=9, column=1,padx=2,pady=1)       
    martes=tk.Button(programar,text ="MARTES",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    martes.grid(row=9, column=2,padx=2,pady=1)    
    miercoles=tk.Button(programar,text ="MIERCOLES",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    miercoles.grid(row=9, column=3,padx=2,pady=1)       
    jueves=tk.Button(programar,text ="JUEVES",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    jueves.grid(row=9, column=4,padx=2,pady=1)    
    viernes=tk.Button(programar,text ="VIERNES",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    viernes.grid(row=9, column=5,padx=2,pady=1)    
    sabado=tk.Button(programar,text ="SABADO",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    sabado.grid(row=10, column=1,padx=2,pady=1)    
    domingo=tk.Button(programar,text ="DOMINGO",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    domingo.grid(row=10, column=2,padx=2,pady=1)    
    #HORARIO
    label_electrovalvula=tk.Label(programar,text="HORA DE INICIO",font=("Helvetica",24),fg ="#A64B29",bg="#000000",width=20,height=1)
    label_electrovalvula.grid(row=11,column=1,columnspan=2)    
    seis_am=tk.Button(programar,text ="06:00",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    seis_am.grid(row=12, column=1,padx=2,pady=1)       
    siete_am=tk.Button(programar,text ="07:00",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    siete_am.grid(row=12, column=2,padx=2,pady=1)    
    cinco_pm=tk.Button(programar,text ="17:00",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    cinco_pm.grid(row=12, column=3,padx=2,pady=1)       
    seis_pm=tk.Button(programar,text ="18:00",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    seis_pm.grid(row=12, column=4,padx=2,pady=1)    
    siete_pm=tk.Button(programar,text ="19:00",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    siete_pm.grid(row=12, column=5,padx=2,pady=1)    
    #DURACION
    label_electrovalvula=tk.Label(programar,text="DURACION",font=("Helvetica",24),fg ="#A64B29",bg="#000000",width=20,height=1)
    label_electrovalvula.grid(row=13,column=1,columnspan=2)    
    cinco_min=tk.Button(programar,text ="05 min",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    cinco_min.grid(row=14, column=1,padx=2,pady=1)       
    diez_min=tk.Button(programar,text ="10 min",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    diez_min.grid(row=14, column=2,padx=2,pady=1)    
    quince_min=tk.Button(programar,text ="15 min",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    quince_min.grid(row=14, column=3,padx=2,pady=1)       
    veinte_min=tk.Button(programar,text ="20 min",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    veinte_min.grid(row=14, column=4,padx=2,pady=1)    
    treinta_min=tk.Button(programar,text ="30 min",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    treinta_min.grid(row=14, column=5,padx=2,pady=1)    
    regar=tk.Button(programar,text ="GUARDAR",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    regar.grid(row=15, column=1,padx=2,pady=1,columnspan=2,rowspan=2)    
    #no_regar=tk.Button(programar,text ="NO REGAR",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    #no_regar.grid(row=15, column=3,padx=2,pady=1)    
    regresar=tk.Button(programar,text ="REGRESAR",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    regresar.grid(row=15, column=4,padx=2,pady=1,columnspan=2)    
    programar.bind("<KeyPress>",programar_cursor)
    
def programas_cursor(event):
    if (event.keysym=="KP_Begin"):
        programas.destroy()
    
def ventana_programas():
    global programas 
    ventana.deiconify()
    programas=tk.Toplevel()
    programas.attributes("-fullscreen",True)
    programas.config(cursor="none") 
    #programas.geometry('350x200')
    programas.configure(background="#000000")
    
    with open('/home/pi/Documents/riego/programas_riego.json') as file:
        programas_riego=json.load(file)
        
    label_programa_01=tk.Label(programas,text="PROGRAMA 01",font=("Helvetica",26),fg ="#A64B29",bg="#000000",width=20,height=1,anchor="center")
    label_programa_01.grid(row=1,column=1,columnspan=2)
    label_programa_01_dia=tk.Label(programas,text="DIAS:",font=("Helvetica",22),fg ="#FFFFFF",bg="#000000",width=20,height=1,anchor="w",padx=20)
    label_programa_01_dia.grid(row=2,column=1)
    label_programa_01_dia=tk.Label(programas,text=programas_riego["programa-01"]["dia"],font=("Helvetica",22),fg ="#FFFFFF",bg="#000000",width=20,height=1,anchor="w")
    label_programa_01_dia.grid(row=2,column=2)
    label_programa_01_hora=tk.Label(programas,text="HORA:",font=("Helvetica",22),fg ="#FFFFFF",bg="#000000",width=20,height=1,anchor="w")
    label_programa_01_hora.grid(row=3,column=1)
    label_programa_01_hora=tk.Label(programas,text=programas_riego["programa-01"]["hora"],font=("Helvetica",22),fg ="#FFFFFF",bg="#000000",width=20,height=1,anchor="w")
    label_programa_01_hora.grid(row=3,column=2)
    label_programa_01_tiempo=tk.Label(programas,text="DURACION:",font=("Helvetica",22),fg ="#FFFFFF",bg="#000000",width=20,height=1,anchor="w")
    label_programa_01_tiempo.grid(row=4,column=1)
    label_programa_01_tiempo=tk.Label(programas,text=programas_riego["programa-01"]["tiempo"]+" min",font=("Helvetica",22),fg ="#FFFFFF",bg="#000000",width=20,height=1,anchor="w")
    label_programa_01_tiempo.grid(row=4,column=2)
    label_programa_01_zona=tk.Label(programas,text="ZONAS:",font=("Helvetica",22),fg ="#FFFFFF",bg="#000000",width=20,height=1,anchor="w")
    label_programa_01_zona.grid(row=5,column=1)
    label_programa_01_zona=tk.Label(programas,text=programas_riego["programa-01"]["zona"][0:2]+" "+programas_riego["programa-01"]["zona"][2:4]+" "+programas_riego["programa-01"]["zona"][4:6]+" "+programas_riego["programa-01"]["zona"][6:8]
                                    +" "+programas_riego["programa-01"]["zona"][8:10]+" "+programas_riego["programa-01"]["zona"][10:12]+" "+programas_riego["programa-01"]["zona"][12:14]+" "+programas_riego["programa-01"]["zona"][14:16],font=("Helvetica",22),fg ="#FFFFFF",bg="#000000",width=20,height=1,anchor="w")
    label_programa_01_zona.grid(row=5,column=2)
    label_programa_01_bomba=tk.Label(programas,text="ELECTROBOMBAS:",font=("Helvetica",22),fg ="#FFFFFF",bg="#000000",width=20,height=1,anchor="w")
    label_programa_01_bomba.grid(row=6,column=1)
    label_programa_01_bomba=tk.Label(programas,text=programas_riego["programa-01"]["bomba"][0:2]+" "+programas_riego["programa-01"]["bomba"][2:4],font=("Helvetica",22),fg ="#FFFFFF",bg="#000000",width=20,height=1,anchor="w")
    label_programa_01_bomba.grid(row=6,column=2)
    
    label_programa_02=tk.Label(programas,text="PROGRAMA 02",font=("Helvetica",26),fg ="#A64B29",bg="#000000",width=20,height=1)
    label_programa_02.grid(row=7,column=1,columnspan=2)
    label_programa_02_dia=tk.Label(programas,text="DIAS:",font=("Helvetica",22),fg ="#FFFFFF",bg="#000000",width=20,height=1,anchor="w")
    label_programa_02_dia.grid(row=8,column=1)
    label_programa_02_dia=tk.Label(programas,text=programas_riego["programa-02"]["dia"],font=("Helvetica",22),fg ="#FFFFFF",bg="#000000",width=20,height=1,anchor="w")
    label_programa_02_dia.grid(row=8,column=2)
    label_programa_02_hora=tk.Label(programas,text="HORA:",font=("Helvetica",22),fg ="#FFFFFF",bg="#000000",width=20,height=1,anchor="w")
    label_programa_02_hora.grid(row=9,column=1)
    label_programa_02_hora=tk.Label(programas,text=programas_riego["programa-02"]["hora"],font=("Helvetica",22),fg ="#FFFFFF",bg="#000000",width=20,height=1,anchor="w")
    label_programa_02_hora.grid(row=9,column=2)
    label_programa_02_tiempo=tk.Label(programas,text="DURACION:",font=("Helvetica",22),fg ="#FFFFFF",bg="#000000",width=20,height=1,anchor="w")
    label_programa_02_tiempo.grid(row=10,column=1)
    label_programa_02_tiempo=tk.Label(programas,text=programas_riego["programa-02"]["tiempo"]+" min",font=("Helvetica",22),fg ="#FFFFFF",bg="#000000",width=20,height=1,anchor="w")
    label_programa_02_tiempo.grid(row=10,column=2)
    label_programa_02_zona=tk.Label(programas,text="ZONAS:",font=("Helvetica",22),fg ="#FFFFFF",bg="#000000",width=20,height=1,anchor="w")
    label_programa_02_zona.grid(row=11,column=1)
    label_programa_02_zona=tk.Label(programas,text=programas_riego["programa-02"]["zona"][0:2]+" "+programas_riego["programa-02"]["zona"][2:4]+" "+programas_riego["programa-02"]["zona"][4:6]+" "+programas_riego["programa-02"]["zona"][6:8]
                                    +" "+programas_riego["programa-02"]["zona"][8:10]+" "+programas_riego["programa-02"]["zona"][10:12]+" "+programas_riego["programa-02"]["zona"][12:14]+" "+programas_riego["programa-02"]["zona"][14:16],font=("Helvetica",22),fg ="#FFFFFF",bg="#000000",width=20,height=1,anchor="w")
    label_programa_02_zona.grid(row=11,column=2)
    label_programa_02_bomba=tk.Label(programas,text="ELECTROBOMBAS:",font=("Helvetica",22),fg ="#FFFFFF",bg="#000000",width=20,height=1,anchor="w")
    label_programa_02_bomba.grid(row=12,column=1)
    label_programa_02_bomba=tk.Label(programas,text=programas_riego["programa-02"]["bomba"][0:2]+" "+programas_riego["programa-02"]["bomba"][2:4],font=("Helvetica",22),fg ="#FFFFFF",bg="#000000",width=20,height=1,anchor="w")
    label_programa_02_bomba.grid(row=12,column=2)
    
    label_programa_03=tk.Label(programas,text="PROGRAMA 03",font=("Helvetica",26),fg ="#A64B29",bg="#000000",width=20,height=1)
    label_programa_03.grid(row=13,column=1,columnspan=2)
    label_programa_03_dia=tk.Label(programas,text="DIAS:",font=("Helvetica",22),fg ="#FFFFFF",bg="#000000",width=20,height=1,anchor="w")
    label_programa_03_dia.grid(row=14,column=1)
    label_programa_03_dia=tk.Label(programas,text=programas_riego["programa-03"]["dia"],font=("Helvetica",22),fg ="#FFFFFF",bg="#000000",width=20,height=1,anchor="w")
    label_programa_03_dia.grid(row=14,column=2)
    label_programa_03_hora=tk.Label(programas,text="HORA:",font=("Helvetica",22),fg ="#FFFFFF",bg="#000000",width=20,height=1,anchor="w")
    label_programa_03_hora.grid(row=15,column=1)
    label_programa_03_hora=tk.Label(programas,text=programas_riego["programa-03"]["hora"],font=("Helvetica",22),fg ="#FFFFFF",bg="#000000",width=20,height=1,anchor="w")
    label_programa_03_hora.grid(row=15,column=2)
    label_programa_03_tiempo=tk.Label(programas,text="DURACION:",font=("Helvetica",22),fg ="#FFFFFF",bg="#000000",width=20,height=1,anchor="w")
    label_programa_03_tiempo.grid(row=16,column=1)
    label_programa_03_tiempo=tk.Label(programas,text=programas_riego["programa-03"]["tiempo"]+" min",font=("Helvetica",22),fg ="#FFFFFF",bg="#000000",width=20,height=1,anchor="w")
    label_programa_03_tiempo.grid(row=16,column=2)
    label_programa_03_zona=tk.Label(programas,text="ZONAS:",font=("Helvetica",22),fg ="#FFFFFF",bg="#000000",width=20,height=1,anchor="w")
    label_programa_03_zona.grid(row=17,column=1)
    label_programa_03_zona=tk.Label(programas,text=programas_riego["programa-03"]["zona"][0:2]+" "+programas_riego["programa-03"]["zona"][2:4]+" "+programas_riego["programa-03"]["zona"][4:6]+" "+programas_riego["programa-03"]["zona"][6:8]
                                    +" "+programas_riego["programa-03"]["zona"][8:10]+" "+programas_riego["programa-03"]["zona"][10:12]+" "+programas_riego["programa-03"]["zona"][12:14]+" "+programas_riego["programa-03"]["zona"][14:16],font=("Helvetica",22),fg ="#FFFFFF",bg="#000000",width=20,height=1,anchor="w")
    label_programa_03_zona.grid(row=17,column=2)  
    label_programa_03_bomba=tk.Label(programas,text="ELECTROBOMBAS:",font=("Helvetica",22),fg ="#FFFFFF",bg="#000000",width=20,height=1,anchor="w")
    label_programa_03_bomba.grid(row=18,column=1)
    label_programa_03_bomba=tk.Label(programas,text=programas_riego["programa-03"]["bomba"][0:2]+" "+programas_riego["programa-03"]["bomba"][2:4],font=("Helvetica",22),fg ="#FFFFFF",bg="#000000",width=20,height=1,anchor="w")
    label_programa_03_bomba.grid(row=18,column=2)    
    label_sensores=tk.Label(programas,text="SENSORES",font=("Helvetica",26),fg ="#A64B29",bg="#000000",width=20,height=1)
    label_sensores.grid(row=1,column=3,columnspan=2) 
    #base_datos = sqlite3.connect('/home/pi/datosSensor/prueba3-base.db')
    base_datos = sqlite3.connect('/home/pi/datosSensor/prueba3.db')
    datos = base_datos.cursor()
    datos.execute('SELECT * FROM DATASENSOR3')
    rows = datos.fetchall()
    dates = []
    values = []
    i=len(rows) 
    graficar = rows[i-60:i] 
    i=0

    for row in graficar:
        i=i+1
        values.append(row[0])
        #fecha = str(pd.to_datetime(row[1],unit='ms'))
        #dates.append(fecha[14:19])
        dates.append(i)
        #print(dates)
    
    figure = plt.Figure(figsize=(5,5), dpi=100)
    grafica = figure.add_subplot(1,1,1)
    grafica.plot(dates,values,'-')
    grafica.set_title("CAUDAL")
    grafica.set_xlabel("Tiempo")
    grafica.set_ylabel("Caudal")

    canvas = FigureCanvasTkAgg(figure,programas)
    canvas.get_tk_widget().grid(row=2, column=3, rowspan=15 ,columnspan=2)   
    
    programas.bind("<KeyPress>",programas_cursor)

def manual_cursor(event):
    global e_1_m_s,e_2_m_s,e_3_m_s,e_4_m_s,e_5_m_s,e_6_m_s,e_7_m_s,e_8_m_s,e_9_m_s,e_10_m_s,b_1_m_s,b_2_m_s
    global regar_m_s,regresar_m_s
    global ubicacion_manual
    if (event.keysym=="KP_Right"):
        ubicacion_manual=ubicacion_manual+1
        if ubicacion_manual <=14 and ubicacion_manual>0:
            print("")
        else:
            ubicacion_manual = 1    
            
    elif (event.keysym=="KP_Left"):
        ubicacion_manual=ubicacion_manual-1
        if ubicacion_manual <=14  and ubicacion_manual>0:
            print("")
        else:
            ubicacion_manual = 1
    
    if ubicacion_manual == 1:        
        if e_1_m_s == False:
            e_1_m.config(bg="#F26D3D")
        if e_2_m_s == False:
            e_2_m.config(bg="#000000")
        if regresar_m_s == False:
            regresar_m.config(bg="#000000")
           
    elif ubicacion_manual == 2:        
        if e_1_m_s == False:
            e_1_m.config(bg="#000000")
        if e_2_m_s == False:
            e_2_m.config(bg="#F26D3D")
        if e_3_m_s == False:
            e_3_m.config(bg="#000000")
            
    elif ubicacion_manual == 3:        
        if e_2_m_s == False:
            e_2_m.configure(bg="#000000")
        if e_3_m_s == False:
            e_3_m.config(bg="#F26D3D")
        if e_4_m_s == False:
            e_4_m.config(bg="#000000")     
       
    elif ubicacion_manual == 4: 
        if e_3_m_s == False:
            e_3_m.configure(bg="#000000")
        if e_4_m_s == False:
            e_4_m.config(bg="#F26D3D")
        if e_5_m_s == False:
            e_5_m.config(bg="#000000")
            
    elif ubicacion_manual == 5:  
        if e_4_m_s == False:
            e_4_m.config(bg="#000000")
        if e_5_m_s == False:
            e_5_m.config(bg="#F26D3D")
        if e_6_m_s == False:
            e_6_m.config(bg="#000000")
            
    elif ubicacion_manual == 6:
        if e_5_m_s == False:
            e_5_m.config(bg="#000000")
        if e_6_m_s == False:
            e_6_m.config(bg="#F26D3D")
        if e_7_m_s == False:
            e_7_m.config(bg="#000000")       
           
    elif ubicacion_manual == 7:   
        if e_6_m_s == False:
            e_6_m.config(bg="#000000")
        if e_7_m_s == False:
            e_7_m.config(bg="#F26D3D")
        if e_8_m_s == False:
            e_8_m.config(bg="#000000")
            
    elif ubicacion_manual == 8: 
        if e_7_m_s == False:
            e_7_m.config(bg="#000000")
        if e_8_m_s == False:
            e_8_m.config(bg="#F26D3D")
        if e_9_m_s == False:
            e_9_m.config(bg="#000000")
            
    elif ubicacion_manual == 9: 
        if e_8_m_s == False:
            e_8_m.config(bg="#000000")
        if e_9_m_s == False:
            e_9_m.config(bg="#F26D3D")
        if e_10_m_s == False:
            e_10_m.config(bg="#000000")        
            
    elif ubicacion_manual ==10: 
        if e_9_m_s == False:
            e_9_m.config(bg="#000000")
        if e_10_m_s == False:
            e_10_m.config(bg="#F26D3D")
        if b_1_m_s == False:
            b_1_m.config(bg="#000000")
        
    elif ubicacion_manual == 11: 
        if e_10_m_s == False:
            e_10_m.config(bg="#000000")
        if b_1_m_s == False:
            b_1_m.config(bg="#F26D3D")
        if b_2_m_s == False:
            b_2_m.config(bg="#000000")
            
    elif ubicacion_manual == 12:  
        if b_1_m_s == False:
            b_1_m.config(bg="#000000")
        if b_2_m_s == False:
            b_2_m.config(bg="#F26D3D")
        if regar_m_s == False:
            regar_m.config(bg="#000000")
    
    elif ubicacion_manual == 13:        
        if b_2_m_s == False:
            b_2_m.config(bg="#000000")  
        if regar_m_s == False:
            regar_m.config(bg="#F26D3D")
        if regresar_m_s == False:
            regresar_m.config(bg="#000000")
            
    elif ubicacion_manual == 14: 
        if regar_m_s == False:
            regar_m.config(bg="#000000")
        if regresar_m_s == False:
            regresar_m.config(bg="#F26D3D")
    
    if (event.keysym=="KP_Begin"):      
        if ubicacion_manual == 2:
            if e_2_m_s==False:
                e_2_m.config(bg="#04BF9D")
                e_2_m_s=True                
                e_1_m.config(bg="#04BF9D")
                e_1_m_s=True
            else:
                e_2_m.config(bg="#000000")
                e_2_m_s=False                
                e_1_m.config(bg="#000000")
                e_1_m_s=False
            
        elif ubicacion_manual == 3:
            if e_3_m_s==False:
                e_3_m.config(bg="#04BF9D")
                e_3_m_s=True                
                e_1_m.config(bg="#04BF9D")
                e_1_m_s=True
            else:
                e_3_m.config(bg="#000000")
                e_3_m_s=False                
                e_1_m.config(bg="#000000")
                e_1_m_s=False
        elif ubicacion_manual == 4:
            if e_4_m_s==False:
                e_4_m.config(bg="#04BF9D")
                e_4_m_s=True                
                e_1_m.config(bg="#04BF9D")
                e_1_m_s=True
            else:
                e_4_m.config(bg="#000000")
                e_4_m_s=False                
                e_1_m.config(bg="#000000")
                e_1_m_s=False
        elif ubicacion_manual == 5:
            if e_5_m_s==False:
                e_5_m.config(bg="#04BF9D")
                e_5_m_s=True                
                e_1_m.config(bg="#04BF9D")
                e_1_m_s=True
            else:
                e_5_m.config(bg="#000000")
                e_5_m_s=False                
                e_1_m.config(bg="#000000")
                e_1_m_s=False
#         elif ubicacion_programar == 9:
#             if e_6_p_s==False:
#                 e_6_p.config(bg="#04BF9D")
#                 e_6_p_s=True                                
#             else:
#                 e_6_p.config(bg="#000000")
#                 e_6_p_s=False
        elif ubicacion_manual == 7:
            if e_7_m_s==False:
                e_7_m.config(bg="#04BF9D")
                e_7_m_s=True                
                e_6_m.config(bg="#04BF9D")
                e_6_m_s=True
            else:
                e_7_m.config(bg="#000000")
                e_7_m_s=False                
                e_6_m.config(bg="#000000")
                e_6_m_s=False
        elif ubicacion_manual == 8:
            if e_8_m_s==False:
                e_8_m.config(bg="#04BF9D")
                e_8_m_s=True                
                e_6_m.config(bg="#04BF9D")
                e_6_m_s=True
            else:
                e_8_m.config(bg="#000000")
                e_8_m_s=False                
                e_6_m.config(bg="#000000")
                e_6_m_s=False
        elif ubicacion_manual == 9:
            if e_9_m_s==False:
                e_9_m.config(bg="#04BF9D")
                e_9_m_s=True
                e_6_m.config(bg="#04BF9D")
                e_6_m_s=True
            else:
                e_9_m.config(bg="#000000")
                e_9_m_s=False                
                e_6_m.config(bg="#000000")
                e_6_m_s=False
        elif ubicacion_manual == 10:
            if e_10_m_s==False:
                e_10_m.config(bg="#04BF9D")
                e_10_m_s=True
                e_6_m.config(bg="#04BF9D")
                e_6_m_s=True
            else:
                e_10_m.config(bg="#000000")
                e_10_m_s=False
                e_6_m.config(bg="#000000")
                e_6_m_s=False
        elif ubicacion_manual== 11:
            if b_1_m_s==False:
                b_1_m.config(bg="#04BF9D")
                b_1_m_s=True
                
            else:
                b_1_m.config(bg="#000000")
                b_1_m_s=False
                
        elif ubicacion_manual == 12:
            if b_2_m_s==False:
                b_2_m.config(bg="#04BF9D")
                b_2_m_s=True
                
            else:
                b_2_m.config(bg="#000000")
                b_2_m_s=False
               
        
        elif ubicacion_manual == 13:
            if regar_m_s==False:
                regar_m.config(bg="#04BF9D")
                regar_m_s=True
                
                if e_2_m_s==True:
                    maestra_01.off()                
                    zona_01.off()
                if e_3_m_s==True:
                    maestra_01.off()                
                    zona_02.off()
                if e_4_m_s==True:
                    maestra_01.off()                
                    zona_03.off()
                if e_5_m_s==True:
                    maestra_01.off()                
                    zona_04.off()
                if e_7_m_s==True:
                    maestra_02.off()                
                    zona_05.off()
                if e_8_m_s==True:
                    maestra_02.off()                
                    zona_06.off()
                if e_9_m_s==True:
                    maestra_02.on()                
                    zona_07.off()
                if e_10_m_s==True:
                    maestra_02.off()                
                    zona_08.off()
                
                if b_1_m_s == True:
                    electrobomba_01.off()
                
                if b_2_m_s == True:
                    electrobomba_02.off()
                
                e_1_m_s=e_2_m_s=e_3_m_s=e_4_m_s=e_5_m_s=e_6_m_s=e_7_m_s=e_8_m_s=e_9_m_s=e_10_m_s=False
                b_1_m_s=b_2_m_s=False
                e_1_m.config(bg="#000000")
                e_2_m.config(bg="#000000")
                e_3_m.config(bg="#000000")
                e_4_m.config(bg="#000000")
                e_5_m.config(bg="#000000")
                e_6_m.config(bg="#000000")
                e_7_m.config(bg="#000000")
                e_8_m.config(bg="#000000")
                e_9_m.config(bg="#000000")
                e_10_m.config(bg="#000000")
                b_1_m.config(bg="#000000")
                b_2_m.config(bg="#000000")
                 
            else:
                regar_m.config(bg="#000000")
                regar_m_s=False
                maestra_01.on()                
                zona_01.on()
                zona_02.on()
                zona_03.on()
                zona_04.on()
                maestra_02.on()                
                zona_05.on()
                zona_06.on()
                zona_07.on()
                zona_18.on()
                electrobomba_01.on()
                electrobomba_02.on()
            
                        
        elif ubicacion_manual == 14:
            
            e_1_m_s=e_2_m_s=e_3_m_s=e_4_m_s=e_5_m_s=e_6_m_s=e_7_m_s=e_8_m_s=e_9_m_s=e_10_m_s=False
            b_1_m_s=b_2_m_s=False
            e_1_m.config(bg="#000000")
            e_2_m.config(bg="#000000")
            e_3_m.config(bg="#000000")
            e_4_m.config(bg="#000000")
            e_5_m.config(bg="#000000")
            e_6_m.config(bg="#000000")
            e_7_m.config(bg="#000000")
            e_8_m.config(bg="#000000")
            e_9_m.config(bg="#000000")
            e_10_m.config(bg="#000000")
            b_1_m.config(bg="#000000")
            b_2_m.config(bg="#000000")  
            manual.destroy()
        
    
    
    
    
    
def manual_regar():    
    #global programas
    global manual
    global e_1_m,e_2_m,e_3_m,e_4_m,e_5_m,e_6_m,e_7_m,e_8_m,e_9_m,e_10_m,b_1_m,b_2_m,regar_m,regresar_m
    ventana.deiconify()
    manual=tk.Toplevel()
    manual.attributes("-fullscreen",True)
    manual.config(cursor="none") 
    #manual.geometry('350x200')
    manual.configure(background="#000000")
    
    label_manual=tk.Label(manual,text="RIEGO MANUAL",font=("Helvetica",34),fg ="#A64B29",bg="#000000",width=28,height=2)
    label_manual.grid(row=1,column=1,columnspan=5)        
    #ELECTROVALVULAS
    label_electrovalvula_manual=tk.Label(manual,text="ELECTROVALVULAS",font=("Helvetica",24),fg ="#A64B29",bg="#000000",width=20,height=1)
    label_electrovalvula_manual.grid(row=3,column=1,columnspan=2)
    
    
    e_1_m=tk.Button(manual,text ="MAESTRA 01",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    e_1_m.grid(row=4, column=1,padx=2,pady=1)
    e_1_m.config(bg="#F26D3D")
    if e_1_s==False:
        e_1_p.config(fg="#283040")
    
    e_2_m=tk.Button(manual,text ="ZONA 01",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    if e_2_s==False:
        e_2_m.config(fg="#283040")
    e_2_m.grid(row=4, column=2,padx=2,pady=1)    
    
    e_3_m=tk.Button(manual,text ="ZONA 02",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    if e_3_s==False:
        e_3_m.config(fg="#283040")
        
    e_3_m.grid(row=4, column=3,padx=2,pady=1)    
    
    e_4_m=tk.Button(manual,text ="ZONA 03",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    if e_4_s==False:
        e_4_m.config(fg="#283040")
    e_4_m.grid(row=4, column=4,padx=2,pady=1)    
    
    e_5_m=tk.Button(manual,text ="ZONA 04",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    if e_5_s==False:
        e_5_m.config(fg="#283040")
    e_5_m.grid(row=4, column=5,padx=2,pady=1)    
    
    e_6_m=tk.Button(manual,text ="MAESTRA 02",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    if e_6_s==False:
        e_6_m.config(fg="#283040")
    e_6_m.grid(row=5, column=1,padx=2,pady=1)       
    
    e_7_m=tk.Button(manual,text ="ZONA 05",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    if e_7_s==False:
        e_7_m.config(fg="#283040")
    e_7_m.grid(row=5, column=2,padx=2,pady=1)    
    
    e_8_m=tk.Button(manual,text ="ZONA 06",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    if e_8_s==False:
        e_8_m.config(fg="#283040")
    e_8_m.grid(row=5, column=3,padx=2,pady=1)    
    
    e_9_m=tk.Button(manual,text ="ZONA 07",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    if e_9_s==False:
        e_9_m.config(fg="#283040")
    e_9_m.grid(row=5, column=4,padx=2,pady=1)    
    
    e_10_m=tk.Button(manual,text ="ZONA 08",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    if e_10_s==False:
        e_10_m.config(fg="#283040")
    e_10_m.grid(row=5, column=5,padx=2,pady=1)    
    #ELECTROBOMBAS
    label_electrovalvula=tk.Label(manual,text="ELECTROBOMBAS",font=("Helvetica",24),fg ="#A64B29",bg="#000000",width=20,height=1)
    label_electrovalvula.grid(row=6,column=1,columnspan=2)    
    b_1_m=tk.Button(manual,text ="ELECTROBOMBA 01",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=18,height=1)
    if b_1_s==False:
        b_1_m.config(fg="#283040")
    b_1_m.grid(row=7, column=2,padx=2,pady=1)       
    
    b_2_m=tk.Button(manual,text ="ELECTROBOMBA 02",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=18,height=1)
    if b_2_s==False:
        b_2_m.config(fg="#283040")
    b_2_m.grid(row=7, column=4,padx=2,pady=1)    
        
    regar_m=tk.Button(manual,text ="REGAR",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    regar_m.grid(row=15, column=1,padx=2,pady=1,columnspan=2,rowspan=2)    
        
    regresar_m=tk.Button(manual,text ="REGRESAR",fg ="#FFFFFF",bg="#000000",font=("Helvetica",18),width=17,height=1)
    regresar_m.grid(row=15, column=4,padx=2,pady=1,columnspan=2)    
    manual.bind("<KeyPress>",manual_cursor)
    
def abrir_ventana():
    if ubicacion == 1:
        ventana_zonas()
    elif ubicacion == 2:
        ventana_programar()
    elif ubicacion == 3:
        ventana_programas()
    elif ubicacion == 4:
        manual_regar()


#PRINCIPAL     
def handler(event):
        global ubicacion    
        if (event.keysym=="KP_Up"):
            ubicacion=ubicacion-2
            if ubicacion <=4 and ubicacion>0:
                print("")
            else:
                ubicacion = 1
                boton_zona.config(bg="#F26D3D")
                boton_sensores.config(bg="#04BF9D")
                boton_estado.config(bg="#04BF9D")
                boton_configuracion.config(bg="#04BF9D")              
        
        elif (event.keysym=="KP_Right"):
            ubicacion=ubicacion+1
            if ubicacion <=4 and ubicacion>0:
                print("")
            else:
                ubicacion = 1
                boton_zona.config(bg="#F26D3D")
                boton_sensores.config(bg="#04BF9D")
                boton_estado.config(bg="#04BF9D")
                boton_configuracion.config(bg="#04BF9D")
        elif (event.keysym=="KP_Left"):
            ubicacion=ubicacion-1
            if ubicacion <=4 and ubicacion>0:
                print("")
            else:
                ubicacion = 1
                boton_zona.config(bg="#F26D3D")
                boton_sensores.config(bg="#04BF9D")
                boton_estado.config(bg="#04BF9D")
                boton_configuracion.config(bg="#04BF9D")
        elif (event.keysym=="KP_Down"):
            ubicacion=ubicacion+2
            if ubicacion <=4 and ubicacion>0:
                print("")
            else:
                ubicacion = 1
                boton_zona.config(bg="#F26D3D")
                boton_sensores.config(bg="#04BF9D")
                boton_estado.config(bg="#04BF9D")
                boton_configuracion.config(bg="#04BF9D")
                
        elif (event.keysym=="KP_Begin"):
            abrir_ventana()           
            
        if ubicacion == 1:
            boton_zona.config(bg="#F26D3D")
            boton_sensores.config(bg="#04BF9D")
            boton_estado.config(bg="#04BF9D")
            boton_configuracion.config(bg="#04BF9D")
        elif ubicacion == 2:
            boton_zona.config(bg="#04BF9D")
            boton_sensores.config(bg="#F26D3D")
            boton_estado.config(bg="#04BF9D")
            boton_configuracion.config(bg="#04BF9D")        
        elif ubicacion == 3:
            boton_zona.config(bg="#04BF9D")
            boton_sensores.config(bg="#04BF9D")
            boton_estado.config(bg="#F26D3D")
            boton_configuracion.config(bg="#04BF9D")             
        elif ubicacion == 4:
            boton_zona.config(bg="#04BF9D")
            boton_sensores.config(bg="#04BF9D")
            boton_estado.config(bg="#04BF9D")
            boton_configuracion.config(bg="#F26D3D")

ventana.bind("<KeyPress>", handler)
ventana.mainloop()

