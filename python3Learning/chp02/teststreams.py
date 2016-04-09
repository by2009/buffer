#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"erad numbers till eof and show squares"

def interact():
    print('Hello stream world')                     # 输出数据到 sys.stdout
    while True: 
        try:
            reply = input('Enter a number>')        # 输入来自 sys.stdin的数据
        except EOFError:
            break
        else:
            num = int(reply)
            print("%-5d squared is %d"%(num, num ** 2))
    print('Bye')

if __name__ == '__main__':
    interact()
