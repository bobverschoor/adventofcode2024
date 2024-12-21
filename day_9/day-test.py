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
        day.extract_disk_map()
        self.assertEqual((2, 9, 39),
                         day.get_block_from_end(41))
        self.assertEqual((4, 8, 35),
                         day.get_block_from_end(39))
        self.assertEqual((3, 7, 31),
                         day.get_block_from_end(35))
        self.assertEqual((1, 2, 10),
                         day.get_block_from_end(11))
        self.assertEqual((2, 0, -1),
                         day.get_block_from_end(1))
        self.assertEqual(2, day.get_start_of_empty_space_with_length(3, 42))
        self.assertEqual(-1, day.get_start_of_empty_space_with_length(4, 42))
        day.extracted_diskmap[2] = 9
        day.extracted_diskmap[3] = 9
        day.extracted_diskmap[40] = '.'
        day.extracted_diskmap[41] = '.'
        self.assertEqual(8, day.get_start_of_empty_space_with_length(3, 39))
        day.fit_block_in_extracted_map(4, 8, 35)
        self.assertEqual("0099.111...2...333.44.5555.6666.777.8888..", "".join(map(str, day.extracted_diskmap)))
        day.fit_block_in_extracted_map(3, 7, 35)
        day.extracted_diskmap[32] = '.'
        day.extracted_diskmap[33] = '.'
        day.extracted_diskmap[34] = '.'
        self.assertEqual("0099.1117772...333.44.5555.6666.....8888..", "".join(map(str, day.extracted_diskmap)))
        day.fit_block_in_extracted_map(2, 4, 20)
        day.extracted_diskmap[19] = '.'
        day.extracted_diskmap[20] = '.'
        self.assertEqual("0099.111777244.333....5555.6666.....8888..", "".join(map(str, day.extracted_diskmap)))
        day.fit_block_in_extracted_map(1, 2, 12)
        day.extracted_diskmap[11] = '.'
        self.assertEqual("00992111777.44.333....5555.6666.....8888..", "".join(map(str, day.extracted_diskmap)))
        day.extract_disk_map()
        day.defragment_disk2()
        self.assertEqual("00992111777.44.333....5555.6666.....8888..", "".join(map(str, day.extracted_diskmap)))
        self.assertEqual(2858, day.calculate_checksum())

    def test_part2(self):
        day = Day()
        day.diskmap = "1313165"
        day.extract_disk_map()
        day.defragment_disk2()
        self.assertEqual(169, day.calculate_checksum())

if __name__ == '__main__':
    unittest.main()
