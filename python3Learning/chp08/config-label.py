#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from tkinter import *
root = Tk()
labelfont = ('times', 30, 'bold')
widget = Label(root, text='Hello config world')
widget.config(bg='cyan', fg='yellow')
widget.config(font=labelfont)
widget.config(height=3, width=20)
widget.pack(expand=YES, fill=BOTH)
root.mainloop()
