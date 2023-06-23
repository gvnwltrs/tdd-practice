#!/usr/bin/env python3

import unittest

import testmodules.character_copier as cc
import testmodules.ISource as isource 
import testmodules.IDestination as idestination 

class TestCharacterCopier(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.CharacterCopier = cc.CharacterCopier()
        cls.ISource = isource.ISource()
        cls.IDestination = idestination.IDestination()

    def tearDown(self):
        self.CharacterCopier = cc.CharacterCopier()
        self.ISource = isource.ISource()
        self.IDestination = idestination.IDestination()

    def test_for_copy(self):
        pass

    @unittest.skip("reading chars tested good")
    def test_for_read_char(self):
        self.ISource.getchar()
        expected_result = self.ISource.char
        self.assertIsInstance(expected_result, str)

    @unittest.skip("writing chars tested good")
    def test_for_write_char(self):
        self.ISource.getchar()
        self.IDestination.setchar(self.ISource.char)
        expected_result = "abcd"
        self.assertEqual(expected_result, self.IDestination.string)

if __name__ == '__main__':
    unittest.main()
