
# ======================================================================
# Aplenty
#   Advent of Code 2023 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                             r u l e . p y
# ======================================================================
"Rule for the Advent of Code 2023 Day 19 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
COLON = ":"
LESS = "<"
MORE = ">"
CRITERIA = frozenset("xmas")
NOTEST = ""
NOBRANCH = None

# ======================================================================
#                                                                   Rule
# ======================================================================


class Rule(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Aplenty"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.category = ""
        self.test = NOTEST
        self.value = 0
        self.branch = ""

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 0. Precondition axioms
        assert text is not None and len(text) > 0

        # 1. If there is no colon, goto only
        if COLON not in text:
            self.branch = text
            return

        # 2. Split off the criterial and branch name
        parts = text.split(COLON)
        assert len(parts) == 2
        self.branch = parts[1]

        # 3. Get the category and number
        if LESS in parts[0]:
            parts = parts[0].split(LESS)
            assert len(parts) == 2
            self.test = LESS
        else:
            parts = parts[0].split(MORE)
            assert len(parts) == 2
            self.test = MORE

        # 4. Save the category and number
        self.category = parts[0]
        self.value = int(parts[1])

        # 5. Postcondition axioms
        assert self.category in CRITERIA
        assert 0 < self.value <= 999999
        assert len(self.branch) > 0

    def evaluate(self, part):
        "Return branch if rule matches or NOBRANCH if it doesn't"

        # 1. If there is no test, branch
        if self.test == NOTEST:
            return self.branch

        # 2. Get the required value of the part
        value = part.value(self.category)

        # 3. If the test succeeds, branch
        if self.test == LESS and value < self.value:
            return self.branch
        if self.test == MORE and value > self.value:
            return self.branch

        # 4. We are not branching
        return NOBRANCH

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                          r u l e . p y                         end
# ======================================================================
