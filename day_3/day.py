import re


class Day3:
    def __init__(self):
        self._inputfilename = "input.txt"
        self.input = ""
        self.multiplies = []

    def read_input(self):
        with open(self._inputfilename) as f:
            self.input = f.readline()

    def parse4mul(self, line = ""):
        if line == "":
            line = self.input
        pattern = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
        self.multiplies.extend(pattern.findall(line))

    def parse4do_dont(self):
        donotlines = re.split(r"don\'t\(\)", self.input)
        dolines = [donotlines[0]] # de eerste is altijd do
        for line in donotlines[1:]:
            doline = re.split(r"do\(\)", line)
            dolines.extend(doline[1:])
        return dolines

    def calculate_dolines(self):
        for line in self.parse4do_dont():
            self.parse4mul(line)

    def calculate_sum_of_multiplies(self):
        sum = 0
        for m in self.multiplies:
            sum += int(multiply(m))
        return sum

def multiply(m):
    factors = re.findall(r'(\d+)', m)
    return int(factors[0]) * int(factors[1])


if __name__ == '__main__':
    day = Day3()
    day.read_input()
    day.parse4mul()
    print(day.calculate_sum_of_multiplies())
    day.multiplies = []
    day.calculate_dolines()
    print(day.calculate_sum_of_multiplies())
