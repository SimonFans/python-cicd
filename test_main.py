import unittest
from main import add, minus

class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 3), 2)
        self.assertEqual(add(0, 0), 0)

    def test_minus(self):
        self.assertEqual(minus(2, 3), -1)
        self.assertEqual(minus(1, 3), -2)
        self.assertEqual(minus(0, 0), 0)

if __name__ == "__main__":
    unittest.main()