data = [i for i in open("input.txt").readlines()]
instructions_1 = [p.strip() for p in data[0].split(",")]
instructions_2 = [p.strip() for p in data[1].split(",")]


class Point:
    def __init__(self, x, y, steps):
        self.x = x
        self.y = y
        self.steps = steps

    def __repr__(self):
        return f"({self.x}, {self.y} - {self.steps})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


def traversed_coordinates(instructions):
    coordinates = set()
    cx, cy = 0, 0

    total_steps = 0

    for instruction in instructions:
        direction = instruction[:1]
        steps = int(instruction[1:])

        if direction == 'R':
            for c in range(steps):
                cy = cy + 1
                total_steps += 1
                coordinates.add(Point(cx, cy, total_steps))
        elif direction == 'L':
            for c in range(steps):
                cy = cy - 1
                total_steps += 1
                coordinates.add(Point(cx, cy, total_steps))
        elif direction == 'U':
            for c in range(steps):
                cx = cx + 1
                total_steps += 1
                coordinates.add(Point(cx, cy, total_steps))
        elif direction == 'D':
            for c in range(steps):
                cx = cx - 1
                total_steps += 1
                coordinates.add(Point(cx, cy, total_steps))

    return coordinates


coordinates_1 = traversed_coordinates(instructions_1)
coordinates_2 = traversed_coordinates(instructions_2)

intersections = coordinates_1 & coordinates_2

distance = min([abs(point.x) + abs(point.y) for point in intersections])

# solution part 1
print(distance)

used_steps = []

for intersection in intersections:
    for cor in coordinates_2:
        if intersection == cor:
            used_steps.append(intersection.steps + cor.steps)

# solution part 2
print(min(used_steps))
