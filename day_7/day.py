
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

    def determine_calibration_result(self, binary = True):
        totaal = 0
        for calc in self.input:
            uitkomst = calc[0]
            if binary:
                all_permutations = build_binary_tree(calc[1])
            else:
                all_permutations = build_ternary_tree(calc[1])
            if is_correct_outcome(uitkomst, all_permutations):
                totaal = totaal + uitkomst
        return totaal

    def determine_calibration_result_part2(self):
        totaal = 0
        for calc in self.input:
            uitkomst = calc[0]
            all_permutations = build_ternary_tree(calc[1])
            if is_correct_outcome(uitkomst, all_permutations):
                totaal = totaal + uitkomst
        return totaal


class Node_binary:
    def __init__(self, data, operator = ""):
        self.left = None
        self.right = None
        self.number = data[0]
        self.operator = operator
        if len(data) > 1:
            self.insert(data[1:])

    def insert(self, data):
        self.left = Node_binary(data, "+")
        self.right = Node_binary(data, "*")


class Node_ternary:
    def __init__(self, data, operator = ""):
        self.left = None
        self.right = None
        self.middle = None
        self.number = data[0]
        self.operator = operator
        if len(data) > 1:
            self.insert(data[1:])

    def insert(self, data):
        self.left = Node_ternary(data, "+")
        self.right = Node_ternary(data, "*")
        self.middle = Node_ternary(data, "||")

def build_ternary_tree(calc):
    return Node_ternary(calc)

def build_binary_tree(calc):
    return Node_binary(calc)

def is_correct_outcome(uitkomst, permutations):
    paths = []
    collect_paths(permutations, [], paths)
    for path in paths:
        if calculate_left2right(path) == uitkomst:
            return True
    return False


def collect_paths(node, path, paths):
    if node is None:
        return

    # Append this node to the path
    if node.operator != "":
        path.append(node.operator)
    path.append(node.number)


    # If it's a leaf node, store the path
    if node.left is None and node.right is None:
        paths.append(list(path))
    else:
        # Otherwise, try both subtrees
        collect_paths(node.left, path, paths)
        collect_paths(node.right, path, paths)
        if isinstance(node, Node_ternary):
            collect_paths(node.middle, path, paths)
    # Backtrack: remove the last element from the path
    path.pop()
    if len(path) > 1:
        path.pop()


def calculate_left2right(som):
    uitkomst = 0
    i = 0
    while i < len(som):
        if uitkomst == 0:
            op1 = som[i]
            i += 1
            if som[i] == '+':
                i += 1
                op2 = som[i]
                uitkomst = op1 + op2
            elif som[i] == '*':
                i += 1
                op2 = som[i]
                uitkomst = op1 * op2
            elif som[i] == '||':
                i += 1
                op2 = som[i]
                uitkomst = int(str(op1) + str(op2))
        else:
            if som[i] == '+':
                i += 1
                op2 = som[i]
                uitkomst = uitkomst + op2
            elif som[i] == '*':
                i += 1
                op2 = som[i]
                uitkomst = uitkomst * op2
            elif som[i] == '||':
                i += 1
                op2 = som[i]
                uitkomst = int(str(uitkomst) + str(op2))

        i += 1

    return uitkomst


if __name__ == '__main__':
    day = Day7()
    day.read_input()
    print(day.determine_calibration_result())
    print(day.determine_calibration_result(binary=False))