import unittest

from day_7.day import Day7, calculate_left2right


class day(unittest.TestCase):
    def test_result(self):
        day = Day7()
        day._inputfilename = "test_input.txt"
        day.read_input()
        self.assertEqual(9, len(day.input))
        self.assertEqual(29, calculate_left2right([10, '+', 19]))
        self.assertEqual(190, calculate_left2right([10, '*', 19]))
        self.assertEqual(205, calculate_left2right([10, '*', 19, '+', 15]))
        self.assertEqual(3749, day.determine_calibration_result())
        self.assertEqual(1019, calculate_left2right([10, '||', 19]))
        self.assertEqual(19015, calculate_left2right([10, '*', 19, '||', 15]))
        self.assertEqual(11387, day.determine_calibration_result(binary=False))

if __name__ == '__main__':
    unittest.main()
