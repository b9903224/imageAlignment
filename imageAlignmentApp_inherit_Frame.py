# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 23:29:18 2020

@author: b9903/mchsiaoj
"""

import tkinter as tk
from tkinter import filedialog
import os
import numpy as np
from PIL import Image, ImageTk
from utility.insertSignature import insertSignature
import utility

featVer = 'dev'
kernelVer = 'dev'

padx = 0
pady = 0
pathEntryWidth=90
currentPath = os.getcwd()

class ImgShowFrame(tk.Frame):
    def __init__(self, master=None, imgTitle=''):
        tk.Frame.__init__(self)
#        self.pack()
        self.createWidgets(imgTitle)
    def createWidgets(self, imgTitle):
        self.label_img = tk.Label(self)
        self.label_img['text'] = imgTitle
        self.label_img.pack()
        
        self.canvas_img = tk.Canvas(self,width=256,height=256,bg='green')
        self.canvas_img.create_text(120,120,text='No Image',fill="darkblue",font="Times 20 italic bold")
        self.canvas_img.pack()
        
class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.winfo_toplevel().title("Image Alignment")
        self.grid()
#        self.pack()
        self.createWidgets()
        self.insertVersion()
        
    def createWidgets(self):
        
        self.label_intro = tk.Label(self)
        self.label_intro["text"] = """output file name e.g.:
            [xxx].png --> [xxx]_diff.png
            [xxx].png --> [xxx]_featureDemo.png"""
        self.label_intro.grid(row=0,column=1,columnspan=1)
        
        self.label_preImg = tk.Label(self)
        self.label_preImg["text"] = "Pre Img:"
        self.label_preImg.grid(row=1,column=0,padx=padx,pady=pady,sticky=tk.E)
        
        self.label_postImg = tk.Label(self)
        self.label_postImg["text"] = "Post Img:"
        self.label_postImg.grid(row=2,column=0,padx=padx,pady=pady,sticky=tk.E)
        
        self.label_outputPath = tk.Label(self)
        self.label_outputPath["text"] = "Output Path:"
        self.label_outputPath.grid(row=3,column=0,padx=padx,pady=pady,sticky=tk.E)
        
        self.entry_preImg = tk.Entry(self,width=pathEntryWidth)
        self.entry_preImg.grid(row=1,column=1,padx=padx,pady=pady)
        
        self.entry_postImg = tk.Entry(self,width=pathEntryWidth)
        self.entry_postImg.grid(row=2,column=1,padx=padx,pady=pady)
        
        self.entry_outputPath = tk.Entry(self,width=pathEntryWidth)
        self.entry_outputPath.grid(row=3,column=1,padx=padx,pady=pady)
        
        self.btn_preImg = tk.Button(self)
        self.btn_preImg["text"] = "Open Pre Img"
        self.btn_preImg["command"] = lambda: self.loadFileNameToEntry(self.entry_preImg)
        self.btn_preImg.grid(row=1,column=2,padx=padx,pady=pady)
        
        self.btn_postImg = tk.Button(self)
        self.btn_postImg["text"] = "Open Post Img"
        self.btn_postImg["command"] = lambda: self.loadFileNameToEntry(self.entry_postImg)
        self.btn_postImg.grid(row=2,column=2,padx=padx,pady=pady)
        
        self.btn_outputPath = tk.Button(self)
        self.btn_outputPath["text"] = "Open Output Folder"
        self.btn_outputPath["command"] = lambda: self.loadDirectoryToEntry(self.entry_outputPath)
        self.btn_outputPath.grid(row=3,column=2,padx=padx,pady=pady)
        
        self.btn_copyPath_pre = tk.Button(self)
        self.btn_copyPath_pre["text"] = "Copy to Output (Pre)"
        self.btn_copyPath_pre["command"] = lambda: self.copyDirectoryToEntry(self.entry_preImg, self.entry_outputPath)
        self.btn_copyPath_pre.grid(row=1,column=3,padx=padx,pady=pady)
        
        self.btn_copyPath_post = tk.Button(self)
        self.btn_copyPath_post["text"] = "Copy to Output (Post)"
        self.btn_copyPath_post["command"] = lambda: self.copyDirectoryToEntry(self.entry_postImg, self.entry_outputPath)
        self.btn_copyPath_post.grid(row=2,column=3,padx=padx,pady=pady)

        self.imgShowFrame_pre = ImgShowFrame(self.master, imgTitle='Pre Image')
        self.imgShowFrame_pre.grid(row=4,column=0)
#        
#        self.imgShowFrame_post = ImgShowFrame(self,imgTitle='Post Image')
#        self.imgShowFrame_post.grid(row=4,column=1)
                                
    def loadFileNameToEntry(self, entry):
        fileName = filedialog.askopenfilename()
#        print(fileName)
        if fileName:
            entry.delete(0, tk.END)
            entry.insert(0, fileName)
            
    def loadDirectoryToEntry(self, entry):
        directory = filedialog.askdirectory()
        if directory:
            entry.delete(0, tk.END)
            entry.insert(0, directory)
            
    def copyDirectoryToEntry(self, srcEntry, destEtry):
        # copy src to dest
        srcPath = srcEntry.get()
        path, _ = os.path.split(srcPath)
        destEtry.delete(0, tk.END)
        destEtry.insert(0, path)
        
    def insertVersion(self):
#        signatureImg = Image.open('duck.jpg')
        rgb = self.winfo_rgb(self.cget('bg'))
        rgb = [_/255 for _ in rgb]
        fontSize = 10
        img = np.zeros(((fontSize+2)*3,150,3), 'uint8')
        img[..., 0] = rgb[0]*255
        img[..., 1] = rgb[1]*255
        img[..., 2] = rgb[2]*255
        img = insertSignature(img,featVer=featVer,kernelVer=kernelVer,fontSize=fontSize,loc='RU')
#        img = insertSignature(img,featVer=featVer,kernelVer=kernelVer,fontSize=fontSize,loc='RD')
#        utility.imshow(img, 'img')
        signatureImg = Image.fromarray(img)
        signatureImg = ImageTk.PhotoImage(signatureImg)
#        signatureImg = ImageTk.PhotoImage(Image.open('duck.jpg'))
        self.label_signature = tk.Label(self, image=signatureImg)
        self.label_signature.image = signatureImg
        self.label_signature.grid(row=0,column=3)


        
if __name__ == '__main__':
  root = tk.Tk()
  app = Application(root)
  app.mainloop()
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  