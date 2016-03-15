#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import sys
from tkinter import *


def quit(name):
    print('Hello %s, I must be going ...' % name)
    sys.exit()

# 回调函数，带参数则需要通过lambada函数调用，
# 否则直接调用会在创建组件时就自动调用
widget = Button(None,
                text='Hello widget', 
                command=(lambda: quit('Crane')))
widget.pack(side=LEFT, expand=YES, fill=X)
widget.mainloop()
