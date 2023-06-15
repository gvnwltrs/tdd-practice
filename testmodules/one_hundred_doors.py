#!/usr/bin/env python3

class OneHundredDoors:
    def __init__(self):
        self.state = None 

    def run_100_doors(self, passes):
        self.set_up_doors()
        self.set_doors_closed()
        for i in range(passes):
            self.door_pass(i, i+1)
        print('Done! ', self.state)

        
    def set_up_doors(self):
        self.state = [None] * 100

    def set_doors_closed(self):
        for i in range(len(self.state)):
            self.state[i] = '#'

    def door_pass(self, start, step):
        for i in range(start, len(self.state), step):
            self.toggle_door(i)

    def toggle_door(self, i):
        if self.state[i] == '#':
            self.state[i] = '@' #open
        else:
            self.state[i] = '#' #close

if __name__ == '__main__':
    pass


