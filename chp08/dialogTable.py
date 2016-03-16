#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# 定义一个名称：回调演示表

from tkinter.filedialog import askopenfilename
from tkinter.colorchooser import askcolor
from tkinter.messagebox import askquestion, showerror
from tkinter.simpledialog import askfloat

demos = {
    'Open': askopenfilename,
    'Color': askcolor,
    'Query': lambda: askquestion('Warning', 'You typed "rm *"\nConfirm?'),
    'Error': lambda: showerror('Error!', "He's dead, Jim"),
    'Input': lambda: askfloat('Entry', 'Enter credit card number')
}

