from re import findall


def parse_data(data):
    part1, part2 = data.split("\n\n")

    instructions = {}
    for line in part1.splitlines():
        state, fields = line[:-1].split("{")
        fields = [f.split(":") for f in fields.split(",")]
        steps = [(a[0], a[1], int(a[2:]), b) for a, b in fields[:-1]]
        instructions[state] = [*steps, (None, None, None, fields[-1][0])]

    points = [{x: int(n) for x, n in findall(r"(\w)=(\d+)", line)}
              for line in part2.splitlines()]
    print(instructions)
    return instructions, points


def part1(instructions, points):
    def value(point):
        state = "in"
        while state not in "AR":
            for var, cond, bound, target in instructions[state]:
                if var is None or \
                   (cond == "<" and point[var] < bound) or \
                   (cond == ">" and point[var] > bound):
                    state = target
                    break
        return sum(point.values()) if state == "A" else 0
    return sum(map(value, points))


from math import prod


def part2(instructions):
    todo = [{"state": "in", "x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}]

    total = 0
    while todo:
        cur = todo.pop()
        state = cur["state"]

        if state == "R":
            continue
        elif state == "A":
            total += prod(cur[d][1] - cur[d][0] + 1 for d in "xmas")
        else:
            for var, cond, bound, target in instructions[state]:
                split = dict(cur)
                split["state"] = target
                if cond == "<":
                    split[var] = (split[var][0], bound - 1)
                    cur[var] = (bound, cur[var][1])
                elif cond == ">":
                    split[var] = (bound + 1, split[var][1])
                    cur[var] = (cur[var][0], bound)
                todo.append(split)
    return total


EXAMPLE_TEXT = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""
instructions, points = parse_data(EXAMPLE_TEXT)
print("Part 1:", part1(instructions, points))
print("Part 2:", part2(instructions))
