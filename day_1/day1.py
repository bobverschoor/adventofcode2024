class Day1:
    def __init__(self):
        self._inputfilename = "input.txt"
        self.list1 = []
        self.list2 = []

    def read_input(self):
        with open(self._inputfilename) as f:
            lines = f.readlines()
        for line in lines:
            first, second = line.split()
            self.list1.append(int(first))
            self.list2.append(int(second))

    def calculate_distance(self):
        list1 = sorted(self.list1)
        list2 = sorted(self.list2)
        distance = 0
        for i in range(len(list1)):
            distance += abs(list1[i] - list2[i])
        return distance

    def calculate_simularity(self):
        simularity = 0
        for i in range(len(self.list1)):
            simularity += self.list1[i] * self.appearance_list2(self.list1[i])
        return simularity

    def appearance_list2(self, number):
        appearance = 0
        for i in range(len(self.list2)):
            if number == self.list2[i]:
                appearance += 1
        return appearance

if __name__ == '__main__':
    day_1 = Day1()
    day_1.read_input()
    print(day_1.calculate_distance())
    print(day_1.calculate_simularity())
