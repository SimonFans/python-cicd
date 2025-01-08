import unittest
from main import add

class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 3), 2)
        self.assertEqual(add(0, 0), 0)

if __name__ == "__main__":
    unittest.main()