
# ======================================================================
# Aplenty
#   Advent of Code 2023 Day 19 -- Eric Wastl -- https://adventofcode.com
#
# Python implementation by Dr. Dean Earl Wright III
# ======================================================================

# ======================================================================
#                            p a r t . p y
# ======================================================================
"Part for the Advent of Code 2023 Day 19 puzzle"

# ----------------------------------------------------------------------
#                                                                 import
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
#                                                              constants
# ----------------------------------------------------------------------
LEFT_BRACE = "{"
RIGHT_BRACE = "}"
STRIP = LEFT_BRACE + RIGHT_BRACE
COMMA = ","
EQUALS = "="
CATEGORIES = "xmas"

# ======================================================================
#                                                                   Part
# ======================================================================


class Part(object):   # pylint: disable=R0902, R0903, R0205
    "Object for Aplenty"

    def __init__(self, text=None, part2=False):

        # 1. Set the initial values
        self.part2 = part2
        self.text = text
        self.categories = {}

        # 2. Process text (if any)
        if text is not None and len(text) > 0:
            self._process_text(text)

    def _process_text(self, text):
        "Assign values from text"

        # 0. Precondition axioms
        assert text is not None and len(text) > 0
        assert text.startswith(LEFT_BRACE)
        assert text.endswith(RIGHT_BRACE)

        # 1. Strip the braces
        text = text.strip(STRIP)

        # 2. Split into categories
        cats = text.split(COMMA)
        assert len(cats) == 4

        # 3. Loop for all the categories
        for cat in cats:

            # 4. Split out the category name and value
            catparts = cat.split(EQUALS)
            assert len(catparts) == 2
            category = catparts[0]
            value = int(catparts[1])
            assert category in CATEGORIES
            assert 0 < value < 999999

            # 5. Add the category
            assert category not in self.categories
            self.categories[category] = value

    def value(self, category):
        "Get the value for the specified category"

        # 0. Precondition axioms
        assert category in CATEGORIES
        assert category in self.categories

        # 1. Return the requested value
        return self.categories[category]

    def total(self):
        "Return the total of the values"
        return sum(self.categories.values())

# ----------------------------------------------------------------------
#                                                  module initialization
# ----------------------------------------------------------------------


if __name__ == '__main__':
    pass

# ======================================================================
# end                          p a r t . p y                         end
# ======================================================================
