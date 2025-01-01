
# ======================================================================
# Keypad Conundrum
#   Advent of Code 2024 Day 21 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         k e y p a d . p y
# ======================================================================
"A solver for the Advent of Code 2024 Day 21 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
DOOR_LOC = {
    "7": (0, 0), "8": (0, 1), "9": (0, 2),
    "4": (1, 0), "5": (1, 1), "6": (1, 2),
    "1": (2, 0), "2": (2, 1), "3": (2, 2),
    "X": (3, 0), "0": (3, 1), "A": (3, 2),
}
ROBOT_LOC = {
    "X": (0, 0), "^": (0, 1), "A": (0, 2),
    "<": (1, 0), "v": (1, 1), ">": (1, 2),
}
DOOR_PAD = 0
ROBOT_PAD = 1
KEYPAD = [DOOR_LOC, ROBOT_LOC]
BADPAD = [(3, 0), (0, 0)]
ROWDIR = {-1: "^", 1: "v"}
COLDIR = {-1: "<", 1: ">"}

# ======================================================================
#                                                                 Keypad
# ======================================================================


class Keypad(object):   # pylint: disable=R0902, R0205
    "Object for Keypad Conundrum"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.codes = []
        self.robots = 3
        if part2:
            self.robots = 26
        self.presses = []
        self.memo_len = {}
        self.memo_key = {}

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text()

    def _process_text(self):
        "Assign values from text"

        assert self.text is not None and len(self.text) > 0

        # 1. Loop for all pf the lines of text
        for line in self.text:

            # 2. Save the code
            self.codes.append(line)

    @staticmethod
    def complexity(length, code):
        "Return the complexity of the code"
        return length * int(code.replace("A", ""))

    def sum_complexity(self):
        "Return the sum of the complexties for all the codes"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all the codes
        for code in self.codes:

            # 3. Get the minimum path length
            length = self.min_seq_len(DOOR_PAD,
                                      code,
                                      self.robots)

            # 4. Accumulate the complexity
            result += self.complexity(length, code)

        # 5. Return the sum of the code complexities
        return result

    def min_seq_len(self, key_pad, code, robots):
        "Return the length of the minimimum sequence to implement the code"

        # 1. If we know it already, return the answer
        key = (key_pad, code, robots)
        if key in self.memo_len:
            return self.memo_len[key]

        # 2. Recursion base condition
        if robots == 0:
            self.memo_len[key] = len(code)
            return len(code)

        # 3. Get ready for the next level down
        new_key = "A"
        new_len = 0

        # 4. Loop for each symbol in the code
        for symbol in code:
            sym_len = 999999999999

            # 5. Loop for all the sequences from here to that symbol
            paths = self.key_to_key(key_pad, new_key, symbol)
            assert len(paths) > 0
            for symbols in paths:

                # 6. Get the mininimum length to produce this sequence
                seq_len = self.min_seq_len(ROBOT_PAD,
                                           symbols + 'A',
                                           robots - 1)

                # 7. Find the miminum of these
                sym_len = min(sym_len, seq_len)

            # 8. Accumulate the lengths
            new_len += sym_len

            # 9. Now we are at a new key
            new_key = symbol

        # 10. Remember this solution and return it
        self.memo_len[key] = new_len
        return new_len

    @staticmethod
    def sign(number):
        "Returns either 1, 0, or -1"
        if number == 0:
            return 0
        if number < 0:
            return -1
        return 1

    def key_to_key(self, key_pad, key_from, key_to):
        "Return list of sequences necessary to get from key to key"

        # 1. If we know it already, return the answer
        key = (key_pad, key_from, key_to)
        if key in self.memo_key:
            return self.memo_key[key]

        # 2. Get locations
        loc_from = KEYPAD[key_pad][key_from]
        loc_to = KEYPAD[key_pad][key_to]

        # 3. Start at the beginning
        queue = [(loc_from, '')]
        result = []

        # 3. Loop while there is something to do
        while queue:
            loc_here, path = queue.pop()

            # 4. Are we there yet?, Add path to the result
            if loc_here == loc_to:
                result.append(path)
                continue

            # 5. Column movement: < or > or none
            delta = self.sign(loc_to[1] - loc_here[1])
            if delta != 0:
                new_loc = (loc_here[0], loc_here[1] + delta)
                if new_loc != BADPAD[key_pad]:
                    queue.append((new_loc, path + COLDIR[delta]))

            # 6. Row movement: ^ or v or none
            delta = self.sign(loc_to[0] - loc_here[0])
            if delta != 0:
                new_loc = (loc_here[0] + delta, loc_here[1])
                if new_loc != BADPAD[key_pad]:
                    queue.append((new_loc, path + ROWDIR[delta]))

        # 7. Remember and return list of key to key sequences
        self.memo_key[key] = result
        return result

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. No solution if no text
        if self.text is None:
            return None

        # 2. Return the solution for part one
        return self.sum_complexity()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. No solution if no text
        if self.text is None:
            return None

        # 2. Return the solution for part two
        return self.sum_complexity()

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                        k e y p a d . p y                       end
# ======================================================================
