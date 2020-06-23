# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 22:11:54 2020

@author: b9903/mchsiaoj
"""

import tkinter as tk
class Application:
    def __init__(self, master):
        master.title("Image Alignment App")
#        master.geometry('200x100+200+200')
        var = tk.StringVar()
        l = tk.Label(master,textvariable=var,bg='green', font=('Arial', 12), width=15, height=2)
        l.pack()
        b = tk.Button(master,text='hit me',width=15, height=2,command=self.hit_me)
        b.pack()
        self.master = master
        self.l = l
        self.b = b
        self.on_hit = False
        self.var = var
    def hit_me(self):
        var = self.var
        if self.on_hit == False:     # 从 False 状态变成 True 状态
            self.on_hit = True
            var.set('you hit me')   # 设置标签的文字为 'you hit me'
        else:       # 从 True 状态变成 False 状态
            self.on_hit = False
            var.set('') # 设置 文字为空
    
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
    
    
    
    
    
    
    
    
    