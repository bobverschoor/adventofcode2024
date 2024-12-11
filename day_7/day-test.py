import unittest

from day_7.day import Day7


class day(unittest.TestCase):
    def test_result(self):
        day = Day7()
        day._inputfilename = "test_input.txt"
        day.read_input()
        self.assertEqual(9, len(day.input))
        day.determine_calibration_result()


if __name__ == '__main__':
    unittest.main()
