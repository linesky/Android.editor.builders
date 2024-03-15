import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter import *
import subprocess
import shutil
import os
from PIL import Image 
from PIL import ImageTk
import PIL


images=None
ccanvas=None
def convert_16bit_to_rgb( colors,bytess):
    # Extrai os bits relevantes do high byte e low byte
    colorss=colors
    xxx=128
    t=0
    for n in range(8):
        t=xxx & bytess
        if t!=0:
            colorss=colorss+[1]
        else:
            colorss=colorss+[0]
        xxx=xxx>>1
    # Retorna os valores RGB como uma tupla de 3 bytes
    return colorss


def encodess(s:str)->str:
    
    sss=list(s)
    
    return sss
def msgbox(msgs:str,color:str):
    Window = tk.Toplevel(bg=color)

    
    filename = tk.filedialog.askopenfilename(title="load file")
    
    f1 = open(filename,"rb")
    sss1:str=str(f1.read(4))
    
   
    sss1=sss1.replace("b'","")
    sss1=sss1.replace("'","")
    sss1=sss1.replace("\\x00","\0")
    print(sss1)
    if sss1!="EGA4":
        f1.close()
        print("return title")
        return None
    # obtém as dimensões da imagem
    
    Width=f1.read(4)
    r0=Width[0]
    r1=Width[1]
    r2=Width[2]
    r3=Width[3]
    Width:int=r0+r1*256+r2*256*256+r3*256*256*256
    print("*"+str(Width))

    Height=f1.read(4)
    r0=Height[0]
    r1=Height[1]
    r2=Height[2]
    r3=Height[3]
    Height:int=r0+r1*256+r2*256*256+r3*256*256*256
    print("*"+str(Height))

    # percorre todos os pixels da imagem e muda a cor azul para vermelho
    canvas = tk.Canvas(Window, width=Width, height=Height, bg=color)
    blues=""
    greens=""
    reds=""
    bt=""
    for plane in range(4):
        for y in range(Height):

            for x in range((Width+0)//8):
                # obtém o valor RGB do pixel atual
                rgb= f1.read(1)
                rgb=(rgb[0] & 255)
 
                if 0==0:    
                    rgbb="00000000"+bin(rgb).replace("b","")
                    ty=len(rgbb)
                    tyy=ty-8
                    rgbb=rgbb[tyy:ty]

                    if plane==0:
                        blues=blues+rgbb
                    if plane==1:
                        greens=greens+rgbb
                    if plane==2:
                        reds=reds+rgbb
                    if plane==3:
                        bt=bt+rgbb
                                                
    
    yx=0   
    for y in range(Height):
        
        for x in range(Width):
            # obtém o valor RGB do pixel atual
            #yx=(y*(Width))+x           
            # verifica se o pixel é azul (R=0, G=0, B=255) e o substitui por vermelho (R=255, G=0, B=0)
            #if r == 0 and g == 0 and b == 255:
            btt="0"
            bblue="0"
            ggreen="0"
            rred="0"
            if bt[yx]!="0":
                btt="F"
            if blues[yx]!="0":
                bblue="F"
            if greens[yx]!="0":
                ggreen="F"
            if reds[yx]!="0":
                rred="F"
            ssss="#"+rred+btt+ggreen+btt+bblue+btt

            canvas.create_line((x, y),(x+1,y), fill=ssss)
            yx+=1
    
    print("dones")
    canvas.pack()
    
    
class BareboneBuilder:
    def __init__(self, root):
        i:int=0
        self.root = root
        self.root.title("")

        # Janela amarela
        self.root.configure(bg='blue')
        # Botões
        self.run_button = tk.Button(self.root, text="load file", command=self.build_kernel)
        self.run_button.pack(pady=5)
       

    def build_kernel(self):
        msgbox("hello world....",'blue') 
       
        
        
       






if __name__ == "__main__":
    root = tk.Tk()
    builder = BareboneBuilder(root)
    root.mainloop()
