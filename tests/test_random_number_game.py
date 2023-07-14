#!/usr/bin/bash python3

import unittest
from unittest.mock import patch
from testmodules.random_number_game import RandomNumberGame 

class TestRandomNumberGame(unittest.TestCase):

    def test_for_class_random_number_gen(self):
        rng = RandomNumberGame()
        rng.init_game()
        num_generated = rng.num_to_guess 
        self.assertIsNotNone(num_generated)
    
    def test_for_request_and_input(self):
        rng = RandomNumberGame()
        rng.init_game()
        with patch('builtins.input', return_value=5):
            result = rng.get_input()
        expected_result = 5
        self.assertEqual(expected_result, result)
    
    def test_for_answer_not_correct(self):
        pass

if __name__ == '__main__':
    unittest.main()