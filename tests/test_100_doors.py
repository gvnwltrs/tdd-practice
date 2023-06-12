#!/usr/bin/env python3

import unittest

import testmodules.one_hundred_doors as Doors 

# There are 100 doors in a row that are all closed. You make 100 passes through the doors. With each pass you toggle the doors state. On each pass you visit the Nth door. That is on the first pass you visit every door. On the second pass you visit every 2nd door. On the third pass you visit every 3rd door and so on until you complete the 100th pass.
#
# The first pass you visit every door and open it.
# The second pass you visit only every second door (#2, #4, #6, …) and close them as you visit.
# The third pass you visit every 3rd door (#3, #6, #9, …) toggling the door’s state.
# If the door is closed you open it, it if is open you close it.
# Continue until you complete the 100th pass only visiting the 100th door.
# After 100 passes what is the state of each door?
# Print which doors are open and which are closed as a single string.
# Use @ for an open door and # for a closed door.
#
# Examples
# The first six doors will look something like this : @@##@@##
#
# Bonus
# Add a third state of holding (use H). By adding this state, you must toggle between open, holding and closed when visiting the doors.
# How could you have better abstracted the problem to make these adjustments simpler?


class Test100Doors(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.doors = Doors.OneHundredDoors()
        cls.doors.set_up_doors()

    def test_for_100_doors(self):
        self.assertEqual(100, len(self.doors.state))
    
    def test_for_doors_closed(self):
        self.doors.set_doors_closed()
        expected_state = ['#'] * 100
        self.assertEqual(expected_state, self.doors.state)

    def test_doors_first_pass(self):
        self.doors.first_pass()
        expected_state = ['@'] * 100
        self.assertEqual(expected_state, self.doors.state)

    def test_doors_second_pass(self):
        self.doors.second_pass()
        expected_state = ['@', '#'] * 50
        self.assertEqual(expected_state, self.doors.state)

    def test_doors_third_pass(self):
        self.doors.third_pass()
        expected_state = ['@', '#', '#', '#', '@', '@']
        self.assertEqual(expected_state, self.doors.state[:6])

if __name__ == '__main__':
    unittest.main()


