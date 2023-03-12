import unittest

from src.guest import Guest

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest_1 = Guest("Guest 1")
        self.guest_2 = Guest("Guest 2")

    def test_has_name(self):
        self.assertEqual("Guest 1", self.guest_1.name)
        self.assertEqual("Guest 2", self.guest_2.name)