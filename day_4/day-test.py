import unittest

from day_4.day import Day4, count_xmas_horizontal_left2right, transpose, forward_cross2lines, backward_cross2lines


class day(unittest.TestCase):
    def test_result(self):
        day = Day4()
        day._inputfilename = "test_input.txt"
        day.read_input()
        self.assertEqual("MMMSXXMASM",day.wordsearch[0])
        self.assertEqual("MXMXAXMASX",day.wordsearch[9])

        self.assertEqual(1, count_xmas_horizontal_left2right("MMMSXXMASM"))
        self.assertEqual(1, count_xmas_horizontal_left2right("MMMSXMXMAS"))
        self.assertEqual(["147", "258", "369"], transpose(["123", "456", "789"]))
        self.assertEqual(["147", "258"], transpose(["12", "45", "78"]))
        crosslines = forward_cross2lines(day.wordsearch)
        self.assertEqual(19, len(crosslines))
        crosslines = backward_cross2lines(day.wordsearch)
        self.assertEqual(19, len(crosslines))
        self.assertEqual(18, day.count_xmas())
        self.assertEqual(9, day.count_mas())


if __name__ == '__main__':
    unittest.main()
