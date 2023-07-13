#!/usr/bin/env python3 

import random

class RandomNumberGame:

    def __init__(self):
        self.num_to_guess = None

    def init_game(self):
        self.num_to_guess = random.randint(1,20)
        