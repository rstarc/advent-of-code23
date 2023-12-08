def sum_of_points(input: str):
    """Return the sum of points across all scratchcards"""
    points = []
    with open(input) as file:
        for card in file:
            # Strip trailing whitespace
            card = card.rstrip()
            card = card.split(": ")[1]
            sides = card.split("|")
            numbers = [int(n) for n in sides[1].split(" ") if len(n) > 0]
            winning = [int(n) for n in sides[0].split(" ") if len(n) > 0]

            matches = len([n for n in numbers if n in winning])
            if matches == 0:
                points.append(0)
            else:
                points.append(2 ** (matches - 1))

    return sum(points)


def sum_of_scratchcards(input: str):
    """Return the sum of total scratchcards"""
    cards = []
    with open(input) as file:
        for i, card in enumerate(file):
            card = card.rstrip()
            # Calculate the number of matches in advance
            card = card.split(": ")[1]
            sides = card.split("|")
            numbers = [int(n) for n in sides[1].split(" ") if len(n) > 0]
            winning = [int(n) for n in sides[0].split(" ") if len(n) > 0]
            matches = len([n for n in numbers if n in winning])

            cards.append((i, matches))

    for i, matches in cards:
        for j in range(matches):
            cards.append(cards[i + j + 1])

    return len(cards)


print(sum_of_points("input.txt"))
print(sum_of_scratchcards("input.txt"))
