import unittest

from day_9.day import Day


class day(unittest.TestCase):
    def test_result(self):
        day = Day()
        day._inputfilename = "test_input.txt"
        day.read_input()
        day.extract_disk_map()
        self.assertEqual([0, 0, '.','.','.',1, 1, 1, '.','.','.',2, '.','.','.', 3, 3,3,'.', 4,4,'.',5,5,5,5,'.',
                          6,6,6,6,'.',7,7,7,'.',8,8,8,8,9,9], day.extracted_diskmap)
        day.defragment_disk()
        self.assertEqual("0099811188827773336446555566", "".join(map(str, day.defragmented_diskmap)))
        self.assertEqual(1928, day.calculate_checksum())


if __name__ == '__main__':
    unittest.main()
