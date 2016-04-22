#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""
找出整个目录树下最大的Python源码文件。
搜索Python源码库，利用pprint漂亮地显示结果
"""

import sys, os, pprint

trace = False
if sys.platform.startswith('win'):
    dirname = r'C:\Python3\Lib'
else:
    dirname = r'/usr/lib/python3.4/' if len(sys.argv) == 1 else sys.argv[1]

allsizes = []
for (thisDir, subHere, fileHere) in os.walk(dirname):
    if trace: print(thisDir)
    for filename in fileHere:
        if filename.endswith('.py'):
            if trace: print('...', filename)
            fullname = os.path.join(thisDir, filename)
            fullsize = os.path.getsize(fullname)
            allsizes.append((fullsize, fullname))

allsizes.sort()
print(allsizes[:2])
print(allsizes[-2:])
