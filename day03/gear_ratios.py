from typing import List, Dict, Tuple
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


def sum_of_gear_ratios(input: str):
    schematic_lines: List[str] = []
    with open(input) as file:
        # Don't forget to strip the line endings!
        # Otherwise we include the '\n' character when a digit is at the end of a line
        #  which could (purely theoretically of course) cause almost 60 minutes of debugging
        schematic_lines = [line[:-1] for line in file]

    lines_y: Dict[int, str] = {}
    for i, line in enumerate(schematic_lines):
        lines_y[i] = line

    # For all gears, record their coordinates (keys) and adjacent numbers
    gear_numbers: Dict[Tuple[int, int], List[int]] = {}
    for y, line in lines_y.items():
        # Check the lines from start to end of the number, plus one on either end
        neighboring_lines = schematic_lines[
            max(0, y - 1) : min(len(schematic_lines), y + 1) + 1
        ]

        # Find all numbers in this string and check gear adjacency
        matches = re.finditer(r"\d+", line)
        for match in matches:
            start_x, end_x = match.span()
            number = int(match.group(0))

            for i, neighbor in enumerate(neighboring_lines):
                if y == 0:
                    y_coord = min(max(0, y + i), len(schematic_lines))
                else:
                    y_coord = min(max(0, y + (i - 1)), len(schematic_lines))

                x_coord_start = max(0, start_x - 1)
                x_coord_end = min(len(neighbor), end_x + 1)
                substring = neighbor[x_coord_start:x_coord_end]
                # Add to list of adjacent gears
                for x_delta, c in enumerate(substring):
                    if is_symbol(c):
                        coords = (x_coord_start + x_delta, y_coord)
                        # Initialize list if empty
                        if coords not in gear_numbers:
                            gear_numbers[coords] = []
                        gear_numbers[coords].append(number)

    # All gears with exactly two adjancent numbers
    numbers = [xs[0] * xs[1] for xs in gear_numbers.values() if len(xs) == 2]
    return sum(numbers)


print(sum_of_part_numbers("input.txt"))
print(sum_of_gear_ratios("input.txt"))
