#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import sys

def filter_files(name, fuction):
    with open(name, 'r') as input, open(name + '.out', 'w') as output:
        for line in input:
            output.write(fuction(line))

def filter_stream(fuction):
    while True:
        line = sys.stdin.readline()
        if not line: break
        print(fuction(line), end='')

if __name__=='__main__':
    filter_stream(lambda line: line)
