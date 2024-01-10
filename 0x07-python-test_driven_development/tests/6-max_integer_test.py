#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class print_max_integer(unittest.TestCase):

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer(list()), None)
        self.assertEqual(max_integer([1, 2, 3, True]), 3)
        self.assertEqual(max_integer([1, 2, 3, 4, -5]), 4)
        self.assertEqual(max_integer([1, 2, 3, 4.5]), 4.5)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-5, -15, -30]), -5)

    def test_types(self):
        self.assertRaises(TypeError, max_integer, 3+5j)
        #self.assertRaises(TypeError, max_integer, "radius")
