import re
file = open('day1.txt', 'r')
lines = [line.rstrip() for line in file]
file.close()
def part1(lines):
    sum_ttl = 0
    for line in lines:
        num = [c for c in line if c.isdigit()]
        sum_ttl += int(num[0] + num[-1])
    return sum_ttl

def part2(lines):
    digits = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
        }
    pattern = re.compile(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))')

    sum_ttl = 0
    for line in lines:
        words = []
        for word in pattern.findall(line):
            if word in digits:
                words.append(str(digits[word]))
            else:
                words.append(word)
        sum_ttl += int(words[0] + words[-1])
    return sum_ttl


part1_ttl = part1(lines)
part2_ttl = part2(lines)
print(part1(lines))
print(part2(lines))
print("parte1: ", part1_ttl)
print("parte2: ", part2_ttl)