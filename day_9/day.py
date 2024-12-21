from itertools import batched


class Day:
    def __init__(self):
        self._inputfilename = "input.txt"
        self.diskmap = ""
        self.extracted_diskmap = []
        self.defragmented_diskmap = []

    def read_input(self):
        with open(self._inputfilename) as f:
            self.diskmap = f.read()

    def extract_disk_map(self):
        self.extracted_diskmap = []
        id = 0
        if len(self.diskmap) % 2 == 1:
            self.diskmap = self.diskmap + '0'
        for fileblock, freespaceblock in batched(self.diskmap, n=2):
            for i in range(int(fileblock)):
                self.extracted_diskmap.append(id)
            for i in range(int(freespaceblock)):
                self.extracted_diskmap.append('.')
            id += 1

    def defragment_disk(self):
        last_item = len(self.extracted_diskmap) - 1
        for i in range(len(self.extracted_diskmap)):
            if self.extracted_diskmap[i] == '.':
                while self.extracted_diskmap[last_item] == '.':
                    last_item -= 1
                if last_item > i:
                    self.defragmented_diskmap.append(self.extracted_diskmap[last_item])
                    self.extracted_diskmap[last_item] = '.'
                else:
                    break
            else:
                self.defragmented_diskmap.append(self.extracted_diskmap[i])

    def defragment_disk2(self):
        original_extracted_diskmap = self.extracted_diskmap.copy()
        start_next_block = len(original_extracted_diskmap) - 1
        while start_next_block >= 0:
            length_block, id, start_next_block  = self.get_block_from_end(start_next_block)
            if self.fit_block_in_extracted_map(length_block, id, start_next_block + 1) and length_block > 0:
                for i in range(start_next_block + 1, start_next_block + 1 + length_block):
                    self.extracted_diskmap[i] = '.'
        self.defragmented_diskmap = self.extracted_diskmap

    def fit_block_in_extracted_map(self, length_block, id, end_fit):
        start_of_fitting_block = self.get_start_of_empty_space_with_length(length_block, end_fit)
        if start_of_fitting_block >= 0:
            for i in range(length_block):
                self.extracted_diskmap[start_of_fitting_block + i] = id
            return True
        else:
            return False

    def get_start_of_empty_space_with_length(self, length_block, end_fit):
        free_space_length = 0
        start_of_block = -1
        for i in range(end_fit):
            if self.extracted_diskmap[i] == '.':
                if start_of_block == -1:
                    start_of_block = i
                free_space_length += 1
            else:
                if free_space_length >= length_block:
                    return start_of_block
                else:
                    free_space_length = 0
                    start_of_block = -1
        if free_space_length >= length_block:
            return start_of_block
        return -1


    def get_block_from_end(self, item_nr):
        if item_nr > 0:
            for i in range(item_nr, 0, -1):
                while self.extracted_diskmap[i] == '.':
                    i -= 1
                id = self.extracted_diskmap[i]
                start_block = i
                length = 0
                if start_block >= 0:
                    while self.extracted_diskmap[start_block] == id:
                        start_block -= 1
                        length += 1
                return length, id, start_block
        return -1, -1, -1


    def calculate_checksum(self):
        checksum = 0
        for i in range(len(self.defragmented_diskmap)):
            if self.defragmented_diskmap[i] != '.':
               checksum += i * int(self.defragmented_diskmap[i])
        return checksum



if __name__ == '__main__':
    day = Day()
    day.read_input()
    day.extract_disk_map()
    day.defragment_disk()
    print(day.calculate_checksum())
    day.extract_disk_map()
    day.defragment_disk2()
    print(day.calculate_checksum())
