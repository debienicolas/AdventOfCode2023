
def string_to_int(string):
    if "one" in string:
        string = string.replace("one", "o1e")
    if "two" in string:
        string = string.replace("two", "t2o")
    if "three" in string:
        string = string.replace("three", "t3ree")
    if "four" in string:
        string = string.replace("four", "f4ur")
    if "five" in string:
        string = string.replace("five", "f5ve")
    if "six" in string:
        string = string.replace("six", "s6x")
    if "seven" in string:
        string = string.replace("seven", "s7ven")
    if "eight" in string:
        string = string.replace("eight", "e8ght")
    if "nine" in string:
        string = string.replace("nine", "n9ne")
    if "zero" in string:
        string = string.replace("zero", "z0ro")
    return string


def get_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return lines

def part1(lines):
    total = 0
    for line in lines:
        line = line.replace("\n", "")
        numbers = [int(x) for x in line if x.isdigit()]
        calibration_number = str(numbers[0]) + str(numbers[-1])
        calibration_number = int(calibration_number)
        total += calibration_number
    return total

def part2(lines):
    total = 0
    for line in lines:
        line = line.replace("\n", "")
        line = string_to_int(line)
        numbers = [int(x) for x in line if x.isdigit()]
        calibration_number = str(numbers[0]) + str(numbers[-1])
        calibration_number = int(calibration_number)
        total += calibration_number
    return total


if __name__ == "__main__":
    file_path = "Day1/input.txt"
    lines = get_lines(file_path)
    print("Part 1: " + str(part1(lines)))
    print("Part 2: " + str(part2(lines)))