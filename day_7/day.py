import itertools


class Day7:
    def __init__(self):
        self._inputfilename = "input.txt"
        self.input = []

    def read_input(self):
        with open(self._inputfilename) as f:
            lines = f.readlines()
        for line in lines:
            line = line.strip()
            uitkomst, factor = line.split(':')
            factor = factor.strip()
            factoren = list(map(int, factor.split(' ')))
            self.input.append([int(uitkomst), factoren])

    def determine_calibration_result(self):
        possible_calibrations = []
        for calc in self.input:
            uitkomst = calc[0]
            all_permutations = calculate_possibilities(calc[1])
            print(all_permutations)


def calculate_possibilities(calc):
    calc_permutations = []
    for c in calc:
        if len(calc_permutations) != 0:
            calc_permutations.append("+")
            calc_permutations.append(c)
        else:
            calc_permutations.append(c)
    all_permutations = []
    max_permutations = 2 ** (len(calc) - 1 )
    for i in range(max_permutations):
        perm = []
        for c in range(len(calc_permutations)):
            if '+' == calc_permutations[c]:
                perm.append('+')
                calc_permutations[c] = '*'
            elif '*' == calc_permutations[c]:
                perm.append('*')
                calc_permutations[c] = '+'
            else:
                perm.append(calc_permutations[c])
        all_permutations.append(perm)
    return all_permutations


if __name__ == '__main__':
    day = Day7()
    day.read_input()
