class Day:
    def __init__(self):
        self._inputfilename = "input.txt"

    def read_input(self):
        with open(self._inputfilename) as f:
            lines = f.readlines()
        for line in lines:
            pass


if __name__ == '__main__':
    day = Day()
    day.read_input()
