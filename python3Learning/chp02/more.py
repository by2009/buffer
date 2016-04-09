#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""
分割字符串或文本文件并交互进行分页
"""


def more(text, numberlines=15):
    lines = text.splitlines()       # 效果类似spilt('\n')，不过不用在末尾加''
    while lines:
        chunk = lines[:numberlines]
        lines = lines[numberlines:]
        for line in chunk:
            print(line)
        if lines and input('''--More--[press key 'y' or 'Y' to continue]''') not in ['y', 'Y']:
            break

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        more(sys.stdin.read())
    else:
        more(open(sys.argv[1]).read())
