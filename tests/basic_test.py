import unittest
from app import app

class Test_Basic(unittest.TestCase):
    def test_basic_test(self):
        self.assertEqual("Hulk2", "Hulk")
