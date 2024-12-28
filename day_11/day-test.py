import unittest

from day_11.day import Day


class day(unittest.TestCase):
    def test_result(self):
        day = Day()
        day._input_filename = "test_input.txt"
        day.read_input()
        self.assertEqual([125, 17], day.input)
        self.assertEqual(3, day.run(1))

if __name__ == '__main__':
    unittest.main()
