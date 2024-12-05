class Day5:
    def __init__(self):
        self._inputfilename = "input.txt"
        self.ordering_pairs = {}
        self.updated_pagenumbers = []
        self.incorrect_pagenumbers = []

    def read_input(self):
        with open(self._inputfilename) as f:
            lines = f.readlines()
        first_section = True
        for line in lines:
            line = line.strip()
            if line == "":
                first_section = False
                continue
            if first_section:
                ordering = list(map(int, line.split('|')))
                if ordering[0] in self.ordering_pairs:
                    self.ordering_pairs[ordering[0]].append(ordering[1])
                else:
                    self.ordering_pairs[ordering[0]] = [ordering[1]]
            else:
                self.updated_pagenumbers.append(list(map(int, line.split(','))))

    def determine_middlepagenumbers_of_correctupdate(self):
        middlepagenumber = 0
        for pagenumbers in self.updated_pagenumbers:
            update_correct, changeable1, changeable2 = self.is_updates_correct(pagenumbers)
            if update_correct:
                middlepagenumber += pagenumbers[int(len(pagenumbers)/2)]
            else:
                self.incorrect_pagenumbers.append(pagenumbers)
        return middlepagenumber

    def correct_updates(self):
        middlepagenumber = 0
        for pagenumbers in self.incorrect_pagenumbers:
            update_correct, changeable1, changeable2 = self.is_updates_correct(pagenumbers)
            while not update_correct:
                temp = pagenumbers[changeable1]
                pagenumbers[changeable1] = pagenumbers[changeable2]
                pagenumbers[changeable2] = temp
                update_correct, changeable1, changeable2 = self.is_updates_correct(pagenumbers)
            middlepagenumber += pagenumbers[int(len(pagenumbers)/2)]
        return middlepagenumber


    def is_updates_correct(self, updates):
        for i in range(len(updates)):
            for j in range(i + 1, len(updates)):
                if updates[i] in self.ordering_pairs:
                    if updates[j] not in self.ordering_pairs[updates[i]]:
                        return False, j, i
        updates = list(reversed(updates))
        for i in range(len(updates)):
            for j in range(i + 1, len(updates)):
                if updates[i] in self.ordering_pairs:
                    if updates[j] in self.ordering_pairs[updates[i]]:
                        return False, len(updates) - i - 1, len(updates) - j - 1
        return True, 0, 0


if __name__ == '__main__':
    day = Day5()
    day.read_input()
    print(day.determine_middlepagenumbers_of_correctupdate())
    print(day.correct_updates())
