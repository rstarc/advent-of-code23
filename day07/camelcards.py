from typing import Tuple, Dict, List
from collections import OrderedDict


def total_winnings_with_joker(input: str) -> int:
    card_strings = [
        "A",
        "K",
        "Q",
        "T",
        "9",
        "8",
        "7",
        "6",
        "5",
        "4",
        "3",
        "2",
        "J",
    ]
    card_to_int = {k: i for i, k in enumerate(card_strings)}
    # Card representation that is easy to sort: 6 integers, lower is "better"
    # Allows us to sort lexicographically
    bids: Dict[Tuple[int, int, int, int, int, int], int] = {}
    with open(input) as file:
        for line in file:
            parts = line.rstrip().split(" ")
            bid = int(parts[1])

            # Parse the string into our representation
            cards = parts[0]
            card_repr: List[int] = []  # empty tuple
            card_freq: Dict[str, int] = {}
            for card in cards:
                card_repr.append(card_to_int[card])

                # Gather card frequency statistics
                if card in card_freq:
                    card_freq[card] += 1
                else:
                    card_freq[card] = 1

            hand_type = 6
            # Compute the type
            freq = card_freq.values()
            j_count = 0
            if "J" in cards:
                j_count = card_freq["J"]
                # If there's a joker, we have at least a pair
                hand_type = 5

            if 5 in freq:
                # five of a kind
                hand_type = 0
            elif 4 in freq:
                # four of a kind
                hand_type = 1
                if j_count != 0:
                    # -> five of a kind
                    hand_type = 0
            elif 3 in freq and 2 in freq:
                # Full house
                hand_type = 2
                if j_count != 0:
                    # Must be five of a kind no matter which frequency J has
                    hand_type = 0
            elif 3 in freq:
                # three of a kind
                hand_type = 3
                if j_count != 0:
                    # Four of a kind - the others not being a pair has been checked already
                    hand_type = 1
            elif [1, 2, 2] == sorted(freq):
                # two pair
                hand_type = 4
                if j_count == 1:
                    # -> [3, 2] -> full house
                    hand_type = 2
                elif j_count == 2:
                    # -> four of a kind
                    hand_type = 1
            elif 2 in freq:
                # one pair
                hand_type = 5
                if j_count != 0:
                    # -> Three of a kind - other cards are all different
                    hand_type = 3
            # default: high card

            card_repr = [hand_type] + card_repr
            bids[tuple(card_repr)] = bid

    # Finally - sort the whole thing, and compute the winnings
    ordered_bids = OrderedDict(sorted(bids.items(), reverse=True))
    total_winnings = 0
    for rank, key in enumerate(ordered_bids):
        bid = ordered_bids[key]
        total_winnings += (rank + 1) * bid

    return total_winnings


def total_winnings(input: str) -> int:
    card_strings = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    card_to_int = {k: i for i, k in enumerate(card_strings)}
    # Card representation that is easy to sort: 6 integers, lower is "better"
    # Allows us to sort lexicographically
    bids: Dict[Tuple[int, int, int, int, int, int], int] = {}
    with open(input) as file:
        for line in file:
            parts = line.rstrip().split(" ")
            bid = int(parts[1])

            # Parse the string into our representation
            cards = parts[0]
            card_repr: List[int] = []  # empty tuple
            card_freq: Dict[str, int] = {}
            for card in cards:
                card_repr.append(card_to_int[card])

                # Gather card frequency statistics
                if card in card_freq:
                    card_freq[card] += 1
                else:
                    card_freq[card] = 1

            hand_type = 6
            # Compute the type
            freq = card_freq.values()
            if 5 in freq:
                # five of a kind
                hand_type = 0
            elif 4 in freq:
                # four of a kind
                hand_type = 1
            elif 3 in freq and 2 in freq:
                # Full house
                hand_type = 2
            elif 3 in freq:
                # three of a kind
                hand_type = 3
            elif [1, 2, 2] == sorted(freq):
                # two pair
                hand_type = 4
            elif 2 in freq:
                # one pair
                hand_type = 5
            # default: high card

            card_repr = [hand_type] + card_repr
            bids[tuple(card_repr)] = bid

    # Finally - sort the whole thing, and compute the winnings
    ordered_bids = OrderedDict(sorted(bids.items(), reverse=True))
    total_winnings = 0
    for rank, key in enumerate(ordered_bids):
        bid = ordered_bids[key]
        total_winnings += (rank + 1) * bid

    return total_winnings


print(total_winnings("input.txt"))
print(total_winnings_with_joker("input.txt"))
