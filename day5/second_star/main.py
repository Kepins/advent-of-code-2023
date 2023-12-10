def transform_ranges(seeds_ranges, map):
    out_seeds_ranges = []
    for initial_r in seeds_ranges:
        rs = [initial_r]
        for line in map:
            after_line_rs = []
            for r in rs:
                start = max(r[0], line["s"])
                end = min(r[1], line["s"] + line["r"])

                if start <= end:
                    out_seeds_ranges.append((start + line["d"] - line["s"], end + line["d"] - line["s"]))

                    if start != r[0]:
                        after_line_rs.append((r[0], start))
                    if end != r[1]:
                        after_line_rs.append((end, r[1]))
                else:
                    after_line_rs.append(r)
            rs = after_line_rs
        out_seeds_ranges += rs

    return out_seeds_ranges


def get_min_location(seeds_ranges, maps):
    for m in maps:
        seeds_ranges = transform_ranges(seeds_ranges, m)

    return min([r[0] for r in seeds_ranges])


if __name__ == "__main__":
    # read seeds
    seeds_ranges_input = [int(s) for s in input().split(":")[1].split(" ") if s]

    seeds_ranges = []
    for i in range(0, len(seeds_ranges_input), 2):
        seeds_ranges.append((seeds_ranges_input[i], seeds_ranges_input[i] + seeds_ranges_input[i+1]))

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
                    "d": nums[0],
                    "s": nums[1],
                    "r": nums[2],
                })
        maps.append(map_data)

    print(get_min_location(seeds_ranges, maps))
