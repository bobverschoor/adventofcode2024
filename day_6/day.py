class Day6:
    def __init__(self):
        self._inputfilename = "input.txt"
        self.input = []
        self.guard_x = 0
        self.guard_y = 0
        self.init_guard_x = 0
        self.init_guard_y = 0
        self.guard_direction = "^"
        self.init_guard_direction = "^"
        self.track = []
        self.loop_detected = False

    def init_track(self):
        self.track = []
        for y in range(len(self.input)):
            line = []
            for x in range(len(self.input[y])):
                line.append(["."])
            self.track.append(line)

    def read_input(self):
        with open(self._inputfilename) as f:
            lines = f.readlines()
        y = 0
        x = 0
        j = 0
        for line in lines:
            self.input.append(list(line.strip()))
            if self.init_guard_direction in line:
                for i in range(len(line)):
                    if line[i] == self.guard_direction:
                        x = i
                        y = j
            j += 1
        self.init_guard_x = x
        self.init_guard_y = y
        self.guard_x = self.init_guard_x
        self.guard_y = self.init_guard_y
        self.init_track()

    def determine_possible_obstructions(self):
        options = 0
        possibilities = self.new_track()
        for y in range(len(possibilities)):
            for x in range(len(possibilities[y])):
                if is_possibilities(possibilities[y][x]):
                    grid = self.new_input()
                    self.init_track()
                    self.guard_x = self.init_guard_x
                    self.guard_y = self.init_guard_y
                    self.guard_direction = self.init_guard_direction
                    grid[y][x] = "#"
                    while self.walk_guard(grid):
                        if self.is_start_position() or self.has_walked_before():
                            options += 1
                            break
        return options

    def determine_guard_track(self):
        steps = 0
        while self.walk_guard():
            pass
        for y in range(len(self.track)):
            for x in range(len(self.track[y])):
                if ('^' in self.track[y][x] or ">" in self.track[y][x] or
                        "v" in self.track[y][x] or "<" in self.track[y][x]):
                    steps += 1
        return steps

    def walk_guard(self, area=None):
        if not area:
            area = self.input
        try:
            if self.guard_direction == "^":
                while area[self.guard_y][self.guard_x] != "#":
                    if self.guard_x < 0 or self.guard_y < 0:
                        raise IndexError
                    self.track[self.guard_y][self.guard_x].append(self.guard_direction)
                    self.guard_y -= 1
                self.guard_direction = ">"
                self.guard_y += 1
            elif self.guard_direction == ">":
                while area[self.guard_y][self.guard_x] != "#":
                    if self.guard_x < 0 or self.guard_y < 0:
                        raise IndexError
                    self.track[self.guard_y][self.guard_x].append(self.guard_direction)
                    self.guard_x += 1
                self.guard_direction = "v"
                self.guard_x -= 1
            elif self.guard_direction == "v":
                while area[self.guard_y][self.guard_x] != "#":
                    if self.guard_x < 0 or self.guard_y < 0:
                        raise IndexError
                    self.track[self.guard_y][self.guard_x].append(self.guard_direction)
                    self.guard_y += 1
                self.guard_direction = "<"
                self.guard_y -= 1
            elif self.guard_direction == "<":
                while area[self.guard_y][self.guard_x] != "#":
                    if self.guard_x < 0 or self.guard_y < 0:
                        raise IndexError
                    self.track[self.guard_y][self.guard_x].append(self.guard_direction)
                    self.guard_x -= 1
                self.guard_direction = "^"
                self.guard_x += 1
            return True
        except IndexError:
            #print("Index out of bounds")
            #print(self.guard_x, self.guard_y, self.guard_direction)
            return False

    def print_track(self):
        for y in range(len(self.track)):
            line = ""
            for x in range(len(self.track[y])):
                for z in self.track[y][x]:
                    line += str(z)
            print(str(y) + line)

    def new_input(self):
        new_input = []
        for y in range(len(self.input)):
            line = []
            for x in range(len(self.input[y])):
                line.append(self.input[y][x])
            new_input.append(line)
        return new_input

    def is_start_position(self):
        if (self.guard_direction == self.init_guard_direction and
                self.guard_y == self.init_guard_y and
                self.guard_x == self.init_guard_x):
            return True
        return False

    def has_walked_before(self):
        for y in range(len(self.track)):
            for x in range(len(self.track[y])):
                if (is_multiple("^", self.track[y][x]) or is_multiple(">", self.track[y][x]) or
                        is_multiple("v", self.track[y][x]) or is_multiple("<", self.track[y][x])):
                    return True
        return False

    def new_track(self):
        new_input = []
        for y in range(len(self.track)):
            line = []
            for x in range(len(self.track[y])):
                line.append(self.track[y][x])
            new_input.append(line)
        return new_input


def is_multiple(el, ellist):
    times = 0
    for kar in ellist:
        if el == kar:
            times += 1
    return times > 1

def is_possibilities(items):
    for el in items:
        if el in ["^", ">", "v", "<"]:
            return True
    return False

if __name__ == '__main__':
    day = Day6()
    day.read_input()
    print(day.determine_guard_track())
    print(day.determine_possible_obstructions() - 3)