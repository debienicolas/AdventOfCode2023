file_path = "Day1/input.txt"

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




file_path = "Day1/input.txt"

string1 = "six1mpffbnbnnlxthree"
print(string_to_int(string1))

with open(file_path, 'r') as file:
    lines = file.readlines()
    total = 0
    for line in lines:
        line = line.replace("\n", "")
        line = string_to_int(line)
        print(line)
        numbers = [int(x) for x in line if x.isdigit()]
        print(numbers)
        calibration_number = str(numbers[0]) + str(numbers[-1])
        calibration_number = int(calibration_number)
        total += calibration_number
        print(calibration_number)
print(total)

with open(file_path,'r') as file:
    lines = file.readlines()
    total = 0
    for line in lines:
        line = line.replace("\n", "")
        numbers = [int(x) for x in line if x.isdigit()]
        calibration_number = str(numbers[0]) + str(numbers[-1])
        calibration_number = int(calibration_number)
        total += calibration_number
        

print(total)