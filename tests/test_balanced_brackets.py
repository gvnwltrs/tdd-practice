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
import testmodules.balanced_brackets

class TestBalancedBrackets(unittest.TestCase):
    pass

    def test_this(self):
        pass

if __name__ == '__main__':
    main.unittest()
    pass
