#!/usr/bin/env python3

class BalancedBrackets:
    def __init__(self):
       self.brackets = "" 
       self.begin = []
       self.end = []

    def check_closing_brackets(self, string):
        first_close = False 
        for char in string:
            if char == '[' and first_close == False:
                self.begin.append('[')
            elif char == ']':
                first_close = True
                self.end.append(']')


        if len(self.begin) == len(self.end):
            return True

        return False

if __name__ == '__main__':
    pass
