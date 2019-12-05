# inspired by https://www.reddit.com/r/adventofcode/comments/e5u5fv/2019_day_4_solutions/f9p88bu

start = 240298
end = 784956

ordered = set()

for unordered in range(start, end):
    if list(str(unordered)) == sorted(str(unordered)):
        ordered.add(str(unordered))

part1 = set()
part2 = set()

for password in ordered:
    for char in password:
        if password.count(char) >= 2:
            part1.add(password)
        if password.count(char) == 2:
            part2.add(password)

# solution part 1
print(len(part1))
# solution part 2
print(len(part2))
