
#Creado por Domingo Vaca Nieves 2022

import pytube, tkinter, os
from tkinter import ttk, messagebox


if "Videos_Descargados" in os.listdir():
    os.chdir("Videos_Descargados")
else:
    os.mkdir("Videos_Descargados")
    os.chdir("Videos_Descargados")

class Ventana(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        master.title("Descargar de YouTube")
        master.resizable(False, False)
        master.geometry("800x250")
        
        self.var_op= tkinter.IntVar() 
        
        self.lbl_indicion= ttk.Label(text= "Inserta la url del video: ")
        self.lbl_indicion.place(x= 20, y=10)
        
        self.entr_url = ttk.Entry()
        self.entr_url.place(x=20, y=30, width=500)
        
        self.rbtn_a = ttk.Radiobutton(text= "Video", variable= self.var_op, value= 22)
        self.rbtn_a.place(x=20, y=70)
        
        self.rbtn_v = ttk.Radiobutton(text= "Audio", variable= self.var_op, value= 251)
        self.rbtn_v.place(x=20, y=100)

        self.btn_descargar= ttk.Button(text= "Descargar", command= self._regist)
        self.btn_descargar.place(x=200, y=200, width=400)
        
    def comprobar_video(self):
        try:
            self.streams.download()
        except: 
            self.msg_cancelar= messagebox("ERROR", "No se pudo descargar el archivo contacte al creador o revise la url")
            print("No se pudo descargar el video")
            
    def _regist(self):
        self.yt = pytube.YouTube(self.entr_url.get())
        self.streams= self.yt.streams.get_by_itag(self.var_op.get())
        print(self.yt.title)
        
        self.msg_alerta= messagebox.askquestion("¿Descargar?", f"Seguro que quieres descargar: {self.yt.title}")
        
        if self.msg_alerta == "yes":
            self.comprobar_video()

v1= Ventana(tkinter.Tk())
v1.mainloop()