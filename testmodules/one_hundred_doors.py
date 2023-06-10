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
        for i in range(0, len(self.state), 2):
            self.state[i+1] = '#'

if __name__ == '__main__':
    pass


