import functools


def get_next(seed, map):
    for line in map:
        if line["source"] <= seed < line["source"] + line["range"]:
            return line["destination"] + seed - line["source"]
    return seed


def get_location(seed, maps):
    for m in maps:
        seed = get_next(seed, m)
    return seed


if __name__ == "__main__":
    # read seeds
    seeds = [int(s) for s in input().split(":")[1].split(" ") if s]
    # read newline
    input()

    maps = []
    is_more_maps = True

    while is_more_maps:
        # read map str
        input()

        map_data = []

        is_more_in_map = True
        while is_more_in_map:
            try:
                line = input()
            except EOFError:
                is_more_maps = False
                is_more_in_map = False
                break
            if line == "":
                is_more_in_map = False
            else:
                nums = [int(n) for n in line.split(" ")]
                map_data.append({
                    "destination": nums[0],
                    "source": nums[1],
                    "range": nums[2],
                })
        maps.append(map_data)

    seeds_min_location = min(map(functools.partial(get_location, maps=maps), seeds))

    print(seeds_min_location)
