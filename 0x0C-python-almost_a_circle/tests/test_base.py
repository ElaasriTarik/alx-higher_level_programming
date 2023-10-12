import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_with_id(self):
        b1 = Base(1)
        self.assertEqual(b1.id, 1)

    def test_without_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 3)

if __name__ == "__main__":
    unittest.main()
