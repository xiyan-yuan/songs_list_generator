# -*- coding:utf-8 -*-  
# file: TkinterCanvas.py  
#  
import tkinter as tk   
import tkinter.font as tf    # 导入Tkinter模块  
from PIL import Image, ImageTk  
from collections import Counter
import random
import time

root = tk.Tk()  
canvas = tk.Canvas(root,  
    width = 200,      # 指定Canvas组件的宽度  
    height = 600,      # 指定Canvas组件的高度  
    bg = 'white')      # 指定Canvas组件的背景色  
#im = Tkinter.PhotoImage(file='img.gif')     # 使用PhotoImage打开图片  
image = Image.open("small.jpg")  
image = image.resize((200, 600), 2)
im = ImageTk.PhotoImage(image)  
canvas.create_image(100,280,image = im)      # 使用create_image将图片添加到Canvas组件中  

w = open('list.txt','r')
l = w.readlines()
songs=[]
for k in l:
    k = k.strip('\n')  #去掉读取中的换行字符
    songs.append(k.replace(' ', ''))   
while '' in songs:
    songs.remove('') 

#b = dict(Counter(songs))
#print ({key:value for key,value in b.items()if value > 1}) 
songs=list(set(songs))

current = random.sample(songs, 20)  
tot = ''
for c in current:
    if len(c) < 14:
        sp = 14 - len(c)
        c = ' ' * sp + c + ' ' * sp
    tot += c + '\n'
    
ft = tf.Font(family='手书体', size=16)
t = canvas.create_text(100,280,  
   text = tot,  
   font=ft,
   fill = '#0000CD')  
canvas.pack()         # 将Canvas添加到主窗口  
txtlist = []
txtlist.append(t)
def update_list():
    canvas.delete(txtlist[-1])
    current2 = random.sample(songs, 20)  
    tot2 = ''
    for c in current2:
        if len(c) < 14:
            sp = 14 - len(c)
            c = ' ' * sp + c + ' ' * sp
        tot2 += c + '\n'

    e = canvas.create_text(100,280,  
       text = tot2,  
       font=ft,
       fill = '#0000CD') 
    txtlist.append(e)
    canvas.after(10000, update_list)
    
update_list()

root.mainloop()  