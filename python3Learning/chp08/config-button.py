#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from tkinter import *

widget = Button(text='Spam', padx=10, pady=10)
widget.pack(padx=40, pady=40)
widget.config(cursor='hand2')
widget.config(bd=16, relief=GROOVE)
widget.config(bg='dark green', fg='white')
widget.config(font=('helvetica', 20, 'underline italic'))
mainloop()
