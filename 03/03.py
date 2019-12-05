[path1, path2] = [line.split(",") for line in open("input.txt").readlines()]


def get_traversed_coordinates(instructions):
    coordinates = dict()
    x, y, steps_taken = 0, 0, 0

    for instruction in instructions:
        direction = instruction[0]
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


coordinates1 = get_traversed_coordinates(path1)
coordinates2 = get_traversed_coordinates(path2)

intersections = coordinates1.keys() & coordinates2.keys()

distance = min([abs(point[0]) + abs(point[1]) for point in intersections])

# solution part 1
print(distance)

# solution part 2
print(min(coordinates1[point] + coordinates2[point] for point in intersections))
