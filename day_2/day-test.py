import unittest

from day_2.day import Day, is_report_safe


class day(unittest.TestCase):
    def test_result(self):
        day = Day()
        day._inputfilename = "test_input.txt"
        day.read_input()
        self.assertEqual([7, 6, 4, 2, 1], day.reports[0])
        self.assertTrue(is_report_safe([7, 6, 4, 2, 1], 0))
        self.assertFalse(is_report_safe([1, 2, 7, 8, 9], 0))
        self.assertFalse(is_report_safe([9, 7, 6, 2, 1], 0))
        self.assertTrue(is_report_safe([1, 3, 2, 4, 5], 0))
        self.assertTrue(is_report_safe([8, 6, 4, 4, 1], 0))
        self.assertTrue(is_report_safe([1, 3, 6, 7, 9], 0))
        self.assertTrue(is_report_safe([93,92,91,88,87,86,85], 0))
        self.assertTrue(is_report_safe([1, 3, 4, 5, 8, 10, 7], 0))
        self.assertTrue(is_report_safe([7, 9, 12, 15, 16, 17, 20, 24], 0))
        self.assertTrue(is_report_safe([9, 8, 11, 12, 15, 17, 19], 0))
        self.assertEqual(4, day.report_safety())


if __name__ == '__main__':
    unittest.main()
