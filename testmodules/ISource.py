#!/usr/bin/env python3
import sys

class ISource():
    def __init__(self):
        self.char = '' 

    def getchar(self):
        while True:
            c = sys.stdin.read(1)
            if c == ' ':
                break
            self.char += c 

