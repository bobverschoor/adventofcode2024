
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
            all_permutations = build_binary_tree(calc[1])



class Node:
    def __init__(self, data):
        self.plus = None
        self.multiply = None
        self.number = data[0]
        if len(data) > 1:
            self.insert(data[1:])

    def insert(self, data):
        self.plus = Node(data)
        self.multiply = Node(data)

    def uitkomst(self):
        if self.plus:
            return self.number + self.plus.uitkomst()
        if self.multiply:
            return self.number * self.multiply.uitkomst()


def build_binary_tree(calc):
    return Node(calc)


def collect_paths(node, path, paths):
    if node is None:
        return

    # Append this node to the path
    path.append(node.data)

    # If it's a leaf node, store the path
    if node.left is None and node.right is None:
        paths.append(list(path))
    else:
        # Otherwise, try both subtrees
        collect_paths(node.left, path, paths)
        collect_paths(node.right, path, paths)
    # Backtrack: remove the last element from the path
    path.pop()


def paths(root):
    paths = []
    collect_paths(root, [], paths)
    return paths



if __name__ == '__main__':
    day = Day7()
    day.read_input()
