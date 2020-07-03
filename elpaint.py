import tkinter
from tkinter import filedialog,messagebox
from tkinter.ttk import Scale
import PIL.ImageGrab as ImageGrab
import numpy as np

from test_num import Resultado

class PaintApp():
    def __init__(self,root):
        self.root = root
        self.root.title("Draw your Number")
        self.root.geometry("380x310")
        self.root.configure(background = 'white')
        self.root.resizable(0,0)

        self.eraser_button = tkinter.Button(self.root,text="Clear",bd=4,bg='white',command=self.clearall,width=8)
        self.eraser_button.place(x=0,y=40)
        
        self.save_button = tkinter.Button(self.root,text="Predict",bd=4,bg='white',command=self.pasar_a_CNN,width=8)
        self.save_button.place(x=0,y=70)
        
        self.negro_button = tkinter.Button(self.root,bg = 'black',bd=2,width=8)
        self.negro_button.place(x=4,y=10)
        
        
        self.canvas = tkinter.Canvas(self.root,bg='white',bd=5,height = 280,width=280)
        self.canvas.place(x=80,y=10)
        
        self.canvas.bind("<B1-Motion>",self.paint)
        
        self.etiqueta = tkinter.Label(self.root, text = "Número:" )
        self.etiqueta.place(x=0,y = 280)
        
        # self.lineas = []
        # for i in range(0,281,10):
        #     self.lineas.append(self.canvas.create_line(i,0,i,280))
        #     self.lineas.append(self.canvas.create_line(0,i,280,i))
        
    def drawlines(self):
        self.canvas.delete(self.lineas)
        self.canvas.delete(self.lineas)
    
    def clearall(self):
        self.etiqueta.config(text = "Número : ")
        self.canvas.delete("all")
        
    def paint(self,event):
        x1,y1 = (event.x-1),(event.y-2)
        x2,y2 = (event.x+1),(event.y+2)
        self.canvas.create_oval(x1,y1,x2,y2,fill='black',outline="black",width=15 )
    
    def pasar_a_CNN(self):
            x = self.root.winfo_rootx() + self.canvas.winfo_x()
            y = self.root.winfo_rooty() + self.canvas.winfo_y()
            
            x1 = x + self.canvas.winfo_width()
            y1 = y + self.canvas.winfo_height()
            
            
            image = ImageGrab.grab().crop((x,y,x1,y1))
            res = Resultado(image)
            
            self.etiqueta.config(text = "Número : "+str(res))
        
root = tkinter.Tk()
p = PaintApp(root)
root.mainloop()

