#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import sys
from tkinter import *

class HelloClass:
    def __init__(self):
        widget = Button(None, text='Hello even world', command=self.quit)
        widget.pack()

    def quit(self):
        print('Hello class method world')
        sys.exit()

HelloClass()
mainloop()
