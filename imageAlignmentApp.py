# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 23:29:18 2020

@author: b9903/mchsiaoj
"""

import tkinter as tk
from tkinter import filedialog

padx = 5
pady = 5
pathEntryWidth=75

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)        
        self.winfo_toplevel().title("Image Alignment")
        self.grid()
        self.createWidgets()
        
    def createWidgets(self):
        self.label_preImg = tk.Label(self)
        self.label_preImg["text"] = "Pre Img:"
        self.label_preImg.grid(row=0,column=0,padx=padx,pady=pady,sticky=tk.E)
        
        self.label_postImg = tk.Label(self)
        self.label_postImg["text"] = "Post Img:"
        self.label_postImg.grid(row=1,column=0,padx=padx,pady=pady,sticky=tk.E)
        
        self.entry_preImg = tk.Entry(self,width=pathEntryWidth)
        self.entry_preImg.grid(row=0,column=1,padx=padx,pady=pady)
        
        self.entry_postImg = tk.Entry(self,width=pathEntryWidth)
        self.entry_postImg.grid(row=1,column=1,padx=padx,pady=pady)
        
        self.btn_preImg = tk.Button(self)
        self.btn_preImg["text"] = "Open File"
        self.btn_preImg["command"] = lambda: self.loadFileNameToEntry(self.entry_preImg)
        self.btn_preImg.grid(row=0,column=2,padx=padx,pady=pady)
        
        self.btn_postImg = tk.Button(self)
        self.btn_postImg["text"] = "Open File"
        self.btn_postImg["command"] = lambda: self.loadFileNameToEntry(self.entry_postImg)
        self.btn_postImg.grid(row=1,column=2,padx=padx,pady=pady)
        
    def loadFileNameToEntry(self, entry):
        fileName = filedialog.askopenfilename()
        entry.delete(0, tk.END)
        entry.insert(0, fileName)
if __name__ == '__main__':
  root = tk.Tk()
  app = Application(root)
  app.mainloop()
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  