#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import sys
from tkinter import *

class HelloCallable:
    def __init__(self):
        self.msg = 'Hello __call__ world'

    def __call__(self):
        print(self.msg)
        sys.exit()

widget = Button(None, text='Hello even world', command=HelloCallable())
widget.pack()
mainloop()
