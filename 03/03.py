data = [i for i in open("input.txt").readlines()]
instructions_1 = [p.strip() for p in data[0].split(",")]
instructions_2 = [p.strip() for p in data[1].split(",")]


def traversed_coordinates(instructions):
    coordinates = set()
    cx, cy = (0, 0)

    for instruction in instructions:
        direction = instruction[:1]
        steps = int(instruction[1:])

        if direction == 'R':
            for c in range(steps):
                cy = cy + 1
                coordinates.add((cx, cy))
        elif direction == 'L':
            for c in range(steps):
                cy = cy - 1
                coordinates.add((cx, cy))
        elif direction == 'U':
            for c in range(steps):
                cx = cx + 1
                coordinates.add((cx, cy))
        elif direction == 'D':
            for c in range(steps):
                cx = cx - 1
                coordinates.add((cx, cy))

    return coordinates


coordinates_1 = traversed_coordinates(instructions_1)
coordinates_2 = traversed_coordinates(instructions_2)

intersections = coordinates_1 & coordinates_2

distance = min([abs(x[0]) + abs(x[1]) for x in intersections])

# solution part 1
print(distance)
