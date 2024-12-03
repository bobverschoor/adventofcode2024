import unittest

from day_3.day import Day3


class day(unittest.TestCase):
    def test_result(self):
        day = Day3()
        day._inputfilename = "test_input.txt"
        day.read_input()
        self.assertEqual("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))", day.input)
        day.parse4mul()
        self.assertEqual(["mul(2,4)","mul(5,5)","mul(11,8)","mul(8,5)"], day.multiplies)
        self.assertEqual(161, day.calculate_sum_of_multiplies())
        day.multiplies = []
        dolines = day.parse4do_dont()
        self.assertEqual(["xmul(2,4)&mul[3,7]!^", "?mul(8,5))"], dolines)
        day.calculate_dolines()
        self.assertEqual(48, day.calculate_sum_of_multiplies())

if __name__ == '__main__':
    unittest.main()
