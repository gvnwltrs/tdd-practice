#!/usr/bin/env python3 

# Take an input string with X opening brackets [ and Y closing brackets ], in a random order.
#
# Determine if the generated string of brackets is balanced, that is it consists of pairs of opening/closing brackets in the correct order with no matched opening and closing pairs.
#
# The kata has been structured to be simple, yet loosely guided. You will need to make decisions just like you were writing code for production.
#
# The examples are not meant to guide your implementation, they are there merely to guide you.
#
# Do not worry about input other than brackets and empty string.
#
# Examples
# (empty) “”
# [] OK
# [][] OK
# [[]] OK
# [[[][]]] OK
# ][ FAIL
# ][][ FAIL
# [][]][ FAIL
# Hint
# Start off returning string.empty as the default condition. This will allow you properly work the red-green-refactor cycle.

import unittest
import testmodules.balanced_brackets as bb

class TestBalancedBrackets(unittest.TestCase):

    def setUp(cls):
        cls.balancer = bb.BalancedBrackets()

    def test_get_a_string(self):
        expected_result = "" 
        self.assertIsInstance(expected_result, type(self.balancer.brackets))

    def test_check_for_balanced_bracket(self):
        string = "[]"
        self.assertTrue(self.balancer.check_closing_brackets(string))

    def test_check_for_complex_balanced_closing_bracket(self):
        string = "[[[[]]]]"
        self.assertTrue(self.balancer.check_closing_brackets(string))

    def test_check_for_unbalanced_closing_bracket(self):
        string = "[]]"
        self.assertFalse(self.balancer.check_closing_brackets(string))

    def test_check_for_complex_unbalanced_closing_bracket(self):
        string = "[[]]]]"
        self.assertFalse(self.balancer.check_closing_brackets(string))

    def test_check_for_unbalanced_closing_bracket_starting(self):
        string = "]["
        self.assertFalse(self.balancer.check_closing_brackets(string))

if __name__ == '__main__':
    main.unittest()
