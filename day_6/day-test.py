import unittest

from day_6.day import Day6


class day(unittest.TestCase):
    def test_result(self):
        day = Day6()
        day._inputfilename = "test_input.txt"
        day.read_input()
        self.assertEqual(4, day.guard_x)
        self.assertEqual(6, day.guard_y)
        day.walk_guard()
        self.assertEqual(4, day.guard_x)
        self.assertEqual(1, day.guard_y)
        self.assertEqual(">", day.guard_direction)
        day.walk_guard()
        self.assertEqual(8, day.guard_x)
        self.assertEqual(1, day.guard_y)
        self.assertEqual("v", day.guard_direction)
        day.walk_guard()
        self.assertEqual(8, day.guard_x)
        self.assertEqual(6, day.guard_y)
        self.assertEqual("<", day.guard_direction)
        day.walk_guard()
        self.assertEqual(2, day.guard_x)
        self.assertEqual(6, day.guard_y)
        self.assertEqual("^", day.guard_direction)
        self.assertEqual(41, day.determine_guard_track())
        day.print_track()
        self.assertEqual(6, day.determine_possible_obstructions())


if __name__ == '__main__':
    unittest.main()
