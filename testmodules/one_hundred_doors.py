#!/usr/bin/env python3

class OneHundredDoors:
    def __init__(self):
        self.state = None 

    def set_up_doors(self):
        self.state = [None] * 100


    def set_doors_closed(self):
        for i in range(len(self.state)):
            self.state[i] = '#'

    def first_pass(self):
        for i in range(len(self.state)):
            self.state[i] = '@'

    def second_pass(self):
        for i in range(1, len(self.state), 2):
            self.state[i] = '#'

    def third_pass(self):
        for i in range(2, len(self.state), 3):
            if self.state[i] == '@':
                self.state[i] = '#'
            elif self.state[i] == '#':
                self.state[i] = '@'
                

if __name__ == '__main__':
    pass


