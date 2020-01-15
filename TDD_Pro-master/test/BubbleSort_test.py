import unittest
import src.BubbleSort
class test(unittest.TestCase):
    def test_bublesort(self):
        self.assertIsNotNone(src.BubbleSort.bubblesort([17,22,25,30,45]))
        self.assertEqual(src.BubbleSort.bubblesort([17,22,25,30,45]),[17,22,25,30,45])
        self.assertEqual(len(src.BubbleSort.bubblesort([17,22,25,30,45])),5)


if __name__ == '__main__':
    unittest.main()
