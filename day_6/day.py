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
        for y in range(len(self.input)):
            for x in range(len(self.input[y])):
                if self.input[y][x] != "#" and self.input[y][x] != "^":
                    grid = self.new_input()
                    self.init_track()
                    self.guard_x = self.init_guard_x
                    self.guard_y = self.init_guard_y
                    self.guard_direction = self.init_guard_direction
                    self.loop_detected = False
                    grid[y][x] = "#"
                    self.print_track()
                    while self.walk_guard(grid):
                        pass
                    if self.loop_detected:
                        print("option: " + str(x) + ":" + str(y))
                        self.print_track()
                        options += 1
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
                    if self.guard_direction in self.track[self.guard_y][self.guard_x]:
                        self.loop_detected = True
                        raise IndexError
                    if self.track[self.guard_y][self.guard_x] == ['.']:
                        self.track[self.guard_y][self.guard_x] = []
                    self.track[self.guard_y][self.guard_x].append(self.guard_direction)
                    self.guard_y -= 1
                self.guard_y += 1
                self.guard_direction = ">"
            elif self.guard_direction == ">":
                while area[self.guard_y][self.guard_x] != "#":
                    if self.guard_x < 0 or self.guard_y < 0:
                        raise IndexError
                    if self.guard_direction in self.track[self.guard_y][self.guard_x]:
                        self.loop_detected = True
                        raise IndexError
                    if self.track[self.guard_y][self.guard_x] == ['.']:
                        self.track[self.guard_y][self.guard_x] = []
                    self.track[self.guard_y][self.guard_x].append(self.guard_direction)
                    self.guard_x += 1
                self.guard_x -= 1
                self.guard_direction = "v"
            elif self.guard_direction == "v":
                while area[self.guard_y][self.guard_x] != "#":
                    if self.guard_x < 0 or self.guard_y < 0:
                        raise IndexError
                    if self.guard_direction in self.track[self.guard_y][self.guard_x]:
                        self.loop_detected = True
                        raise IndexError
                    if self.track[self.guard_y][self.guard_x] == ['.']:
                        self.track[self.guard_y][self.guard_x] = []
                    self.track[self.guard_y][self.guard_x].append(self.guard_direction)
                    self.guard_y += 1
                self.guard_y -= 1
                self.guard_direction = "<"
            elif self.guard_direction == "<":
                while area[self.guard_y][self.guard_x] != "#":
                    if self.guard_x < 0 or self.guard_y < 0:
                        raise IndexError
                    if self.guard_direction in self.track[self.guard_y][self.guard_x]:
                        self.loop_detected = True
                        raise IndexError
                    if self.track[self.guard_y][self.guard_x] == ['.']:
                        self.track[self.guard_y][self.guard_x] = []
                    self.track[self.guard_y][self.guard_x].append(self.guard_direction)
                    self.guard_x -= 1
                self.guard_x += 1
                self.guard_direction = "^"
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



if __name__ == '__main__':
    day = Day6()
    day.read_input()
    print(day.determine_guard_track())
    print(day.determine_possible_obstructions())