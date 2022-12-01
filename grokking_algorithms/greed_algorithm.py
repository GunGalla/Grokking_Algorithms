'''Example of "greed" algorithm'''

stations = {
    "one": {"id", "nv", "ut"},
    "two": {"wa", "id", "mt"},
    "three": {"or", "nv", "ca"},
    "four": {"nv", "ut"},
    "five": {"ca", "az"},
}

states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}


def greed_choice(items):
    final_set = set()
    while items:
        best_station = None
        states_covered = set()
        for station, states in stations.items():
            covered = items & states
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered
        items -= states_covered
        final_set.add(best_station)
    return final_set


print(greed_choice(states_needed))
