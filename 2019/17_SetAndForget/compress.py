import re

L1 = "R,6,L,10,R,8,R,8,R,12"
L2 = "L,8,L,10,R,6,L,10"
L3 = 'R,8,R,8,R,12,L,10'
L4 = "R,6,L,10,R,12,L,8"
L5 = "L,10,R,12,L,10,R,6"
L6 = "L,10,R,6,L,10,R,8"
L7 = "R,8,R,12,L,8,L,10"
L8 = "R,6,L,10,R,8,R,8,R,12"
L9 = "L,10,R,6,L,10,"

INPUT = ','.join([L1, L2, L3, L4, L5, L6, L7, L8, L9])
print(INPUT)

compress = re.compile(r'^(.{1,21})\1*(.{1,21})(?:\1|\2)*(.{1,21})(?:\1|\2|\3)*$')

result = compress.match(INPUT)


if result is None:
    print("pooh")
else:
    print(result.group(1))
    print(result.group(2))
    print(result.group(3))

inputs = ["A,B,A,C,B,C,A,B,A,C,", result.group(1), result.group(2), result.group(3)]

print(inputs)

final = []
for row in range(4):
    row_chars = inputs[row][:-1].split(',')
    print(row_chars)
    one_row = []
    for xyz in row_chars:
        if len(xyz) > 1:
            one_row.append(ord(xyz[0]))
            one_row.append(ord(xyz[1]))
        else:
            one_row.append(ord(xyz))
        one_row.append(ord(','))
    one_row[-1] = 10
    final.extend(one_row)
print(final)

