#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""
找出单个目录下最大的Python源码文件。
搜索Python源码库，除非指定了dir命令行参数
"""

import os, glob, sys

dirname = r'/usr/lib/python3.4/' if len(sys.argv) == 1 else sys.argv[1]

allsizes = []
allpy = glob.glob(dirname + os.sep + '*.py')
for filename in allpy:
    filesize = os.path.getsize(filename) 
    allsizes.append((filesize, filename))

allsizes.sort()
print(allsizes[:2])
print(allsizes[-2:])
