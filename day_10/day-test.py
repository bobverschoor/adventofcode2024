import unittest

from day_10.day import Day


class day(unittest.TestCase):
    def test_result_1(self):
        day = Day()
        day._input_filename = "test_input.txt"
        day.read_input()
        self.assertEqual(7, len(day.input))
        self.assertEqual(['.','.','.','0','.','.','.'], day.input[0])
        day.walk_valid_moves(0,0, day.input)
        self.assertEqual(0, day.number_of_trailheads)
        day.walk_valid_moves(3,0, day.input)
        self.assertEqual(2, day.number_of_trailheads)

    def test_result_2(self):
        day = Day()
        day._input_filename = "test_input2.txt"
        day.read_input()
        day.walk_valid_moves(3,0, day.input)
        self.assertEqual(4, day.number_of_trailheads)

    def test_result_3(self):
        day = Day()
        day._input_filename = "test_input3.txt"
        day.read_input()
        day.get_tailheads()
        self.assertEqual(3, day.number_of_trailheads)

    def test_result_4(self):
        day = Day()
        day._input_filename = "test_input4.txt"
        day.read_input()
        day.get_tailheads()
        self.assertEqual(36, day.number_of_trailheads)

    def test_result_5(self):
        day = Day()
        day._input_filename = "test_input5.txt"
        day.read_input()
        day.distinct = True
        day.get_tailheads()
        self.assertEqual(3, day.number_of_trailheads)

    def test_result_6(self):
        day = Day()
        day._input_filename = "test_input6.txt"
        day.read_input()
        day.distinct = True
        day.get_tailheads()
        self.assertEqual(13, day.number_of_trailheads)

    def test_result_7(self):
        day = Day()
        day._input_filename = "test_input7.txt"
        day.read_input()
        day.distinct = True
        day.get_tailheads()
        self.assertEqual(227, day.number_of_trailheads)

    def test_result_8(self):
        day = Day()
        day._input_filename = "test_input8.txt"
        day.read_input()
        day.distinct = True
        day.get_tailheads()
        self.assertEqual(81, day.number_of_trailheads)

if __name__ == '__main__':
    unittest.main()
