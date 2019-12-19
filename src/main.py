# -*- coding:utf-8 -*-  
 
import tkinter as tk   
import tkinter.font as tf    # 导入Tkinter模块  
from PIL import Image, ImageTk  
from collections import Counter

root = tk.Tk()  
canvas = tk.Canvas(root,  
    width = 1000,      # 指定Canvas组件的宽度  
    height = 600,      # 指定Canvas组件的高度  
    bg = 'white')      # 指定Canvas组件的背景色  
#im = Tkinter.PhotoImage(file='img.gif')     # 使用PhotoImage打开图片  
image = Image.open("a.jpg")  
image = image.resize((1000, 600), 2)
im = ImageTk.PhotoImage(image)  
canvas.create_image(500,300,image = im)      # 使用create_image将图片添加到Canvas组件中  

page_lists = []
page_strs = []

def get_songs_list():
    row_count = 25

    # load all songs
    w = open('list.txt','r')
    l = w.readlines()
    songs=[]
    for k in l:
        k = k.strip('\n')  #去掉读取中的换行字符
        songs.append(k.replace(' ', ''))   
    while '' in songs:
        songs.remove('') 
    songs=list(set(songs))
    songs.sort(key = lambda i:len(i),reverse=False) 
    
    # split to columns
    songs_columns = [songs[i:i+row_count] for i in range(0,len(songs),row_count)]
    
    page_length = 0
    page_list = []
    for songs_column in songs_columns:
  #      for song in songs_column:
  #          if len(song) < len(songs_column[-1]):
  #              song += '    ' * (len(songs_column[-1]) - len(song))
        page_length += len(songs_column[-1])
        
        if page_length > 30:
            page_lists.append(page_list)
            page_list = [songs_column]
            page_length = len(songs_column[-1])
        else:
            page_list.append(songs_column)
    page_lists.append(page_list)
    
    
    
    
    for page in page_lists:
        page_str = ''
        page_row_count = len(page[0])
        for i in range(page_row_count):
            for j in range(len(page)):
                if len(page[j]) <= i:
                    continue
                n = str(page_row_count * j + i) + '.'
                c = len(page[j][-1]) - len(page[j][i])
                m = page[j][i] + '    ' * c
                if len(n) == 2:
                    n = '0' + n

                page_str += n + m + '    '
            page_str += '\n'
        page_strs.append(page_str)
            
    
    
    
        
get_songs_list()

    
ft = tf.Font(family='手书体', size=15)
t = canvas.create_text(500,300,  
   text = page_strs[0],  
   font=ft,
   fill = '#0000CD')  
canvas.pack()         # 将Canvas添加到主窗口  
txtlist = []
txtlist.append(t)
def de(event):
    canvas.delete(txtlist[-1])
    q = len(txtlist) % len(page_lists)
    e = canvas.create_text(500,300,  
    text = page_strs[q],  
    font=ft,
    fill = '#0000CD')
    txtlist.append(e)
    
page_image = Image.open("p.jpg") 
page_image = page_image.resize((100, 36), 2)
im2 = ImageTk.PhotoImage(page_image)  
bb = canvas.create_image(500,576,image = im2)

canvas.tag_bind(bb, '<ButtonPress-1>', de)    

root.mainloop()  