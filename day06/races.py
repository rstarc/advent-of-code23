import re


def ways_to_win_multiple(input: str):
    """For the given races, return the product of the number of ways to beat the record"""
    with open(input) as file:
        times = [int(n) for n in re.findall(r"\d+", file.readline())]
        distances = [int(n) for n in re.findall(r"\d+", file.readline())]

        product = 1
        for max_time, record in zip(times, distances):
            # Try half the possible times due to the symmetric nature of the problem
            ways_to_win = 0
            # print(f"{max_time}ms - record {record}mm")
            for hold_time in range(0, max_time):  # range(0, max_time // 2 + 1):
                speed = hold_time
                distance = speed * (max_time - hold_time)
                # print(f"hold for {hold_time} -> speed {speed} -> distance {distance}")
                if distance > record:
                    ways_to_win += 1

            # print(f"{ways_to_win} ways")
            product *= ways_to_win

        return product


def ways_to_win_single(input: str):
    """Assume there's only one race - how many ways are there to win?"""
    with open(input) as file:
        time = int("".join(re.findall(r"\d+", file.readline())))
        record = int("".join(re.findall(r"\d+", file.readline())))

        # Find the minimum hold time
        # This would be much easier if I had the patience to think this through as a math prblem
        minimum = 0
        for hold_time in range(0, time):
            if hold_time * (time - hold_time) > record:
                minimum = hold_time
                break
        # Since this is symmetric, we can compute the maximum time, and thus the number fo ways
        ways_to_win = time - minimum * 2 + 1
        return ways_to_win


print(ways_to_win_multiple("input.txt"))
print(ways_to_win_single("sample.txt"))
print(ways_to_win_single("input.txt"))
