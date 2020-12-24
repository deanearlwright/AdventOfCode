# ======================================================================
# Jurassic Jigsaw
#   Advent of Code 2020 Day 20 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                           t i l e . p y
# ======================================================================
"A single tile for the Advent of Code 2020 Day 20 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
B_TOP = 0
B_BOTTOM = 1
B_LEFT = 2
B_RIGHT = 3

# ----------------------------------------------------------------------
#                                                                utility
# ----------------------------------------------------------------------


def get_borders(square):
    "Compute the top, right, bottom, and left borders of the tile"

    # 0 Pre-condition axioms
    assert len(square) == len(square[0])

    # 1. Start with nothing then add then clockwise from top
    result = []

    # 2. Top and Bottom
    result.append(''.join(square[0]))
    result.append(''.join(square[-1]))

    # 3. Left and Right
    result.append(''.join([_[0] for _ in square]))
    result.append(''.join([_[-1] for _ in square]))

    # 4. Return the borders
    return result


def get_flippings(square):
    "Compute the possible flipped permutations of the tile"

    # 0 Pre-condition axioms
    assert len(square) == len(square[0])

    # 1. Start with nothing
    result = []

    # 3. Not flipped at all  [Example 3079]
    result.append(square.copy())

    # 4. Top and bottom flipped  [Example 2311]
    result.append(square[::-1])

    # 5. Left and right flipped
    result.append([_[::-1] for _ in square])

    # 6. Top and bottom and Left and right flipped
    result.append([_[::-1] for _ in square][::-1])

    # 7. Return all the possible flipping of the tile
    assert len(result) == 4
    return result


def get_rotations(square):
    "Compute the possible rotations of the tile"

    # 0 Pre-condition axioms
    assert len(square) == len(square[0])

    # 1. Start with nothing
    result = []
    size = len(square)

    # 3. Not rotated at all (or maybe four times) [Example 3079]
    result.append(square)

    # 4. Rotate the tile three ways (note 3 clockwise is same as 1 counter-clockwise)
    previous = square
    for _ in range(3):
        rotation = [_[:] for _ in square]
        for row in range(size):
            for col in range(size):
                rotation[row][col] = previous[size - col - 1][row]
        result.append(rotation)
        previous = rotation

    # 5. Return all the possible rotations of the tile
    assert len(result) == 4
    return result


def get_orientations(square):
    "Compute the possible rotations of the tile"

    # 0 Pre-condition axioms
    assert len(square) == len(square[0])

    # 1. Start with nothing
    result = []

    # 2. Get all of the possible rotations
    for rotation in get_rotations(square):

        # 3. And all of the flippings of those rotations
        for flipping in get_flippings(rotation):

            # 4. If this is new, add it
            if flipping not in result:
                result.append(flipping)

    # 5. Return the unique orientations
    return result


def str_tile(square):
    "Pretty print the square"
    # 0 Pre-condition axioms
    assert len(square) == len(square[0])
    lines = []
    for line in square:
        lines.append(''.join(line))
    return '\n'.join(lines)


def remove_border(square):
    "Strip off the top, right, bottom, and right borders"
    # 0 Pre-condition axioms
    assert len(square) == len(square[0])

    # 1. Retrun the stripped square
    return [_[1:-1] for _ in square[1:-1]]


# ======================================================================
#                                                                   Tile
# ======================================================================


class Tile(object):   # pylint: disable=R0902, R0205
    "Object for Jurassic Jigsaw"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.number = None
        self.lines = []
        self.orientations = []
        self.borders = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Fill in number and lines from supplied text"

        # 1. First line of text has number
        assert text[0].startswith('Tile ')
        assert text[0].endswith(':')
        self.number = int(text[0].split()[1][:-1])

        # 2. The rest are the image lines
        for line in text[1:]:
            self.lines.append(list(line))
        assert len(self.lines) == len(self.lines[0])

        # 3. Get all of the possible orientations
        self.orientations = get_orientations(self.lines)

        # 4. Get the borders of the orientations
        for orientation in self.orientations:
            self.borders.append(get_borders(orientation))

    def get_number(self):
        "Get the tile number"
        return self.number

    def __str__(self):
        return str_tile(self.lines)


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          t i l e . p y                         end
# ======================================================================
