import unittest

from day_1.day1 import Day1


class day1(unittest.TestCase):
    def test_result(self):
        day1 = Day1()
        day1._inputfilename = "test_input.txt"
        day1.read_input()
        self.assertEqual([3, 4, 2, 1, 3, 3], day1.list1)
        self.assertEqual([4,3,5,3,9,3], day1.list2)
        distence = day1.calculate_distance()
        self.assertEqual(11, distence)
        simularity = day1.calculate_simularity()
        self.assertEqual(31, simularity)


if __name__ == '__main__':
    unittest.main()
