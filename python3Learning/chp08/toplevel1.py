#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import tkinter
from tkinter import *

tkinter.NoDefaultRoot()

win1 = Tk()
win2 = Tk()

Button(win1, text='Spam', command=win1.destroy).pack()
Button(win2, text='SPAM', command=win2.destroy).pack()
win1.mainloop()
