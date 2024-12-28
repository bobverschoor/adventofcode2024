import functools


class Day:
    def __init__(self):
        self._input_filename = "input.txt"
        self.input = []
        self.times_blinked = 0

    def read_input(self):
        with (open(self._input_filename) as f):
            line = f.readline()
        line = line.strip()
        self.input = list(map(int, line.split()))

    @functools.cache
    def single_blink(self, value):
        text_value = str(value)
        num_digits = len(text_value)
        if value == 0:
            return (1, None)
        elif num_digits % 2 == 0:
            half = num_digits // 2
            links = int(text_value[:half])
            rechts = int(text_value[half:])
            return (links, rechts)
        else:
            return (value * 2024, None)

    @functools.cache
    def count_stone_blinks(self, stone, depth):
        left_stone, right_stone = self.single_blink(stone)
        if depth == 1:
            if right_stone is None:
                return 1
            else:
                return 2
        else:
            output = self.count_stone_blinks(left_stone, depth - 1)
            if right_stone is not None:
                output += self.count_stone_blinks(right_stone, depth - 1)
            return output

    def run(self, count):
        output = 0
        for stone in self.input:
            output += self.count_stone_blinks(stone, count)
        return output


if __name__ == '__main__':
    day = Day()
    day.read_input()
    print(day.run(25))
    print(day.run(75))
