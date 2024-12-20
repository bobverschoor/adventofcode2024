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

    def calculate_checksum(self):
        checksum = 0
        for i in range(len(self.defragmented_diskmap)):
            checksum += i * int(self.defragmented_diskmap[i])
        return checksum



if __name__ == '__main__':
    day = Day()
    day.read_input()
    day.extract_disk_map()
    day.defragment_disk()
    print(day.calculate_checksum())
