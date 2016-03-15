#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import sys
from tkinter import *

widget = Button(None, text='Hello widget world', command=sys.exit)
widget.pack(side=LEFT, expand=YES, fill=X)
widget.mainloop()
