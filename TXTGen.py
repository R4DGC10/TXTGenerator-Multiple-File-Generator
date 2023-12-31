
from logging import root
import tkinter
#Librerias 
import tkinter as tk
import os
import time
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image 
from tkinter import messagebox


#Icono del Taskbar
import ctypes
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

#Creacion de Ventana y Dimensiones
window = tkinter.Tk()
window.title("TXT Generator (Closed Developer)")
window.resizable(False, False)
window.iconbitmap(r"C:\Users\cepc2\OneDrive\Desktop\Projects\CodePy\TXTGen\TXTGenerator\icono_new.ico")
window.geometry("500x300")
window.configure(bg="white")

#COORDENADAS
coordenada_x = window.winfo_x()
coordenada_y = window.winfo_y()

#print("Coordenada X:", coordenada_x)
#print("Coordenada Y:", coordenada_y)



#Contenido
title_main = tkinter.Label(window, text = ".txt file Generator || Generador de Archivos de Texto", font = "arial", bg = "green")
title_main.pack(fill = tkinter.X)


label = tkinter.Label(window, text = "Ingrese el nombre del archivo a generar", font = "arial",bg = "white")
label.pack()


#PopUp  (About Button)
def pop_window():
   
    AboutWindow = Toplevel()
    AboutWindow.title("Acerca de")
    AboutWindow.resizable(False, False)
    AboutWindow.iconbitmap(r"C:\Users\cepc2\OneDrive\Desktop\Projects\CodePy\TXTGen\TXTGenerator\icono_new.ico")
    AboutWindow.geometry("200x200")
    
    about_msg = tkinter.Label(AboutWindow, text="Developed by cpacheco_c 2023",bg = "white")
    about_msg2 = tkinter.Label(AboutWindow, text="Using Tkinter Library in Python v3.11.4",bg = "white")
    about_msg2 = tkinter.Label(AboutWindow, text="Non comercial Software ",bg = "white")
    about_msg.pack()
    about_msg2.pack()
    button = tk.Button(AboutWindow, text="Cerrar", command=AboutWindow.destroy)
    button.pack(pady=5)

def contact_dev():
    AboutWindow = Toplevel()
    AboutWindow.title("Contacta al desarrollador",bg = "white")
    AboutWindow.resizable(False,False)
    AboutWindow.iconbitmap(r"C:\Users\cepc2\OneDrive\Desktop\Projects\CodePy\TXTGen\TXTGenerator\icono_new.ico")
    AboutWindow.geometry("500x300")

    contact_msg = tkinter.Label(AboutWindow, text = "Contacto Comercial",bg = "white")
    contact_msg2= tkinter.Label(AboutWindow, text="c4dgr10xp@protonmail.com",bg = "white")
    contact_msg.pack()
    contact_msg2.pack()
    button = tk.Button(AboutWindow, text="Cerrar",bg = "white", command=AboutWindow.destroy)
    button.pack(pady=5)





credits_popup = tkinter.Button(window, text = "Acerca de", command = pop_window)
credits_popup.pack(side="bottom")

hide_popup = tkinter.Button(window, text = "Contacta al desarrollador", command =  contact_dev)
hide_popup.pack(side="bottom")



name_input = tkinter.Entry(window,  font = "arial",bg = "white")
name_input.pack()



#Ruta de Guardado Custom
label = tkinter.Label(window, text = "Ruta de Guardado", font = "arial",bg = "white")
label.pack()

file_input = tkinter.Entry(window)
file_input.pack()

#Modificar Contenido
label_editor = tkinter.Label(window, text = "Modificar contenido del archivo", font = "arial",bg = "white")
label_editor.pack()

label_editor_input = tkinter.Entry(window)
label_editor_input.pack()


#Pop Up al intentar cerrar
def on_close():
    if messagebox.askokcancel("Saliendo", "¿Está seguro de que desea salir del programa?"):
        window.destroy()
window.protocol("WM_DELETE_WINDOW", on_close)


#Funcion define ruta y nombre del archivo.txt
#Compureba que haya un nombre escrito para el archivo

def filename():
    #Re-Declaracion de variables para ser utilizadas localmente en la funcion filename()
    name_doc = name_input.get()
    file_path = file_input.get()
    mod_txt = label_editor_input.get()
    
    if not name_doc:
        msg = tkinter.Label(window,text = "Por favor rellene casilla => Nombre del Archivo!", font = "arial", bg = "red")
        msg.pack(fill = tkinter.X)
        msg.pack()
        window.after(1500, msg.destroy) 
        
    #Comprueba una ruta valida
    elif not file_path or not os.path.exists(file_path):
        # Verificar si la ruta de archivo es válida
        msg = tkinter.Label(window,text = "Por favor rellene casilla => Ruta del Archivo!", font = "arial", bg = "red")
        msg.pack(fill = tkinter.X)
        msg.pack()
        window.after(1500, msg.destroy)
    else:
        #print(name_doc)
        file_name = name_input.get()
        file_path = file_input.get() # Obtener la ruta de archivo del widget Entry
        create_file(file_path, file_name)
        msg_correct = tkinter.Label(window,text = "Archivo Generado Exitosamente :) en " + file_path , font = "arial", bg = "green")
        msg_correct.pack(fill = tkinter.X)
        msg_correct.pack()
        window.after(1000, msg_correct.destroy)


Confirm1_button = tkinter.Button(window, text = "Confirmar", command = filename)
Confirm1_button.pack()



#Obtiene Hora
current = time.strftime("%D:%Y:%H:%M:%S", time.localtime())
print(current)

def create_file(file_path, file_name):
    generated_time = current
    file_content = "Archivo Generado mediante TXTGenerator => " + file_name 
    file_c2 = "Fecha de Creacion =>   " + generated_time 
    file_input = label_editor_input.get()
    file_blank = " "
    
    with open(os.path.join(file_path, file_name), 'w' ) as file:
        file.write(file_content +"\n")
        file.write(file_c2+"\n")
        file.write("TXTGenerator_cpacheco_c_2023")
        file.write(file_blank+"\n")
        file.write(file_input)
        print("Archivo generado en ",file_path, "de nombre ",file_name, "//Fecha: ",current )


#Añadir imagen, requisito pip install pillow
logo = Image.open(r"C:\Users\cepc2\OneDrive\Desktop\Projects\CodePy\TXTGen\TXTGenerator\icono_new.ico")
logo = logo.resize((100, 100))
logo_tk = ImageTk.PhotoImage(logo)



pic_logo = tk.Label(window, image=logo_tk)
pic_logo.place(x=30,y=70)





#Bucle main de la ventana
window.mainloop()

