from copy import deepcopy

class Day:
    def __init__(self):
        self._input_filename = "input.txt"
        self.input = []
        self.number_of_trailheads = 0
        self.reached_tops = []
        self.distinct = False

    def read_input(self):
        with open(self._input_filename) as f:
            lines = f.readlines()
        for line in lines:
            line = line.strip()
            self.input.append(list(line))

    def get_tailheads(self):
        for y in range(len(self.input)):
            for x in range(len(self.input[y])):
                if self.input[y][x] == '0':
                    grid = deepcopy(self.input)
                    self.reached_tops = []
                    self.walk_valid_moves(x, y, grid)


    def walk_valid_moves(self, x, y, grid):
        if grid[y][x] != '.':
            value = int(grid[y][x])
        else:
            value = grid[y][x]
        if value == 9:
            if self.distinct:
                self.number_of_trailheads += 1
            else:
                if not top_already_reached(x, y, self.reached_tops):
                    self.number_of_trailheads += 1
                    self.reached_tops.append((x, y))
        else:
            if is_valid_int(x, y + 1, value, grid):
                self.walk_valid_moves(x, y + 1, grid)
            if is_valid_int(x + 1, y, value, grid):
                self.walk_valid_moves(x + 1, y, grid)
            if is_valid_int(x, y - 1, value, grid):
                self.walk_valid_moves(x, y - 1, grid)
            if is_valid_int(x - 1, y, value, grid):
                self.walk_valid_moves(x - 1, y, grid)

def is_valid_int(x, y, value, grid):
    if 0 <= y < len(grid) and 0 <= x < len(grid[y]):
        if grid[y][x] != '.' and int(grid[y][x]) == value + 1:
            return True
    return False


def top_already_reached(x, y, tops):
    for top in tops:
        reached_x, reached_y = top
        if reached_x == x and reached_y == y:
            return True
    return False


if __name__ == '__main__':
    day = Day()
    day.read_input()
    day.get_tailheads()
    print(day.number_of_trailheads)

    day2 = Day()
    day2.read_input()
    day2.distinct = True
    day2.get_tailheads()
    print(day2.number_of_trailheads)
