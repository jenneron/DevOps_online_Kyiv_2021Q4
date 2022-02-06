import main
import unittest

class TestSquare (unittest.TestCase):
    def test_discriminant(self):
        self.assertEqual(main.discriminant(1, 12, 36), 0)

    def test_roots(self):
        # two roots case
        self.assertEqual(main.roots(16, 1, 2, -3), [1, -3])
        # one root case
        self.assertEqual(main.roots(0, 1, 12, 36), [-6])
        # no roots case
        self.assertEqual(main.roots(-8, 3, 2, 1), None)

    def test_square(self):
        # two roots case
        self.assertEqual(main.solv_square(1, 2, -3), [1, -3])
        # one root case
        self.assertEqual(main.solv_square(1, 12, 36), [-6])
        # no roots case
        self.assertEqual(main.solv_square(3, 2, 1), None)

if __name__ == '__main__':
    unittest.main()
