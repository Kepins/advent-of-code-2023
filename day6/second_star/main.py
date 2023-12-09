
def num_ways_to_beat(race_time: int, record_distance: int) -> int:
    num_ways = 0
    for time in range(1, race_time):
        # time is equal to speed in [m/s]
        distance = time * (race_time - time)
        if distance > record_distance:
            num_ways += 1
    return num_ways


if __name__ == "__main__":
    time_line = input()
    distance_line = input()

    races_times_str = [s for s in time_line.split(":")[1].split(" ") if s]
    record_distances_str = [s for s in distance_line.split(":")[1].split(" ") if s]

    race_time = int("".join(races_times_str))
    record_distance = int("".join(record_distances_str))

    print(num_ways_to_beat(race_time, record_distance))
