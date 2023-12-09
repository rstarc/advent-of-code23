from typing import Dict, Tuple, List
import re
import itertools


def get_map_destination(map: Dict[int, Tuple[int, int]], src: int):
    """Given a source (key) , find and return the destination in the map"""
    # The input format is: { source_range_start : (destination_range_start, length) }

    # Try to find the corresponding destination
    for src_start in map:
        if src >= src_start:
            dst_start, range_len = map[src_start]
            if src <= (src_start + range_len - 1):
                dst = dst_start + (src - src_start)
                return dst

    # Unmapped source number -> equal to destination number
    return src


def min_location_of_seeds(input: str):
    """Parse the input and return the least soil location of all input seeds"""
    with open(input) as file:
        # Parse seeds
        seeds = [int(n) for n in re.findall(r"\d+", file.readline())]

        # Parse all the maps
        maps: Dict[str, Dict[int, Tuple[int, int]]] = {}
        current_map = ""
        for line in file:
            line = line.rstrip()
            if "map" in line:
                current_map = line
                maps[current_map] = {}
                continue

            # Parse numbers and add them to the map
            map_entry = re.findall(r"\d+", line)
            if len(map_entry) == 3:
                # This must be a non-empty line - parse it and add it to the map
                dst_range_start = int(map_entry[0])
                src_range_start = int(map_entry[1])
                range_len = int(map_entry[2])
                maps[current_map][src_range_start] = (
                    dst_range_start,
                    range_len,
                )

        # With everything parsed, map each seed to its final destination
        soil_map: Dict[int, int] = {}
        for seed in seeds:
            source = seed
            dest = source
            for map_name in maps:
                dest = get_map_destination(maps[map_name], source)
                source = dest

            soil_map[seed] = dest

    # return the lowest location number
    return min(soil_map.values())


def min_location_of_seed_ranges(input: str):
    """Parse the input and return the least soil location of all input seeds in the input seed range"""
    with open(input) as file:
        # Parse seeds
        seed_ranges = [int(n) for n in re.findall(r"\d+", file.readline())]
        seeds: List[Tuple[int, int]] = []
        assert len(seed_ranges) % 2 == 0
        for start, length in zip(seed_ranges[0::2], seed_ranges[1::2]):
            seeds.append((start, length))

        # Parse all the maps - now backwards
        maps: Dict[str, Dict[int, Tuple[int, int]]] = {}
        current_map = ""
        for line in file:
            line = line.rstrip()
            if "map" in line:
                current_map = line
                maps[current_map] = {}
                continue

            # Parse numbers and add them to the map
            map_entry = re.findall(r"\d+", line)
            if len(map_entry) == 3:
                # This must be a non-empty line - parse it and add it to the map
                dst_range_start = int(map_entry[0])
                src_range_start = int(map_entry[1])
                range_len = int(map_entry[2])
                maps[current_map][dst_range_start] = (
                    src_range_start,
                    range_len,
                )

        # Starting from the lowest possible location, check if its original seed is in the initial list
        # Ideally, we would not check individual locations, but ranges of locations - this is still kind of a brute-force approach
        for location in itertools.count(start=0):
            dst = location
            src = dst
            for map_name in reversed(maps):
                # Get the source value
                src = get_map_destination(maps[map_name], dst)
                dst = src
            # Check if this is seed is in our range
            for start, length in seeds:
                if src >= start and src < start + length:
                    return location


print(min_location_of_seeds("input.txt"))
print(min_location_of_seed_ranges("input.txt"))
