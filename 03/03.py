data = [i for i in open("input.txt").readlines()]
instructions_1 = [p for p in data[0].split(",")]
instructions_2 = [p for p in data[1].split(",")]


def get_traversed_coordinates(instructions):
    coordinates = dict()
    x, y, steps_taken = 0, 0, 0

    for instruction in instructions:
        direction = instruction[:1]
        steps = int(instruction[1:])

        for s in range(steps):
            if direction == "R":
                y += 1
            elif direction == "L":
                y -= 1
            elif direction == "U":
                x += 1
            elif direction == "D":
                x -= 1

            steps_taken += 1
            coordinates[(x, y)] = steps_taken

    return coordinates


coordinates_1 = get_traversed_coordinates(instructions_1)
coordinates_2 = get_traversed_coordinates(instructions_2)

intersections = coordinates_1.keys() & coordinates_2.keys()

distance = min([abs(point[0]) + abs(point[1]) for point in intersections])

# solution part 1
print(distance)

# solution part 2
print(min(coordinates_1[point] + coordinates_2[point] for point in intersections))
