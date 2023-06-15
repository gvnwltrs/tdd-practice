#!/usr/bin/env python3

import unittest

import testmodules.character_copier as cc
import testmodules.ISource as isource 
import testmodules.IDestination as idestination 

class TestCharacterCopier(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.CharacterCopier = cc.CharacterCopier()
        cls.ISource = isource.ISource("c")
        cls.IDestination = idestination.IDestination("c")

    def tearDown(self):
        pass

    def test_for_copy(self):
        pass

    def test_for_read_char(self):
        pass

    def test_for_write_char(self):
        pass

if __name__ == '__main__':
    unittest.main()
