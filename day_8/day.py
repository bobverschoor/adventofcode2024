class Day:
    def __init__(self):
        self._inputfilename = "input.txt"
        self.input = []
        self.antinodes = []

    def read_input(self):
        with open(self._inputfilename) as f:
            lines = f.readlines()
        for line in lines:
            line = line.strip()
            self.input.append(list(line))
        for y in range(len(self.input)):
            self.antinodes.append([])
            for x in range(len(self.input[y])):
                self.antinodes[y].append('.')

    def nr_of_antinodes(self):
        nr = 0
        for y in range(len(self.antinodes)):
            for x in range(len(self.antinodes[y])):
                if self.antinodes[y][x] == '#':
                    nr += 1
        return nr

    def map_antinodes(self, all=False):
        for y in range(len(self.input)):
            for x in range(len(self.input[y])):
                if self.input[y][x] != '.':
                    if all:
                        self.antinodes[y][x] = '#'
                    antenna_frequency = self.input[y][x]
                    antenna_pairs = self.find_antenna_pairs_xy(antenna_frequency, y)
                    self.mark_antinodes(antenna_pairs, all)

    def find_antenna_pairs_xy(self, antenna_frequency, y_start):
        pairs = []
        for y in range(y_start, len(self.input)):
            for x in range(len(self.input[y])):
                if self.input[y][x] == antenna_frequency:
                    pairs.append((x, y))
        return pairs

    def mark_antinodes(self, antenna_pairs, all=False):
        while len(antenna_pairs) > 0:
            pair = antenna_pairs.pop(0)
            for other_pair in antenna_pairs:
                if all:
                    for antinode in self.find_all_antinodes(pair, other_pair):
                        x, y = antinode
                        self.place_marker(x, y)
                else:
                    x, y = find_antinode(pair, other_pair)
                    self.place_marker(x, y)
                    x, y = find_antinode(other_pair, pair)
                    self.place_marker(x, y)

    def place_marker(self, x, y):
        if self.on_grid(x, y):
            self.antinodes[y][x] = '#'

    def find_all_antinodes(self, pair1, pair2):
        direction = tuple(map(lambda i, j: i - j, pair1, pair2))
        antinodes = self.all_antinodes_in_one_direction(pair1, direction)
        direction = tuple(map(lambda i, j: i - j, pair2, pair1))
        antinodes.extend(self.all_antinodes_in_one_direction(pair1, direction))
        return antinodes


    def all_antinodes_in_one_direction(self, pair1, direction):
        antinodes = []
        while True:
            x, y = tuple(map(sum, zip(pair1, direction)))
            if self.on_grid(x, y):
                pair1 = (x, y)
                antinodes.append(pair1)
            else:
                return antinodes

    def on_grid(self, x, y):
        if 0 <= x < len(self.input[0]) and 0 <= y < len(self.input):
            return True
        return False



def find_antinode(pair1, pair2):
    direction = tuple(map(lambda i, j: i - j, pair1, pair2))
    return tuple(map(sum, zip(pair1, direction)))



if __name__ == '__main__':
    day = Day()
    day.read_input()
    day.map_antinodes()
    print(day.nr_of_antinodes())
    day_p2 = Day()
    day_p2.read_input()
    day_p2.map_antinodes(all=True)
    print(day_p2.nr_of_antinodes())