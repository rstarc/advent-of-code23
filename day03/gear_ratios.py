from typing import List
import re


def is_symbol(s: str) -> bool:
    """Given a string, check whether it is a symbol"""
    return not (s.isdecimal() or s == ".")


def sum_of_part_numbers(input: str):
    schematic_lines: List[str] = []
    with open(input) as file:
        # Don't forget to strip the line endings!
        # Otherwise we include the '\n' character when a digit is at the end of a line
        #  which could (purely theoretically of course) cause almost 60 minutes of debugging
        schematic_lines = [line[:-1] for line in file]

    part_numbers: List[int] = []
    for i, line in enumerate(schematic_lines):
        # Check the lines from start to end of the number, plus one on either end
        neighboring_lines = schematic_lines[
            max(0, i - 1) : min(len(schematic_lines), i + 1) + 1
        ]

        # Find all potential part numbers in this string
        matches = re.finditer(r"\d+", line)
        for match in matches:
            # Check this line, the previous line, and the next line for adjacent symbols
            start_i, end_i = match.span()
            number = int(match.group(0))

            for neighbor in neighboring_lines:
                substring = neighbor[
                    max(0, start_i - 1) : min(len(neighbor), end_i + 1)
                ]
                # If we find any symbol, this is a part number
                if any([is_symbol(c) for c in substring]):
                    part_numbers.append(number)
                    # Check next match
                    break

    return sum(part_numbers)


print(sum_of_part_numbers("input.txt"))
