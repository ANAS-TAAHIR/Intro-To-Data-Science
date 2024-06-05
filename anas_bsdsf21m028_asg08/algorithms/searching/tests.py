# unit test
import unittest
import linear, binary, interpolation, exponential, jump

class TestLinearSearch(unittest.TestCase):
    def test_linear_search(self):
        data = [1, 2, 3, 4, 5]
        self.assertTrue(linear.linear_search(data, 1))
        self.assertTrue(linear.linear_search(data, 5))
        self.assertFalse(linear.linear_search(data, 6))
    
    def test_binary_search(self):
        data = [1, 2, 3, 4, 5]
        self.assertEqual(binary.binary_search(data, 1), 0)
        self.assertEqual(binary.binary_search(data, 5), 4)
        self.assertIsNone(binary.binary_search(data, 6))

    def test_interpolation_search(self):
        data = [1, 2, 3, 4, 5]
        self.assertEqual(interpolation.interpolation_search(data, 1), 0)
        self.assertEqual(interpolation.interpolation_search(data, 5), 4)
        self.assertEqual(interpolation.interpolation_search(data, 6), -1)

    def test_exponential_search(self):
        data = [1, 2, 3, 4, 5]
        self.assertEqual(exponential.exponential_search(data, 1), 0)
        self.assertEqual(exponential.exponential_search(data, 5), 4)
        self.assertEqual(exponential.exponential_search(data, 6), -1)
    
    def test_jump_search(self):
        data = [1, 2, 3, 4, 5]
        self.assertEqual(jump.jump_search(data, 1), 0)
        self.assertEqual(jump.jump_search(data, 5), 4)
        self.assertEqual(jump.jump_search(data, 6), -1)

if __name__ == "__main__":
    unittest.main()
