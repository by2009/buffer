#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import sys
from tkinter import *

win1 = Toplevel()
win2 = Toplevel()
Button(win1, text='Spam', command=sys.exit()).pack()
Button(win2, text='SPAM', command=sys.exit()).pack()

label(text='Popups').pack()
win1.mainloop()
