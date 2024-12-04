import re


class Day4:
    def __init__(self):
        self._inputfilename = "input.txt"
        self.wordsearch = []

    def read_input(self):
        with open(self._inputfilename) as f:
            lines = f.readlines()
        for line in lines:
            self.wordsearch.append(line.strip())

    def count_xmas(self):
        count = 0
        count += count_horizontal(self.wordsearch)
        count += count_horizontal(transpose(self.wordsearch))
        count += count_horizontal(forward_cross2lines(self.wordsearch))
        count += count_horizontal(backward_cross2lines(self.wordsearch))
        return count

    def count_mas(self):
        return count_cross_mas(self.wordsearch)


def forward_cross2lines(words):
    cross_lines = []
    for x in range(len(words[0])):
        line = ""
        x_prev = x
        y = 0
        while x_prev >= 0:
            line += words[y][x_prev]
            x_prev -= 1
            y += 1
        cross_lines.append(line)
    for y in range(1, len(words)):
        line = ""
        y_prev = y
        x = len(words[0]) - 1
        while y_prev < len(words) and x >= 0:
            line += words[y_prev][x]
            y_prev += 1
            x -= 1
        cross_lines.append(line)
    return cross_lines

def backward_cross2lines(words):
    cross_lines = []
    for x in reversed(range(len(words[0]))):
        line = ""
        x_prev = x
        y = 0
        while x_prev < len(words[0]):
            line += words[y][x_prev]
            x_prev += 1
            y += 1
        cross_lines.append(line)
    for y in range(1, len(words)):
        line = ""
        y_prev = y
        x = 0
        while y_prev < len(words) and x < len(words[0]):
            line += words[y_prev][x]
            y_prev += 1
            x += 1
        cross_lines.append(line)
    return cross_lines


def transpose(words):
    trans_list = [[words[j][i] for j in range(len(words))] for i in range(len(words[0]))]
    transposed = []
    for line in trans_list:
        kars = ""
        for kar in line:
            kars += kar
        transposed.append(kars)
    return transposed


def count_horizontal(input_block):
    count = 0
    for line in input_block:
        count += count_xmas_horizontal_left2right(line)
        count += count_xmas_horizontal_left2right(line[::-1])
    return count


def count_xmas_horizontal_left2right(line):
    return len(re.findall(r'XMAS', line))


def count_cross_mas(input_block):
    count = 0
    for y in range(len(input_block)):
        for x in range(len(input_block[0])):
            if input_block[y][x] == "A":
                if 0 < y < len(input_block) - 1 and len(input_block[0]) - 1 > x > 0:
                    kar_left_up = input_block[y - 1][x - 1]
                    kar_left_down = input_block[y + 1][x - 1]
                    kar_right_up = input_block[y - 1][x + 1]
                    kar_right_down = input_block[y + 1][x + 1]
                    if ((kar_left_up == "M" and kar_right_down == "S") or
                       (kar_left_up == "S" and kar_right_down == "M")) and \
                        ((kar_left_down == "M" and kar_right_up == "S") or
                         (kar_left_down == "S" and kar_right_up == "M")):
                        count += 1
    return count



if __name__ == '__main__':
    day = Day4()
    day.read_input()
    print(day.count_xmas())
    print(day.count_mas())
