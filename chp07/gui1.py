#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from tkinter import Label                       # 获取组件对象
widget = Label(None, text='Hello GUI world!')   # 生成
widget.pack()                                   # 布置
widget.mainloop()                               # 开始事件循环
