#!/usr/bin/env python3 

import random

class RandomNumberGame:

    def __init__(self):
        self.num_to_guess = None
        self.user_guess = None

    def init_game(self):
        self.num_to_guess = random.randint(1,20)
        
    def get_input(self):
        print('Enter a number between 1 and 20')
        self.user_guess = int(input())
        return self.user_guess
