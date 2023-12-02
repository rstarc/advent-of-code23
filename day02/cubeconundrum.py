import re
from typing import List


def sum_of_possible_games(input: str) -> int:
    # Maximum color values
    rgb_max = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    possible_games: List[int] = []

    with open(input) as file:
        for game in file:
            rounds_string = game.split(":")[1]
            rounds_list = rounds_string.split(";")

            # Check all rounds
            possible = True
            for round in rounds_list:
                for color in rgb_max.keys():  # explicit is better than implicit
                    match = re.search(rf"(\d+)\s{color}", round)
                    if match is not None:
                        color_count = int(match.group(1))
                        if color_count > rgb_max[color]:
                            possible = False

            # Add ID to list if possible
            if possible:
                match = re.search(r"Game\s(\d+):", game)
                if match is None:
                    raise ValueError(f"Line does not contain a valid game!:\n{game}")
                else:
                    game_id = int(match.group(1))
                    possible_games.append(game_id)

    return sum(possible_games)


def sum_of_powers_of_minimum_cubes(input: str) -> int:
    powers_of_minimum_cubes: List[int] = []

    with open(input) as file:
        for game in file:
            rounds_string = game.split(":")[1]
            rounds_list = rounds_string.split(";")

            # Use 1 as default value so we don't multiply by 0
            required_rgb = {
                "red": 1,
                "green": 1,
                "blue": 1,
            }

            for round in rounds_list:
                for color in required_rgb.keys():  # explicit is better than implicit
                    match = re.search(rf"(\d+)\s{color}", round)
                    if match is not None:
                        color_count = int(match.group(1))
                        required_rgb[color] = max(required_rgb[color], color_count)

            # Add list
            # Using a pythonic version of a functional 'fold' - https://stackoverflow.com/a/55890523
            power = 1
            [power := power * x for x in required_rgb.values()]
            powers_of_minimum_cubes.append(power)

    return sum(powers_of_minimum_cubes)


print(sum_of_possible_games("input.txt"))
print(sum_of_powers_of_minimum_cubes("input.txt"))
