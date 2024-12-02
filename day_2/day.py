class Day:
    def __init__(self):
        self._inputfilename = "input.txt"
        self.reports = []

    def read_input(self):
        with open(self._inputfilename) as f:
            lines = f.readlines()
        for line in lines:
            self.reports.append(list(map(int, line.split())))

    def report_safety(self):
        nr_of_safe_reports = 0
        i = 1
        for report in self.reports:
            if is_report_safe(report, 0):
                nr_of_safe_reports += 1
            else:
                print("False :" + str(i) + ":" + str(report))
            i += 1
        return nr_of_safe_reports


def is_report_safe(report, toleration):
    direction = ""
    if toleration > 1:
        return False
    for i in range(1, len(report)):
        difference = report[i] - report[i - 1]
        if 1 <= abs(difference) <= 3:
            direction = bepaal_richting(difference, direction)
            if not is_juiste_richting(difference, direction):
                toleration += 1
                for j in range(len(report)):
                    new_report = report[:j]
                    new_report.extend(report[j + 1:])
                    if is_report_safe(new_report, toleration):
                        return True
                return False
        else:
            toleration += 1
            for j in range(len(report)):
                new_report = report[:j]
                new_report.extend(report[j + 1:])
                if is_report_safe(new_report, toleration):
                    return True
            return False
    return True


def bepaal_richting(difference, direction):
    if direction:
        return direction
    if difference > 0:
        return "+"
    else:
        return "-"


def is_juiste_richting(difference, direction):
    if difference < 0:
        if direction == "+":
            return False
        else:
            return True
    else:
        if direction == "-":
            return False
        else:
            return True


if __name__ == '__main__':
    day = Day()
    day.read_input()
    print(day.report_safety())
