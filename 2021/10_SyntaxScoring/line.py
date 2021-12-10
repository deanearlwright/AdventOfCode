# ======================================================================
# Syntax Scoring
#   Advent of Code 2021 Day 10 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         l i n e . p y
# ======================================================================
"Line for the Advent of Code 2021 Day 10 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
STARTERS = frozenset(['(', '[', '<', '{'])
ENDERS = frozenset([')', ']', '>', '}'])
MATCHING = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}
SYNTAX_SCORING = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
AUTOCOMPLETE_SCORING = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}

# ======================================================================
#                                                                   Line
# ======================================================================


class Line(object):   # pylint: disable=R0902, R0205
    "Object for Syntax Scoring"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.corrupted = False
        self.incomplete = False
        self.illegal = None
        self.score = 0

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self.process_text()

    def process_text(self):
        "Assign values from text"

        # 1. Look for first illegal character
        illegal = self.first_illegal()

        # 2. If the is none, it is a good line
        if illegal is None:
            return

        # 3. A dollar sign indicates end-of-line or incomplete
        if illegal == '$':
            self.incomplete = True
            return

        # 4. Else we have a corrupted line
        self.corrupted = True
        self.illegal = illegal
        self.score = SYNTAX_SCORING[illegal]

    def first_illegal(self):
        "Find the first illegal character"

        # 1. Nothing to match yet
        matching = []

        # 2. Loop all of the characters in the line
        for char in self.text:

            # 3. Add starters to what we have to match
            if char in STARTERS:
                matching.append(char)
                continue

            # 4. If an ender, We need to check the last starter
            if char in ENDERS:
                match_me = matching.pop()
                if MATCHING[match_me] == char:
                    continue

                # 5. Found our first corruption on the line
                return char

            # 6. Bad character
            print("unexpected character", char)

        # 7. End of line, if stuff to match then incomplete
        if len(matching) > 0:
            self.score = Line.autocomplete_score(matching)
            return '$'

        # 8. Else all is well
        return None

    def get_score(self):
        "Return the score for the line"
        return self.score

    @staticmethod
    def autocomplete_score(matching):
        "Compute a score base on whats left to match"

        # 1. Start with nothing
        result = 0

        # 2. Reverse the order of the character left to match
        matching.reverse()

        # 3. Loop for each character
        for char in matching:

            # 4. Accumulate the score
            result = result * 5 + AUTOCOMPLETE_SCORING[char]

        # 5. Return the autocomplete score
        return result


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                          l i n e . p y                         end
# ======================================================================
