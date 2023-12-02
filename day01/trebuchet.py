from typing import List


def part_one(input: str) -> int:
    values: List[int] = []

    with open(input) as file:
        for line in file:
            # Filter out non-decimal letters
            digits = [c for c in line if c.isdecimal()]
            value = int(f"{digits[0]}{digits[-1]}")
            values.append(value)

    return sum(values)


def part_two(input: str):
    values: List[int] = []
    string_to_digit = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    with open(input) as file:
        for line in file:
            digits = []
            # Iterate over the string
            for i in range(len(line)):
                substring = line[i:]
                if substring[0].isdecimal():
                    digits.append(substring[0])

                for num in string_to_digit:
                    if substring.startswith(num):
                        digits.append(string_to_digit[num])
                        # We could skip the iteration by the number of characters
                        # that we consumed, but i'm lazy

            value = int(f"{digits[0]}{digits[-1]}")
            values.append(value)

    return sum(values)


print(part_one("input.txt"))
print(part_two("input.txt"))
