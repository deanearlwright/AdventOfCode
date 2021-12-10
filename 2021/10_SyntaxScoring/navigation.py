# ======================================================================
# Syntax Scoring
#   Advent of Code 2021 Day 10 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                         n a v i g a t i o n . p y
# ======================================================================
"A solver for the Advent of Code 2021 Day 10 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------
import line

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------

# ======================================================================
#                                                             Navigation
# ======================================================================


class Navigation(object):   # pylint: disable=R0902, R0205
    "Object for Syntax Scoring"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.lines = []

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            for text_line in self.text:
                self.lines.append(line.Line(text=text_line, part2=part2))

    def syntax_error_score(self):
        "Get the total syntax error score"

        # 1. Start with nothing
        result = 0

        # 2. Loop for all of the lines
        for a_line in self.lines:

            # 3. Add the score for this line if the line is corrupt
            if a_line.corrupted:
                result += a_line.get_score()

        # 4. Return the total score
        return result

    def autocomplete_score(self):
        "Get the autocomplete score"

        # 1. Start with nothing
        scores = []

        # 2. Loop for all of the lines
        for a_line in self.lines:

            # 3. Add the score for this line if the line is corrupt
            if a_line.incomplete:
                scores.append(a_line.get_score())

        # 4. Sort the scores
        scores.sort()

        # 5. Return the middle score
        return scores[len(scores) // 2]

    def part_one(self, verbose=False, limit=0):
        "Returns the solution for part one"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part one
        return self.syntax_error_score()

    def part_two(self, verbose=False, limit=0):
        "Returns the solution for part two"

        # 0. Precondition axioms
        assert verbose in [True, False]
        assert limit >= 0

        # 1. Return the solution for part two
        return self.autocomplete_score()


# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------
if __name__ == '__main__':
    pass

# ======================================================================
# end                    n a v i g a t i o n . p y                   end
# ======================================================================
