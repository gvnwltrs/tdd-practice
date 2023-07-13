#!/usr/bin/bash python3

import unittest
from testmodules.random_number_game import RandomNumberGame 

class TestRandomNumberGame(unittest.TestCase):

    def test_for_class_random_number_gen(self):
        rng = RandomNumberGame()
        rng.init_game()
        num_generated = rng.num_to_guess 
        self.assertIsNotNone(num_generated)

if __name__ == '__main__':
    unittest.main()