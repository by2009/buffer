#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import sys
from tkinter import *

def hello(even):
    print('Press twice to exit')

def quit(even):
    print('hello, I must be going...')
    sys.exit()

widget = Button(None, text='Hello even world') 
widget.pack()
widget.bind('<Button-1>', hello)        # 绑定鼠标左键单击事件
widget.bind('<Double-1>', quit)         # 绑定鼠标左键双击事件
widget.mainloop()
