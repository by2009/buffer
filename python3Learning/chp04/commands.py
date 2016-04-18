#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from sys import argv
from scanfile import scanner

class UnknowCommand(Exception): pass

commands = {'*': 'Ms.', '+':'Mr.'}

def processLine(line):
    try:
        print(commands[line[0]], line[1:-1])
    except KeyError:
        raise UnknowCommand(line)

filename = 'data.txt'    
if len(argv) == 2:
    filename = argv[1]
scanner(filename, processLine)    
