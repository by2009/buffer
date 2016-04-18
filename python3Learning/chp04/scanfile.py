#!/usr/bin/env python3
# -*- coding=utf-8 -*-

def scanner(name, function):
    list(map(function, open(name, 'r')))
