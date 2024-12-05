import unittest

from day_5.day import Day5


class day(unittest.TestCase):
    def test_result(self):
        day = Day5()
        day._inputfilename = "test_input.txt"
        day.read_input()
        self.assertEqual([13, 61, 47, 29, 53, 75], day.ordering_pairs[97])
        self.assertEqual([29, 13], day.ordering_pairs[53])
        self.assertEqual([75,47,61,53,29], day.updated_pagenumbers[0])
        self.assertEqual([97,13,75,29,47], day.updated_pagenumbers[5])
        self.assertEqual(143, day.determine_middlepagenumbers_of_correctupdate())
        self.assertEqual([[75,97,47,61,53], [61,13,29], [97,13,75,29,47]], day.incorrect_pagenumbers)
        self.assertEqual(123, day.correct_updates())

if __name__ == '__main__':
    unittest.main()
