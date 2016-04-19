#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import _thread

def child(tid):
    print('Hello from child', tid)

def parent():
    i = 0
    while True:
        i+=1
        _thread.start_new_thread(child, (i,))
        if input() == 'q': break

if __name__ == '__main__':
    parent()
