#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from tkinter import *

def greeting():
    print('Hello stdout world')

win = Frame()    
win.pack()
Button(win, text='Hello', command=greeting).pack(side=LEFT, anchor=N)
Label(win, text='Hello container world').pack(side=TOP)
Button(win, text='Quit', command=win.quit).pack(side=RIGHT)

win.mainloop()
